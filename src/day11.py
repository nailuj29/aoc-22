import utils

class Monkey():
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.throws = 0

def parse_monkeys(data):
    raw_monkeys = data.split('\n\n')
    raw_monkeys = [monkey.split('\n') for monkey in raw_monkeys]
    raw_monkeys = [[line.strip() for line in monkey] for monkey in raw_monkeys]
    raw_monkeys = [monkey[1:] for monkey in raw_monkeys]
    monkeys = []
    for raw_monkey in raw_monkeys:
        items = raw_monkey[0].split(': ')[1]
        items = items.split(', ')
        items = [int(item) for item in items]
        raw_operation = raw_monkey[1].split(': ')[1]
        raw_operation = raw_operation.split(' ')[3:]
        op = raw_operation[0]
        operand = raw_operation[1]
        if operand == 'old':
            op = '**'
            operand = 2

        operand = int(operand)
        test = int(raw_monkey[2].split(' ')[-1])
        if_true = int(raw_monkey[3].split(' ')[-1])
        if_false = int(raw_monkey[4].split(' ')[-1])

        monkeys.append(Monkey(items, [op, operand], test, if_true, if_false))

    return monkeys

def round(monkeys, managable=True):
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.test
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for i in range(len(monkey.items)):
            operand = monkey.operation[1]
            match monkey.operation[0]:
                case '*':
                    monkey.items[i] *= operand
                case '+':
                    monkey.items[i] += operand
                case '**':
                    monkey.items[i] **= operand
            if managable:
                monkey.items[i] //= 3

        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            if item % monkey.test == 0:
                monkeys[monkey.if_true].items.append(item % lcm)
            else:
                monkeys[monkey.if_false].items.append(item % lcm)
            monkey.throws += 1

def day11p1(data):
    monkeys = parse_monkeys(data)
    for i in range(20):
        round(monkeys)

    throws = [monkey.throws for monkey in monkeys]
    throws.sort()
    return throws[-1] * throws[-2]

def day11p2(data):
    monkeys = parse_monkeys(data)
    for i in range(10000):
        round(monkeys, False)

    throws = [monkey.throws for monkey in monkeys]
    throws.sort()
    return throws[-1] * throws[-2]

assert day11p1(utils.read(11, True)) == 10605
assert day11p2(utils.read(11, True)) == 2713310158
print(day11p1(utils.read(11)))
print(day11p2(utils.read(11)))