

from os import getenv
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env.local'

DVELOPMENT_MODE = getenv('DVELOPMENT_MODE', 'False') == 'True'

if Path.is_file(dotenv_file):
  dotenv.load_dotenv(dotenv_file )


SECRET_KEY = getenv('DJANGO-SECRET_KEY', get_random_secret_key())


DEBUG = getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1, localhost').split(',')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djoser',
    'corsheaders',
    'social_django',
    'storages',
    'rest_framework',
    'users'
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.CustomJWTAuthentication'
    ]
}

DJOSER = {
  'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
  'SEND_ACTIVATION_EMAIL': True,
  'ACTIVATION_URL': 'activation/{uid}/{token}',
  'USER_CREATEdf_PASSWORD_RETYPE': False,
  'TOKEN_MODEL': None,
  'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS':getenv('REDIRECT_URLS').split(',')
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auth.urls'

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

WSGI_APPLICATION = 'auth.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# email settings
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_ACCESS_KEY_ID=''
AWS_SES_SECRET_ACCESS_KEY=''
AWS_SES_REGION_NAME=''
AWS_SES_REGION_ENDPOINT=''


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

if DEVELOPMENT_MODE is True:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media'
else:
   


AUTH_USER_MODEL ='users.UserAccount'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 5
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv('GOOGLE_AUTH_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('GOOGLE_AUTH_SECRET_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            
        },
    },
}



CORS_ALLOWED_ORIGINS = getenv('CORS_ALLOWED_ORIGINS','http://localhost:3000,http://localhost:127.0.0.1:3000'.split(','))
CORS_ALLOWED_CREDENTIALS = True