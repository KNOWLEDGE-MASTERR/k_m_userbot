"""Emoji

Available Commands:

.sunny"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("sunny"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0,18)
    #input_str = event.pattern_match.group(1)
   # if input_str == "sunny":
    await event.edit("sunny")
    animation_chars = [
            "S",
            "U",
            "N",
            "NN",
            "Y",
            "FUCK",
            "U",
            "SUNNY",
            "BC",
            "FK",
            "UU",
            "SUNNY",
            "ALSO",
            "KNOWN",
            "AS",
            "GAJNII",
            "ALso",
            "click here👉 @gajnii"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
