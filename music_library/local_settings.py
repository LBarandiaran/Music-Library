# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g@02@8x89*loc1tmyc_jq(op9mzv1x((kp-^kddyha(qgcp^nl'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'Pa$$word',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}