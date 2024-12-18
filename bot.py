import telebot
from keyboars import start_keyboard, film_find_keyboard
from sql_query import convert_sql_data_to_str, excecute_sql_query

TOKEN = "7158656277:AAG8zdNYKe7p5o6QyCmXzwwXhoVIlfhzUDQ"
bot = telebot.TeleBot(TOKEN)
search_var = get_search_var("123")

@bot.message_handler(commands=['start'])
def bot_start(message) -> None:
    text = """Привет, я бот который поможет найти тебе твой любимый фильм по разным критериям!
Напиши"поиск" или нажми на кнопку внизу чтобы найти фильм!"""
    keyboard = start_keyboard()
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_search_type(message) -> None:
    text = "Выберите вариант поиска:"
    keyboard = film_find_keyboard()
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

def get_search_var(message) -> str:
    string_h = {"movies.name":"название фильма", "genres.name":"жанр","year":"год","raiting":"рейтинг фильма","age_raiting":"возрастной рейтинг фильм"}
    return message.text

@bot.callback_query_handler(lambda call: "search_type/" in call.data)
def get_sql_data(call) -> None:
    try:

        sql_data = convert_sql_data_to_str(excecute_sql_query(search_type=call.data[13:], search_var=search_var))
        bot.send_message(call.message.chat.id, sql_data)
    except Exception:
        bot.send_message(call.message.chat.id, "Неверно указанны данные для поиска!")
        bot.register_next_step_handler(call, get_search_var)


bot.polling(non_stop=True, interval=1)    