from pathlib import Path
from server.const import HOST_DNS
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=9h+o7t6dv2yn=n03k*r7x7i^m@$dtkt0dbt@p4idpld#pfa5-'

# CSP_DEFAULT_SRC = ["'self'"]
# CSP_SCRIPT_SRC = ["'self'", "https://telegram.org", "'unsafe-inline'"]
# CSP_STYLE_SRC = ["'self'", "https://telegram.org"]
# CSP_IMG_SRC = ["'self'", "data:"]
# CSP_FRAME_ANCESTORS = ["'self'", "https://web.telegram.org"]

# Basic Content Security Policy
CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'", "https://telegram.org"]

# (Optional) If you want to enforce CSP on style or other resources
CSP_STYLE_SRC = ["'self'", "'nonce-{nonce}'"]
CSP_IMG_SRC = ["'self'", "data:"]
CSP_FRAME_ANCESTORS = ["'self'", "https://web.telegram.org"]

# Example security settings
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = ""



DEBUG = True

hosts = [f"https://{HOST_DNS}"]

CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = hosts
ALLOWED_HOSTS = ["*"]
CORS_ORIGINS_WHITELIST = hosts
CSRF_ALLOWED_ORIGINS = hosts

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'corsheaders',
    'api.apps.ApiConfig',
	'tailwind',
    'theme',
	'django_browser_reload',
    'bot.apps.BotConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.CSPNonceMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite', 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]