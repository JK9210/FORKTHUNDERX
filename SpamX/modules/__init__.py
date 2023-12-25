from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝒯𝐻𝒰𝒟𝐸𝑅 𝒳 🍷"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/d44e21c2ba129c6aba2ab.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝒯𝐻𝒰𝒩𝒟𝐸𝑅 𝒳"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **𝑀𝒶𝓈𝓉𝑒𝓇:** {owner_mention}
➠ **𝒫𝓎𝓉𝒽𝑜𝓃 𝒱𝑒𝓇𝓈𝒾𝑜𝓃:** `{platform.python_version()}`
➠ **𝒮𝓅𝒶𝓂𝒳 𝒱𝑒𝓇𝓈𝒾𝑜𝓃:** `{__version__}`
➠ **𝒫𝓎𝓇𝑜𝑔𝓇𝒶𝓂 𝒱𝑒𝓇𝓈𝒾𝑜𝓃:** `{pyro_vr}`
➠ **𝒫𝓎 𝒯𝒽𝓊𝓃𝒹𝑒𝓇 𝒳 𝒱𝑒𝓇𝓈𝒾𝑜𝓃:** `{pip_vr}`
➠ **𝒢𝓇𝑜𝓊𝓅:** @UNI_INDIA_0000
━───────╮•╭───────━
➠ **𝒮𝑜𝓊𝓇𝒸𝑒 𝒞𝑜𝒹𝑒:** [•Repo•](https://github.com/APL9210/THUNDERX)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
