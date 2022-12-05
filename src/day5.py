import utils
import re

def process_stacks(data):
    data = data.split('\n')
    data = data[0:len(data)-1]
    data.reverse()
    stacks = [] 
    for i in range((len(data[0]) + 1) // 4):
        stacks.append([])

    for line in data:
        j = 0
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[j].append(line[i])
            j += 1

    return stacks

def process_lines(data):
    lines = data.split('\n')

    regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

    code = []
    for line in lines:
        res = re.search(regex, line)
        code.append([int(res.group(1)), int(res.group(2)) - 1, int(res.group(3)) - 1])
    
    return code

def day5p1(data):
    data = data.split('\n\n')
    stacks = process_stacks(data[0])

    code = process_lines(data[1])
    for line in code:
        for i in range(line[0]):
            stacks[line[2]].append(stacks[line[1]].pop())

    result = ''
    for stack in stacks:
        result += stack[-1]

    return result

def day5p2(data):
    data = data.split('\n\n')
    stacks = process_stacks(data[0])

    code = process_lines(data[1])
    for line in code:
        temp = []
        for i in range(line[0]):
            temp.append(stacks[line[1]].pop())
        temp.reverse()
        for item in temp:
            stacks[line[2]].append(item)

    result = ''
    for stack in stacks:
        result += stack[-1]

    return result

assert day5p1(utils.read(5, True)) == 'CMZ'
assert day5p2(utils.read(5, True)) == 'MCD'
print(day5p1(utils.read(5)))
print(day5p2(utils.read(5)))