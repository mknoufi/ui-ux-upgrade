#!/bin/bash

# UI/UX Upgrade App Packaging Script
# Creates a distributable package for easy installation

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
PACKAGE_NAME="${APP_NAME}-${VERSION}"
DIST_DIR="dist"
PACKAGE_DIR="${DIST_DIR}/${PACKAGE_NAME}"

# Files to include in package
INCLUDE_FILES=(
    "ui_ux_upgrade/"
    "hooks.py"
    "modules.txt"
    "README.md"
    "pyproject.toml"
    "install.sh"
    "LICENSE"
)

# Files to exclude from package
EXCLUDE_PATTERNS=(
    "*.pyc"
    "__pycache__"
    ".git"
    ".gitignore"
    ".DS_Store"
    "*.log"
    "node_modules"
    ".env"
    "*.tmp"
    "*.bak"
)

# Create distribution directory
create_dist_dir() {
    print_status "Creating distribution directory..."
    
    if [ -d "$DIST_DIR" ]; then
        rm -rf "$DIST_DIR"
    fi
    
    mkdir -p "$PACKAGE_DIR"
    print_success "Distribution directory created: $PACKAGE_DIR"
}

# Copy files to package
copy_files() {
    print_status "Copying files to package..."
    
    for file in "${INCLUDE_FILES[@]}"; do
        if [ -e "$file" ]; then
            print_status "Copying: $file"
            cp -r "$file" "$PACKAGE_DIR/"
        else
            print_warning "File not found: $file"
        fi
    done
    
    print_success "Files copied successfully"
}

# Create installation instructions
create_install_instructions() {
    print_status "Creating installation instructions..."
    
    cat > "$PACKAGE_DIR/INSTALL.md" << 'EOF'
# UI/UX Upgrade App Installation

## Quick Installation

1. **Extract the package** to your ERPNext apps directory:
   ```bash
   cd apps
   tar -xzf ui_ux_upgrade-1.0.0.tar.gz
   ```

2. **Run the installation script**:
   ```bash
   cd ui_ux_upgrade-1.0.0
   ./install.sh your-site-name
   ```

## Manual Installation

If you prefer manual installation:

1. **Copy the app** to your ERPNext apps directory:
   ```bash
   cp -r ui_ux_upgrade /path/to/your/erpnext/apps/
   ```

2. **Install the app**:
   ```bash
   bench --site your-site-name install-app ui_ux_upgrade
   ```

3. **Build assets**:
   ```bash
   bench build --app ui_ux_upgrade
   ```

4. **Restart services**:
   ```bash
   bench restart
   ```

## Configuration

After installation:

1. Access your ERPNext site
2. Navigate to "UI/UX Upgrade" module
3. Configure UI Settings
4. Use Theme Manager for customization

## Support

For support and documentation, see README.md
EOF

    print_success "Installation instructions created"
}

# Create version file
create_version_file() {
    print_status "Creating version file..."
    
    cat > "$PACKAGE_DIR/VERSION" << EOF
UI/UX Upgrade App
Version: $VERSION
Build Date: $(date)
Compatible with: ERPNext v15+
EOF

    print_success "Version file created"
}

# Create checksum file
create_checksum() {
    print_status "Creating checksum file..."
    
    cd "$PACKAGE_DIR"
    find . -type f -exec md5sum {} \; > CHECKSUMS.md5
    cd - > /dev/null
    
    print_success "Checksum file created"
}

# Create tar.gz package
create_package() {
    print_status "Creating package archive..."
    
    cd "$DIST_DIR"
    tar -czf "${PACKAGE_NAME}.tar.gz" "$PACKAGE_NAME"
    cd - > /dev/null
    
    print_success "Package created: $DIST_DIR/${PACKAGE_NAME}.tar.gz"
}

# Create zip package
create_zip_package() {
    print_status "Creating ZIP package..."
    
    cd "$DIST_DIR"
    zip -r "${PACKAGE_NAME}.zip" "$PACKAGE_NAME"
    cd - > /dev/null
    
    print_success "ZIP package created: $DIST_DIR/${PACKAGE_NAME}.zip"
}

# Show package information
show_package_info() {
    echo
    print_success "Package Creation Complete!"
    echo
    echo "Package Information:"
    echo "==================="
    echo "Name: $PACKAGE_NAME"
    echo "Version: $VERSION"
    echo "Build Date: $(date)"
    echo
    echo "Created Files:"
    echo "=============="
    echo "📦 $DIST_DIR/${PACKAGE_NAME}.tar.gz"
    echo "📦 $DIST_DIR/${PACKAGE_NAME}.zip"
    echo "📁 $PACKAGE_DIR/ (extracted package)"
    echo
    echo "Package Contents:"
    echo "================="
    echo "✅ UI/UX Upgrade app files"
    echo "✅ Installation script"
    echo "✅ Documentation (README.md)"
    echo "✅ Installation instructions (INSTALL.md)"
    echo "✅ Version information (VERSION)"
    echo "✅ Checksums (CHECKSUMS.md5)"
    echo
    echo "Distribution:"
    echo "============="
    echo "The package can be distributed and installed on other ERPNext systems"
    echo "using the provided installation script or manual instructions."
    echo
    print_success "Package ready for distribution!"
}

# Clean up function
cleanup() {
    if [ "$1" = "clean" ]; then
        print_status "Cleaning up extracted package directory..."
        rm -rf "$PACKAGE_DIR"
        print_success "Cleanup complete"
    fi
}

# Main packaging function
main() {
    echo "=========================================="
    echo "   UI/UX Upgrade App Packaging"
    echo "=========================================="
    echo
    
    # Check if we're in the app directory
    if [ ! -f "hooks.py" ] || [ ! -d "ui_ux_upgrade" ]; then
        print_error "This script must be run from the ui_ux_upgrade app directory"
        exit 1
    fi
    
    # Create distribution
    create_dist_dir
    copy_files
    create_install_instructions
    create_version_file
    create_checksum
    create_package
    create_zip_package
    
    # Show results
    show_package_info
    
    # Clean up if requested
    if [ "$1" = "clean" ]; then
        cleanup clean
    fi
}

# Run main function with arguments
main "$@"
