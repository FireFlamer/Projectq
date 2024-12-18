from telebot import types

def start_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup()
    find_button = types.KeyboardButton("Поиск")
    keyboard.add(find_button)
    return keyboard

def film_find_keyboard() -> types.InlineKeyboardMarkup:
    search = [["По названию фильма","name"], ["По жанру","genre.name"],["По году","year"],["По рейтингу","raiting"],["По возрастному рейтингу","age_raiting"]]
    keyboard = types.InlineKeyboardMarkup()
    btn_name = types.InlineKeyboardButton("По названию фильма", callback_data="search_type/movies.name")
    btn_genre = types.InlineKeyboardButton("По жанру", callback_data="search_type/genre")
    btn_year = types.InlineKeyboardButton("По году", callback_data="search_type/year")
    btn_raiting = types.InlineKeyboardButton("По рейтингу", callback_data="search_type/raiting")
    btn_age_ratiting = types.InlineKeyboardButton("По возрастному рейтингу", callback_data="search_type/age_raiting")
    keyboard.add(btn_name, btn_genre, btn_year, btn_raiting, btn_age_ratiting)

    return keyboard

