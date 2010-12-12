DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.database',
    }
}
ROOT_URLCONF = 'src.urls'
INSTALLED_APPS = (
	'djcelery',
	'ghettoq',
	'blog',
)
AMQP_SERVER = "127.0.0.1"
AMQP_PORT = 5672
AMQP_USER = "myuser"
AMQP_PASSWORD = "mypassword"
AMQP_VHOST = "myvhost"

import djcelery
djcelery.setup_loader()
