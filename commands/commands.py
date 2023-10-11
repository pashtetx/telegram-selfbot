import random, asyncio

from database.database import add_block_user, remove_block_user, all_block_users

async def hello(message):
    await message.reply("Привет!")

async def pentagon(message, args):
    sentences = [
        "Взламываю пентагон 💻",
        "Общаюсь с иноплонетянами 👽",
        "Работаю 💀",
        "Думаю 🧠",
    ]

    for i in range(1, 11):
        if i == 10:
            await message.edit(f"{i}0%, Успешно!")
        else:
            await message.edit(f"{i}0%, {random.choice(sentences)}")
        await asyncio.sleep(0.5)
        
async def block_user(message, args):
    if args[0]:
        add_block_user(args[0])
        await message.reply(f"Юзер {args[0]} заблокирован. ⛔")
    else:
        await message.reply("Укажите аргумент")

async def unblock_user(message, args):
    if args[0]:

        block_users = [i[0] for i in all_block_users()]

        if args[0] in block_users:
            remove_block_user(args[0])
            await message.reply(f"Юзер {args[0]} разблокирован. ✅" )
        else:
            await message.reply("Этот юзер не состоит в заблокинованных юзеров. ")
    else:
        await message.reply("Укажите аргумент.")

async def typing(message, args):
    if args[0]:
        word = " ".join(args)
        content = ""
        for i in word:
            await asyncio.sleep(random.choice([0.1, 0.05, 0.15, 0.2]))
            content += i
            if i == " ":
                continue
            await message.edit(content)
            for i in range(0,2):
                await message.edit(content + "|")
                await asyncio.sleep(0.2)
                await message.edit(content)
                

async def blocklist(message, args):
    content = "Заблокированные пользователи: \n"
    for i in all_block_users():
        content += f"{i[0]}\n"
    await message.reply(content)

def register_commands(command_manager):
    commands = {
        "hello":hello,
        "pentagon": pentagon,
        "block_user": block_user,
        "unblock_user": unblock_user,
        "blocklist": blocklist,
        "typing":typing
    }
    for command_name, command_function in commands.items():
        command_manager.add_command(command_name, command_function)
