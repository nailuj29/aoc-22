import utils

def process_data(data):
    lines = data.split('\n')
    i = 0
    elves = [0]
    for line in lines:
        if not line:
            i += 1
            elves.append(0)
        else:
            elves[i] += int(line)
    return elves

def day1p1(data):
    elves = process_data(data)
            
    return max(elves)

def day1p2(data):
    elves = process_data(data)
            
    elves.sort(reverse=True)
    return sum(elves[0:3])

assert day1p1(utils.read(1, True)) == 24000
assert day1p2(utils.read(1, True)) == 45000
print(day1p1(utils.read(1)))
print(day1p2(utils.read(1)))