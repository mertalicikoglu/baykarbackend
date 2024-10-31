import os
from pathlib import Path

# BASE_DIR, projenizin ana dizinini temsil eder
BASE_DIR = Path(__file__).resolve().parent.parent

# Gizli anahtar (üretim ortamında bu değeri gizli tutmalısınız)
SECRET_KEY = 'django-insecure-your_secret_key_here'

# Geliştirme için DEBUG aktif, üretimde kapatın
DEBUG = True

# Hangi hostların projeye erişebileceği
ALLOWED_HOSTS = []

# Yüklü Uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin paneli
    'django.contrib.auth',   # Kullanıcı kimlik doğrulama
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',        # Django REST Framework
    'rest_framework.authtoken',  # Token tabanlı kimlik doğrulama
    'app',  # Kendi uygulamanızın adı
]

# Orta Katman (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Oturum yönetimi
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Kullanıcı doğrulama
    'django.contrib.messages.middleware.MessageMiddleware',  # Mesaj yönetimi
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Temel URL Yönlendirmesi
ROOT_URLCONF = 'baykarbackend.urls'

# Şablon Ayarları (TEMPLATES)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Şablonların konumu
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

# WSGI Uygulaması
WSGI_APPLICATION = 'baykarbackend.wsgi.application'

# Veritabanı Ayarları (PostgreSQL kullanıyoruz)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aircraftdb',
        'USER': 'aircraftuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Şifre Doğrulama
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

# Uluslararasılaştırma
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik Dosyalar (CSS, JavaScript, Görseller)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Varsayılan Birincil Anahtar Alan Türü
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework Ayarları
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Yanıtları JSON olarak döndürmek için
    ],
}

DEBUG = True
ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}