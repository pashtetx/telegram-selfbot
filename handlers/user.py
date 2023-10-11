from config import Config
from controllers.message_controller import MessageController
from commands.exeception import CommandNotFound, MessageNotCommand

import asyncio

async def on_message(client, message):
    config = Config()
    message_controller = MessageController(message)
    if message.from_user.id == int(config.admin_id):
        try:
            command_function = message_controller.get_command_func()
            await command_function(message, message_controller.commands_manager.args)
        except CommandNotFound:
            await message.reply("Такой команды не существует.")
            await asyncio.sleep(5)
            await message.delete(revoke = True)
        except MessageNotCommand:
            pass
    else:
        if message_controller.message_block_user:
            await message.delete(revoke = True)
