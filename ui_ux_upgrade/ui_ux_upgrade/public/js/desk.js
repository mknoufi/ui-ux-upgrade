// Modern UI/UX Upgrade - Desk Enhancement
// Enhanced functionality for ERPNext desk

frappe.ui.ModernDesk = {
    init: function() {
        // Initialize modern desk enhancements
        this.enhanceNavigation();
        this.addModernStyles();
        this.setupKeyboardShortcuts();
        console.log('Modern Desk UI initialized');
    },

    enhanceNavigation: function() {
        // Enhance sidebar navigation
        const sidebar = document.querySelector('.desk-sidebar');
        if (sidebar) {
            sidebar.classList.add('modern-sidebar');
        }

        // Add hover effects to navigation items
        const navItems = document.querySelectorAll('.desk-sidebar .sidebar-item');
        navItems.forEach(function(item) {
            item.classList.add('modern-nav-item');
        });
    },

    addModernStyles: function() {
        // Add modern classes to existing elements
        const mainContent = document.querySelector('.main-section');
        if (mainContent) {
            mainContent.classList.add('modern-main-content');
        }

        // Enhance form controls
        const formControls = document.querySelectorAll('.form-control');
        formControls.forEach(function(control) {
            control.classList.add('modern-form-control');
        });
    },

    setupKeyboardShortcuts: function() {
        // Add modern keyboard shortcuts
        frappe.ui.keys.add_key('ctrl+shift+t', function() {
            // Toggle modern theme
            console.log('Theme toggle shortcut pressed');
        });
    }
};

// Initialize when page is ready
$(document).ready(function() {
    frappe.ui.ModernDesk.init();
});