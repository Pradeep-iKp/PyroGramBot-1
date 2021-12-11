import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User, Message

@Client.on_message(filters.command('submit') & filters.private)
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=1857338892, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=1857338892, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@Client.on_message(filters.command('reply') & filters.private)
async def replyt(bot, message):
    if message.from_user.id == 1857338892: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=1857338892, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")

                
#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 1857338892:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1857338892,
        text="Hello".format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )


@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == 1857338892:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1857338892,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption="Hehe".format(reference_id, info.first_name),
        parse_mode="html"
    )


@Client.on_message(filters.user(1857338892) & filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )


@Client.on_message(filters.user(1857338892) & filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        )
