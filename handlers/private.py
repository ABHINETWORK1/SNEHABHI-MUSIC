from time import time
from datetime import datetime
from pyrogram import Client, filters
from helpers.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import sudo_users_only

from config import BOT_NAME as bn
from helpers.filters import other_filters2

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
š š§šµš¶š šš šš±šš®š»š°š² š§š²š¹š²š“šæš®šŗ š ššš¶š° šš¼š \nšŗš„šš» š¢š» š£šæš¶šš®šš² š©š£š¦ š¦š²šæšš²šæ \nš¼šš²š²š¹ šš¶š“šµ š¤šš®š¹š¶šš š ššš¶š° šš» š©š \nā­šš²šš²š¹š¼š½š²š± šš [ABHISHEK THAKUR](https://t.me/ABHI_NETWORK)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā°š¢šš»š²šæā±", url="https://t.me/SNEHU_IS_MINE")
                  ],[
                    InlineKeyboardButton(
                        "ā°š¦šš½š½š¼šæšā±", url="https://t.me/ABHI_NETWORK1"
                    ),
                    InlineKeyboardButton(
                        "ā°ššæš¼šš½ā±", url="https://t.me/ABHI_NETWORK"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ā°š¢šš»š²šæā±", url="https://t.me/ABHI_IS_MINE"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""ā **šššš šššššš ÉŖź± Źį“É“É“ÉŖÉ“É¢**\n<b>š  **į“į“į“ÉŖį“į“:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "āØ É¢Źį“į“į“", url=f"https://t.me/ABHI_NETWORK"
                    ),
                    InlineKeyboardButton(
                        "š£ į“Źį“É“É“į“Ź", url=f"https://t.me/ABHI_NETWORK1"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("į“ÉŖÉ“É“É¢...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "š`į“į“É“É¢!!`\n"
        f"āØ  `{delta_ping * 1000:.3f} į“ź±`"
    )

@Client.on_message(filters.command("uptime") & ~filters.private & ~filters.channel)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "š³ ź±į“į“į“į“ź±:\n"
        f"ā¢ **į“į“į“ÉŖį“į“:** `{uptime}`\n"
        f"ā¢ **ź±į“į“Źį“ į“ÉŖį“į“:** `{START_TIME_ISO}`"
    )
