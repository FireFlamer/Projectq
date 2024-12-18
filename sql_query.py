import sqlite3 as sq3

def excecute_sql_query(search_type: str, search_var: str) -> None:
    connection = sq3.connect("films.db")
    sql_query = f"""SELECT movies.title, movies.year, movies.duration, movies.rating, movies.age_rating 
                    FROM movies JOIN genres ON movies.genre_id = genres.id 
                    WHERE  {search_type} = '{search_var.lower()}'"""

    sql_data = connection.execute(sql_query)
    return sql_data

def convert_sql_data_to_str(sql_data: list[tuple]) -> str:
    string = ""

    string += "Название, год, длительность, рейтинг, возрастной рейтинг" + "\n"
    for data in sql_data:
        string += ", ".join(map(str, data)) + "\n"

    
    return string.replace("None", "Нет")

