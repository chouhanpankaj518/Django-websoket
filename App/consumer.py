from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
import json
import asyncio
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept() 
        group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(
            group_name,
            self.channel_name)
        
        
        
    async def receive(self,text_data = None):
        data = json.loads(text_data)
        msg = data.get('msg', "")
       
        group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_send(
            group_name,
            {
                'type':'chat_message',
                'message':msg
            }
        )
    async def chat_message(self, event):
           
            message = event['message']
            await self.send(text_data=json.dumps({
             'message': message,
             }))
        
        
    async def disconnect(self,event):
        print("socket disconnected **")
        group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_discard(group_name,self.channel_name)
        