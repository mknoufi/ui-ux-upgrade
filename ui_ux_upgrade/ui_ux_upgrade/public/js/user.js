// Modern UI/UX Upgrade - User Enhancement
// Enhanced functionality for ERPNext User doctype

frappe.ui.form.on('User', {
    onload: function(frm) {
        // Initialize modern user form enhancements
        frappe.ui.ModernUser.init(frm);
    },

    refresh: function(frm) {
        // Add modern styling when form refreshes
        frappe.ui.ModernUser.enhanceForm(frm);
    }
});

frappe.ui.ModernUser = {
    init: function(frm) {
        // Initialize modern user functionality
        this.enhanceUserProfile(frm);
        this.addModernButtons(frm);
        this.setupValidation(frm);
        console.log('Modern User form initialized');
    },

    enhanceForm: function(frm) {
        // Add modern classes to form elements
        const formContainer = frm.$wrapper.find('.form-layout');
        formContainer.addClass('modern-user-form');

        // Enhance user image section
        const imageSection = frm.$wrapper.find('.user-image-section');
        imageSection.addClass('modern-user-image');

        // Add modern styling to tabs
        const tabs = frm.$wrapper.find('.form-tabs');
        tabs.addClass('modern-tabs');
    },

    enhanceUserProfile: function(frm) {
        // Add profile card styling
        const profileSection = frm.$wrapper.find('.form-section').first();
        profileSection.addClass('modern-profile-section');

        // Enhance user image display
        if (frm.doc.user_image) {
            const imageWrapper = frm.$wrapper.find('.user-image');
            imageWrapper.addClass('modern-avatar');
        }

        // Add status indicators
        if (frm.doc.enabled) {
            frm.$wrapper.find('.form-layout').addClass('user-active');
        } else {
            frm.$wrapper.find('.form-layout').addClass('user-inactive');
        }
    },

    addModernButtons: function(frm) {
        // Enhance existing buttons
        const buttons = frm.$wrapper.find('.btn');
        buttons.addClass('modern-btn');

        // Add custom buttons with modern styling
        if (frm.doc.name && frm.doc.name !== 'Administrator') {
            frm.add_custom_button(__('Reset Password'), function() {
                frappe.ui.ModernUser.resetPassword(frm);
            }).addClass('modern-btn modern-btn-warning');

            frm.add_custom_button(__('Send Welcome Email'), function() {
                frappe.ui.ModernUser.sendWelcomeEmail(frm);
            }).addClass('modern-btn modern-btn-primary');
        }
    },

    setupValidation: function(frm) {
        // Add real-time email validation
        frm.$wrapper.on('blur', 'input[data-fieldname="email"]', function() {
            const email = $(this).val();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            
            if (email && !emailRegex.test(email)) {
                $(this).addClass('error');
                frappe.show_alert({
                    message: __('Please enter a valid email address'),
                    indicator: 'red'
                });
            } else {
                $(this).removeClass('error');
            }
        });

        // Add password strength indicator
        frm.$wrapper.on('input', 'input[data-fieldname="new_password"]', function() {
            const password = $(this).val();
            frappe.ui.ModernUser.showPasswordStrength(password, $(this));
        });
    },

    resetPassword: function(frm) {
        frappe.confirm(__('Are you sure you want to reset the password for this user?'), function() {
            frappe.call({
                method: 'frappe.core.doctype.user.user.reset_password',
                args: {
                    user: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Password reset email sent successfully'),
                            indicator: 'green'
                        });
                    }
                }
            });
        });
    },

    sendWelcomeEmail: function(frm) {
        frappe.call({
            method: 'frappe.core.doctype.user.user.send_welcome_mail_to_user',
            args: {
                user: frm.doc.name
            },
            callback: function(r) {
                if (!r.exc) {
                    frappe.show_alert({
                        message: __('Welcome email sent successfully'),
                        indicator: 'green'
                    });
                }
            }
        });
    },

    showPasswordStrength: function(password, input) {
        // Simple password strength indicator
        let strength = 0;
        if (password.length >= 8) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;

        const strengthLabels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'];
        const strengthColors = ['red', 'orange', 'yellow', 'lightgreen', 'green'];

        // Remove existing strength indicator
        input.siblings('.password-strength').remove();

        if (password.length > 0) {
            const strengthHtml = `<div class="password-strength" style="color: ${strengthColors[strength - 1] || 'red'}; font-size: 12px; margin-top: 5px;">
                Password Strength: ${strengthLabels[strength - 1] || 'Very Weak'}
            </div>`;
            input.after(strengthHtml);
        }
    }
};