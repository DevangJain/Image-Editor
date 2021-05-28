# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters
from config import Config
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    if Config.UPDATE_CHANNEL:
        try:
            user = await bot.get_chat_member(Config.UPDATE_CHANNEL, update.chat.id)
            if user.status == "kicked":
              await bot.edit_message_text(text=script.BANNED_USER_TEXT, message_id=fmsg.message_id)
              return
        except UserNotParticipant:
            await bot.edit_message_text(chat_id=update.chat.id, text=script.FORCE_SUBSCRIBE_TEXT, message_id=fmsg.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel 💻", url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")]]))
            return
        except Exception:
            await bot.edit_message_text(chat_id=update.chat.id, text=script.SOMETHING_WRONG, message_id=fmsg.message_id)
            return
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE",
                            url="https://github.com/TroJanzHEX/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE",
                            url="https://github.com/TroJanzHEX/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE",
                            url="https://github.com/TroJanzHEX/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
