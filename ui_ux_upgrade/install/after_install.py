"""
After Install Script for UI/UX Upgrade
Sets up modern UI elements and configurations
"""

import frappe
from frappe import _
from ui_ux_upgrade.upgrade_checker.doctype_setup import create_upgrade_check_doctype
from ui_ux_upgrade.suggestions.doctype_setup import create_ui_suggestions_doctype

def after_install():
    """Setup modern UI elements after installation"""
    
    # Create UI Settings
    create_ui_settings()
    
    # Create Theme Manager
    create_theme_manager()
    
    # Create Upgrade Check doctype
    create_upgrade_check_doctype()
    
    # Create UI Suggestions doctype
    create_ui_suggestions_doctype()
    
    # Create Modern Dashboard
    create_modern_dashboard()
    
    # Setup default themes
    setup_default_themes()
    
    # Create custom pages
    create_custom_pages()
    
    print("✅ UI/UX Upgrade installed successfully!")

def create_ui_settings():
    """Create UI Settings doctype if not exists"""
    if not frappe.db.exists("DocType", "UI Settings"):
        # Create UI Settings doctype
        ui_settings = frappe.get_doc({
            "doctype": "DocType",
            "name": "UI Settings",
            "module": "UI/UX Upgrade",
            "custom": 1,
            "fields": [
                {
                    "fieldname": "enable_animations",
                    "label": "Enable Animations",
                    "fieldtype": "Check",
                    "default": 1
                },
                {
                    "fieldname": "modern_theme",
                    "label": "Modern Theme",
                    "fieldtype": "Select",
                    "options": "Default\nDark\nLight\nCustom"
                },
                {
                    "fieldname": "enable_glassmorphism",
                    "label": "Enable Glassmorphism",
                    "fieldtype": "Check",
                    "default": 1
                },
                {
                    "fieldname": "enable_shadows",
                    "label": "Enable Shadows",
                    "fieldtype": "Check",
                    "default": 1
                }
            ]
        })
        ui_settings.insert()

def create_theme_manager():
    """Create Theme Manager doctype if not exists"""
    if not frappe.db.exists("DocType", "Theme Manager"):
        theme_manager = frappe.get_doc({
            "doctype": "DocType",
            "name": "Theme Manager",
            "module": "UI/UX Upgrade",
            "custom": 1,
            "fields": [
                {
                    "fieldname": "theme_name",
                    "label": "Theme Name",
                    "fieldtype": "Data",
                    "reqd": 1
                },
                {
                    "fieldname": "primary_color",
                    "label": "Primary Color",
                    "fieldtype": "Color"
                },
                {
                    "fieldname": "secondary_color",
                    "label": "Secondary Color",
                    "fieldtype": "Color"
                },
                {
                    "fieldname": "css_code",
                    "label": "Custom CSS",
                    "fieldtype": "Code",
                    "options": "CSS"
                }
            ]
        })
        theme_manager.insert()

def create_modern_dashboard():
    """Create Modern Dashboard page"""
    if not frappe.db.exists("Page", "modern-dashboard"):
        modern_dashboard = frappe.get_doc({
            "doctype": "Page",
            "name": "modern-dashboard",
            "title": "Modern Dashboard",
            "module": "UI/UX Upgrade",
            "template": "modern-dashboard.html"
        })
        modern_dashboard.insert()

def setup_default_themes():
    """Setup default themes"""
    themes = [
        {
            "theme_name": "Modern Light",
            "primary_color": "#2563eb",
            "secondary_color": "#f8fafc"
        },
        {
            "theme_name": "Modern Dark",
            "primary_color": "#1e293b",
            "secondary_color": "#334155"
        },
        {
            "theme_name": "E-Mart Blue",
            "primary_color": "#1e40af",
            "secondary_color": "#dbeafe"
        }
    ]
    
    for theme in themes:
        if not frappe.db.exists("Theme Manager", {"theme_name": theme["theme_name"]}):
            theme_doc = frappe.get_doc({
                "doctype": "Theme Manager",
                **theme
            })
            theme_doc.insert()

def create_custom_pages():
    """Create custom pages for modern UI"""
    pages = [
        {
            "name": "modern-login",
            "title": "Modern Login",
            "template": "modern-login.html"
        },
        {
            "name": "modern-setup",
            "title": "Modern Setup",
            "template": "modern-setup.html"
        }
    ]
    
    for page in pages:
        if not frappe.db.exists("Page", page["name"]):
            page_doc = frappe.get_doc({
                "doctype": "Page",
                "name": page["name"],
                "title": page["title"],
                "module": "UI/UX Upgrade",
                "template": page["template"]
            })
            page_doc.insert()
