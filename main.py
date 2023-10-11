from pyrogram import Client
from dotenv import dotenv_values
from handlers import register_handlers
from config import Config
from commands.commands import register_commands
from commands import CommandManager

def start():
    config = Config()
    client = Client("client", api_id=config.api_id, api_hash=config.api_hash)
    register_handlers(client)
    client.run()

if __name__ == "__main__":
    start()