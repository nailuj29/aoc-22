import functools
import utils

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left > right:
            return False
        elif right > left:
            return True
        else:
            return None

    if type(left) == list and type(right) == int:
        return compare(left, [right])

    if type(left) == int and type(right) == list:
        return compare([left], right)

    if type(left) == list and type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            if compare(left[i], right[i]) != None:
                return compare(left[i], right[i])
            i += 1

        if len(left) > len(right):
            return False
        elif len(right) > len(left):
            return True

        return None

def day13p1(data):
    indices = []
    for i, comparison in enumerate(data.split('\n\n')):
        parts = comparison.split('\n')
        left = eval(parts[0])
        right = eval(parts[1])
        if compare(left, right):
            indices.append(i + 1)

    return sum(indices)

def day13p2(data):
    comparisons = data.split('\n\n')
    lists = ('\n'.join(comparisons)).split('\n')
    lists.append('[[6]]')
    lists.append('[[2]]')
    lists = [eval(list) for list in lists]
    lists.sort(key=functools.cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
    lists = [str(list) for list in lists]
    indices = []
    indices.append(lists.index('[[6]]') + 1)
    indices.append(lists.index('[[2]]') + 1)
    return indices[0] * indices[1]

assert day13p1(utils.read(13, True)) == 13
assert day13p2(utils.read(13, True)) == 140
print(day13p1(utils.read(13)))
print(day13p2(utils.read(13)))