from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User, Message

@Client.on_message(filters.command('submit') & filters.private)
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=ADMIN, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=ADMIN, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@Client.on_message(filters.command('reply') & filters.private)
async def replyt(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")
