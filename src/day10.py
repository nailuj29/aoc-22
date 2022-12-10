import utils

def run(lines, breakpoints):
    cycles = 0
    x = 1
    outputs = []
    for line in lines:
        cycles += 1


        if cycles in breakpoints:
            outputs.append(cycles * x)

        if line[0] == "addx":
            cycles += 1
            if cycles in breakpoints:
                outputs.append(cycles * x)
            x += int(line[1])

    return outputs

def run_image(lines):
    cycles = 0
    x = 1
    image = [False] * 240
    for line in lines:
        cycles += 1
        if x-1 <= (cycles-1) % 40 <= x+1:
            image[cycles-1] = True

        if line[0] == "addx":
            cycles += 1
            if x-1 <= (cycles-1) % 40 <= x+1:
                image[cycles-1] = True
            x += int(line[1])

    return image

def day10p1(data):
    data = data.split('\n')
    data = [line.split(' ') for line in data]
    outputs = run(data, [20, 60, 100, 140, 180, 220])
    return sum(outputs)

def day10p2(data):
    data = data.split('\n')
    data = [line.split(' ') for line in data]
    image = run_image(data)
    for i in range(0,6):
        for j in range(0, 40):
            if image[i*40+j]:
                print('#', end='')
            else:
                print('.', end='')
        print()

assert day10p1(utils.read(10, True)) == 13140
print(day10p1(utils.read(10)))
print()
print("*" * 60)
print()
day10p2(utils.read(10, True))
print()
print("*" * 60)
print()
day10p2(utils.read(10))