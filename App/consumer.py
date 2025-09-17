# from channels.generic.websocket import AsyncWebsocketConsumer
# from time import sleep
# import json
# import asyncio

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept() 
#         group_name = self.scope['url_route']['kwargs']['group_name']
#         await self.channel_layer.group_add(
#             group_name,
#             self.channel_name)
        
        
        
#     async def receive(self,text_data = None):
#         from .models import Chat,Group

#         data = json.loads(text_data)
#         msg = data.get('msg', "")
       
#         group_name = self.scope['url_route']['kwargs']['group_name']
        
#         group = Group.objects.get(name=group_name)
        
#         chat = Chat.objects.create(
#             message=msg,
#             group=group
#             )
#         chat.save()
        
#         await self.channel_layer.group_send(
#             group_name,
#             {
#                 'type':'chat_message',
#                 'message':msg
#             }
#         )
#     async def chat_message(self, event):
           
#             message = event['message']
#             await self.send(text_data=json.dumps({
#              'message': message,
#              }))
        
        
        
        
#     async def disconnect(self,event):
#         print("socket disconnected **")
#         group_name = self.scope['url_route']['kwargs']['group_name']
#         await self.channel_layer.group_discard(group_name,self.channel_name)










from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        from .models import Chat, Group
        data = json.loads(text_data)
        msg = data.get('msg', "")

        # ORM calls ko sync_to_async ke andar wrap karo
        group = await sync_to_async(Group.objects.get)(name=self.group_name)
        chat = await sync_to_async(Chat.objects.create)(message=msg, group=group)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': msg
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        }))

    async def disconnect(self, event):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("socket disconnected **")
