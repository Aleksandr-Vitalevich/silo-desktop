from functools import wraps
from time import sleep
import sqlite3

def retry_on_lock(func) :
    '''Декоратор повторно пытается выполнить транзакцию при блокировке базы данных'''
    @wraps(func)
    def wrapper(*args,**kwargs) :
        '''Функция обертка'''
        max_retry = 3
        delay = 1.0
        for retries in range(1,max_retry + 1) :
            try :
                res = func(*args,**kwargs)
                return res
            except sqlite3.Error as e :
                if retries == max_retry :
                    raise e
                sleep(delay)
    return wrapper
                
            