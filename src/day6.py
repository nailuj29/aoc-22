import utils

def day6p1(data):
    for i in range(3, len(data)):
        packet = [data[i-3], data[i-2], data[i-1], data[i]]
        unique = set(packet)
        if len(unique) == len(packet):
            return i + 1

    return -1

def day6p2(data):
    for i in range(13, len(data)):
        packet = data[i-13:i+1]
        unique = set(packet)
        if len(unique) == len(packet):
            return i + 1

    return -1


assert day6p1(utils.read(6, True)) == 10
assert day6p2(utils.read(6, True)) == 29
print(day6p1(utils.read(6)))
print(day6p2(utils.read(6)))