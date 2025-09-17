from django.urls import re_path
import App.consumer

websocket_urlpatterns = [
    # re_path('ws/chat/<str:group_name>/$',consumer.ChatConsumer.as_asgi())
     re_path(r'ws/chat/(?P<group_name>\w+)/$', App.consumer.ChatConsumer.as_asgi()),
     
]