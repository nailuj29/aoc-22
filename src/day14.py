import utils

SAND_POINT = (500, 0)

def gen_grid(data):
    data = data.split('\n')
    data = [line.split(' -> ') for line in data]
    grid = set()
    for line in data:
        for i in range(1, len(line)):
            start = line[i-1].split(',')
            start = (int(start[0]), int(start[1]))
            end = line[i].split(',')
            end = (int(end[0]), int(end[1]))

            if start[0] == end[0]:
                for y in range(min(start[1], end[1]), max(start[1],  end[1]) + 1):
                    grid.add((start[0], y))
                    
                    
            if start[1] == end[1]:
                for x in range(min(start[0], end[0]), max(start[0],  end[0]) + 1):
                    grid.add((x, start[1]))
                    
    return grid

def day14p1(data):
    grid = gen_grid(data)
    max_y = max([point[1] for point in grid])
    sand_count = 0
    while True:
        sand = SAND_POINT
        at_rest = False
        while not at_rest:
            if sand[1] >= max_y:
                return sand_count
            
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                at_rest = True
                sand_count += 1
                grid.add(sand)
                
def day14p2(data):
    grid = gen_grid(data)
    max_y = max([point[1] for point in grid])
    sand_count = 0
    while True:
        sand = SAND_POINT
        at_rest = False
        while not at_rest:
            if sand[1] == max_y + 1:
                at_rest = True
                sand_count += 1
                grid.add(sand) 
            elif (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                at_rest = True
                sand_count += 1
                grid.add(sand)
                
            if sand == (500, 0) and at_rest:
                return sand_count

assert day14p1(utils.read(14, True)) == 24
assert day14p2(utils.read(14, True)) == 93
print(day14p1(utils.read(14)))
print(day14p2(utils.read(14)))
