"""
UI Suggestions DocType setup
"""

import frappe

def create_ui_suggestions_doctype():
    """Create UI Suggestions doctype"""
    if not frappe.db.exists("DocType", "UI Suggestions"):
        doctype = frappe.get_doc({
            "doctype": "DocType",
            "name": "UI Suggestions",
            "module": "UI/UX Upgrade",
            "custom": 1,
            "is_submittable": 0,
            "track_changes": 1,
            "fields": [
                {
                    "fieldname": "category",
                    "label": "Category",
                    "fieldtype": "Select",
                    "options": "Theme\nPerformance\nAccessibility\nUser Experience\nGeneral",
                    "reqd": 1
                },
                {
                    "fieldname": "priority",
                    "label": "Priority",
                    "fieldtype": "Select",
                    "options": "High\nMedium\nLow",
                    "default": "Medium",
                    "reqd": 1
                },
                {
                    "fieldname": "title",
                    "label": "Title",
                    "fieldtype": "Data",
                    "reqd": 1
                },
                {
                    "fieldname": "description",
                    "label": "Description",
                    "fieldtype": "Text Editor",
                    "reqd": 1
                },
                {
                    "fieldname": "action",
                    "label": "Recommended Action",
                    "fieldtype": "Text",
                    "reqd": 1
                },
                {
                    "fieldname": "icon",
                    "label": "Icon",
                    "fieldtype": "Data"
                },
                {
                    "fieldname": "status",
                    "label": "Status",
                    "fieldtype": "Select",
                    "options": "Pending\nIn Progress\nCompleted\nDismissed",
                    "default": "Pending"
                },
                {
                    "fieldname": "completed_on",
                    "label": "Completed On",
                    "fieldtype": "Date",
                    "depends_on": "eval: doc.status == 'Completed'"
                },
                {
                    "fieldname": "notes",
                    "label": "Notes",
                    "fieldtype": "Text"
                }
            ],
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                },
                {
                    "role": "Administrator",
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