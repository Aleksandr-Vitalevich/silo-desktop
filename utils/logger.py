from datetime import datetime
import os
from functools import wraps
import time
MODULE_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_logs_file = os.path.join(MODULE_BASE_DIR,"system_logs.log")

def db_logger(func) :
    '''Декоратор логирования'''
    @wraps(func)
    def wrapper(*args,**kwargs) :
        '''Наша функция обертка'''
        start_time_func = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_perf = time.perf_counter()
        try :
            result = func(*args,**kwargs)
            end_perf = time.perf_counter()
            time_delta = end_perf - start_perf
            log_entry = f"[{start_time_func}] : FUNCTION : {func.__name__} | STATUS: SUCCESS | MSG: {result} | TIME_WORK : {time_delta:.4f}\n"    
            with open(path_logs_file,'a',encoding='utf-8') as file :
                file.write(log_entry)
            return result
        except Exception as e :
            error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end_perf = time.perf_counter()
            time_delta = end_perf - start_perf
            log_entry = f"[{error_time}] : FUNCTION : {func.__name__} | STATUS: ERROR | MSG: {str(e)} | TIME_WORK : {time_delta:.4f}\n"
            with open(path_logs_file,'a',encoding='utf-8') as file :
                file.write(log_entry)    
            raise e

    return wrapper