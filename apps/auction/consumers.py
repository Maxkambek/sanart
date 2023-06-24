import json
from datetime import timedelta
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from accounts.models import User
from auction.models import Auction, Message
from main.models import Property


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        if data['command'] in self.commands:
            self.commands[data['command']](self, data)

    def fetch_messages(self, data):
        auction = Auction.objects.get(id=int(data['auction_id']))
        messages = Message.objects.filter(auction=auction)
        content = {
            'messages': self.messages_to_json(messages),
            'command': 'messages'
        }
        self.send_message(content)

    def new_message(self, data):
        sender = data['from']
        auction_id = int(data['auction_id'])
        sender_user = User.objects.get(id=sender)
        auction = Auction.objects.get(id=auction_id)
        current_price = auction.item.current_price
        message = Message.objects.create(
            sender=sender_user,
            price=data['price'],
            auction=auction
        )
        message.save()
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def fetch_items(self, data):
        print(data)
        auction = Auction.objects.get(id=int(data['auction_id']))
        items = Property.objects.filter(id=auction.item.id)
        content = {
            'items': self.items_to_json(items),
            'command': 'items'
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': message.sender.id,
            'sender': message.sender.phone,
            'price': message.price,
            'timestamp': str((message.time_stamp +
                              timedelta(hours=5.5)).strftime("%H:%M")), }

    def items_to_json(self, items):
        result = []
        for item in items:
            result.append(self.item_to_json(item))
        return result

    def item_to_json(self, item):
        return {
            'name': item.name,
            'item_image': item.property_images.first().image.url,
            'price': item.current_price,
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
        'fetch_items': fetch_items,
    }

    """ 
    1. {
        "command":"fetch_messages",
        "auction_id":"1",
    }
    2. {
        "command":"new_message",
        "from":"1",         //user_id,
        "auction_id":"2",
        "price":"123568"
    }    
    3. {
        "command":"fetch_items",
        "from":"1",         //user_id,
        "auction_id":"2",
    }
    """

    def send_chat_message(self, message):

        print(f'Hello  {message}  ')
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
