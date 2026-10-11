import sqlite3
from db_manager.db_config import DB_PATH
from utils.logger import db_logger
from utils.retry import retry_on_lock
from utils.input_cleaner import clean_inputs

@db_logger
@retry_on_lock
@clean_inputs
def add_data(args,db_path=DB_PATH) :
    '''Функция принимает аргументы в виде словаря и записывает их в базу'''
    try :
        with sqlite3.connect(db_path) as connection :
            cursor = connection.cursor()
            get_values_place = ', '.join(['?'] * len(args))
            get_placeholders = ', '.join(args)
            get_values = tuple(args.values())
            add_query = f"INSERT OR IGNORE INTO personal_safe ({get_placeholders}) VALUES ({get_values_place}) "
            cursor.execute(add_query,get_values)
        return "success"
    except sqlite3.Error as e :
         raise e

@db_logger
@retry_on_lock
def delete_data(id,db_path=DB_PATH) :
    '''Функция принимает id записи и проводит удаление записи'''
    try :
        with sqlite3.connect(db_path) as connection :
            cursor = connection.cursor()
            query_check = 'SELECT * FROM personal_safe WHERE id = ?'
            delete_value = (id,)
            cursor.execute(query_check,delete_value)
            res = cursor.fetchone()
            if res :
                delete_query = "DELETE FROM personal_safe WHERE id = ?"
                cursor.execute(delete_query,delete_value)
                return "success"
            else :
                 return "not find"
    except sqlite3.Error as e :
         raise e

@db_logger
@retry_on_lock
def show_data(db_path=DB_PATH) :
    '''Функция возвращает все записи из базы'''
    try :
        with sqlite3.connect(db_path) as connection :
                cursor = connection.cursor()
                show_query = "SELECT * FROM personal_safe"
                cursor.execute(show_query)
                res = cursor.fetchall()
        return res
    except sqlite3.Error as e :
         raise e
