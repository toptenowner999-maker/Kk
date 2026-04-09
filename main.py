import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔒 CONFIG
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

USERS_FILE = "users.txt"
BANNED_FILE = "banned.txt"

# 📂 LOAD DATA
def load_data(file):
    try:
        with open(file, "r") as f:
            return set(map(int, f.read().split()))
    except:
        return set()

def save_data(file, user_id):
    with open(file, "a") as f:
        f.write(f"{user_id}\n")

users = load_data(USERS_FILE)
banned_users = load_data(BANNED_FILE)

# 🔥 START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if user_id in banned_users:
        return

    if user_id not in users:
        users.add(user_id)
        save_data(USERS_FILE, user_id)

    text = """🔥 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐔𝐍𝐋𝐎𝐂𝐊𝐄𝐃 🔥

𝐇𝐃 + 𝐔𝐥𝐭𝐫𝐚-𝐅𝐫𝐞𝐬𝐡 𝐕𝐢𝐝𝐞𝐨𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐍𝐨𝐰

𝐀𝐥𝐥 𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐏𝐚𝐜𝐤𝐚𝐠𝐞

💎 𝐎𝐧𝐥𝐲 ₹49 (Limited Offer) 💎

✅ Full HD Quality  
✅ Instant Delivery  
✅ 100% Working Links  
"""

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("💎 𝐁𝐔𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌", callback_data="buy"),
        InlineKeyboardButton("🎁 𝐅𝐑𝐄𝐄 𝐃𝐄𝐌𝐎", url="https://t.me/PookiesHub_bot?start=BQADAQADxxYAAn876UVC1Tb49aCdbxYE")
    )
    markup.add(
        InlineKeyboardButton("🛠️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/NYRAHELPCENTRE?text=HELLO%20%20BHAI%20MUJHE%20PREMIUM%20SUBSCRIPTION%20CHAHIYE")
    )

    bot.send_photo(
        chat_id=user_id,
        photo="https://kommodo.ai/i/nc5zJIJa4gO94AzXLemD",
        caption=text,
        reply_markup=markup
    )

# 💰 BUY BUTTON
@bot.callback_query_handler(func=lambda call: call.data == "buy")
def buy(call):
    text = """💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐌𝐄𝐌𝐁𝐄𝐑𝐒𝐇𝐈𝐏 💎

📦 Plan: Lifetime  
💰 Price: ₹49  

━━━━━━━━━━━━━━━  
🏦 UPI ID: <code>q78849684@ybl</code>  
━━━━━━━━━━━━━━━  

💡 Payment ke baad button click karo 👇
"""

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ 𝐆𝐄𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊", callback_data="paid")
    )

    bot.send_photo(
        chat_id=call.from_user.id,
        photo="https://kommodo.ai/i/nGT8k6KYx4dU09gc1NC2",
        caption=text,
        reply_markup=markup
    )

    bot.answer_callback_query(call.id)

# ❌ PAYMENT CHECK
@bot.callback_query_handler(func=lambda call: call.data == "paid")
def paid(call):
    bot.answer_callback_query(call.id, "❌ Payment not detected")

    bot.send_message(
        call.from_user.id,
        "❌ Payment failed. Pehle payment karo phir try karo."
    )

# 📊 STATS
@bot.message_handler(commands=['stats'])
def stats(message):
    if message.from_user.id != ADMIN_ID:
        return

    bot.reply_to(message,
        f"""📊 BOT STATS

👤 Total Users: {len(users)}
🚫 Banned: {len(banned_users)}
"""
    )

# 🚫 BAN
@bot.message_handler(commands=['ban'])
def ban(message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])
        banned_users.add(user_id)
        save_data(BANNED_FILE, user_id)
        bot.reply_to(message, "🚫 User banned")
    except:
        bot.reply_to(message, "Usage: /ban user_id")

# ✅ UNBAN
@bot.message_handler(commands=['unban'])
def unban(message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])
        banned_users.discard(user_id)
        bot.reply_to(message, "✅ User unbanned")
    except:
        bot.reply_to(message, "Usage: /unban user_id")

# 📢 BROADCAST (ALL TYPES)
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.from_user.id != ADMIN_ID:
        return

    if not message.reply_to_message:
        bot.reply_to(message, "Reply to any message to broadcast ❌")
        return

    msg = message.reply_to_message
    success = 0
    failed = 0

    for user in users:
        if user in banned_users:
            continue

        try:
            bot.copy_message(
                chat_id=user,
                from_chat_id=message.chat.id,
                message_id=msg.message_id
            )
            success += 1
        except:
            failed += 1

    bot.reply_to(message,
        f"""📢 Broadcast Done

✅ Success: {success}
❌ Failed: {failed}
"""
    )

print("🔥 Bot Running...")
bot.infinity_polling()
