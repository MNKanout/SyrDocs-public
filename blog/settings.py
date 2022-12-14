'''Syrdocs settings'''
import os
import json
import django_heroku

class MissingConfigration(Exception):
    '''Missing configration'''


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS = ['syrwegian.com','45.132.241.24','localhost',"syrnotebook-0-1.herokuapp.com"]

# CKeditor settings
CKEDITOR_CONFIGS = {
    'default': {
        'disableNativeSpellChecker' : False,
        "removePlugins": "contextMenu",
    },
}

# TinyMCE settings
TINYMCE_DEFAULT_CONFIG = {
    "selector": "textarea",
    "plugins": '''export, pagebreak, code, emoticons, image,
    table, paste, lists,advlist, checklist, link, hr, charmap,
    directionality,table,spellchecker,paste,searchreplace,autoresize,
    directionality,export,fullpage''',
    "toolbar": '''undo redo styleselect bold italic  toolbar alignleft
    aligncenter alignright forecolor backcolor linkimage fullpage export pagebreak | 
    formatselect fontselect fontsizeselect bold 
    italic underline strikethrough forecolor backcolor subscript superscript | 
    alignleft aligncenter alignright alignjustify indent outdent rtl ltr | 
    bullist numlist checklist | 
    emoticons image table link hr charmap''',
    "custom_undo_redo_levels": 10,
    "menubar": False,
    "browser_spellcheck": True,
    "resize": False,
    "branding": False,
    "toolbar_mode": "floating",
}
# Application definition
INSTALLED_APPS = [
    #My apps
    'blogs',
    'users',
    'dictionaries',

    #Thirdparty apps
    'bootstrap4',
    'tinymce',

    #Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


#DATABASE_URL
django_heroku.settings(locals())



# Get credentials from config file
try:
    with open("config.json",encoding='utf-8') as f:
        data = json.load(f)
        print(data["NAME"])
        #Core
        SECRET_KEY = data['SECRET_KEY']

        #Debug
        debug = data["DEBUG"]
        if debug == "True":
            DEBUG = True
        else:
            DEBUG = False
        # Database
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': data["NAME"],
                'USER': data["USER"],
                'PASSWORD': data["PASSWORD"],
                'HOST': data["HOST"],
                'PORT': '5432',
            }
        }
# Get credentials from enviroment variables
except FileNotFoundError as error:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise MissingConfigration('No project configration was found') from error
    debug = os.environ.get('DEBUG')
    if debug == "True":
        DEBUG = True
    else:
        DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("NAME"),
            'USER': os.environ.get("USER"),
            'PASSWORD': os.environ.get("PASSWORD"),
            'HOST': os.environ.get("HOST"),
            'PORT': '5432',
        }
    }





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'blogs/static'),
    ]

#My settings
LOGIN_URL = 'users:login'
