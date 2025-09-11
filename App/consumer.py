from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
import json
import asyncio
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept() 
       
        await self.send(text_data="Connection established")
        await self.channel_layer.group_add('chat_group',self.channel_name)
        
        print('channel layer...',self.channel_layer)
        print('channel name...',self.channel_name)
        
    async def receive(self,text_data):
        data = json.loads(text_data)
        msg = data.get('msg', '')
        print("Message from client:", msg)
    
        for i in range(10):
           await self.send(text_data = json.dumps({'count':i}))
           await asyncio.sleep(1)
        
        
        
    async def disconnect(self,event):
        print("socket disconnected **")
        await self.channel_layer.group_discard('chat_group',self.channel_name)
        print("channel layer",self.channel_layer)
        print("channel name",self.channel_name)