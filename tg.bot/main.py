import telebot
from logic_ai import get_class

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8145386398:AAGXWewIrHGmrMJG7kZQcEEX5cMjpq3c0Fo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Вот список моих комманд: /start - начать; /bye - пока; /complete - определение глобального потепления  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['complete'])
def send_r(message):
    bot.reply_to(message, "Здравствуйте чтобы вам помочь мне надо узнать, как выглядит улица в вашем городе/районе. Для этого сделайте фото вашего вида из окна и отправьте фото с подписью /ai. ")
    

@bot.message_handler(content_types=['photo'])
def ai(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    
    with open('images/'+file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class('images/'+file_name)
    bot.reply_to(message, result)
@bot.message_handler(commands=['advice'])
def send_advice(message):
    bot.reply_to(message, "Экономьте энергию: используйте энергоэффективные приборы, выключайте свет и технику, когда они не нужны. Используйте общественный транспорт: сокращайте использование автомобиля, ходите пешком или пересаживайтесь на велосипед. Снижайте отходы: перерабатывайте, компостируйте органику, выбирайте многоразовые вещи вместо одноразовых.")    


# Запускаем бота
bot.polling()