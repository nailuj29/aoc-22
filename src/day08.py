import utils

def visible(data, x, y):
    if x == 0 or y == 0:
        return True

    if x == len(data[0]) - 1 or y == len(data) - 1:
        return True

    height = data[y][x]
    left = True
    for x1 in range(0, x):
        if data[y][x1] >= height:
            left = False
            
    right = True
    for x1 in range(x+1, len(data[0])):
        if data[y][x1] >= height:
            right = False

    up = True
    for y1 in range(0, y):
        if data[y1][x] >= height:
            up = False

    down = True
    for y1 in range(y+1, len(data)):
        if data[y1][x] >= height:
            down = False
    
    return left or right or up or down

def score(data, x, y):
    height = data[y][x]

    left = 0
    for x1 in range(x-1, -1, -1):
        left += 1
        if height <= data[y][x1]:
            break
    
    right = 0
    for x1 in range(x+1, len(data[0])):
        right += 1
        if height <= data[y][x1]:
            break
        
    up = 0
    for y1 in range(y-1, -1, -1):
        up += 1
        if height <= data[y1][x]:
            break
        
    down = 0
    for y1 in range(y+1, len(data)):
        down += 1
        if height <= data[y1][x]:
            break
        
    return left * right * up * down

def day8p1(data):
    data = data.split("\n")
    data = [list(line) for line in data]
    data = [[int(x) for x in line] for line in data]
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if visible(data, x, y):
                count += 1
    return count

def day8p2(data):
    data = data.split("\n")
    data = [list(line) for line in data]
    data = [[int(x) for x in line] for line in data]
    scores = []
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            scores.append(score(data, x, y))
    
    return max(scores)

assert day8p1(utils.read(8, True)) == 21
assert day8p2(utils.read(8, True)) == 8
print(day8p1(utils.read(8)))
print(day8p2(utils.read(8)))