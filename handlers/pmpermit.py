from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"RUKO ZARA SABAR KARO YAHA SPAM NA KARO JALDI JAO @ABHI_NETWORK 👈👈YAHA CLICK KARKE JOIN HO JAO WAHA BAT KARENGE"
  return
