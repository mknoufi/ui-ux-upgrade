app_name = "ui_ux_upgrade"
app_title = "UI/UX Upgrade"
app_publisher = "E-Mart Systems"
app_description = "Modern UI/UX enhancements for ERPNext with improved design, animations, and user experience"
app_email = "support@emart.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/ui_ux_upgrade/css/modern-ui.css"
app_include_js = "/assets/ui_ux_upgrade/js/modern-ui.js"

# include js, css files in header of web template
web_include_css = "/assets/ui_ux_upgrade/css/web-modern-ui.css"
web_include_js = "/assets/ui_ux_upgrade/js/web-modern-ui.js"

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "ui_ux_upgrade/public/scss/website"

# include js in page
page_js = {
    "desk": "public/js/desk.js",
    "login": "public/js/login.js",
    "setup": "public/js/setup.js"
}

# include js in doctype views
doctype_js = {
    "Dashboard": "public/js/dashboard.js",
    "User": "public/js/user.js",
    "Company": "public/js/company.js"
}

# Svg Icons
# ------------------
# include app icons in desk
app_include_icons = "ui_ux_upgrade/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "modern-dashboard"

# website user home page (by Role)
role_home_page = {
    "System Manager": "modern-dashboard",
    "Administrator": "modern-dashboard",
    "User": "modern-dashboard"
}

# Installation
# ------------

after_install = "ui_ux_upgrade.install.after_install"

# Uninstallation
# ------------

before_uninstall = "ui_ux_upgrade.uninstall.before_uninstall"

# Desk Notifications
# ------------------

notification_config = "ui_ux_upgrade.notifications.get_notification_config"

# Permissions
# -----------

has_permission = {
    "Dashboard": "ui_ux_upgrade.permissions.has_dashboard_permission",
}

# Document Events
# ---------------

doc_events = {
    "User": {
        "on_update": "ui_ux_upgrade.events.user_updated",
        "after_insert": "ui_ux_upgrade.events.user_created"
    },
    "Company": {
        "on_update": "ui_ux_upgrade.events.company_updated"
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": [
        "ui_ux_upgrade.tasks.daily_cleanup"
    ],
    "weekly": [
        "ui_ux_upgrade.tasks.weekly_optimization"
    ]
}

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
    "frappe.desk.desktop.get_desktop_page": "ui_ux_upgrade.overrides.get_modern_desktop_page",
    "frappe.desk.doctype.dashboard.dashboard.get": "ui_ux_upgrade.overrides.get_modern_dashboard"
}

# Override Doctype Dashboards
# ------------------------------

override_doctype_dashboards = {
    "Dashboard": "ui_ux_upgrade.dashboard.get_dashboard_data"
}

# Request Events
# ----------------

before_request = ["ui_ux_upgrade.utils.before_request"]
after_request = ["ui_ux_upgrade.utils.after_request"]

# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "User",
        "filter_by": "name",
        "redact_fields": ["api_key", "api_secret"],
        "partial": 1,
    }
]
