// Modern UI/UX Upgrade - Dashboard Enhancement
// Enhanced functionality for ERPNext dashboard doctype

frappe.ui.form.on('Dashboard', {
    onload: function(frm) {
        // Initialize modern dashboard enhancements
        frappe.ui.ModernDashboard.init(frm);
    },

    refresh: function(frm) {
        // Add modern styling when form refreshes
        frappe.ui.ModernDashboard.enhanceForm(frm);
    }
});

frappe.ui.ModernDashboard = {
    init: function(frm) {
        // Initialize modern dashboard functionality
        this.enhanceCharts(frm);
        this.addModernWidgets(frm);
        this.setupInteractions(frm);
        console.log('Modern Dashboard initialized for form');
    },

    enhanceForm: function(frm) {
        // Add modern classes to form elements
        const formContainer = frm.$wrapper.find('.form-layout');
        formContainer.addClass('modern-dashboard-form');

        // Enhance cards
        const cards = frm.$wrapper.find('.card, .panel');
        cards.addClass('modern-card');

        // Add hover effects to dashboard items
        const dashboardItems = frm.$wrapper.find('.dashboard-item');
        dashboardItems.addClass('modern-dashboard-item');
    },

    enhanceCharts: function(frm) {
        // Enhance chart containers
        const chartContainers = frm.$wrapper.find('.chart-container');
        chartContainers.each(function() {
            $(this).addClass('modern-chart-container');
            
            // Add loading animation
            if (!$(this).find('.chart-loading').length) {
                $(this).append('<div class="chart-loading modern-spinner"></div>');
            }
        });
    },

    addModernWidgets: function(frm) {
        // Add modern widget styling
        const widgets = frm.$wrapper.find('.widget');
        widgets.addClass('modern-widget');

        // Enhance widget headers
        const widgetHeaders = frm.$wrapper.find('.widget-header');
        widgetHeaders.addClass('modern-widget-header');
    },

    setupInteractions: function(frm) {
        // Add smooth hover effects
        frm.$wrapper.on('mouseenter', '.modern-dashboard-item', function() {
            $(this).addClass('hovered');
        });

        frm.$wrapper.on('mouseleave', '.modern-dashboard-item', function() {
            $(this).removeClass('hovered');
        });

        // Add click animations
        frm.$wrapper.on('click', '.modern-widget', function() {
            const widget = $(this);
            widget.addClass('clicked');
            setTimeout(function() {
                widget.removeClass('clicked');
            }, 150);
        });
    }
};