from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, Auction, Property
from datetime import timedelta

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    pass
