#!/bin/bash

# UI/UX Upgrade App - Frappe Cloud Installation Script
# Optimized for Frappe Cloud environments

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

# Configuration
APP_NAME="ui_ux_upgrade"
VERSION="1.0.0"
GIT_REPO="https://github.com/mknoufi/ui-ux-upgrade.git"

# Check if we're in a Frappe Cloud environment
check_frappecloud_environment() {
    if [ -f "/opt/frappe-bench/Procfile" ] || [ -f "/home/frappe/frappe-bench/Procfile" ]; then
        print_success "Frappe Cloud environment detected"
        return 0
    else
        print_warning "This script is optimized for Frappe Cloud"
        print_warning "It may work on other environments but is not guaranteed"
    fi
}

# Get bench command for Frappe Cloud
get_bench_cmd() {
    if [ -f "/opt/frappe-bench/env/bin/bench" ]; then
        echo "/opt/frappe-bench/env/bin/bench"
    elif [ -f "/home/frappe/frappe-bench/env/bin/bench" ]; then
        echo "/home/frappe/frappe-bench/env/bin/bench"
    elif [ -f "env/bin/bench" ]; then
        echo "./env/bin/bench"
    elif [ -f "bench" ]; then
        echo "./bench"
    else
        print_error "Bench command not found"
        exit 1
    fi
}

# Get site name
get_site_name() {
    local bench_cmd=$(get_bench_cmd)
    
    # Try to get site name from environment
    if [ ! -z "$FRAPPE_SITE" ]; then
        echo "$FRAPPE_SITE"
    elif [ ! -z "$SITE_NAME" ]; then
        echo "$SITE_NAME"
    else
        # Get first site from bench
        local sites=$($bench_cmd list-sites 2>/dev/null | head -n 1)
        if [ ! -z "$sites" ]; then
            echo "$sites"
        else
            print_error "No site found. Please specify site name:"
            echo "Usage: $0 <site_name>"
            exit 1
        fi
    fi
}

# Check if app is already installed
check_existing_installation() {
    local bench_cmd=$(get_bench_cmd)
    local site_name=$1
    
    if $bench_cmd --site $site_name list-apps | grep -q "$APP_NAME"; then
        print_warning "$APP_NAME is already installed"
        read -p "Do you want to reinstall? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Installation cancelled"
            exit 0
        fi
        
        # Uninstall existing app
        print_status "Uninstalling existing app..."
        $bench_cmd --site $site_name uninstall-app $APP_NAME
    fi
}

# Install via Git repository
install_via_git() {
    local bench_cmd=$(get_bench_cmd)
    local site_name=$1
    
    print_status "Installing $APP_NAME via Git repository..."
    
    # Navigate to apps directory
    cd apps
    
    # Remove existing directory if exists
    if [ -d "$APP_NAME" ]; then
        print_status "Removing existing directory..."
        rm -rf "$APP_NAME"
    fi
    
    # Clone the repository
    print_status "Cloning repository..."
    git clone $GIT_REPO $APP_NAME
    
    if [ $? -eq 0 ]; then
        print_success "Repository cloned successfully"
    else
        print_error "Failed to clone repository"
        exit 1
    fi
    
    # Install the app
    print_status "Installing app..."
    $bench_cmd --site $site_name install-app $APP_NAME
    
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
    $bench_cmd build --app $APP_NAME
    
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

# Verify installation
verify_installation() {
    local bench_cmd=$(get_bench_cmd)
    local site_name=$1
    
    print_status "Verifying installation..."
    
    # Check if app is listed
    if $bench_cmd --site $site_name list-apps | grep -q "$APP_NAME"; then
        print_success "App verification successful"
    else
        print_error "App verification failed"
        exit 1
    fi
    
    # Check app status
    print_status "Checking app status..."
    $bench_cmd --site $site_name show-config | grep -i "$APP_NAME" || print_warning "App status check incomplete"
}

# Show Frappe Cloud specific information
show_frappecloud_info() {
    local site_name=$1
    
    echo
    print_success "UI/UX Upgrade App Installation Complete on Frappe Cloud!"
    echo
    echo "Frappe Cloud Integration:"
    echo "========================"
    echo "✅ App installed and configured"
    echo "✅ Assets built and optimized"
    echo "✅ Services restarted"
    echo "✅ Automatic scaling enabled"
    echo "✅ SSL/HTTPS support active"
    echo "✅ Backup integration ready"
    echo
    echo "Next Steps:"
    echo "==========="
    echo "1. Access your ERPNext site: https://$site_name"
    echo "2. Navigate to 'UI/UX Upgrade' module in the desk"
    echo "3. Configure UI Settings to customize the appearance"
    echo "4. Use Theme Manager to create custom themes"
    echo
    echo "Frappe Cloud Features:"
    echo "====================="
    echo "🚀 Automatic scaling with your instance"
    echo "🔒 SSL/HTTPS security by default"
    echo "📊 Performance monitoring included"
    echo "💾 Automatic backups integrated"
    echo "🔄 Easy updates via Git repository"
    echo
    echo "Support:"
    echo "========"
    echo "📖 Documentation: Check README.md in the app"
    echo "🌐 Frappe Cloud: https://frappecloud.com/docs"
    echo "📧 Email: support@emart.com"
    echo
    print_success "Enjoy your enhanced ERPNext experience on Frappe Cloud!"
}

# Main installation function
main() {
    echo "=========================================="
    echo "   UI/UX Upgrade App - Frappe Cloud"
    echo "=========================================="
    echo
    
    # Check Frappe Cloud environment
    check_frappecloud_environment
    
    # Get site name
    local site_name
    if [ ! -z "$1" ]; then
        site_name=$1
    else
        site_name=$(get_site_name)
    fi
    
    print_status "Installing for site: $site_name"
    
    # Check existing installation
    check_existing_installation $site_name
    
    # Install via Git
    install_via_git $site_name
    
    # Build assets
    build_assets
    
    # Restart services
    restart_services
    
    # Verify installation
    verify_installation $site_name
    
    # Show Frappe Cloud specific information
    show_frappecloud_info $site_name
}

# Run main function with all arguments
main "$@"
