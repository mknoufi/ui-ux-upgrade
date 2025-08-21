// Modern UI/UX Upgrade - Setup Enhancement
// Enhanced functionality for ERPNext setup wizard

frappe.ui.ModernSetup = {
    init: function() {
        // Initialize modern setup enhancements
        this.enhanceSetupWizard();
        this.addProgressIndicator();
        this.setupAnimations();
        console.log('Modern Setup UI initialized');
    },

    enhanceSetupWizard: function() {
        // Add modern styling to setup wizard
        const setupContainer = document.querySelector('.setup-wizard');
        if (setupContainer) {
            setupContainer.classList.add('modern-setup-wizard');
        }

        // Enhance form fields
        const formGroups = document.querySelectorAll('.setup-wizard .form-group');
        formGroups.forEach(function(group) {
            group.classList.add('modern-form-group');
        });

        // Enhance buttons
        const buttons = document.querySelectorAll('.setup-wizard .btn');
        buttons.forEach(function(btn) {
            btn.classList.add('modern-btn');
            if (btn.classList.contains('btn-primary')) {
                btn.classList.add('modern-btn-primary');
            }
        });
    },

    addProgressIndicator: function() {
        // Enhance progress indicator
        const progressBar = document.querySelector('.progress-bar');
        if (progressBar) {
            progressBar.classList.add('modern-progress-bar');
        }

        // Add step indicators
        const steps = document.querySelectorAll('.setup-wizard .step');
        steps.forEach(function(step, index) {
            step.classList.add('modern-step');
            step.setAttribute('data-step', index + 1);
        });
    },

    setupAnimations: function() {
        // Add slide animations between steps
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'childList') {
                    const newSteps = mutation.addedNodes;
                    newSteps.forEach(function(node) {
                        if (node.nodeType === 1 && node.classList.contains('step')) {
                            node.style.opacity = '0';
                            node.style.transform = 'translateX(50px)';
                            
                            setTimeout(function() {
                                node.style.transition = 'all 0.3s ease';
                                node.style.opacity = '1';
                                node.style.transform = 'translateX(0)';
                            }, 50);
                        }
                    });
                }
            });
        });

        const setupWizard = document.querySelector('.setup-wizard');
        if (setupWizard) {
            observer.observe(setupWizard, { childList: true, subtree: true });
        }
    }
};

// Initialize when page is ready
$(document).ready(function() {
    frappe.ui.ModernSetup.init();
});