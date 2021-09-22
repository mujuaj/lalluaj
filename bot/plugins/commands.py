#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
#adding force subscribe option to bot
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text=""" <b> ⚠️ YOU HAVE NOT SUBSCRIBED OUR CHANNEL⚠️
Join on our channel to get movies ✅
⚠️താങ്കൾ ഞങ്ങളുടെ ചാനൽ സബ്സ്ക്രൈബ് ചെയ്തിട്ട് ഇല്ല ! ⚠️
ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്യതാൽ താങ്കൾക്ക് movies കിട്ടുന്നത് ആണ് ✅\n𝘼𝙛𝙩𝙚𝙧 𝙟𝙤𝙞𝙣𝙞𝙣𝙜 𝙘𝙡𝙞𝙘𝙠 𝙤𝙣 𝙩𝙝𝙚 𝙛𝙞𝙡𝙚 𝙗𝙪𝙩𝙩𝙤𝙣 𝙞𝙣 𝙜𝙧𝙤𝙪𝙥 𝙖𝙣𝙙 𝙮𝙤𝙪 𝙬𝙞𝙡𝙡 𝙜𝙚𝙩 𝙛𝙞𝙡𝙚.
⬇️Channel link⬇️ </b>""",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡ 𝐉𝐎𝐈𝐍 𝐅𝐎𝐑 𝐅𝐈𝐋𝐄 ⚡️", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f''' <b>Join <a href="https://t.me/worldmoviesaj">MOVIE HUB HD⬛️◼️◾️▪️</a>\n\n <code>{file_name}</code>\n\n<a href="https://t.me/AJmovieLINKS ">𝘼𝙇𝙇 𝙈𝙊𝙑𝙄𝙀𝙎 𝘼𝙉𝘿 𝙎𝙀𝙍𝙄𝙀𝙎 𝙃𝘿</a>\n\n© Powered by <a href="https://t.me/AJmovieLINKS ">𝚈𝙾𝚄 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝚆𝙴 𝙿𝚁𝙾𝚅𝙸𝙳𝙴</a></b> \n@worldmoviesaj\n@AJmovieLINKS''',
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'More Movies', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption =  f" <code> {file_name} <code> \n <b> @worldmoviesaj <b> \n  ◻⬜ Powered by ⬛◼  @AJmovieLINKS ",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'More Movies', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption =  f" <code>{file_name}<code> \n <b> @worldmoviesaj <b> \n ◻⬜ Powered by ⬛◼  @AJmovieLINKS ",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '╽𝗠𝗼𝗿𝗲 𝗠𝗼𝘃𝗶𝗲𝘀╽', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('More Movies', url='https://t.me/worldmoviesaj'),
        InlineKeyboardButton('Source Code 🧾', url ='https://t.me/AJmovieLINKS')],                               
     [
        InlineKeyboardButton('Support 🛠', url='https://t.me/AJmovieLINKS')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

