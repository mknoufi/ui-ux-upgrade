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
