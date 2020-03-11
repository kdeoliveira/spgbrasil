"""
WSGI config for www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import time
import traceback
import signal

from django.core.wsgi import get_wsgi_application

sys.path.append('~/spgbrasil/src/')
sys.path.append('~/spgbrasil/server_env/lib/python3.5/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'www.settings')

try: 
	application = get_wsgi_application()
except Exception:
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(), signal.SIGINT)
		time.sleep(2.5)
