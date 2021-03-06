from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from helpers.filters import command


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c70635cc28eec97a43f40.jpg",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐๐จ๐ญ\n\nโ๐ฟ๐๐ ๐๐๐๐ ๐ฑ๐ข - ๐ท๐๐๐๐๐_๐ก๐ณ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("โฅ๏ธ Creator โฅ๏ธ", url=f"https://t.me/Harshu_xD")],
                [InlineKeyboardButton("Channel๐ฅ", url=f"https://t.me/StarterChannel")],
            ]
        ),
    )


@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/389f418594b430aad58a6.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ฅ Managed By ๐", url=f"https://t.me/Harshu_xD")]]
        ),
    )
