#15-11-2021
#okbei
            
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User, Message



            

@Bot.on_message(filters.command('submit') & filters.private)
async def report(_, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=OWNER_ID, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=OWNER_ID, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@Bot.on_message(filters.command('reply') & filters.private)
async def replyt(_, message):
    if message.from_user.id == OWNER_ID: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=OWNER_ID, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                          
@Bot.on_message(filters.command('send') & filters.private)
async def send(_, message):
    if message.from_user.id == OWNER_ID: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/send"," "))
                                    await bot.copy_message(chat_id=chatid, from_chat_id=OWNER_ID, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                                    
@Bot.on_message(filters.command('pin') & filters.private)
async def pin(_, message):
    if message.from_user.id == OWNER_ID: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/pin"," "))
                                    p=await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await p.pin()
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group And pinned</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")
                                    


@Bot.on_message(filters.command('id') & filters.group)
async def id(_, message):
    await message.reply_text(f"<b>➲ Chat ID:</b> <code>{message.chat.id}</code>")
    
Bot.run()
