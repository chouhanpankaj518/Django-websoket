from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
import json
import asyncio
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # accept the connection
        print("socket connected ***")
        # await self.send({
        #      'type': 'text',
        # })
        await self.send(text_data="Connection established")
        
    async def receive(self,text_data):
        print("received message: ", text_data)
        for i in range(10):
        #    await self.send({
        #     'type': 'websocket.send',
        #     'text': str(i)
        #    })2
           await self.send(text_data = json.dumps({'count':i}))
           await asyncio.sleep(1)
        
    async def disconnect(self,event):
        print("socket disconnected **")