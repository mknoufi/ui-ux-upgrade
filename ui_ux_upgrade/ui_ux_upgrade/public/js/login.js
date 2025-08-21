// Modern UI/UX Upgrade - Login Enhancement
// Enhanced functionality for ERPNext login page

frappe.ui.ModernLogin = {
    init: function() {
        // Initialize modern login enhancements
        this.enhanceLoginForm();
        this.addAnimations();
        this.setupValidation();
        console.log('Modern Login UI initialized');
    },

    enhanceLoginForm: function() {
        // Add modern styling to login form
        const loginForm = document.querySelector('.login-content');
        if (loginForm) {
            loginForm.classList.add('modern-login-form');
        }

        // Enhance input fields
        const inputs = document.querySelectorAll('.login-content input');
        inputs.forEach(function(input) {
            input.classList.add('modern-input');
            
            // Add floating label effect
            const wrapper = document.createElement('div');
            wrapper.className = 'modern-input-wrapper';
            input.parentNode.insertBefore(wrapper, input);
            wrapper.appendChild(input);
        });

        // Enhance login button
        const loginBtn = document.querySelector('.btn-login');
        if (loginBtn) {
            loginBtn.classList.add('modern-btn', 'modern-btn-primary');
        }
    },

    addAnimations: function() {
        // Add fade-in animation
        const loginContainer = document.querySelector('.login-content');
        if (loginContainer) {
            loginContainer.style.opacity = '0';
            loginContainer.style.transform = 'translateY(20px)';
            
            setTimeout(function() {
                loginContainer.style.transition = 'all 0.5s ease';
                loginContainer.style.opacity = '1';
                loginContainer.style.transform = 'translateY(0)';
            }, 100);
        }
    },

    setupValidation: function() {
        // Add real-time validation feedback
        const inputs = document.querySelectorAll('.login-content input');
        inputs.forEach(function(input) {
            input.addEventListener('blur', function() {
                if (this.value.trim() === '') {
                    this.classList.add('error');
                } else {
                    this.classList.remove('error');
                    this.classList.add('valid');
                }
            });
        });
    }
};

// Initialize when page is ready
$(document).ready(function() {
    frappe.ui.ModernLogin.init();
});