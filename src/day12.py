import utils

# Dijkstra's algorithm google trends be like: 📈
def dijkstra(grid, start, end):
    dist = {}
    vertices = set()

    current = (0, 0)
    for line in grid:
        for char in line:
            if start(char):
                current = (line.index(char), grid.index(line))
                break
    
    for y, row in enumerate(grid):
        for x in range(len(row)):
            dist[(x, y)] = float('inf')
            vertices.add((x, y))

    original_grid = grid
    grid = list(map(lambda x: x.replace('S', 'a').replace('E', 'z'), grid))
    
    dist[current] = 0

    start = True
    rev = grid[current[1]][current[0]] == 'z' 
    while len(vertices) > 0:
        if start:
            start = False
            vertex = current
        else:
            vertex = min(vertices, key=lambda x: dist[x])

        vertices.remove(vertex)

        neighbors = []
        
        if vertex[0] > 0:
            neighbors.append((vertex[0]-1, vertex[1]))

        if vertex[1] > 0:
            neighbors.append((vertex[0], vertex[1]-1))

        if vertex[0] < len(grid[0])-1:
            neighbors.append((vertex[0]+1, vertex[1]))

        if vertex[1] < len(grid)-1:
            neighbors.append((vertex[0], vertex[1]+1))

        for neighbor in filter(lambda n: n in vertices, neighbors):
            if rev:
                if ord(grid[vertex[1]][vertex[0]]) - 1 > ord(grid[neighbor[1]][neighbor[0]]):
                    continue
            else:
                if ord(grid[neighbor[1]][neighbor[0]]) - 1 > ord(grid[vertex[1]][vertex[0]]):
                    continue
            alt = dist[vertex] + 1
            if alt < dist[neighbor]:
                dist[neighbor] = alt

    end_dists = []
    for y, row in enumerate(grid):
        for x in range(len(row)):
            if end(original_grid[y][x]):
                end_dists.append(dist[(x, y)])

    return min(end_dists)

def day12p1(data):
    data = data.split('\n')
    return dijkstra(data, lambda c: c == 'S', lambda c: c == 'E')

def day12p2(data):
    data = data.split('\n')
    return dijkstra(data, lambda c: c == 'E', lambda c: c == 'a')

assert day12p1(utils.read(12, True)) == 31
assert day12p2(utils.read(12, True)) == 29
print(day12p1(utils.read(12)))
print(day12p2(utils.read(12)))