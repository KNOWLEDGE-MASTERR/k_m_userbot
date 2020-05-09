"""Use cmd `.kon` to tell about you"""

from telethon import events
from uniborg.util import admin_cmd
import asyncio
from userbot import ALIVE_NAME




@borg.on(admin_cmd(pattern="maikonhu"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1
    

    animation_ttl = range(0, 10)

    

  

    await event.edit("sun")

    animation_chars = [

         "{DEFAULTUSER} tera pehla baap",
         "{DEFAULTUSER} teri maa ka 100th pati",
         "{DEFAULTUSER} tere khandaan ka owner",
         "{DEFAULTUSER} tujhe paida krne wala",
         "{DEFAULTUSER} tujhe chakka sabit krne wala",
         "{DEFAULTUSER} tera bhai is duniya me laane wala",
         "{DEFAULTUSER} teri maa ko kothe me baithane wala",
         "{DEFAULTUSER} ke talwe tera baaap chatta hai",
         "{DEFAULTUSER} aakhir tera baap hi to hai",
         "{DEFAULTUSER} hoo mai"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])
