import os

# This is the main entry point for your Django project.
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import App.routing

# from App import routing

 
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack( 
    URLRouter(
        App.routing.websocket_urlpatterns
    ))
})