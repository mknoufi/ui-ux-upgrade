# Upgrade Checker and Suggestions Features

## Overview

The UI/UX Upgrade app now includes two new powerful features:

1. **Upgrade Checker** - Automatically checks for new versions and updates
2. **UI/UX Suggestions** - Provides intelligent recommendations for UI improvements

## Features

### Upgrade Checker

The upgrade checker automatically monitors for new versions of the UI/UX Upgrade app:

- **Automatic Checks**: Daily scheduled checks for updates
- **Version Comparison**: Compares current version with latest GitHub releases
- **Release Notes**: Shows what's new in available updates
- **Upgrade Instructions**: Provides step-by-step upgrade guidance
- **Notification System**: Alerts system managers when updates are available

#### Usage

1. Navigate to **Upgrade Check** in the UI/UX Upgrade module
2. Click **New** to create a manual upgrade check
3. The system will automatically check for updates daily
4. View results in the Upgrade Check list

#### API Endpoints

- `GET /api/method/ui_ux_upgrade.api.get_upgrade_status` - Check for upgrades
- `GET /api/method/ui_ux_upgrade.api.get_upgrade_help` - Get upgrade instructions
- `POST /api/method/ui_ux_upgrade.api.create_upgrade_check_record` - Create upgrade record

### UI/UX Suggestions

The suggestions system analyzes your current UI configuration and provides actionable recommendations:

#### Suggestion Categories

1. **Theme Suggestions**
   - Custom theme creation recommendations
   - Color scheme improvements
   - Branding enhancements

2. **Performance Suggestions**
   - Animation optimization
   - Resource usage improvements
   - Loading speed enhancements

3. **Accessibility Suggestions**
   - High contrast themes
   - Reduced motion options
   - Screen reader compatibility

4. **User Experience Suggestions**
   - Mobile optimization
   - User onboarding improvements
   - Feedback collection systems

#### Usage

1. Navigate to **UI Suggestions** in the UI/UX Upgrade module
2. The system automatically generates suggestions based on your configuration
3. Review suggestions by category and priority
4. Mark suggestions as completed when implemented

#### API Endpoints

- `GET /api/method/ui_ux_upgrade.api.get_suggestions` - Get all suggestions
- `GET /api/method/ui_ux_upgrade.api.get_filtered_suggestions` - Get filtered suggestions
- `POST /api/method/ui_ux_upgrade.api.create_suggestions_records` - Create suggestion records

## Configuration

### Scheduled Tasks

The app includes automated tasks:

- **Daily**: Upgrade checks and suggestion analysis
- **Weekly**: Performance optimization and cleanup

### Permissions

Both features require System Manager or Administrator permissions:

- **Upgrade Check**: System Manager access
- **UI Suggestions**: System Manager and Administrator access

## Installation

These features are automatically installed with the UI/UX Upgrade app. The necessary doctypes and configurations are created during installation.

## Example API Usage

### Check for Upgrades

```javascript
frappe.call({
    method: 'ui_ux_upgrade.api.get_upgrade_status',
    callback: function(r) {
        if (r.message.success && r.message.update_available) {
            console.log('Update available:', r.message.latest_version);
        }
    }
});
```

### Get Suggestions

```javascript
frappe.call({
    method: 'ui_ux_upgrade.api.get_suggestions',
    callback: function(r) {
        if (r.message.success) {
            console.log('Suggestions:', r.message.suggestions);
        }
    }
});
```

## Troubleshooting

### Common Issues

1. **Network Errors**: Ensure internet connectivity for upgrade checks
2. **Permission Errors**: Verify user has System Manager role
3. **API Timeouts**: Check GitHub API rate limits

### Debug Mode

Enable debug mode in UI Settings to see detailed logs and error messages for troubleshooting.