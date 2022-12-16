import utils
import re
import joblib

REGEX = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'

def parse_sensors(data):
    grid = {}
    for line in data.split('\n'):
        matches = re.match(REGEX, line)
        sensor_pos = (int(matches.group(1)), int(matches.group(2)))
        beacon_pos = (int(matches.group(3)), int(matches.group(4)))
        
        offsets = (abs(sensor_pos[0] - beacon_pos[0]), abs(sensor_pos[1] - beacon_pos[1]))
        distance = offsets[0] + offsets[1]
        x_range = set(range(sensor_pos[0] - distance, sensor_pos[0] + distance + 1))
        y_range = set(range(sensor_pos[1] - distance, sensor_pos[1] + distance + 1))
        grid[sensor_pos] = {'x': x_range, 'y': y_range, 'beacon': beacon_pos, 'dist': distance}
        
    return grid
        
def day15p1(data, row):
    grid = parse_sensors(data)
    
    no_beacons = set()
    for sensor in grid.keys():
        data = grid[sensor]
        if row in data['y']:
            y_dist = abs(sensor[1] - row)
            start = min(data['x']) + y_dist
            end = max(data['x']) - y_dist
            for x in range(start, end + 1):
                if (x, row) != data['beacon']:
                    no_beacons.add((x, row))
                    
    return len(no_beacons)

def day15p2(data):
    grid = parse_sensors(data)
    
    
    dists = {}
    for sensor in grid.keys():
        dists[sensor] = {}
        for other in grid.keys():
            if other == sensor:
                continue
            
            dist = abs(other[0] - sensor[0]) + abs(other[1] - sensor[1])
            dists[sensor][other] = dist
    
    to_check = set()
    for sensor, sensor_dists in dists.items():
        beacon_dist = abs(grid[sensor]['beacon'][0] - sensor[0]) + \
                        abs(grid[sensor]['beacon'][1] - sensor[1])
        for other in sensor_dists.keys():
            other_beacon_dist = abs(grid[other]['beacon'][0] - other[0]) + \
                        abs(grid[other]['beacon'][1] - other[1])
            if sensor_dists[other] == beacon_dist + other_beacon_dist + 2:
                if (other, sensor) not in to_check:
                    to_check.add((sensor, other))
             
    to_check = list(to_check)  
    x_dir = 1 if to_check[0][0][0] < to_check[0][1][0] else -1
    y_dir = 1 if to_check[0][0][1] < to_check[0][1][1] else -1
    dir_a = x_dir, y_dir
    
    x_dir = 1 if to_check[1][0][0] < to_check[1][1][0] else -1
    y_dir = 1 if to_check[1][0][1] < to_check[1][1][1] else -1
    dir_b = x_dir, y_dir
    
    beacon_a = grid[to_check[0][0]]['beacon']
    beacon_b = grid[to_check[1][0]]['beacon']
    
    beacon_dist_a = abs(beacon_a[0] - to_check[0][0][0]) \
                    + abs(beacon_a[1] - to_check[0][0][1])
                    
    beacon_dist_b = abs(beacon_b[0] - to_check[1][0][0]) \
                    + abs(beacon_b[1] - to_check[1][0][1])
                    
    for i in range(beacon_dist_a + 2):
        x = to_check[0][0][0] + (i * dir_a[0])
        y = to_check[0][0][1] + (beacon_dist_a + 1 - i) * dir_a[1]
        if abs(to_check[1][0][0] - x) + abs(to_check[1][0][1] - y) \
            == beacon_dist_b + 1:
            return x * 4000000 + y

assert day15p1(utils.read(15, True), 10) == 26
# assert day15p2(utils.read(15, True)) == 56000011 test input is weird
print(day15p1(utils.read(15), 2000000))
print(day15p2(utils.read(15)))