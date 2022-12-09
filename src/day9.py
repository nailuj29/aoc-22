import utils

def update_tail_pos(head_pos, tail_pos):
        x_diff = head_pos[0] - tail_pos[0]
        y_diff = head_pos[1] - tail_pos[1]

        if x_diff > 1 and y_diff > 0 or x_diff > 0 and y_diff > 1:
            return (tail_pos[0] + 1, tail_pos[1] + 1)
        elif x_diff > 1 and y_diff < 0 or x_diff > 0 and y_diff < -1:
            return (tail_pos[0] + 1, tail_pos[1] - 1)
        elif x_diff < -1 and y_diff > 0  or x_diff < 0 and y_diff > 1:
            return (tail_pos[0] - 1, tail_pos[1] + 1)
        elif x_diff < -1 and y_diff < 0 or x_diff < 0 and y_diff < -1:
            return (tail_pos[0] - 1, tail_pos[1] - 1)
        elif x_diff > 1:
            return (tail_pos[0] + 1, tail_pos[1])
        elif x_diff < -1:
            return (tail_pos[0] - 1, tail_pos[1])
        elif y_diff > 1:
            return (tail_pos[0], tail_pos[1] + 1)
        elif y_diff < -1:
            return (tail_pos[0], tail_pos[1] - 1)
        else:
            return tail_pos


def move(positions, direction, count):
    positions = positions[:]
    head_pos = positions[0]
    tail_positions = set()
    if direction == 'U':
        for i in range(count):
            positions[0] = (head_pos[0], head_pos[1] + 1)
            for i in range(1, len(positions)):
                positions[i] = update_tail_pos(positions[i-1], positions[i])
            tail_positions.add(positions[-1])
            head_pos = positions[0]

    if direction == 'D':
        for i in range(count):
            positions[0] = (head_pos[0], head_pos[1] - 1)
            for i in range(1, len(positions)):
                positions[i] = update_tail_pos(positions[i-1], positions[i])
            tail_positions.add(positions[-1])
            head_pos = positions[0]

    if direction == 'L':
        for i in range(count):
            positions[0] = (head_pos[0] - 1, head_pos[1])
            for i in range(1, len(positions)):
                positions[i] = update_tail_pos(positions[i-1], positions[i])
            tail_positions.add(positions[-1])
            head_pos = positions[0]
            
    if direction == 'R':
        for i in range(count):
            positions[0] = (head_pos[0] + 1, head_pos[1])
            for i in range(1, len(positions)):
                positions[i] = update_tail_pos(positions[i-1], positions[i])
            tail_positions.add(positions[-1])
            head_pos = positions[0]

    return positions, tail_positions

def day9p1(data):
    data = data.split('\n') 
    data = [line.split(' ') for line in data]
    data = [(line[0], int(line[1])) for line in data]
    tail_positions = {(0, 0)}
    head_pos = (0, 0)
    tail_pos = (0, 0)
    for line in data:
        positions, temp_tail_positions = move([head_pos, tail_pos], line[0], line[1])
        head_pos = positions[0]
        tail_pos = positions[1]
        tail_positions = tail_positions.union(temp_tail_positions)
    return len(tail_positions)

def day9p2(data):
    data = data.split('\n') 
    data = [line.split(' ') for line in data]
    data = [(line[0], int(line[1])) for line in data]
    tail_positions = {(0, 0)}
    positions = [(0,0)] * 10
    for line in data:
        positions, temp_tail_positions = move(positions, line[0], line[1])
        tail_positions = tail_positions.union(temp_tail_positions)
    return len(tail_positions)

assert day9p1(utils.read(9, True)) == 13
# assert day9p1(utils.read(9, True)) == 1 
# input no worky because im too lazy to make multiple test input work :)
print(day9p1(utils.read(9)))
print(day9p2(utils.read(9)))