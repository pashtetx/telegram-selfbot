from .controller import Controller
from commands import CommandManager
from database.database import all_block_users


class MessageController(Controller):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.commands_manager = CommandManager(message)
        self.block_users = [i[0] for i in all_block_users()]
        if message.from_user.id in self.block_users:
            self.message_block_user = True
        else:
            self.message_block_user = False

    def get_command_func(self):
        return self.commands_manager.get_command_function()
    