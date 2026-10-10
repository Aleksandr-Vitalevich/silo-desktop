import sqlite3
from db_manager.db_config import DB_PATH
from utils.logger import db_logger
from utils.retry import retry_on_lock

@db_logger
@retry_on_lock
def add_data_to_diary(text,db_path=DB_PATH) :
    '''Функция принимает текст и записывает их в базу'''
    try :
        with sqlite3.connect(db_path) as connection :
            cursor = connection.cursor()
            value = (text,)
            add_query = f"INSERT OR IGNORE INTO personal_diary (text_diary) VALUES (?) "
            cursor.execute(add_query,value)
        return "success"
    except sqlite3.Error as e :
        raise e

@db_logger
@retry_on_lock
def show_data_to_diary(db_path=DB_PATH) :
    '''Функция возвращает все записи из базы'''
    try :
        with sqlite3.connect(db_path) as connection :
            cursor = connection.cursor()
            show_query = "SELECT * FROM personal_diary ORDER BY created_at DESC"
            cursor.execute(show_query)
            res = cursor.fetchall()
        return res
    except sqlite3.Error as e :
            raise e
