#!/bin/bash

# UI/UX Upgrade App Installation Script
# For ERPNext v15+ systems

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in a bench directory
check_bench_environment() {
    if [ ! -f "bench" ] && [ ! -f "env/bin/bench" ]; then
        print_error "This script must be run from a bench directory"
        print_error "Please navigate to your ERPNext bench directory and try again"
        exit 1
    fi
    
    print_success "Bench environment detected"
}

# Get bench command
get_bench_cmd() {
    if [ -f "env/bin/bench" ]; then
        echo "./env/bin/bench"
    elif [ -f "bench" ]; then
        echo "./bench"
    else
        print_error "Bench command not found"
        exit 1
    fi
}

# Check if app is already installed
check_existing_installation() {
    local bench_cmd=$(get_bench_cmd)
    local site_name=$1
    
    if $bench_cmd --site $site_name list-apps | grep -q "ui_ux_upgrade"; then
        print_warning "UI/UX Upgrade app is already installed"
        read -p "Do you want to reinstall? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Installation cancelled"
            exit 0
        fi
    fi
}

# Install the app
install_app() {
    local bench_cmd=$(get_bench_cmd)
    local site_name=$1
    
    print_status "Installing UI/UX Upgrade app..."
    
    # Install the app
    $bench_cmd --site $site_name install-app ui_ux_upgrade
    
    if [ $? -eq 0 ]; then
        print_success "App installed successfully"
    else
        print_error "Failed to install app"
        exit 1
    fi
}

# Build assets
build_assets() {
    local bench_cmd=$(get_bench_cmd)
    
    print_status "Building assets..."
    
    # Build the app assets
    $bench_cmd build --app ui_ux_upgrade
    
    if [ $? -eq 0 ]; then
        print_success "Assets built successfully"
    else
        print_error "Failed to build assets"
        exit 1
    fi
}

# Restart services
restart_services() {
    local bench_cmd=$(get_bench_cmd)
    
    print_status "Restarting services..."
    
    # Restart bench services
    $bench_cmd restart
    
    if [ $? -eq 0 ]; then
        print_success "Services restarted successfully"
    else
        print_warning "Failed to restart services automatically"
        print_status "Please restart your ERPNext services manually"
    fi
}

# Show installation summary
show_summary() {
    local site_name=$1
    
    echo
    print_success "UI/UX Upgrade App Installation Complete!"
    echo
    echo "Installation Summary:"
    echo "====================="
    echo "✅ App installed successfully"
    echo "✅ Assets built and compiled"
    echo "✅ Services restarted"
    echo
    echo "Next Steps:"
    echo "==========="
    echo "1. Access your ERPNext site: http://localhost:8000"
    echo "2. Navigate to 'UI/UX Upgrade' module in the desk"
    echo "3. Configure UI Settings to customize the appearance"
    echo "4. Use Theme Manager to create custom themes"
    echo
    echo "Features Available:"
    echo "=================="
    echo "🎨 Modern design system with enhanced components"
    echo "🌙 Dark mode support"
    echo "📱 Responsive design for mobile devices"
    echo "✨ Smooth animations and transitions"
    echo "🎯 Theme management and customization"
    echo
    echo "Documentation:"
    echo "=============="
    echo "📖 README.md - Complete documentation"
    echo "🔧 UI Settings - Configure app preferences"
    echo "🎨 Theme Manager - Create custom themes"
    echo
    print_success "Enjoy your enhanced ERPNext experience!"
}

# Main installation function
main() {
    echo "=========================================="
    echo "   UI/UX Upgrade App Installation"
    echo "=========================================="
    echo
    
    # Check bench environment
    check_bench_environment
    
    # Get site name
    if [ -z "$1" ]; then
        print_error "Please provide a site name"
        echo "Usage: $0 <site_name>"
        echo "Example: $0 erpnext.local"
        exit 1
    fi
    
    local site_name=$1
    print_status "Installing for site: $site_name"
    
    # Check existing installation
    check_existing_installation $site_name
    
    # Install app
    install_app $site_name
    
    # Build assets
    build_assets
    
    # Restart services
    restart_services
    
    # Show summary
    show_summary $site_name
}

# Run main function with all arguments
main "$@"
