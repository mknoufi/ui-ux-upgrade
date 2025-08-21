/**
 * Modern UI/UX Upgrade JavaScript
 * Enhanced interactions and animations for ERPNext
 */

class ModernUI {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.applyModernStyles();
        this.initializeAnimations();
        this.setupThemeManager();
    }

    setupEventListeners() {
        // Modern button interactions
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-modern')) {
                this.addRippleEffect(e);
            }
        });

        // Form enhancements
        document.addEventListener('focusin', (e) => {
            if (e.target.classList.contains('input-modern')) {
                this.enhanceInputFocus(e.target);
            }
        });

        // Card hover effects
        document.addEventListener('mouseenter', (e) => {
            if (e.target.classList.contains('modern-card')) {
                this.enhanceCardHover(e.target);
            }
        });

        // Smooth scrolling for navigation
        document.addEventListener('click', (e) => {
            if (e.target.getAttribute('data-smooth-scroll')) {
                e.preventDefault();
                this.smoothScrollTo(e.target.getAttribute('href'));
            }
        });
    }

    applyModernStyles() {
        // Add modern classes to existing elements
        this.enhanceExistingElements();
        this.setupResponsiveDesign();
        this.applyCustomThemes();
    }

    enhanceExistingElements() {
        // Enhance buttons
        document.querySelectorAll('.btn-primary').forEach(btn => {
            btn.classList.add('btn-modern', 'btn-modern-primary');
        });

        document.querySelectorAll('.btn-secondary').forEach(btn => {
            btn.classList.add('btn-modern', 'btn-modern-secondary');
        });

        // Enhance cards
        document.querySelectorAll('.card').forEach(card => {
            card.classList.add('modern-card');
        });

        // Enhance forms
        document.querySelectorAll('form').forEach(form => {
            form.classList.add('form-modern');
        });

        // Enhance inputs
        document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], textarea, select').forEach(input => {
            input.classList.add('input-modern');
        });

        // Enhance tables
        document.querySelectorAll('table').forEach(table => {
            table.classList.add('table-modern');
        });
    }

    setupResponsiveDesign() {
        // Mobile menu toggle
        const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
        if (mobileMenuToggle) {
            mobileMenuToggle.addEventListener('click', () => {
                this.toggleMobileMenu();
            });
        }

        // Responsive sidebar
        this.setupResponsiveSidebar();
    }

    setupResponsiveSidebar() {
        const sidebar = document.querySelector('.sidebar');
        const sidebarToggle = document.querySelector('.sidebar-toggle');
        
        if (sidebarToggle && sidebar) {
            sidebarToggle.addEventListener('click', () => {
                sidebar.classList.toggle('sidebar-collapsed');
            });
        }
    }

    initializeAnimations() {
        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.modern-card, .dashboard-card').forEach(el => {
            observer.observe(el);
        });
    }

    setupThemeManager() {
        // Theme switching functionality
        this.loadSavedTheme();
        this.setupThemeSwitcher();
    }

    loadSavedTheme() {
        const savedTheme = localStorage.getItem('modern-ui-theme');
        if (savedTheme) {
            this.applyTheme(savedTheme);
        }
    }

    setupThemeSwitcher() {
        const themeSwitcher = document.querySelector('.theme-switcher');
        if (themeSwitcher) {
            themeSwitcher.addEventListener('change', (e) => {
                this.applyTheme(e.target.value);
                localStorage.setItem('modern-ui-theme', e.target.value);
            });
        }
    }

    applyTheme(themeName) {
        document.documentElement.setAttribute('data-theme', themeName);
        
        // Apply custom CSS variables based on theme
        const themes = {
            'light': {
                '--bg-primary': '#ffffff',
                '--text-primary': '#1f2937',
                '--border-color': '#e5e7eb'
            },
            'dark': {
                '--bg-primary': '#1f2937',
                '--text-primary': '#f9fafb',
                '--border-color': '#374151'
            },
            'blue': {
                '--bg-primary': '#eff6ff',
                '--text-primary': '#1e40af',
                '--border-color': '#bfdbfe'
            }
        };

        if (themes[themeName]) {
            Object.entries(themes[themeName]).forEach(([property, value]) => {
                document.documentElement.style.setProperty(property, value);
            });
        }
    }

    addRippleEffect(event) {
        const button = event.currentTarget;
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        button.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 600);
    }

    enhanceInputFocus(input) {
        input.parentElement.classList.add('input-focused');
        
        input.addEventListener('blur', () => {
            if (!input.value) {
                input.parentElement.classList.remove('input-focused');
            }
        });
    }

    enhanceCardHover(card) {
        card.style.transform = 'translateY(-4px)';
        card.style.boxShadow = '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)';
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '';
        });
    }

    smoothScrollTo(target) {
        const element = document.querySelector(target);
        if (element) {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    toggleMobileMenu() {
        const mobileMenu = document.querySelector('.mobile-menu');
        if (mobileMenu) {
            mobileMenu.classList.toggle('mobile-menu-open');
        }
    }

    // Utility methods
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert-modern alert-modern-${type} fade-in`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    showLoading(element) {
        const spinner = document.createElement('div');
        spinner.className = 'spinner-modern';
        element.appendChild(spinner);
        
        return () => {
            spinner.remove();
        };
    }

    // Dashboard enhancements
    enhanceDashboard() {
        this.setupDashboardCards();
        this.setupCharts();
        this.setupRealTimeUpdates();
    }

    setupDashboardCards() {
        document.querySelectorAll('.dashboard-card').forEach(card => {
            // Add hover effects
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'scale(1.02)';
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'scale(1)';
            });
        });
    }

    setupCharts() {
        // Enhanced chart interactions
        document.querySelectorAll('.chart-container').forEach(chart => {
            chart.addEventListener('mouseenter', () => {
                chart.style.transform = 'scale(1.05)';
            });
            
            chart.addEventListener('mouseleave', () => {
                chart.style.transform = 'scale(1)';
            });
        });
    }

    setupRealTimeUpdates() {
        // Real-time data updates with smooth transitions
        setInterval(() => {
            this.updateDashboardData();
        }, 30000); // Update every 30 seconds
    }

    updateDashboardData() {
        // Fetch and update dashboard data with animations
        fetch('/api/method/ui_ux_upgrade.api.get_dashboard_data')
            .then(response => response.json())
            .then(data => {
                this.animateValueChanges(data);
            })
            .catch(error => {
                console.error('Error updating dashboard:', error);
            });
    }

    animateValueChanges(data) {
        // Animate value changes in dashboard cards
        Object.entries(data).forEach(([key, value]) => {
            const element = document.querySelector(`[data-metric="${key}"]`);
            if (element) {
                this.animateNumber(element, value);
            }
        });
    }

    animateNumber(element, targetValue) {
        const currentValue = parseInt(element.textContent) || 0;
        const increment = (targetValue - currentValue) / 30;
        let current = currentValue;
        
        const timer = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= targetValue) || 
                (increment < 0 && current <= targetValue)) {
                element.textContent = targetValue;
                clearInterval(timer);
            } else {
                element.textContent = Math.round(current);
            }
        }, 50);
    }
}

// Initialize Modern UI when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.modernUI = new ModernUI();
    
    // Enhance dashboard if on dashboard page
    if (document.querySelector('.dashboard')) {
        window.modernUI.enhanceDashboard();
    }
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ModernUI;
}
