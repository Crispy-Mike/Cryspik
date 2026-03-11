import telebot
from telebot import types

token="8673223512:AAH-eK9YJHxkdgNsy3tHJ64JS0eHZ-IW7qI"

bot=telebot.TeleBot(token)

# URL твоего Web App (замени на свой HTTPS)
WEB_APP_URL = "https://твой-хостинг.github.io/Cryptik.html"

@bot.message_handler(commands=["start"])
def start_bot(message):
    with open(r"C:\Cryptik\first.jpg", "rb") as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption="Это бот для обмена криптовалюты, для подробностей его возможностей воспользуйтесь командой /help, для запуска используйте команду /cryptic."
        )

@bot.message_handler(commands=["help"])
def help_bot(message):
    bot.send_message(message.chat.id, "Команды:\n/start-краткое описание бота,\n/help-все команды бота,\n/cryptic-запуск самого обменника,\n/rules-полное описание всех соглашений, правил.")

@bot.message_handler(commands=["cryptic"])
def cryptic(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 Запустить обменник", web_app=types.WebAppInfo(url=WEB_APP_URL))
    markup.add(btn)
    bot.send_message(message.chat.id, "Нажми кнопку ниже:", reply_markup=markup)

bot.infinity_polling()
