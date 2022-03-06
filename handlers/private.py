from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from helpers.filters import command


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c70635cc28eec97a43f40.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭\n\n⚜𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 - 𝙷𝚊𝚛𝚜𝚑𝚞_𝚡𝙳**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("♥️ Creator ♥️", url=f"https://t.me/Harshu_xD")],
                [InlineKeyboardButton("Channel🔥", url=f"https://t.me/StarterChannel")],
            ]
        ),
    )


@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/389f418594b430aad58a6.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💥 Managed By 💞", url=f"https://t.me/Harshu_xD")]]
        ),
    )
