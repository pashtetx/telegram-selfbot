from pyrogram import Client
from .user import on_message
from pyrogram.handlers import MessageHandler

def register_handlers(client: Client):
    handlers = (MessageHandler(on_message),)
    for h in handlers:
        client.add_handler(h)
