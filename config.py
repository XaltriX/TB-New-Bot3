from operator import add
import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler


FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002256940690"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME</b>\n{uptime}")

#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "ʙʀᴜʜ ᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ sᴇɴᴘᴀɪ!!")

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7429276554:AAEk_n5FsligsrJ50QjFPA1PHMFLqo0eEwM") 

#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "21165589"))

#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")

#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002149484754"))

#your database channel link
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/+ddfydq6pKYtmNjU9")

VERIFY_LOG_ID = int(os.environ.get("VERIFY_LOG_ID", "-1002149484754"))
LOG_ID = int(os.environ.get("LOG_ID", "-1002133701521"))

#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "2048030675"))

#port set to default 8080
PORT = os.environ.get("PORT", "8081")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://aeoni:neon@aeoni.vkrl4.mongodb.net/?retryWrites=true&w=majority&appName=aeoni")
DB_NAME = os.environ.get("DB_NAME", "gts")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "160"))
START_MSG = os.environ.get("START_MESSAGE", 
"""<b>ʜᴇʟʟᴏ 😎 {first}</b>

<b>ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴜᴛɪʟɪᴛʏ ʙᴏᴛ🤖</b>

<b>ɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ📥 ʏᴏᴜʀ ᴠɪᴅᴇᴏs, ɪᴍᴀɢᴇs, ᴅᴏᴄᴜᴍᴇɴᴛs ғʀᴏᴍ ᴛᴇʀᴀʙᴏx.ᴄᴏᴍ ᴡɪᴛʜ ᴀ ᴍᴀxɪᴍᴜᴍ sᴘᴇᴇᴅ⚡️</b>

<b>ᴊᴜsᴛ sᴇɴᴅ ʏᴏᴜʀ ʟɪɴᴋs</b>

<i>ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅs </i>
    - /help
    - /tutorial
    """)
OWNER_TAG = os.environ.get("OWNER_TAG", "")
TIME = int(os.environ.get("TIME", "3600"))

KEYWORDS = {
    'terabox': 'www.terabox.com',
    '1024tera': 'www.1024tera.com',
    'terashare': 'www.teraboxshare.com',
    'teraboxlink': 'www.teraboxlink.com',
    '1024terabox': 'www.1024terabox.com',
    'teraboxsharelink': 'www.terasharelink.com',
    'teraboxapp': 'www.teraboxapp.com',
    'teraboxshare': 'www.teraboxshare.com',
    'terasharelink': 'www.terasharelink.com',
    'nephobox': 'www.nephobox.com'
}

PAYMENT_LOGS = int(environ.get('PAYMENT_LOGS', '00000'))
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "FALSE") == "TRUE" else False 

# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "onepageyam.com")

# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "")
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "ebc6952165f90b393ed2d4d8d4df30ecf58c9172")
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "21600")) # Add time in seconds
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID", "https://t.me/teraslinks")
#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (os.environ.get("USE_PAYMENT", "FALSE") == "FALSE") & (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", "")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "30 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "110 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "299 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "550 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "999 rs")

#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "<b>Hello {first}</b>\n \n<b>You need to join my channels to use me</b>\n\n<b>Kindly please join the below channels</b>")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "True") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
#you can add admin inside the bot
HELP_TXT = f"""<b>Hᴏᴡ ᴛᴏ Usᴇ?💡</b>
\n<b>Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ</b>

\n<b>Rᴇᴀsᴏɴ ғᴏʀ Dᴏᴡɴʟᴏᴀᴅ Fᴀɪʟᴇᴅ🚩</b>\n
   \n<b>♦ Mᴀʏ ʙᴇ ᴅᴜᴇ ᴛᴏ ᴛʜᴇ Fɪʟᴇ sɪᴢᴇ📁</b> 
   \n<b>♦ Mᴜʟᴛɪᴘʟᴇ Fɪʟᴇs🗂 ɪɴ ᴛʜᴇ ʟɪɴᴋ </b>
   \n<b>♦ ᴅᴜᴇ ᴛᴏ Tᴇʀᴀʙᴏx Eʀʀᴏʀ🚧</b>
   \n<b>♦ Sᴇʀᴠᴇʀ ᴛɪᴍᴇᴏᴜᴛ ᴇʀʀᴏʀ</b>
   \n<b>♦ Eʀʀᴏʀ ᴡʜɪʟᴇ ɢᴇᴛᴛɪɴɢ ʀᴇsᴘᴏɴsᴇ ғʀᴏᴍ sᴇʀᴠᴇʀ</b>

\n<b>ᴀɴʏ ɪssᴜᴇs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴠɪᴀ</b> @FileDatas_bot

"""



#no need to add anything from now on

ADMINS = []
ADMINS.append(OWNER_ID)
ADMINS.append(2048030675)

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
