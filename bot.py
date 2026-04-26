import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================================
# BOT SETTINGS
# =========================================

BOT_TOKEN = "8611980454:AAGTu7AFyYe8hvS61o1qPBCd-oqzEmkMfTs"
CHANNEL_ID = -1002386905127
OWNER_ID = 6710659540

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# =========================================
# START COMMAND
# =========================================

@bot.message_handler(commands=['start'])
def start(message):

    user_name = message.from_user.first_name

    welcome_text = f"""
✨ <b>Welcome {user_name}</b> 💎

🔥 Welcome To Premium Config Hub 🚀
📥 Latest Files
🎬 YouTube Tutorials
🔗 Direct Download Links
⚡ Daily Updates

💎 Enjoy Premium Services 😎
"""

    bot.send_message(message.chat.id, welcome_text)

# =========================================
# HELP COMMAND
# =========================================

@bot.message_handler(commands=['help'])
def help_command(message):

    help_text = """
🤖 <b>Premium Bot Commands</b>

/post = Create premium post
/id = Get your Telegram ID

📸 Send photo → Auto post
🎵 Send audio → Auto post
🎤 Send voice → Auto post
📂 Send file → Auto post
"""

    bot.send_message(message.chat.id, help_text)

# =========================================
# GET USER ID
# =========================================

@bot.message_handler(commands=['id'])
def get_id(message):

    bot.reply_to(
        message,
        f"🆔 Your Telegram ID:\n<code>{message.from_user.id}</code>"
    )

# =========================================
# ADMIN CHECK
# =========================================

def is_admin(user_id):

    return user_id == OWNER_ID

# =========================================
# /POST COMMAND
# =========================================

@bot.message_handler(commands=['post'])
def create_post(message):

    if not is_admin(message.from_user.id):

        bot.reply_to(message, "❌ You are not authorized.")
        return

    text = """
📌 Send details like this:

Title | Description | YouTube Link | Download Link

Example:

BGMI CONFIG | Zero Lag Gameplay | https://youtube.com/video | https://your-short-link.com
"""

    bot.send_message(message.chat.id, text)

    bot.register_next_step_handler(message, process_post)

# =========================================
# PROCESS POST
# =========================================

def process_post(message):

    try:

        data = message.text.split('|')

        if len(data) < 4:

            bot.reply_to(
                message,
                "❌ Wrong Format!\n\nUse:\nTitle | Description | YouTube Link | Download Link"
            )
            return

        title = data[0].strip()
        description = data[1].strip()
        youtube_link = data[2].strip()
        download_link = data[3].strip()

        caption = f"""
🔥 <b>NEW PREMIUM RELEASE</b> 🔥

📌 <b>Title:</b>
⚡ {title}

📝 <b>Description:</b>
🚀 {description}

🎬 <b>Tutorial Video:</b>
{youtube_link}

━━━━━━━━━━━━━━━
💎 Powered By Premium Bot
"""

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "📥 Download Now",
            url=download_link
        )

        btn2 = InlineKeyboardButton(
            "🎬 Watch Video",
            url=youtube_link
        )

        markup.row(btn1)
        markup.row(btn2)

        bot.send_message(
            CHANNEL_ID,
            caption,
            reply_markup=markup
        )

        bot.reply_to(
            message,
            "✅ Post sent successfully!"
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

# =========================================
# PHOTO HANDLER
# =========================================

@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    if not is_admin(message.from_user.id):
        return

    try:

        file_id = message.photo[-1].file_id

        caption = """
🖼️ <b>NEW PREMIUM IMAGE</b>

🔥 Uploaded Successfully
💎 Stay Tuned For More Updates
"""

        bot.send_photo(
            CHANNEL_ID,
            file_id,
            caption=caption
        )

        bot.reply_to(
            message,
            "✅ Photo posted successfully!"
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

# =========================================
# VOICE HANDLER
# =========================================

@bot.message_handler(content_types=['voice'])
def handle_voice(message):

    if not is_admin(message.from_user.id):
        return

    try:

        voice_id = message.voice.file_id

        caption = """
🎧 <b>NEW VOICE UPDATE</b>

🔥 Exclusive Audio Uploaded
💎 Stay Tuned
"""

        bot.send_voice(
            CHANNEL_ID,
            voice_id,
            caption=caption
        )

        bot.reply_to(
            message,
            "✅ Voice posted successfully!"
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

# =========================================
# AUDIO HANDLER
# =========================================

@bot.message_handler(content_types=['audio'])
def handle_audio(message):

    if not is_admin(message.from_user.id):
        return

    try:

        audio_id = message.audio.file_id

        caption = """
🎵 <b>NEW AUDIO FILE</b>

🚀 Premium Audio Uploaded
💎 Enjoy Listening
"""

        bot.send_audio(
            CHANNEL_ID,
            audio_id,
            caption=caption
        )

        bot.reply_to(
            message,
            "✅ Audio posted successfully!"
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

# =========================================
# DOCUMENT HANDLER
# =========================================

@bot.message_handler(content_types=['document'])
def handle_document(message):

    if not is_admin(message.from_user.id):
        return

    try:

        doc_id = message.document.file_id

        caption = """
📂 <b>NEW FILE UPLOADED</b>

🔥 Premium File Available
📥 Download Now
"""

        bot.send_document(
            CHANNEL_ID,
            doc_id,
            caption=caption
        )

        bot.reply_to(
            message,
            "✅ File posted successfully!"
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Error:\n{e}"
        )

# =========================================
# DEFAULT MESSAGE
# =========================================

@bot.message_handler(func=lambda message: True)
def default_reply(message):

    bot.reply_to(
        message,
        "🤖 Use /help to see commands."
    )

# =========================================
# START BOT
# =========================================

print("✅ Premium Telegram Bot Running...")

bot.infinity_polling()
