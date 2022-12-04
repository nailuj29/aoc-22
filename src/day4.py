import utils

def get_assignments(data):
    pairs = data.split("\n")
    pairs = list(map(lambda p: p.split(","), pairs))
    assignments = []
    for pair in pairs:
        elf1 = pair[0].split("-")
        elf2 = pair[1].split("-")
        assignment1 = range(int(elf1[0]), int(elf1[1]) + 1)
        assignment2 = range(int(elf2[0]), int(elf2[1]) + 1)
        assignments.append([set(assignment1), set(assignment2)])
    return assignments
            
def d4p1(data):
    assignments = get_assignments(data)

    count = 0
    for assignment in assignments:
        if len(assignment[0].union(assignment[1])) == max(len(assignment[0]), len(assignment[1])):
            count += 1

    return count


def d4p2(data):
    assignments = get_assignments(data)

    count = 0
    for assignment in assignments:
        if len(assignment[0].union(assignment[1])) != len(assignment[0]) + len(assignment[1]):
            count += 1

    return count


assert d4p1(utils.read(4, True)) == 2
assert d4p2(utils.read(4, True)) == 4
print(d4p1(utils.read(4)))
print(d4p2(utils.read(4)))