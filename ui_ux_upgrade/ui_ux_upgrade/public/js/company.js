// Modern UI/UX Upgrade - Company Enhancement
// Enhanced functionality for ERPNext Company doctype

frappe.ui.form.on('Company', {
    onload: function(frm) {
        // Initialize modern company form enhancements
        frappe.ui.ModernCompany.init(frm);
    },

    refresh: function(frm) {
        // Add modern styling when form refreshes
        frappe.ui.ModernCompany.enhanceForm(frm);
    }
});

frappe.ui.ModernCompany = {
    init: function(frm) {
        // Initialize modern company functionality
        this.enhanceCompanyProfile(frm);
        this.addModernButtons(frm);
        this.setupCharts(frm);
        console.log('Modern Company form initialized');
    },

    enhanceForm: function(frm) {
        // Add modern classes to form elements
        const formContainer = frm.$wrapper.find('.form-layout');
        formContainer.addClass('modern-company-form');

        // Enhance logo section
        const logoSection = frm.$wrapper.find('.company-logo-section');
        logoSection.addClass('modern-company-logo');

        // Add modern styling to tabs
        const tabs = frm.$wrapper.find('.form-tabs');
        tabs.addClass('modern-tabs');

        // Add company status indicator
        if (frm.doc.is_group) {
            frm.$wrapper.find('.form-layout').addClass('company-group');
        }
    },

    enhanceCompanyProfile: function(frm) {
        // Add profile card styling
        const profileSection = frm.$wrapper.find('.form-section').first();
        profileSection.addClass('modern-company-profile');

        // Enhance company logo display
        if (frm.doc.company_logo) {
            const logoWrapper = frm.$wrapper.find('.company-logo');
            logoWrapper.addClass('modern-company-avatar');
        }

        // Add domain indicator
        if (frm.doc.domain) {
            const domainBadge = `<span class="modern-badge modern-badge-primary">${frm.doc.domain}</span>`;
            frm.$wrapper.find('.form-section').first().append(domainBadge);
        }
    },

    addModernButtons: function(frm) {
        // Enhance existing buttons
        const buttons = frm.$wrapper.find('.btn');
        buttons.addClass('modern-btn');

        // Add custom buttons with modern styling
        if (frm.doc.name) {
            frm.add_custom_button(__('Company Dashboard'), function() {
                frappe.ui.ModernCompany.openDashboard(frm);
            }).addClass('modern-btn modern-btn-primary');

            frm.add_custom_button(__('Financial Reports'), function() {
                frappe.ui.ModernCompany.openFinancialReports(frm);
            }).addClass('modern-btn modern-btn-secondary');

            // Add chart of accounts button
            frm.add_custom_button(__('Chart of Accounts'), function() {
                frappe.set_route('Tree', 'Account', {
                    company: frm.doc.name
                });
            }).addClass('modern-btn modern-btn-info');
        }
    },

    setupCharts: function(frm) {
        // Add company performance charts
        if (frm.doc.name && !frm.doc.__islocal) {
            frm.dashboard.add_section(
                frappe.render_template('company_dashboard', {
                    company: frm.doc.name
                }),
                __('Company Overview')
            );

            // Add modern styling to dashboard section
            setTimeout(function() {
                frm.$wrapper.find('.form-dashboard-section').addClass('modern-dashboard-section');
            }, 100);
        }
    },

    openDashboard: function(frm) {
        // Open modern company dashboard
        frappe.route_options = {
            company: frm.doc.name
        };
        frappe.set_route('query-report', 'Company Dashboard');
    },

    openFinancialReports: function(frm) {
        // Show financial reports menu
        const reports = [
            'Balance Sheet',
            'Profit and Loss Statement',
            'Cash Flow',
            'General Ledger'
        ];

        const reportLinks = reports.map(report => {
            return `<a href="#query-report/${report}" class="modern-link" 
                    onclick="frappe.route_options = {company: '${frm.doc.name}'}">
                    ${__(report)}
                  </a>`;
        }).join('<br>');

        frappe.msgprint({
            title: __('Financial Reports'),
            message: reportLinks,
            wide: true
        });
    }
};