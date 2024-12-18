import sqlite3 as sq3

def take_sql_query() -> str:
    sql_query = ""

    while True:
        user_sql_string = input()
        if user_sql_string:
            sql_query += user_sql_string + " "
        else:
            break

    return sql_query

def excecute_sql_query(sql_query: str) -> list[tuple] | None:
    print("Начинаю выполнение запроса...")
    
    connection = sq3.connect("music.db")
    try:
        sql_data = connection.execute(sql_query)
        print("Запрос успешно выполнен.")
        return sql_data.fetchall()
    except Exception:
        print("Неверно введённый sql-запрос!")
    connection.close()
    return None

def save_to_file(sql_data: list[tuple], file_type: str= ".txt") -> None:
    file_name = input("Введите название файла для сохранения результата: ")

    with open(f"{file_name + file_type}", "a", encoding='utf-8') as f:
        for data in sql_data:
            f.write(", ".join([str(dt) for dt in data]) + "\n")
        f.close()


print("Добро пожаловать в программу для выполнения SQL-запросов.\nВведите SQL-запрос (отправьте пустую строку для выполнения запроса): ")
dt = excecute_sql_query(take_sql_query())
if dt:
    save_to_file(dt)





