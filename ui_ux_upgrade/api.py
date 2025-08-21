"""
API endpoints for UI/UX Upgrade features
"""

import frappe
from frappe import _
from ui_ux_upgrade.upgrade_checker.upgrade_checker import check_for_upgrades, get_upgrade_instructions
from ui_ux_upgrade.suggestions.suggestions import get_ui_suggestions, get_suggestion_details

@frappe.whitelist()
def get_upgrade_status():
    """Get current upgrade status"""
    return check_for_upgrades()

@frappe.whitelist()
def get_upgrade_help():
    """Get upgrade instructions"""
    return get_upgrade_instructions()

@frappe.whitelist()
def get_suggestions():
    """Get UI/UX suggestions"""
    return get_ui_suggestions()

@frappe.whitelist()
def get_filtered_suggestions(category=None, priority=None):
    """Get filtered suggestions"""
    return get_suggestion_details(category, priority)

@frappe.whitelist()
def create_upgrade_check_record():
    """Create an upgrade check record"""
    try:
        upgrade_data = check_for_upgrades()
        
        if upgrade_data.get("success"):
            doc = frappe.get_doc({
                "doctype": "Upgrade Check",
                "current_version": upgrade_data.get("current_version"),
                "latest_version": upgrade_data.get("latest_version"),
                "update_available": upgrade_data.get("update_available", False),
                "last_checked": frappe.utils.now(),
                "release_notes": upgrade_data.get("release_notes", ""),
                "release_url": upgrade_data.get("release_url", ""),
                "status": "Checked"
            })
            doc.insert()
            return {
                "success": True,
                "message": _("Upgrade check record created successfully"),
                "name": doc.name
            }
        else:
            return {
                "success": False,
                "message": upgrade_data.get("message", "Unknown error")
            }
            
    except Exception as e:
        frappe.log_error(f"Failed to create upgrade check record: {str(e)}", "UI/UX Upgrade API")
        return {
            "success": False,
            "message": _("Failed to create upgrade check record: {0}").format(str(e))
        }

@frappe.whitelist()
def create_suggestions_records():
    """Create suggestion records from analysis"""
    try:
        suggestions_data = get_ui_suggestions()
        
        if not suggestions_data.get("success"):
            return suggestions_data
        
        created_suggestions = []
        
        for suggestion in suggestions_data.get("suggestions", []):
            doc = frappe.get_doc({
                "doctype": "UI Suggestions",
                "category": suggestion.get("category"),
                "priority": suggestion.get("priority").title(),
                "title": suggestion.get("title"),
                "description": suggestion.get("description"),
                "action": suggestion.get("action"),
                "icon": suggestion.get("icon"),
                "status": "Pending"
            })
            doc.insert()
            created_suggestions.append(doc.name)
        
        return {
            "success": True,
            "message": _("{0} suggestion records created").format(len(created_suggestions)),
            "suggestions": created_suggestions
        }
        
    except Exception as e:
        frappe.log_error(f"Failed to create suggestion records: {str(e)}", "UI/UX Upgrade API")
        return {
            "success": False,
            "message": _("Failed to create suggestion records: {0}").format(str(e))
        }