"""
Desktop Configuration for UI/UX Upgrade
Modern desktop enhancements and configurations
"""

from frappe import _

def get_data():
    return [
        {
            "module_name": "UI/UX Upgrade",
            "color": "blue",
            "icon": "octicon octicon-paintcan",
            "type": "module",
            "label": _("UI/UX Upgrade")
        },
        {
            "module_name": "Modern Dashboard",
            "color": "green",
            "icon": "octicon octicon-dashboard",
            "type": "page",
            "label": _("Modern Dashboard"),
            "route": "/modern-dashboard",
            "description": _("Enhanced dashboard with modern design")
        },
        {
            "module_name": "UI Settings",
            "color": "orange",
            "icon": "octicon octicon-gear",
            "type": "doctype",
            "label": _("UI Settings"),
            "name": "UI Settings",
            "description": _("Configure modern UI settings")
        },
        {
            "module_name": "Theme Manager",
            "color": "purple",
            "icon": "octicon octicon-palette",
            "type": "doctype",
            "label": _("Theme Manager"),
            "name": "Theme Manager",
            "description": _("Manage custom themes and styles")
        }
    ]
