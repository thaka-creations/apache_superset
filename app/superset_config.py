# export SUPERSET_CONFIG_PATH=/app/superset_config

SECRET_KEY = "admin"

# cors configs
ENABLE_CORS = True
CORS_OPTIONS = {
    # allows user to make authenticated requests (allows cookies and credentials to be submitted across domains)
    "supports_credentials": True,
    "origins": ["*"],
    "allow_headers": ["*"],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    # max time for which cors requests can be cached
    "max_age": 600,
}

# talisman configs: handles security headers that help against few common web attacks
# pip install flask-talisman
# Enable Flask-Talisman security headers
# When True, Talisman will add security headers to protect against common web vulnerabilities
# See TALISMAN_CONFIG below for specific header configurations
TALISMAN_ENABLED = True

TALISMAN_CONFIG = {
    "force_https": False,
    "frame_options": "SAMEORIGIN",  # Controls X-Frame-Options header. Options: "SAMEORIGIN", "DENY", or "ALLOW-FROM uri"
    "content_security_policy":{
        "default-src": "'self' 'http://localhost:5500'",
        "script-src": "'self' 'unsafe-eval' 'unsafe-inline' http://localhost:5500",
        "style-src": "'self' 'unsafe-inline' http://localhost:5500",
        "img-src": "'self' data:https://apachesuperset.gateway.scarf.sh",
        "frame-ancestors": "'self' http://localhost:5500",
    },
}
# Feature flags are used to enable/disable specific features in Superset
# See https://superset.apache.org/docs/installation/configuring-superset#feature-flags
# Example flags:
# "ALERT_REPORTS": True,  # Enable scheduled email reports
# "DASHBOARD_NATIVE_FILTERS": True,  # Enable dashboard native filters
# "DASHBOARD_CROSS_FILTERS": True,  # Enable cross-filtering between charts
# "DASHBOARD_RBAC": True,  # Enable role-based access control for dashboards
# "DYNAMIC_PLUGINS": True,  # Enable dynamic loading of viz plugins
# "EMBEDDED_SUPERSET": True,  # Enable embedding Superset into other apps
# "ENABLE_TEMPLATE_PROCESSING": True,  # Enable Jinja templating in SQL Lab
# "SCHEDULED_QUERIES": True,  # Enable scheduling queries in SQL Lab
# "THUMBNAILS": True,  # Enable dashboard thumbnails
# "VERSIONED_EXPORT": True  # Enable export with version information

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_RBAC": True,
    "ENABLE_ROW_LEVEL_SECURITY": True,
    "ENABLE_TEMPLATE_PROCESSING": True 
}



