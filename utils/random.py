import random
import time

# last_print_at = time.time()
# interval = 4

# def print_at_interval(*val):
#     if int((last_print_at%3600)/interval) != int((time.time() % 3600)/interval):
#         now = time.time()
#         print(*val)
#         last_print_at = now
    

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
        # print_at_interval("percent: ", 100*x/nos)
        values.insert(pos, x)
    return values