
import telebot

token='5211216918:AAGpq15BNq5wLB8YxtRQJwMJh0aXzBeLQmM'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Приветствую вас! Давайте начнем волну, /button")

from telebot import types
@bot.message_handler(commands=['button'])


def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Утро")
    item2 = types.KeyboardButton("День")
    item3 = types.KeyboardButton("Вечер")
    item4 = types.KeyboardButton("Ночь")
    item5 = types.KeyboardButton("Отмена")
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Укажите ваше время суток", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def bot_ms(message):
    if message.text == "Отмена":
        bot.send_message(message.chat.id, "Отключаюсь, но помните, что я всегда тут /button")
    elif message.text == "Утро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton("😁Спокойное настроение")
        item7 = types.KeyboardButton("😁Веселое настроение")
        item8 = types.KeyboardButton("😁Грустное настроение")
        markup.add(item6, item7, item8)
        bot.send_message(message.chat.id, "Теперь укажите настроение", reply_markup=markup)
    if message.text == "😁Спокойное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item9 = types.KeyboardButton("⌚️Новости")
        item10 = types.KeyboardButton("⌚️Музыка")
        item11 = types.KeyboardButton("⌚️Видео")
        markup.add(item9, item10, item11)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "⌚️Новости":
        bot.send_message(message.chat.id, "Прекрасно, вот ваши новости  https://ria.ru/ . Начнем сначала? /button")
    if message.text == "⌚️Музыка":
        bot.send_message(message.chat.id, "Спокойная музыка уже готова к вашему прослушиванию https://www.youtube.com/playlist?list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4 . Начнем сначала? /button")
    if message.text == "⌚️Видео":
        bot.send_message(message.chat.id, "Видео готово https://www.youtube.com/results?search_query=%D0%BA%D0%B0%D0%BA+%D0%B1%D1%8B%D1%82%D1%8C+%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%BC+%D1%81+%D1%83%D1%82%D1%80%D0%B0 ! Рад был быть полезным . Начнем сначала? /button ")
    if message.text == "😁Веселое настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item12 = types.KeyboardButton("🔌Новости")
        item13 = types.KeyboardButton("🔌Музыка")
        item14 = types.KeyboardButton("🔌Видео")
        markup.add(item12, item13, item14)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "🔌Новости":
        bot.send_message(message.chat.id, "Новости готовы https://t.me/rian_ru . Начнем сначала? /button")
    if message.text == "🔌Музыка":
        bot.send_message(message.chat.id, "А вот и бодрая музыка для вас https://t.me/Muzik! Начнем сначала /button ?")
    if message.text == "🔌Видео":
        bot.send_message(message.chat.id, "Видео готово  https://www.youtube.com/playlist?list=PLUV7j0d8hiH2fO6jOTpwpKdvJA5fjnPaw , приятного просмотра! Начнем сначала? /button")
    if message.text == "😁Грустное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item15 = types.KeyboardButton("⏲Новости")
        item16 = types.KeyboardButton("⏲Музыка")
        item17 = types.KeyboardButton("⏲Видео")
        markup.add(item15, item16, item17)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "⏲Новости":
        bot.send_message(message.chat.id, "Печальные новсти для вашего печального настроя https://t.me/mwarnews . Я буду надеяться, что вам станет лучше! Начнем сначала? /button  ")
    if message.text == "⏲Музыка":
        bot.send_message(message.chat.id, "Грустная музыка для вас: https://t.me/lofisong . Начнем сначала? /button")
    if message.text == "⏲Видео":
        bot.send_message(message.chat.id, "подборка грустных видео https://t.me/sad_songs_and_videoes . Начнем сначала? /button")
    elif message.text == "День":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item18 = types.KeyboardButton("🙂Спокойное настроение")
        item19 = types.KeyboardButton("🙂Веселое настроение")
        item20 = types.KeyboardButton("🙂Грустное настроение")
        markup.add(item18,item19, item20)
        bot.send_message(message.chat.id, "А какое у вас настроение?", reply_markup=markup)
    if message.text == "🙂Спокойное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item21 = types.KeyboardButton("📡Новости")
        item22 = types.KeyboardButton("📡Музыка")
        item23 = types.KeyboardButton("📡Видео")
        markup.add(item21, item22, item23)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "📡Новости":
        bot.send_message(message.chat.id, "Ваши дневыне новости https://78.ru/news/obshestvo ! Начнем сначала /button ? ")
    if message.text == "📡Музыка":
        bot.send_message(message.chat.id, "Музыка для работы или отдыха в середине дня https://tunein.com/radio/Radiostormcom-AT-WORK-s112939/ ! Начнем сначала /button ?")
    if message.text == "📡Видео":
        bot.send_message(message.chat.id, "Видео для вашего спокойного дня https://www.youtube.com/playlist?list=PLgMWV5RtpRaW1Aost49hGH7v2nupaqiO8 . Начнем сначала /button ?")
    if message.text == "🙂Веселое настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item24 = types.KeyboardButton("🔦Новости")
        item25 = types.KeyboardButton("🔦Музыка")
        item26 = types.KeyboardButton("🔦Видео")
        markup.add(item24, item25, item26)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "🔦Новости":
        bot.send_message(message.chat.id, "Ваши интересные новости готовы к просмотру https://78.ru/news/ekonomika ! Начнем сначала? /button")
    if message.text == "🔦Музыка":
        bot.send_message(message.chat.id, "Бодрая музыка для вашего дня https://europaplus.ru/ . Начнем сначала? /button")
    if message.text == "🔦Видео":
        bot.send_message(message.chat.id, "Видео  готово https://t.me/rytpalt . Начнем сначала? /button")
    if message.text == "🙂Грустное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item27 = types.KeyboardButton("☎️Новости")
        item28 = types.KeyboardButton("☎️Музыка")
        item29 = types.KeyboardButton("☎️Видео")
        markup.add(item27, item28, item29)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "☎️Новости":
        bot.send_message(message.chat.id, "Новости готовы https://78.ru/news/donbass . Начнем сначала? /button")
    if message.text == "☎️Музыка":
        bot.send_message(message.chat.id, "А вот и долгожданная музыка https://101.ru/radio/user/783218 . Начнем сначала /button?")
    if message.text == "☎️Видео":
        bot.send_message(message.chat.id, "Видео-ролики подоспели https://www.youtube.com/playlist?list=PLi1UmCqdPHXCAErCbykATZQgLt2k_aUg1 . Начнем сначала? /button")
    elif message.text == "Вечер":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item30 = types.KeyboardButton("😀Спокойное настроение")
        item31 = types.KeyboardButton("😀Веселое настроение")
        item32 = types.KeyboardButton("😀Грустное настроение")
        markup.add(item30,item31,item32)
        bot.send_message(message.chat.id, "Ваше настроение?", reply_markup=markup)
    if message.text == "😀Спокойное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item33 = types.KeyboardButton("📸Новости")
        item34 = types.KeyboardButton("📸Музыка")
        item35 = types.KeyboardButton("📸Видео")
        markup.add(item33, item34, item35)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "📸Новости":
        bot.send_message(message.chat.id, "Новости для вас подобранны https://www.autonews.ru/ . Начнем сначала? /button")
    if message.text == "📸Музыка":
        bot.send_message(message.chat.id, "Музыка готова https://www.bfm.ru/broadcasting/player?radio_city=msk . Начнем сначала? /button")
    if message.text == "📸Видео":
        bot.send_message(message.chat.id, "Видеоролики для вас https://www.youtube.com/playlist?list=PLZ1FUdedsrSJubWkFFh5vKHzawzQk1mYI . Начнем сначала? /button")
    if message.text == "😀Веселое настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item36 = types.KeyboardButton("💿Новости")
        item37 = types.KeyboardButton("💿Музыка")
        item38 = types.KeyboardButton("💿Видео")
        markup.add(item36, item37, item38)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "💿Новости":
        bot.send_message(message.chat.id, "Новости готовы к прочтению https://78.ru/news/sport ! Начнем сначала /button ?")
    if message.text == "💿Музыка":
        bot.send_message(message.chat.id, "Музыка готова https://radiopiterfm.ru/ . Начнем сначала /button ?")
    if message.text == "💿Видео":
        bot.send_message(message.chat.id, "Видео-контент подобран https://www.youtube.com/playlist?list=PLYwsV3XnGQ8jyqqcpes7v6Usi9p2iI5yS . Начнем сначала /button ?")
    if message.text == "😀Грустное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item39 = types.KeyboardButton("📱Новости")
        item40 = types.KeyboardButton("📱Музыка")
        item41 = types.KeyboardButton("📱Видео")
        markup.add(item39, item40, item41)
        bot.send_message(message.chat.id, "А теперь давайте узнаем, какой контент вам нужен", reply_markup=markup)
    if message.text == "📱Новости":
        bot.send_message(message.chat.id, "Ваши новости подобраны https://78.ru/news/proisshestviya . Начнем сначала? /button")
    if message.text == "📱Музыка":
        bot.send_message(message.chat.id, "Музыка готова https://101.ru/radio/channel/354 . Начнем сначала? /button")
    if message.text == "📱Видео":
        bot.send_message(message.chat.id, "Видео пора просмотреть https://www.youtube.com/playlist?list=PLZaLeeSPu2WCbFLAqndFfXu3_Scofvsyk ! Надеюсь оно поможет вам справиться с грустью! Начнем сначала? /button")
    elif message.text == "Ночь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item42 = types.KeyboardButton("😶Спокойное настроение")
        item43 = types.KeyboardButton("😶Веселое настроение")
        item44 = types.KeyboardButton("😶Грустное настроение")
        markup.add(item42, item43, item44)
        bot.send_message(message.chat.id, "Какой у вас настрой? Ночноооой. Ладно, разберемся, что вам нужно", reply_markup=markup)
    if message.text == "😶Спокойное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item45 = types.KeyboardButton("💾Новости")
        item46 = types.KeyboardButton("💾Музыка")
        item47 = types.KeyboardButton("💾Видео")
        markup.add(item45, item46, item47)
        bot.send_message(message.chat.id, "Какой контент вам нужен?", reply_markup=markup)
    if message.text == "💾Новости":
        bot.send_message(message.chat.id, "Новости готовы и ждут вас https://www.1tv.ru/news/mir ! Начнем сначала? /button")
    if message.text == "💾Музыка":
        bot.send_message(message.chat.id, "Музыку заказывали https://101.ru/radio/channel/357 ? Начнем сначала? /button")
    if message.text == "💾Видео":
        bot.send_message(message.chat.id, "Ролик подготовлен https://www.youtube.com/playlist?list=PL1ZzD6D7VgtQwFjjKvxVvlhMDKOulS2c3 . Начнем сначала? /button")
    if message.text == "😶Веселое настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item48 = types.KeyboardButton("🎛Новости")
        item49 = types.KeyboardButton("🎛Музыка")
        item50 = types.KeyboardButton("🎛Видео")
        markup.add(item48, item49, item50)
        bot.send_message(message.chat.id, "Какой контент вам нужен?", reply_markup=markup)
    if message.text == "🎛Новости":
        bot.send_message(message.chat.id, "Мы собрали для вас свежие новости, они ждут https://www.1tv.ru/news/obschestvo . Что-то еще /button ?")
    if message.text == "🎛Музыка":
        bot.send_message(message.chat.id, "Музыка готова https://101.ru/radio/channel/434 . Что-то еще /button ?")
    if message.text == "🎛Видео":
        bot.send_message(message.chat.id, "Видео-ролики подобранны https://www.youtube.com/playlist?list=PLSyU9XVe8SE3m9yZsjfy6Fk8N_j3doZ3w ! Что-то еще /button ?")
    if message.text == "😶Грустное настроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item51 = types.KeyboardButton("💽Новости")
        item52 = types.KeyboardButton("💽Музыка")
        item53 = types.KeyboardButton("💽Видео")
        markup.add(item51, item52, item53)
        bot.send_message(message.chat.id, "Какой контент вам нужен?", reply_markup=markup)
    if message.text == "💽Новости":
        bot.send_message(message.chat.id, "Ваши новости готовы к прочтению https://www.1tv.ru/news/criminal . Еще что-нибудь /button ?")
    if message.text == "💽Музыка":
        bot.send_message(message.chat.id, "Музыка ждет вашего прослушивания https://101.ru/radio/channel/376 ! Что-то еще /button ?")
    if message.text == "💽Видео":
        bot.send_message(message.chat.id, "Видео-контент готов, он попробует исправить ваше настроение https://www.youtube.com/playlist?list=PLforUZ3gckkBgxY7mSIeBoekwcCGPAFat . Что-ниибудь еще /button ?")


bot.polling(none_stop=True)











