class script(object):
    START_TXT = """<b>𝗛𝗲𝘆 {}, {}\n\nɪ
    
𝟭. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲 𝗡𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝗖𝗼𝗿𝗿𝗲𝗰𝘁 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴:
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝟮𝟬𝟬𝟵
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗺𝗼𝘃𝗶𝗲
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱

𝟮. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗪𝗲𝗯 𝗦𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗧𝗵𝗶𝘀 𝗙𝗼𝗿𝗺𝗮𝘁:
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭𝗘𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘀𝗲𝗮𝘀𝗼𝗻 𝟭
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘄𝗲𝗯 𝘀𝗲𝗿𝗶𝗲𝘀

𝟯. 𝗔𝘃𝗼𝗶𝗱 𝗨𝘀𝗶𝗻𝗴 𝗪𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻𝘀/𝗘𝗽𝗶𝘀𝗼𝗱𝗲𝘀/𝗦𝗲𝗿𝗶𝗲𝘀/𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗, 𝗲𝘁𝗰.</b>"""

    GSTART_TXT = """ʜᴇʏ {},\n\nɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\nᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/DeletedFromEarth">ʜᴘ</a>"""
    
    HELP_TXT = """<b>ʜᴇʏ {},
    
ᴡᴇ ʜᴀᴠᴇ ᴅᴇᴠɪᴅᴇᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ᴀɴᴅ ʙᴏᴛ ᴜꜱᴇʀꜱ.</b>"""

    ABOUT_TXT = """<b>★ 𝗦𝗲𝗿𝘃𝗲𝗿: <a href=https://www.heroku.com>𝗛𝗲𝗿𝗼𝗸𝘂!</a>
★ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href=https://pyrogram.org>𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺!</a>
★ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: <a href=https://www.mongodb.com>𝗠𝗼𝗻𝗴𝗼𝗗𝗕!</a>
★ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href=https://www.python.org>𝗣𝘆𝘁𝗵𝗼𝗻!</a></b>"""
    
    CHANNELS = """
<b>⚡ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ ⚡ 

▫ ᴀʟʟ ɴᴇᴡ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs.
▫ ғᴀsᴛᴇsᴛ ʙᴏᴛs ᴀʀᴇ ᴀᴅᴅᴇᴅ.
▫ ғʀᴇᴇ & ᴇᴀsʏ ᴛᴏ ᴜsᴇ.
▫ 𝟸𝟺x𝟽 sᴇʀᴠɪᴄᴇs ᴀᴠᴀɪʟᴀʙʟᴇ.</b>"""
    
    STATUS_TXT = """<b>    
‣ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
‣ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>
‣ ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ : <code>{}</code>
‣ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
‣ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
</b>"""

    LOG_TEXT_G = """#NewGroup
    
Gʀᴏᴜᴘ = {}
Iᴅ = <code>{}</code>
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}

Bʏ @TheMovieProviderBot"""

    LOG_TEXT_P = """<b>#𝗡𝗲𝘄𝗨𝘀𝗲𝗿

★ 𝗡𝗮𝗺𝗲: {}
★ 𝗜𝗗: <code>{}</code></b>"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,
ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """Sᴘᴇʟʟɪɴɢ Mɪꜱᴛᴀᴋᴇ Bʀᴏ ‼️\nᴅᴏɴ'ᴛ ᴡᴏʀʀʏ 😊 Cʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴏɴᴇ ʙᴇʟᴏᴡ 👇"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs @HpMovieRequest</b>"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs @HpMovieRequest</b>"""

    MVE_NT_FND = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ 😕

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs @HpMovieRequest</b>"""
    

    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ǫᴜᴇʀʏ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🍁 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n🌟 {} \n\n🔍 ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ 🔎\n\n⚠️ ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ 👇</b>"""

    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/DeletedFromEarth'>ʜᴘ</a></b>"""

    USERS_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴜꜱᴇʀꜱ ⇊
    
• /batch - ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.
• /stats - ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.
• /request - sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ( ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ )
• /plan - ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ.
• /myplan - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ."""

    GROUP_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ⇊
    
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /shortlink - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /remove_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
• /setshortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /setshortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ.
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ɢʀᴏᴜᴘ.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ."""

    ADMIC_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊
    
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    SHORTLINK_INFO = """<b>
 ❗<u>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ᴜꜱɪɴɢ ʙᴏᴛ</u>❗

★ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ꜱᴛᴀʀᴛ ᴇᴀʀɴɪɴɢ 💸 ᴍᴏɴᴇʏ ᴛᴏᴅᴀʏ ᴡɪᴛʜ ᴏᴜʀ ꜱɪᴍᴘʟᴇ ᴀɴᴅ ᴇᴀꜱʏ-ᴛᴏ-ᴜꜱᴇ ʙᴏᴛ!

›› ꜱᴛᴇᴘ 1 : ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀɴ ᴀᴅᴍɪɴ...

›› ꜱᴛᴇᴘ 2 : ᴜꜱᴇ /connect ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.

›› ꜱᴛᴇᴘ 3 : ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ꜱʜᴏʀᴛʟɪɴᴋ ᴡᴇʙꜱɪᴛᴇ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

★ ᴅᴏɴ'ᴛ ᴡᴀɪᴛ ᴀɴʏ ʟᴏɴɢᴇʀ ᴛᴏ ꜱᴛᴀʀᴛ ᴇᴀʀɴɪɴɢ ᴍᴏɴᴇʏ ꜰʀᴏᴍ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ. ᴀᴅᴅ ᴏᴜʀ ʙᴏᴛ ᴛᴏᴅᴀʏ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴍᴀᴋɪɴɢ ᴍᴏɴᴇʏ 💰! </b>
"""

    SHORTLINK_INFO2 = """<b>
❗<u>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ</u>❗

›› ꜱᴛᴇᴘ 4 : ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴜꜱɪɴɢ ᴀɴʏ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ ᴛʜᴇɴ ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ꜰɪʀꜱᴛ ᴏɴ instantearn.in (ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴜꜱᴇ ᴏᴛʜᴇʀ ʟɪɴᴋ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ).

›› ꜱᴛᴇᴘ 5 : ᴄᴏᴘʏ ʏᴏᴜʀ ᴀᴘɪ ꜰʀᴏᴍ ᴡᴇʙꜱɪᴛᴇ ᴀɴᴅ ᴛʜᴇɴ, ꜱɪᴍᴘʟʏ ꜱᴇᴛ ʏᴏᴜʀ ᴡᴇʙꜱɪᴛᴇ ᴀɴᴅ ᴀᴘɪ ᴜꜱɪɴɢ ᴛʜᴇ /shortlink ᴄᴏᴍᴍᴀɴᴅ.

› ʟɪᴋᴇ ᴛʜɪꜱ :</b>  <code>/shortlink instantearn.in 1502a197c85d59929d50f1cba1d5e6f967d1e962</code>

<b>›› ꜱᴛᴇᴘ 6 : ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

★ ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄᴏɴᴠᴇʀᴛꜱ ʟɪɴᴋꜱ ᴡɪᴛʜ ʏᴏᴜʀ ᴀᴘɪ ᴀɴᴅ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.</b>
"""
    SHORTLINK_INFO3 = """<b>
❗<u>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ</u>❗

›› ꜱᴛᴇᴘ 7 : ᴜꜱᴇ /set_tutorial ᴛᴏ ᴀᴅᴅ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰᴏʀ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.

› ʟɪᴋᴇ ᴛʜɪꜱ :</b> <code>/set_tutorial https://t.me/HowToOpenLinkHP</code>

<b>›› ꜱᴛᴇᴘ 8 : ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ /shortlink_info ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

★ ᴛʜᴀᴛ'ꜱ ɪᴛ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴀ ʟᴏᴛ ᴍᴏɴᴇʏ 💸 ᴜꜱɪɴɢ ᴛʜɪs ʙᴏᴛ.</b>
"""
    
    SELECT = """
➢ ᴄʟɪᴄᴋ ᴏɴ "ǫᴜᴀʟɪᴛʏ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ʟᴀɴɢᴜᴀɢᴇ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ꜱᴇᴀꜱᴏɴ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ꜱᴇᴀꜱᴏɴ.

➢ ᴄʟɪᴄᴋ ᴏɴ "♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ᴄʟɪᴄᴋ.

✯ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴘ
"""

    REQINFO = """➢ ᴄʟɪᴄᴋ "ǫᴜᴀʟɪᴛʏ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ "ʟᴀɴɢᴜᴀɢᴇ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ "ꜱᴇᴀꜱᴏɴ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ꜱᴇᴀꜱᴏɴ.
➢ ᴄʟɪᴄᴋ "♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️" ᴀɴᴅ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ."""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""

    # PLESE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    CREDITS_TXT = """<b>
❤️‍🩹 <u>ꜱᴘᴇᴄɪᴀʟ ᴛʜᴀɴᴋꜱ ᴛᴏ ᴇᴠᴇʀʏᴏɴᴇ</u>

• ᴍᴀɪɴ ᴏᴡɴᴇʀ : <a href="https://t.me/DeletedFromEarth">Hᴀʀꜱʜᴀʟ ❤️‍🔥</a>
• ʙᴀꜱᴇ ʀᴇᴘᴏ : <a href="https://t.me/creatorbeatz">Jᴏᴇʟ ᠰ TɢX</a>
• sᴛʀᴇᴀᴍ ғᴇᴀᴛᴜʀᴇ : <a href="https://t.me/LazyDeveloperr">LazyDeveloper</a>
• sᴛʀᴇᴀᴍ ᴡᴇʙꜱɪᴛᴇ : <a href="https://t.me/Biisal">Bɪɪsᴀʟ</a>
• ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴅᴇꜱ : <a href="https://t.me/Rk_botowner">Rɪꜱʜɪᴋᴇꜱʜ</a>
• ᴡᴇʟᴄᴏᴍᴇ ᴀɴɪᴍᴀᴛɪᴏɴ : <a href="https://t.me/Xavier_707">𝑿𝒂𝒗𝒊𝒆𝒓</a>
• ꜱᴛʀᴇᴀᴍ ꜱʜᴏʀᴛʟɪɴᴋ : <a href="https://t.me/Mr_SPIDY">⚝𝗠𝗿.𝗦𝗣𝗜𝗗𝗬⚝</a>

ɪ ᴀᴍ ꜱᴏʀʀʏ ɪꜰ ɪ ꜰᴏʀɢᴏᴛ ꜱᴏᴍᴇᴏɴᴇ 🫂
ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ʜᴇʟᴘɪɴɢ ɪɴ ᴛʜɪꜱ ᴀᴍᴀᴢɪɴɢ ʀᴏʟʟᴇʀ ᴄᴏᴀꜱᴛᴇʀ ᴊᴏᴜʀɴᴇʏ 🚀</b>
""" 
   # PLEASE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    
    CAPTION = """ 📂 <i><a href="https://telegram.me/HP_MOVIES_WORLD">{file_name}</a></i>\n\n"""

    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search}.

🧿 {title}</b>

<b>⭐ {rating} | ⏰ {runtime} Minutes
📆 {release_date}
🕵️ {director}

●  {languages}
●  {genres}

📖 {plot}

💗 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : {message.chat.title}</b>
"""
    

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @TheMovieProviderBot</b>"""

    LOGO = """

BOT WORKING PROPERLY"""

    #PLANS

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    CPREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PLAN_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>👋 ʜᴇʏ {},
    
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 7 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 10₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>👋 ʜᴇʏ {},
    
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 60₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>👋 ʜᴇʏ {},
    
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 90 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 180₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 ʜᴇʏ {},
    
🏅 <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
⏰ 180 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 250₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>👋 ʜᴇʏ {},

💎 <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
⏰ 365 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 400₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/DeletedFromEarth'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""    

    DEVELOPER_TXT = """
special Thanks To ❤️ Developer -

-Dev [Owner of this bot ]<a href='https://t.me/DeletedFromEarth'>HP</a>
"""
