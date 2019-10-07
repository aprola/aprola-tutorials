import random

def randomArrayGenerator(nos):
    values = []
    x = nos
    while(x > 0):
        y = random.randint(0, 1000)
        try:
            values.index(y)
        except:
            values.append(y)
            x -= 1
    return values


def randomArrayGenerator2(nos):
    values = []
    for x in range(nos):
        y = len(values)
        pos = random.randint(0, y)
        values.insert(pos, x)
    return values