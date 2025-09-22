"""
Django settings for cd_spec_viewer_web_site project.
There are parts of this file and the django admin
page that need to be updated when this is deployed
The parts of this file that need updating will be marked
with (UPDATE ON RELEASE)
"""
import os

# Paths used for file navigation by the program, setting the base directory
# and then the program will navigate from there automatiocally
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
# Key used to pair with google and allows for google authentication
# Sign in with google (needs to be changed to special email when released)
# (UPDATE ON RELEASE)
SECRET_KEY = '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'

# SECURITY WARNING: don't run with debug turned on in production!
# When you go to a page with an error, when enabled this displays
# the error on the page. When disabled, display a regular redirect error
# (UPDATE ON RELEASE)
DEBUG = True

# What hosts django allows to save the site, when released into production
# remove everything except 'cdspeccollab.smcm.edu' to prevent security vulnerabilities
# (UPDATE ON RELEASE)
ALLOWED_HOSTS = ['cdspeccollab.smcm.edu', 'localhost', '127.0.0.1', '*']


# Application definition, various "apps" that django uses for the website
INSTALLED_APPS = [
    'cdspec.apps.CdspecConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    "crispy_forms",
    "crispy_bootstrap4",

    # Google Auth Apps
    'users',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

# The social accounts you can log in with (only google)
SOCIALACCOUNT_PROVIDERS = { 
    "google": {
        "SCOPE": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {"access_type": "online"}
    }
}

# Various middlewares that django uses to make the program run properly
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
]
# Tells django what dirctory contains the urls.py file, which is necessary
# for in website navigation
ROOT_URLCONF = 'cd_spec_viewer_web.urls'

# The templates django uses, and the directory they're stored at
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Python standard for website server integration
WSGI_APPLICATION = 'cd_spec_viewer_web.wsgi.application'

# Used for incrementing BIGINTS inside of databases
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# The database that django uses for the storage of all on site information
# Specified database configuration and how the website should connect to it
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'PASS',
        'HOST': '127.0.0.1', # Means database is on same machine as the site
        'PORT': '5432',
    }
}


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
# How the website does account authentication
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
# How the website authenticates users 
AUTH_USER_MODEL = "users.User"

# The site ID the site these settings apply to in the django admin
SITE_ID = 2 # (UPDATE ON RELEASE), likely needs changed to 3

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
# How the site stores passwords and the hashers it uses for them
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# How django allauth will verify passwords and accounts
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
# How django renders the cripsy forms for login
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
# The template used for account creation and logging in
CRISPY_TEMPLATE_PACK = "bootstrap4"

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = False #TODO This is only required for offline.
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True

# EMAIL
# ------------------------------------------------------------------------------
# The below line sends emails to the console rather than the intended recipient,
# use for testing purposes
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sends confirmation emails using the gmail smtp backend. 
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "bedinger@smcm.edu" # What email sends the confirmation email (UPDATE ON RELEASE)
EMAIL_HOST_PASSWORD = "pnnvmfrufmpbwcxh" # Needs to be gotten from host user email (UPDATE ON RELEASE)
# Do NOT use your email password, get an email app password from google security
# https://itsupport.umd.edu/itsupport?id=kb_article_view&sysparm_article=KB0015112
DEFAULT_FROM_EMAIL = "CD Spec Viewer Web <noreply@example.com>" # Email address the
# confirmation email appears as to the user
EMAIL_TIMEOUT = 5 # If an email takes more that 5 seconds to send to the user, show error
SERVER_EMAIL = DEFAULT_FROM_EMAIL # Email that django uses for sending issues to admins
EMAIL_SUBJECT_PREFIX = "[CD Spec Viewer Web]" # django uses this as an email header prefix


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# When there is an error on the deployed site, they are sent to the below email 
ADMINS = [("""COSC420 SMCM""", "sread@smcm.edu")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# django-allauth / user logging in settings
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"

SOCIALACCOUNT_AUTO_SIGNUP = True  # Automatically create a social account if an email matches
ACCOUNT_AUTHENTICATION_METHOD = "email"  # Makes account authentication use email, confirmation email
ACCOUNT_USERNAME_REQUIRED = True # When you sign up for an account, it requires you to make a username

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# Where when logging in the user is directed to
LOGIN_URL = "account_login"

# When the user logs out or logs in, redirect them to '/' which is the homepage
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_url = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = '/media/'
