import os            
import environ
import cloudinary
from pathlib import Path


# 1. Configuração do Diretório Base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Inicialização do django-environ para ler o ficheiro .env
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = "django-insecure-h+0%xfs3n)!3j6$4lx*kqm^je*j-a(zql4u_t*r1!mfvzyc82+"
DEBUG = True

ALLOWED_HOSTS = ['*']

# 3. Aplicações do Projeto (Atualizado com Cloudinary)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",           # <-- Inserido antes do staticfiles
    "django.contrib.staticfiles",
    "cloudinary",                   # <-- Inserido após o staticfiles
    "portfolio",
    "accounts",
]

LOGIN_REDIRECT_URL = 'portfolio:home'
LOGOUT_REDIRECT_URL = 'portfolio:home'

# 4. Middlewares (Atualizado com WhiteNoise)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <-- WhiteNoise para ficheiros estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

# 5. Templates / HTML
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# 6. Ligação à Base de Dados do Neon (lida diretamente do .env)
# 6. Ligação à Base de Dados do Neon (Lê do Render ou do .env local)
import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# 7. Validação de Passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 8. Internacionalização e Fuso Horário
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
cloudinary.config(
    from_url=env('CLOUDINARY_URL')
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
BASE_URL = 'http://localhost:8000'