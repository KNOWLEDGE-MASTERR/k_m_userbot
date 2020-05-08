"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd
from telethon.tl.functions.users import GetFullUserRequest



@borg.on(admin_cmd(pattern=r"hack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        if idd==1211870654:
            await event.edit("This is My Master\nI can't hack my master's Account\n**How dare you trying to hack my master's account nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ @knowledge_masterr __to release your account__😏")
        else:
            await event.edit("Hacking..")
            animation_chars = [
        
            "`Connecting To Hacked Private Server...`\n\nSTATUS:-",
            "`Target Selected.`\n\nSTATUS:-\nStarting...",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\nSTATUS:-\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\nSTATUS:-\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n**{DOWNLOADED}**\n\nCollecting Data Packages (23.1 kB)",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\nSTATUS:-\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n**{DOWNLOADED}**\n\nCollecting Data Packages (23.1 kB)\n**{COLLECTED}**\n\nDownloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\nSTATUS:-\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n**{DOWNLOADED}**\n\nCollecting Data Packages (23.1 kB)\n**{COLLECTED}**\n\nDownloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\n**{DOWNLOADED}**\n\nBuilding wheel for Tg-Bruteforcing (setup.py)",

            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\nSTATUS:-\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n**{DOWNLOADED}**\n\nCollecting Data Packages (23.1 kB)\n**{COLLECTED}**\n\nDownloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\n**{DOWNLOADED}**\n\nBuilding wheel for Tg-Bruteforcing (setup.py)\n**{DONE}**\n\n",

            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Targeted Account Hacked...\n\nPay 10$ To` @knowledge_masterr `To Remove this hack..`"
            ]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 11])
    else:
        await event.edit("No User is Defined\n Can't hack account")
