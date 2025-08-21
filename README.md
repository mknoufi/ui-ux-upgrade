# UI/UX Upgrade App for ERPNext

A comprehensive UI/UX enhancement package for ERPNext that provides modern design elements, improved user experience, and enhanced visual appeal.

## 🎨 Features

### Modern Design System
- **Color Palette**: Modern, accessible colors
- **Typography**: Improved font system  
- **Spacing**: Consistent spacing system
- **Shadows**: Subtle depth effects
- **Border Radius**: Modern rounded corners

### Enhanced Components
- **Modern Cards**: Hover effects and transitions
- **Glassmorphism**: Modern glass effects
- **Enhanced Buttons**: Ripple effects
- **Modern Forms**: Improved input styling
- **Enhanced Tables**: Better readability
- **Modern Navigation**: Improved sidebar

### Interactive Features
- **Smooth Animations**: Fade-in and slide-up
- **Hover Effects**: Subtle transformations
- **Loading States**: Modern spinners
- **Responsive Design**: Mobile-friendly
- **Dark Mode**: Automatic detection

### Theme Management
- **Multiple Themes**: Light, Dark, and Custom themes
- **Theme Switcher**: Easy theme switching
- **Custom CSS**: Support for custom CSS code
- **Color Customization**: Primary and secondary color options

### 🔄 Upgrade Management
- **Automatic Update Checks**: Daily monitoring for new versions
- **Release Notes**: View what's new in updates
- **Upgrade Instructions**: Step-by-step guidance
- **Version Tracking**: Monitor current and available versions

### 💡 Smart Suggestions
- **UI/UX Analysis**: Intelligent recommendations for improvements
- **Category-based Suggestions**: Theme, Performance, Accessibility, UX
- **Priority System**: High, Medium, Low priority suggestions
- **Action Guidance**: Clear steps for implementing suggestions
- **Modern Color Palette**: Carefully selected colors for better visual hierarchy
- **Typography**: Improved font system with better readability
- **Spacing System**: Consistent spacing using CSS custom properties
- **Border Radius**: Modern rounded corners for a softer look
- **Shadows**: Subtle shadows for depth and elevation

### Enhanced Components
- **Modern Cards**: Hover effects and smooth transitions
- **Glassmorphism**: Modern glass-like effects
- **Enhanced Buttons**: Ripple effects and better interactions
- **Modern Forms**: Improved input styling and focus states
- **Enhanced Tables**: Better readability and hover effects
- **Modern Navigation**: Improved sidebar and navigation elements

### Interactive Features
- **Smooth Animations**: Fade-in and slide-up animations
- **Hover Effects**: Subtle transformations on hover
- **Loading States**: Modern loading spinners
- **Responsive Design**: Mobile-friendly interface
- **Dark Mode Support**: Automatic dark mode detection

### Theme Management
- **Multiple Themes**: Light, Dark, and Custom themes
- **Theme Switcher**: Easy theme switching
- **Custom CSS**: Support for custom CSS code
- **Color Customization**: Primary and secondary color options

## 🚀 Installation

### Prerequisites
- ERPNext v15 or higher
- Frappe Framework v15 or higher

### Installation Steps

1. **Clone the App**
   ```bash
   cd apps
   git clone https://github.com/mknoufi/ui-ux-upgrade.git
   ```

2. **Install the App**
   ```bash
   bench --site your-site.com install-app ui_ux_upgrade
   ```

3. **Build Assets**
   ```bash
   bench build --app ui_ux_upgrade
   ```

4. **Restart Services**
   ```bash
   bench restart
   ```

## 📁 App Structure

```
ui_ux_upgrade/
├── ui_ux_upgrade/
│   ├── config/
│   │   └── desktop.py          # Desktop configuration
│   ├── install/
│   │   └── after_install.py    # Installation setup
│   ├── public/
│   │   ├── css/
│   │   │   └── modern-ui.css   # Main CSS file
│   │   └── js/
│   │       └── modern-ui.js    # Main JavaScript file
│   └── __init__.py
├── hooks.py                    # App configuration
├── modules.txt                 # Module definitions
└── README.md                   # This file
```

## 🎯 Usage

### Basic Usage
The app automatically enhances existing ERPNext elements with modern styling. No additional configuration is required.

### Customization

#### 1. Theme Settings
Navigate to **UI Settings** to configure:
- Enable/disable animations
- Choose theme (Default, Dark, Light, Custom)
- Enable glassmorphism effects
- Enable shadows

#### 2. Theme Manager
Use **Theme Manager** to:
- Create custom themes
- Set primary and secondary colors
- Add custom CSS code

#### 3. Modern Dashboard
Access the enhanced dashboard at `/modern-dashboard` for:
- Improved card layouts
- Better data visualization
- Enhanced interactions

### CSS Classes

#### Modern Components
```css
/* Modern Cards */
.modern-card

/* Glassmorphism Effect */
.glassmorphism

/* Modern Buttons */
.btn-modern
.btn-modern-primary
.btn-modern-secondary

/* Modern Forms */
.form-modern
.input-modern

/* Modern Tables */
.table-modern

/* Modern Alerts */
.alert-modern
.alert-modern-success
.alert-modern-warning
.alert-modern-error
```

#### Animation Classes
```css
/* Fade In Animation */
.fade-in

/* Slide Up Animation */
.slide-up

/* Loading Spinner */
.spinner-modern
```

## 🔧 Configuration

### Custom Themes
1. Go to **Theme Manager**
2. Click **New**
3. Set theme name and colors
4. Add custom CSS if needed
5. Save and apply

### UI Settings
1. Navigate to **UI Settings**
2. Configure your preferences:
   - **Enable Animations**: Toggle smooth animations
   - **Modern Theme**: Choose your preferred theme
   - **Enable Glassmorphism**: Toggle glass effects
   - **Enable Shadows**: Toggle shadow effects

## 🎨 Customization

### Adding Custom CSS
```css
/* Add to Theme Manager or custom CSS file */
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
}

.custom-element {
    background: var(--primary-color);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
}
```

### JavaScript Enhancements
```javascript
// Access the ModernUI instance
window.modernUI.showNotification('Hello World!', 'success');

// Show loading state
const hideLoading = window.modernUI.showLoading(element);
// ... do something
hideLoading();
```

## 📱 Responsive Design

The app includes responsive design features:
- Mobile-friendly navigation
- Responsive cards and tables
- Touch-friendly interactions
- Adaptive layouts

## 🌙 Dark Mode

Automatic dark mode support:
- Detects system preference
- Smooth theme transitions
- Consistent color scheme
- Preserved user preferences

## 🔄 Updates

### Updating the App
```bash
cd apps/ui_ux_upgrade
git pull origin main
bench build --app ui_ux_upgrade
bench restart
```

### Version History
- **v1.0.0**: Initial release with modern design system
- **v1.1.0**: Added theme manager and customization options
- **v1.2.0**: Enhanced animations and interactions

## 🐛 Troubleshooting

### Common Issues

1. **Styles Not Loading**
   ```bash
   bench build --app ui_ux_upgrade
   bench restart
   ```

2. **JavaScript Errors**
   - Check browser console for errors
   - Ensure all assets are built
   - Clear browser cache

3. **Theme Not Applying**
   - Check UI Settings configuration
   - Verify theme exists in Theme Manager
   - Clear browser cache

### Debug Mode
Enable debug mode in UI Settings to see detailed logs and error messages.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Contact: support@emart.com
- Documentation: [Link to docs]

## 🙏 Acknowledgments

- ERPNext Community
- Frappe Framework Team
- Modern UI/UX Design Principles
- CSS Grid and Flexbox

---

**Made with ❤️ by E-Mart Systems**
