from config import Config
from pyrogram.types import Message
from utils.singelton import SingletonMeta
from commands.exeception import MessageNotCommand, CommandNotFound
from commands.commands import register_commands
from config import Config

class CommandManager():

    def __init__(self, message: Message = None) -> None:
        self.message = message
        self.config = Config()
        self.commands = {}
        if message and message.from_user and message.text:
            self.args = self.message.text.split(" ")
            self.args.remove(self.args[0])
            if str(message.from_user.id) == Config().admin_id:
                register_commands(self)
    
    def set_message(self, message: Message):
        self.message = message

    def check_is_command(self, message: Message) -> bool:
        if message.text and message.text.startswith(self.config.command_prefix): # Если сообщение начинается с префикса из конфига
            return True
        return False

    def add_command(self, name: str, function):
        self.commands.setdefault(name, function)
    
    def get_command_function(self):
        if self.check_is_command(self.message):
            try:
                command = self.commands.get(self.message.text.replace(".", "").split(" ")[0])
                if command:
                    return command
                raise CommandNotFound("command not found")
            except IndexError:
                raise CommandNotFound("command not found")
        else:
            raise MessageNotCommand("this message is not command.")