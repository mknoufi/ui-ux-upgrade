"""
Upgrade Check DocType setup
"""

import frappe

def create_upgrade_check_doctype():
    """Create Upgrade Check doctype"""
    if not frappe.db.exists("DocType", "Upgrade Check"):
        doctype = frappe.get_doc({
            "doctype": "DocType",
            "name": "Upgrade Check",
            "module": "UI/UX Upgrade",
            "custom": 1,
            "is_submittable": 0,
            "track_changes": 1,
            "fields": [
                {
                    "fieldname": "current_version",
                    "label": "Current Version",
                    "fieldtype": "Data",
                    "read_only": 1
                },
                {
                    "fieldname": "latest_version",
                    "label": "Latest Version",
                    "fieldtype": "Data",
                    "read_only": 1
                },
                {
                    "fieldname": "update_available",
                    "label": "Update Available",
                    "fieldtype": "Check",
                    "read_only": 1
                },
                {
                    "fieldname": "last_checked",
                    "label": "Last Checked",
                    "fieldtype": "Datetime",
                    "read_only": 1
                },
                {
                    "fieldname": "release_notes",
                    "label": "Release Notes",
                    "fieldtype": "Text Editor",
                    "read_only": 1
                },
                {
                    "fieldname": "release_url",
                    "label": "Release URL",
                    "fieldtype": "Data",
                    "read_only": 1
                },
                {
                    "fieldname": "status",
                    "label": "Status",
                    "fieldtype": "Select",
                    "options": "Pending\nChecked\nError",
                    "default": "Pending"
                }
            ],
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                }
            ]
        })
        doctype.insert()
        return True
    return False