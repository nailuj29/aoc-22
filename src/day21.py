import utils

def parse_monkeys(data):
    data = data.split("\n")
    monkeys = {}
    for line in data:
        line = line.split(": ")
        if '+' in line[1]:
            monkeys[line[0]] = { 'op': 'add', 'operands': line[1].split(" + ") }
        elif '*' in line[1]:
            monkeys[line[0]] = { 'op': 'mul', 'operands': line[1].split(" * ") }
        elif '-' in line[1]:
            monkeys[line[0]] = { 'op': 'sub', 'operands': line[1].split(" - ") }
        elif '/' in line[1]:
            monkeys[line[0]] = { 'op': 'div', 'operands': line[1].split(" / ") }
        else:
            monkeys[line[0]] = { 'op': 'val', 'operands': int(line[1]) }

    return monkeys

def eval_monkey(monkey, monkeys):
    expr = monkeys[monkey]
    match expr['op']:
        case 'add':
            return eval_monkey(expr['operands'][0], monkeys) + eval_monkey(expr['operands'][1], monkeys)
        case 'mul':
            return eval_monkey(expr['operands'][0], monkeys) * eval_monkey(expr['operands'][1], monkeys)
        case 'sub':
            return eval_monkey(expr['operands'][0], monkeys) - eval_monkey(expr['operands'][1], monkeys)
        case 'div':
            return eval_monkey(expr['operands'][0], monkeys) // eval_monkey(expr['operands'][1], monkeys)
        case 'val':
            return expr['operands']

def eval_monkey_human(monkey, monkeys, val):
    if monkey == 'humn':
        return val
    else:
        expr = monkeys[monkey]
    match expr['op']:
        case 'add':
            return eval_monkey_human(expr['operands'][0], monkeys, val) + eval_monkey_human(expr['operands'][1], monkeys, val)
        case 'mul':
            return eval_monkey_human(expr['operands'][0], monkeys, val) * eval_monkey_human(expr['operands'][1], monkeys, val)
        case 'sub':
            return eval_monkey_human(expr['operands'][0], monkeys, val) - eval_monkey_human(expr['operands'][1], monkeys, val)
        case 'div':
            return eval_monkey_human(expr['operands'][0], monkeys, val) // eval_monkey_human(expr['operands'][1], monkeys, val)
        case 'val':
            return expr['operands']

def day21p1(data):
    monkeys = parse_monkeys(data)
    return eval_monkey('root', monkeys)

def day21p2(data):
    monkeys = parse_monkeys(data)
    root = monkeys['root']
    root['op'] = 'sub'
    monkeys['root'] = root
    val = 0
    while True:
        evaled = eval_monkey_human('root', monkeys, val)
        if evaled == 0:
            return val
        val += 1
        if val % 10000 == 0:
            print(val)

assert day21p1(utils.read(21, True)) == 152
# assert day21p2(utils.read(21, True)) == 301
print(day21p1(utils.read(21)))
# print(day21p2(utils.read(21))) # im impatient i dont wanna wait this long