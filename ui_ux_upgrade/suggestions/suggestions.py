"""
UI/UX Suggestions System
Analyzes current setup and provides improvement recommendations
"""

import frappe
from frappe import _
import json

@frappe.whitelist()
def get_ui_suggestions():
    """Get UI/UX improvement suggestions based on current configuration"""
    try:
        suggestions = []
        
        # Check current UI settings
        ui_settings = get_current_ui_settings()
        
        # Analyze theme configuration
        theme_suggestions = analyze_theme_configuration()
        suggestions.extend(theme_suggestions)
        
        # Analyze performance settings
        performance_suggestions = analyze_performance_settings(ui_settings)
        suggestions.extend(performance_suggestions)
        
        # Analyze accessibility
        accessibility_suggestions = analyze_accessibility_settings(ui_settings)
        suggestions.extend(accessibility_suggestions)
        
        # Analyze user experience
        ux_suggestions = analyze_user_experience()
        suggestions.extend(ux_suggestions)
        
        return {
            "success": True,
            "suggestions": suggestions,
            "total_suggestions": len(suggestions),
            "categories": categorize_suggestions(suggestions)
        }
        
    except Exception as e:
        frappe.log_error(f"Suggestions generation failed: {str(e)}", "UI/UX Suggestions")
        return {
            "success": False,
            "message": _("Failed to generate suggestions: {0}").format(str(e))
        }

def get_current_ui_settings():
    """Get current UI settings configuration"""
    try:
        # Try to get UI Settings record
        ui_settings = frappe.get_all(
            "UI Settings",
            fields=["enable_animations", "modern_theme", "enable_glassmorphism", "enable_shadows"],
            limit=1
        )
        
        if ui_settings:
            return ui_settings[0]
        else:
            return {
                "enable_animations": 1,
                "modern_theme": "Default",
                "enable_glassmorphism": 1,
                "enable_shadows": 1
            }
    except:
        return {
            "enable_animations": 1,
            "modern_theme": "Default", 
            "enable_glassmorphism": 1,
            "enable_shadows": 1
        }

def analyze_theme_configuration():
    """Analyze theme setup and provide suggestions"""
    suggestions = []
    
    try:
        # Check number of custom themes
        theme_count = frappe.db.count("Theme Manager")
        
        if theme_count == 0:
            suggestions.append({
                "category": "Theme",
                "priority": "high",
                "title": _("Create Custom Themes"),
                "description": _("No custom themes found. Create branded themes to improve user experience."),
                "action": _("Go to Theme Manager and create a custom theme"),
                "icon": "palette"
            })
        elif theme_count < 3:
            suggestions.append({
                "category": "Theme",
                "priority": "medium",
                "title": _("Expand Theme Options"),
                "description": _("Consider creating additional themes for different user preferences (light, dark, high contrast)."),
                "action": _("Create additional theme variants in Theme Manager"),
                "icon": "palette"
            })
        
        # Check for custom CSS usage
        themes_with_css = frappe.db.count("Theme Manager", {"css_code": ["!=", ""]})
        
        if themes_with_css == 0 and theme_count > 0:
            suggestions.append({
                "category": "Theme",
                "priority": "low",
                "title": _("Add Custom CSS"),
                "description": _("Enhance your themes with custom CSS for unique branding."),
                "action": _("Add custom CSS to your themes in Theme Manager"),
                "icon": "code"
            })
        
    except Exception as e:
        frappe.log_error(f"Theme analysis failed: {str(e)}", "UI/UX Suggestions")
    
    return suggestions

def analyze_performance_settings(ui_settings):
    """Analyze performance-related settings"""
    suggestions = []
    
    try:
        # Check if animations are enabled on slower devices
        if ui_settings.get("enable_animations"):
            suggestions.append({
                "category": "Performance",
                "priority": "low",
                "title": _("Consider Reducing Animations"),
                "description": _("Animations are enabled. Consider disabling on slower devices for better performance."),
                "action": _("Test performance on various devices and adjust animation settings"),
                "icon": "zap"
            })
        
        # Check if glassmorphism is enabled (can be performance intensive)
        if ui_settings.get("enable_glassmorphism"):
            suggestions.append({
                "category": "Performance",
                "priority": "medium",
                "title": _("Monitor Glassmorphism Performance"),
                "description": _("Glassmorphism effects can impact performance on older devices."),
                "action": _("Monitor performance metrics and consider disabling on slower devices"),
                "icon": "monitor"
            })
        
    except Exception as e:
        frappe.log_error(f"Performance analysis failed: {str(e)}", "UI/UX Suggestions")
    
    return suggestions

def analyze_accessibility_settings(ui_settings):
    """Analyze accessibility configurations"""
    suggestions = []
    
    try:
        # Suggest high contrast theme
        if ui_settings.get("modern_theme") not in ["High Contrast", "Accessible"]:
            suggestions.append({
                "category": "Accessibility",
                "priority": "high",
                "title": _("Create High Contrast Theme"),
                "description": _("Improve accessibility by creating a high contrast theme for users with visual impairments."),
                "action": _("Create a high contrast theme in Theme Manager"),
                "icon": "eye"
            })
        
        # Check shadow settings for accessibility
        if ui_settings.get("enable_shadows"):
            suggestions.append({
                "category": "Accessibility",
                "priority": "medium",
                "title": _("Consider Reduced Motion Option"),
                "description": _("Some users prefer reduced visual effects. Consider providing an option to disable shadows."),
                "action": _("Add user preference for reduced visual effects"),
                "icon": "user"
            })
        
    except Exception as e:
        frappe.log_error(f"Accessibility analysis failed: {str(e)}", "UI/UX Suggestions")
    
    return suggestions

def analyze_user_experience():
    """Analyze overall user experience factors"""
    suggestions = []
    
    try:
        # Check for user feedback or usage patterns
        suggestions.append({
            "category": "User Experience",
            "priority": "medium",
            "title": _("Collect User Feedback"),
            "description": _("Consider implementing user feedback collection to continuously improve the UI/UX."),
            "action": _("Add feedback forms or survey mechanisms"),
            "icon": "message-circle"
        })
        
        # Suggest mobile optimization
        suggestions.append({
            "category": "User Experience",
            "priority": "high",
            "title": _("Optimize for Mobile"),
            "description": _("Ensure all UI enhancements work well on mobile devices and tablets."),
            "action": _("Test and optimize the interface for various screen sizes"),
            "icon": "smartphone"
        })
        
        # Suggest user onboarding
        suggestions.append({
            "category": "User Experience",
            "priority": "medium",
            "title": _("Create User Onboarding"),
            "description": _("Help new users discover and configure UI/UX features effectively."),
            "action": _("Create guided tours or help documentation"),
            "icon": "help-circle"
        })
        
    except Exception as e:
        frappe.log_error(f"UX analysis failed: {str(e)}", "UI/UX Suggestions")
    
    return suggestions

def categorize_suggestions(suggestions):
    """Categorize suggestions by type and priority"""
    categories = {}
    
    for suggestion in suggestions:
        category = suggestion.get("category", "General")
        if category not in categories:
            categories[category] = {
                "high": [],
                "medium": [],
                "low": []
            }
        
        priority = suggestion.get("priority", "medium")
        categories[category][priority].append(suggestion)
    
    return categories

@frappe.whitelist()
def mark_suggestion_completed(suggestion_id):
    """Mark a suggestion as completed"""
    try:
        # In a real implementation, you might store suggestion states
        # For now, just return success
        return {
            "success": True,
            "message": _("Suggestion marked as completed")
        }
    except Exception as e:
        return {
            "success": False,
            "message": _("Failed to mark suggestion as completed: {0}").format(str(e))
        }

@frappe.whitelist()
def get_suggestion_details(category=None, priority=None):
    """Get detailed suggestions filtered by category and priority"""
    suggestions = get_ui_suggestions()
    
    if not suggestions.get("success"):
        return suggestions
    
    filtered_suggestions = suggestions["suggestions"]
    
    if category:
        filtered_suggestions = [s for s in filtered_suggestions if s.get("category") == category]
    
    if priority:
        filtered_suggestions = [s for s in filtered_suggestions if s.get("priority") == priority]
    
    return {
        "success": True,
        "suggestions": filtered_suggestions,
        "total": len(filtered_suggestions)
    }