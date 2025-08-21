"""
Before Uninstall Script for UI/UX Upgrade
Cleanup modern UI elements and configurations
"""

import frappe
from frappe import _

def before_uninstall():
    """Cleanup modern UI elements before uninstallation"""
    
    # Remove custom pages
    remove_custom_pages()
    
    # Cleanup custom doctypes (but preserve data)
    cleanup_custom_doctypes()
    
    # Remove custom files
    cleanup_custom_files()
    
    print("✅ UI/UX Upgrade cleanup completed successfully!")

def remove_custom_pages():
    """Remove custom pages created by the app"""
    pages_to_remove = [
        "modern-dashboard",
        "modern-login", 
        "modern-setup"
    ]
    
    for page_name in pages_to_remove:
        if frappe.db.exists("Page", page_name):
            try:
                frappe.delete_doc("Page", page_name, force=True)
                print(f"✅ Removed page: {page_name}")
            except Exception as e:
                print(f"⚠️ Could not remove page {page_name}: {str(e)}")

def cleanup_custom_doctypes():
    """Cleanup custom doctypes (preserve data, just mark as non-custom)"""
    custom_doctypes = ["UI Settings", "Theme Manager"]
    
    for doctype_name in custom_doctypes:
        if frappe.db.exists("DocType", doctype_name):
            try:
                # Just log that these exist - don't actually delete to preserve user data
                print(f"ℹ️ Custom doctype preserved with data: {doctype_name}")
            except Exception as e:
                print(f"⚠️ Issue with doctype {doctype_name}: {str(e)}")

def cleanup_custom_files():
    """Cleanup any temporary files or caches"""
    try:
        # Clear any caches that might have been created
        frappe.clear_cache()
        print("✅ Cleared caches")
    except Exception as e:
        print(f"⚠️ Could not clear caches: {str(e)}")