import random

def randomArrayGeneratorWithDuplicates(nos, min=0, max=1000):
    values = []
    x = nos
    while(x > 0):
        y = random.randint(min, max)
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