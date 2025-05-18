from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "24313439"
# -------------------------------------------------------------
API_HASH = "a007ea183e9276803caba61ad093273b"
# --------------------------------------------------------------
BOT_TOKEN = getenv("7718680866:AAEX_SfFMaE6efdwoGlFjxQnFVVNYV-Yx1g", None)
STRING1 = getenv("BQFy_l8ATqoLGnvyauM5yWnNjDX1k8J9HUQmEmyczAKGRVg7BJmEWO0qLYQ25At1ycxywKV00iV1DELrvN76bqlygOInqxuQwyC4th4eZJ7MWDK9LosQjkBpZlakXPa2N9uCBsw58pqy-sz4CGt9qMcMZRXy18soKCV-2x6kLvo_La783CckOYVx1iIuQPNyxai0U-NX-lYtXC24ys6CVwHjTIrvUlfHEqWFuJhYBJ80MqnDrAj9DaFUzshzHzuW0Po_y5FJIbyJ5AIBw6EEnVLO6JIm5hA_yZGM4cx3RDXcegEcQb4yAX2ZFeU9GC0WyXmXrIolIZgr5PyWdwQXyjnM2hB7bAAAAAGyiepSAA", None)
DB_NAME = "Botbaby"
MONGO_URL = getenv("mongodb+srv://botbaby:botbaby@cluster0.zngip1b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
OWNER_ID = int(getenv("OWNER_ID", "1716902346"))
BOT_ID = int(getenv("BOT_ID", "7290350162"))
SUPPORT_GRP = "infinitygx_bot_support"
UPDATE_CHNL = "gxinfinity_support"
OWNER_USERNAME = "Its_tg_seller"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002620121753"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7290350162").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SpyGamer7t2r/ShizuChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
