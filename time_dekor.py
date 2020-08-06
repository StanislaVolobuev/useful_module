'''декоратор измеряет время выполнения программы в секундах'''
import datetime


def time_process_dekor(func):
    def wrapper(*args, **kwargs):
        print('start')
        start = datetime.datetime.today()
        s = start.minute * 60 + start.second
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        e = (end.minute * 60 + end.second) - s
        print('finished', e, 'sec')
        return result

    return wrapper
