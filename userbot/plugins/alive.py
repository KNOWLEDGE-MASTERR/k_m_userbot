
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**Apun Zinda He Sarr ^.^** \n`🇮🇳BOT Status : ` **☣Hot**\n\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "`Telethon version:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`Database Status:` **😀ALL OK**\n\n`Always with you, my master!\n`"
                     "**Bot Creator:** [KNOWLEDGE MASTER](t.me/knowledge_masterr)\n"
                     "**Co-Owner:** [TELEGRAM KING](t.me/telegrmking)\n\n"
                     "     [🇮🇳Deploy This UserBot🇮🇳](https://github.com/knowledge-master/userbot)") 

