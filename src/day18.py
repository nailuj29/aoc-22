import utils

def day18p1(data):
    data = data.split("\n")
    data = [eval(line) for line in data]
    
    points = set()
    area = 0
    for point in data:
        neighbors = []
        neighbors.append((point[0] + 1, point[1], point[2]))
        neighbors.append((point[0] - 1, point[1], point[2]))
        neighbors.append((point[0], point[1] + 1, point[2]))
        neighbors.append((point[0], point[1] - 1, point[2]))
        neighbors.append((point[0], point[1], point[2] + 1))
        neighbors.append((point[0], point[1], point[2] - 1))

        for neighbor in neighbors:
            if neighbor in points:
                area -= 2

        area += 6
        points.add(point)

    return area

# def day18p2(data):
#     data = data.split("\n")
#     data = [eval(line) for line in data]
    
#     points = set()
#     area = 0
#     for point in data:
#         neighbors = []
#         neighbors.append((point[0] + 1, point[1], point[2]))
#         neighbors.append((point[0] - 1, point[1], point[2]))
#         neighbors.append((point[0], point[1] + 1, point[2]))
#         neighbors.append((point[0], point[1] - 1, point[2]))
#         neighbors.append((point[0], point[1], point[2] + 1))
#         neighbors.append((point[0], point[1], point[2] - 1))


#         topback = (point[0] + 1, point[1] - 1, point[2])
#         topfront = (point[0] + 1, point[1] + 1, point[2])
#         topleft = (point[0] + 1, point[1], point[2] - 1)
#         topright = (point[0] + 1, point[1], point[2] + 1)

#         bottomback = (point[0] - 1, point[1] - 1, point[2])
#         bottomfront = (point[0] - 1, point[1] + 1, point[2])
#         bottomleft = (point[0] - 1, point[1], point[2] - 1)
#         bottomright = (point[0] - 1, point[1], point[2] + 1)

#         frontleft = (point[0], point[1] + 1, point[2] - 1)
#         frontright = (point[0], point[1] + 1, point[2] + 1)
#         backleft = (point[0], point[1] - 1, point[2] - 1)
#         backright = (point[0], point[1] - 1, point[2] + 1)

#         top = [topback, topfront, topleft, topright]
#         top_surrounded = all([edge in points for edge in top])
#         bottom = [bottomback, bottomfront, bottomleft, bottomright]
#         bottom_surrounded = all([edge in points for edge in bottom])
#         left = [topleft, frontleft, backleft, bottomleft]
#         left_surrounded = all([edge in points for edge in left])
#         right = [topright, frontright, backright, bottomright]
#         right_surrounded = all([edge in points for edge in right])
#         front = [topfront, frontleft, frontright, bottomfront]
#         front_surrounded = all([edge in points for edge in front])
#         back = [topback, backleft, backright, bottomback]
#         back_surrounded = all([edge in points for edge in back])

#         if top_surrounded and :

#         for neighbor in neighbors:
#             if neighbor in points:
#                 area -= 2

#         area += 6
#         points.add(point)

#     return area

# Part 2 is way harder than i thought 
assert day18p1(utils.read(18, True)) == 64
# assert day18p2(utils.read(18, True)) == 58
print(day18p1(utils.read(18)))
# print(day18p2(utils.read(18)))