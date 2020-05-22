
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
    await alive.edit("**𝕬𝖕𝖚𝖓 𝖅𝖎𝖓𝖉𝖆 𝕳𝖊 𝕾𝖆𝖗𝖗. \n𝕁𝕒𝕣𝕧𝕚𝕤 𝕚𝕤 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕤𝕖𝕣𝕧𝕚𝕔𝕖 ^.^** \n\n`ʏᴏᴜʀ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ : ` **☣🅷🅾🆃**\n\n"
                     f"`🔴му ρєяυ σωηєя`: {DEFAULTUSER}\n\n"
                     "`⚫️ȶɛʟɛȶɦօռ ʋɛʀֆɨօռ:` **6.0.9**\n`₱Ɏ₮ⱧØ₦:` **3.7.4**\n\n"
                     "`🔵DαƚαႦαʂҽ Sƚαƚυʂ:` **😀ALL OK**\n\n**Älwå¥§ wï†h ¥ðµ, m¥ må§†êr!\n\n**"
                     "**🔸ɮօȶ ƈʀɛǟȶɛɖ ɮʏ:** [♊KNOWLEDGE MASTER♋](t.me/knowledge_masterr) 🔹\n\n"
                     
                    "T̳H̳A̳N̳K̳S̳ ̳T̳O̳ **I̳N̳D̳I̳A̳N̳ ̳B̳H̳A̳I̳**\n\n"
                     "      [❤️ЩΛПƬ YӨЦЯ ӨЩП ЦƧΣЯBӨƬ❤️](t.me/k_m_userbot_updates)") 

