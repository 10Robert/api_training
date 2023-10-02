# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
SECRET_KEY = '1YNw_Po*}uxq,.6mtmmz/Z#7q<(|TIUAly6!]H<g`Xmax`;+;;B:zjK\Ua@-J7g'

# DEBUG DEVE SER False em produção
DEBUG = False

# Seu domínio ou IP devem vir aqui
ALLOWED_HOSTS = [
    '34.16.131.251',
]  # Troque * para seu domínio ou IP

# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_account',
        'USER': 'postgres',
        'PASSWORD': '39366856',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}