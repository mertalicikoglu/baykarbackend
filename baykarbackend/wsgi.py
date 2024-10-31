# baykarbackend/baykarbackend/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Django ayar dosyasını belirtir (proje adı 'baykarbackend' ise)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baykarbackend.settings')

# WSGI uygulaması
application = get_wsgi_application()
