from django.urls import re_path
import App.consumer

websocket_urlpatterns = [
    re_path('ws/chat/',App.consumer.ChatConsumer.as_asgi())
]
