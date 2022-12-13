import functools
import utils

types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def day3p1(data):
    bags = []
    for line in data.split("\n"):
        bags.append([set(line[:len(line)//2]), set(line[len(line)//2:])])

    items = []
    for bag in bags:
        for same in bag[0].intersection(bag[1]):
            items.append(same)

    return sum(map(lambda i: types.index(i) + 1, items))

def day3p2(data):
    bags = list(map(lambda l: set(l), data.split("\n")))
    groups = []
    for i in range(len(bags)):
        if i % 3 == 0:
            groups.append([])
        groups[-1].append(bags[i])

    badges = list(map(lambda g: functools.reduce(lambda a, b: a.intersection(b), g), groups)) # the reduce call computes the intersection of all sets in the group
    the_sum = 0
    for badge in badges:
        for item in badge:
            the_sum += types.index(item) + 1

    return the_sum


assert day3p1(utils.read(3, True)) == 157
assert day3p2(utils.read(3, True)) == 70
print(day3p1(utils.read(3)))
print(day3p2(utils.read(3)))