"""Emoji
Available Commands:
.pureindialover
Credits to @knowledge_masterr
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("knowledge_masterr"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "knowledge_masterr":
    await event.edit("@knowledge_masterr")
    animation_chars = [
            "@knowledge_masterr tera baap",
            "@knowledge_masterr is bot ka creator",
            "@knowledge_masterr bot ko jaan dene wala",
            "@knowledge_masterr owner of TELEGRAM ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@knowledge_masterr"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
