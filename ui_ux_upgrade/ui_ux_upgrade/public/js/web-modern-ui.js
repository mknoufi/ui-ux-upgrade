// Modern UI/UX Upgrade JavaScript - Web Template
// Enhanced functionality for ERPNext web templates

(function() {
    'use strict';

    // Initialize modern web UI
    function initModernWebUI() {
        // Add modern classes to existing elements
        enhanceExistingElements();
        
        // Add smooth scrolling
        addSmoothScrolling();
        
        // Add modern form enhancements
        enhanceForms();
        
        console.log('Modern Web UI initialized');
    }

    // Enhance existing elements
    function enhanceExistingElements() {
        // Add modern card classes to existing containers
        const containers = document.querySelectorAll('.container, .card, .panel');
        containers.forEach(function(container) {
            if (!container.classList.contains('web-modern-card')) {
                container.classList.add('web-modern-card');
            }
        });

        // Enhance buttons
        const buttons = document.querySelectorAll('button, .btn, input[type="submit"]');
        buttons.forEach(function(button) {
            if (!button.classList.contains('web-modern-btn')) {
                button.classList.add('web-modern-btn');
            }
        });
    }

    // Add smooth scrolling
    function addSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        links.forEach(function(link) {
            link.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Enhance forms
    function enhanceForms() {
        const forms = document.querySelectorAll('form');
        forms.forEach(function(form) {
            // Add form validation feedback
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(function(input) {
                input.addEventListener('blur', function() {
                    validateInput(this);
                });
            });
        });
    }

    // Simple input validation
    function validateInput(input) {
        const isValid = input.checkValidity();
        
        if (isValid) {
            input.classList.remove('error');
            input.classList.add('valid');
        } else {
            input.classList.remove('valid');
            input.classList.add('error');
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initModernWebUI);
    } else {
        initModernWebUI();
    }

    // Expose API for external use
    window.ModernWebUI = {
        init: initModernWebUI,
        enhanceElement: function(element) {
            if (element.tagName === 'BUTTON' || element.classList.contains('btn')) {
                element.classList.add('web-modern-btn');
            }
            if (element.classList.contains('container') || element.classList.contains('card')) {
                element.classList.add('web-modern-card');
            }
        }
    };

})();