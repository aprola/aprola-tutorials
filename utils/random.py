import random
import time

from datetime import datetime, timedelta
from functools import wraps

def throttle(seconds=0, minutes=0, hours=0):
    throttle_period = timedelta(seconds=seconds, minutes=minutes, hours=hours)
    def throttle_decorator(fn):
        time_of_last_call = datetime.min
        @wraps(fn)
        def wrapper(*args, **kwargs):
            now = datetime.now()
            if now - time_of_last_call > throttle_period:
                nonlocal time_of_last_call
                time_of_last_call = now
                return fn(*args, **kwargs)
        return wrapper
    return throttle_decorator

@throttle(4)
def print_at_interval(*val):
    print(*val)
    

def randomArrayGeneratorWithDuplicates(nos, min=0, max=1000):
    values = []
    x = nos
    while(x > 0):
        y = random.randint(min, max)
        values.append(y)
        x -= 1
        # print_at_interval("percent: ", 100*(nos-x)/nos)
    return values


def randomArrayGeneratorWithoutDuplicates(nos):
    values = []
    for x in range(nos):
        y = len(values)
        pos = random.randint(0, y)
        print_at_interval("percent: ", 100*x/nos)
        values.insert(pos, x)
    return values