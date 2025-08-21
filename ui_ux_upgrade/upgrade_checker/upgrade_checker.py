"""
Upgrade Checker for UI/UX Upgrade App
Checks for available updates and new features
"""

import frappe
import requests
import json
from frappe import _
from packaging import version
import re

@frappe.whitelist()
def check_for_upgrades():
    """Check for available upgrades from GitHub releases"""
    try:
        current_version = get_current_version()
        latest_release = get_latest_release()
        
        if not latest_release:
            return {
                "success": False,
                "message": _("Unable to check for updates. Please check your internet connection.")
            }
        
        latest_version = latest_release.get("tag_name", "").lstrip("v")
        
        if version.parse(latest_version) > version.parse(current_version):
            return {
                "success": True,
                "update_available": True,
                "current_version": current_version,
                "latest_version": latest_version,
                "release_notes": latest_release.get("body", ""),
                "release_url": latest_release.get("html_url", ""),
                "published_at": latest_release.get("published_at", "")
            }
        else:
            return {
                "success": True,
                "update_available": False,
                "current_version": current_version,
                "latest_version": latest_version,
                "message": _("You are running the latest version.")
            }
            
    except Exception as e:
        frappe.log_error(f"Upgrade check failed: {str(e)}", "UI/UX Upgrade Checker")
        return {
            "success": False,
            "message": _("Failed to check for updates: {0}").format(str(e))
        }

def get_current_version():
    """Get current version from hooks.py or pyproject.toml"""
    try:
        # Try to get from app info first
        from ui_ux_upgrade import __version__
        return __version__
    except (ImportError, AttributeError):
        # Fallback to reading pyproject.toml
        try:
            import toml
            with open(frappe.get_app_path("ui_ux_upgrade", "..", "pyproject.toml"), "r") as f:
                data = toml.load(f)
                return data.get("project", {}).get("version", "1.0.0")
        except:
            # Fallback to manual parsing if toml not available
            try:
                with open(frappe.get_app_path("ui_ux_upgrade", "..", "pyproject.toml"), "r") as f:
                    content = f.read()
                    # Simple regex to extract version
                    import re
                    version_match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
                    if version_match:
                        return version_match.group(1)
            except:
                pass
            return "1.0.0"

def get_latest_release():
    """Get latest release information from GitHub"""
    try:
        # GitHub API endpoint for latest release
        url = "https://api.github.com/repos/mknoufi/ui-ux-upgrade/releases/latest"
        
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "ui-ux-upgrade-app"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            frappe.log_error(f"GitHub API returned status {response.status_code}", "UI/UX Upgrade Checker")
            return None
            
    except requests.RequestException as e:
        frappe.log_error(f"Network error checking for updates: {str(e)}", "UI/UX Upgrade Checker")
        return None

@frappe.whitelist()
def get_upgrade_instructions():
    """Get upgrade instructions for the app"""
    return {
        "instructions": [
            _("1. Navigate to your ERPNext bench directory"),
            _("2. Run: cd apps/ui_ux_upgrade"),
            _("3. Run: git pull origin main"),
            _("4. Run: bench build --app ui_ux_upgrade"),
            _("5. Run: bench restart"),
            _("6. Clear browser cache and refresh")
        ],
        "backup_warning": _("Always backup your site before updating!"),
        "support_url": "https://github.com/mknoufi/ui-ux-upgrade/issues"
    }

@frappe.whitelist()
def schedule_upgrade_check():
    """Schedule automatic upgrade checks"""
    try:
        # This would be called by a scheduled job
        result = check_for_upgrades()
        
        if result.get("success") and result.get("update_available"):
            # Create a notification for system managers
            frappe.publish_realtime(
                "upgrade_available",
                {
                    "title": _("UI/UX Upgrade Update Available"),
                    "message": _("Version {0} is available. Current version: {1}").format(
                        result.get("latest_version"),
                        result.get("current_version")
                    ),
                    "indicator": "blue"
                },
                user=frappe.session.user
            )
            
        return result
        
    except Exception as e:
        frappe.log_error(f"Scheduled upgrade check failed: {str(e)}", "UI/UX Upgrade Checker")
        return {"success": False, "error": str(e)}