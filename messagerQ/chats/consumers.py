from channels.consumer import AsyncConsumer
from .models import * 
from channels.db import database_sync_to_async
import json

class YourConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        data = json.loads(text_data['text'])
        sender_id = data['user_id']
        sender = await database_sync_to_async(User.objects.get)(id=sender_id)
        chat_id = chat = data['chat_id']
        chat = await database_sync_to_async(Chats.objects.get)(id=chat_id)
        message = Messages(text = data['message'],
                           sender = sender,
                           chat = chat,
                           )
        await database_sync_to_async(message.save)()
        time_only = message.created_at.strftime('%H:%M')
        message = json.loads(text_data['text'])['message']
        await self.send({
            "type": "websocket.send",
            "text": f'{time_only}: {sender.username}: {message}' ,
            "button": data['type'],
        })
        await self.send({
            "type": "websocket.send",
            "text": "update",
        })
        
    async def websocket_disconnect(self, event):
        pass