# UI/UX Upgrade App - Frappe Cloud Installation Guide

## 🚀 Installing on Frappe Cloud

This guide will help you install the UI/UX Upgrade app on your Frappe Cloud ERPNext instance.

## 📋 Prerequisites

- ✅ **Frappe Cloud Account** with active subscription
- ✅ **ERPNext v15+** instance running on Frappe Cloud
- ✅ **Site Admin** access to your ERPNext instance
- ✅ **Git repository** access (if using Git deployment)

## 🛠️ Installation Methods

### Method 1: Frappe Cloud Dashboard (Recommended)

#### Step 1: Access Frappe Cloud Dashboard
1. Login to [Frappe Cloud Dashboard](https://frappecloud.com)
2. Navigate to your ERPNext site
3. Go to **Apps** section

#### Step 2: Install via Git Repository
1. **Add Git Repository**:
   ```
   Repository URL: https://github.com/emart-systems/ui-ux-upgrade.git
   Branch: main
   ```

2. **Install the App**:
   - Click **"Install App"**
   - Select `ui_ux_upgrade` from the repository
   - Click **"Install"**

3. **Wait for Installation**:
   - Frappe Cloud will automatically:
     - Clone the repository
     - Install dependencies
     - Build assets
     - Restart services

#### Step 3: Verify Installation
1. Access your ERPNext site
2. Look for **"UI/UX Upgrade"** in the modules list
3. Navigate to **UI Settings** to configure

### Method 2: Manual Installation via Bench Console

#### Step 1: Access Bench Console
1. In Frappe Cloud Dashboard, go to your site
2. Click **"Bench Console"**
3. Wait for the console to load

#### Step 2: Install the App
```bash
# Navigate to apps directory
cd apps

# Clone the repository
git clone https://github.com/emart-systems/ui-ux-upgrade.git

# Install the app
bench --site your-site-name install-app ui_ux_upgrade

# Build assets
bench build --app ui_ux_upgrade

# Restart services
bench restart
```

### Method 3: Custom App Installation

#### Step 1: Upload Package
1. Download the package: `ui_ux_upgrade-1.0.0.tar.gz`
2. In Frappe Cloud Dashboard, go to **Files**
3. Upload the package to your site

#### Step 2: Install via Console
```bash
# Extract the package
cd apps
tar -xzf /path/to/ui_ux_upgrade-1.0.0.tar.gz

# Install the app
bench --site your-site-name install-app ui_ux_upgrade

# Build assets
bench build --app ui_ux_upgrade

# Restart services
bench restart
```

## ⚙️ Configuration

### Step 1: Access UI Settings
1. Login to your ERPNext site
2. Navigate to **Desk** → **UI/UX Upgrade** → **UI Settings**
3. Or search for "UI Settings" in the search bar

### Step 2: Configure Preferences
- **Enable Animations**: Toggle smooth animations
- **Modern Theme**: Choose theme (Default, Dark, Light, Custom)
- **Enable Glassmorphism**: Toggle glass effects
- **Enable Shadows**: Toggle shadow effects

### Step 3: Theme Management
1. Go to **Theme Manager** to create custom themes
2. Set primary and secondary colors
3. Add custom CSS if needed

## 🔧 Frappe Cloud Specific Commands

### Check App Status
```bash
# List installed apps
bench --site your-site-name list-apps

# Check app status
bench --site your-site-name show-config
```

### Update App
```bash
# Update from Git repository
cd apps/ui_ux_upgrade
git pull origin main

# Rebuild assets
bench build --app ui_ux_upgrade

# Restart services
bench restart
```

### Uninstall App
```bash
# Uninstall the app
bench --site your-site-name uninstall-app ui_ux_upgrade

# Remove from apps directory
rm -rf apps/ui_ux_upgrade
```

## 📱 Frappe Cloud Features

### Automatic Scaling
- The app automatically scales with your Frappe Cloud instance
- No additional configuration needed for performance

### Backup Integration
- App data is automatically included in Frappe Cloud backups
- No manual backup configuration required

### SSL/HTTPS Support
- Automatically works with Frappe Cloud SSL certificates
- Secure connections by default

### Monitoring
- App performance is monitored by Frappe Cloud
- Automatic alerts for any issues

## 🐛 Troubleshooting

### Common Issues on Frappe Cloud

#### 1. Installation Fails
```bash
# Check bench environment
bench version

# Check site configuration
bench --site your-site-name show-config

# Check logs
bench --site your-site-name logs
```

#### 2. Assets Not Loading
```bash
# Rebuild assets
bench build --app ui_ux_upgrade

# Clear cache
bench --site your-site-name clear-cache

# Restart services
bench restart
```

#### 3. Module Not Visible
```bash
# Check app installation
bench --site your-site-name list-apps

# Clear desk cache
bench --site your-site-name clear-cache

# Check for conflicts
bench --site your-site-name logs
```

### Frappe Cloud Support

If you encounter issues:

1. **Check Frappe Cloud Status**: Visit [Frappe Cloud Status](https://status.frappecloud.com)
2. **Review Logs**: Use the logs section in Frappe Cloud Dashboard
3. **Contact Support**: Use Frappe Cloud support channels
4. **Community Help**: Post in Frappe Cloud community forums

## 🔄 Updates

### Automatic Updates
If you installed via Git repository:
1. Frappe Cloud can automatically update the app
2. Configure auto-updates in your site settings
3. Manual updates available via bench console

### Manual Updates
```bash
# Update the app
cd apps/ui_ux_upgrade
git pull origin main

# Rebuild assets
bench build --app ui_ux_upgrade

# Restart services
bench restart
```

## 📊 Performance on Frappe Cloud

### Optimizations
- **CDN Integration**: Assets served via Frappe Cloud CDN
- **Caching**: Automatic caching for better performance
- **Compression**: Assets automatically compressed
- **Minification**: CSS/JS automatically minified

### Monitoring
- **Resource Usage**: Monitor via Frappe Cloud Dashboard
- **Performance Metrics**: Available in site analytics
- **Error Tracking**: Automatic error reporting

## 🛡️ Security

### Frappe Cloud Security Features
- **Automatic Updates**: Security patches applied automatically
- **SSL/TLS**: Secure connections by default
- **Firewall**: Built-in firewall protection
- **Backup Security**: Encrypted backups

### Best Practices
1. **Keep Updated**: Enable automatic updates
2. **Monitor Logs**: Regularly check site logs
3. **Use HTTPS**: Always use secure connections
4. **Regular Backups**: Ensure backups are working

## 📞 Support

### Frappe Cloud Support
- **Documentation**: [Frappe Cloud Docs](https://frappecloud.com/docs)
- **Community**: [Frappe Cloud Community](https://community.frappecloud.com)
- **Support**: Contact via Frappe Cloud Dashboard

### UI/UX Upgrade Support
- **Documentation**: Check README.md in the app
- **Issues**: Create GitHub issue
- **Email**: support@emart.com

## 🎯 Quick Start Checklist

- [ ] Frappe Cloud account active
- [ ] ERPNext v15+ instance running
- [ ] Git repository added to Frappe Cloud
- [ ] App installed successfully
- [ ] Assets built and deployed
- [ ] UI Settings configured
- [ ] Theme Manager set up
- [ ] Tested on different devices
- [ ] Performance verified

---

**Made with ❤️ by E-Mart Systems**

For more information, visit: https://github.com/emart-systems/ui-ux-upgrade
