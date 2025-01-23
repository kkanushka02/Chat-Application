# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']  # Get the current user from the scope
        self.room_name = self.scope['url_route']['kwargs']['room_name']  # Room name from URL
        self.room_group_name = f'chat_{self.room_name}'  # Group name for the chat room

        # Add the user to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the room group on disconnect
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        data = json.loads(text_data)
        message = data['message']
        receiver_id = data['receiver_id']

        try:
            # Fetch the receiver user object
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            return  # Handle the case where the receiver does not exist

        # Save the message to the database
        msg = Message.objects.create(sender=self.user, receiver=receiver, content=message)

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,  # Corrected typo here
            {
                'type': 'chat_message',  # Event type
                'message': msg.content,
                'sender': self.user.username,
                'timestamp': str(msg.timestamp),
            }
        )

    async def chat_message(self, event):
        # Receive the message from the group
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'timestamp': timestamp,
        }))
