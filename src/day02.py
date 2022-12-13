import utils
outcomes = {
    'X': ['B', 'A', 'C'],
    'Y': ['C', 'B', 'A'],
    'Z': ['A', 'C', 'B'],
    'A': ['Y', 'X', 'Z'],
    'B': ['Z', 'Y', 'X'],
    'C': ['X', 'Z', 'Y']
}
    
scores = ['X', 'Y', 'Z']

def day2p1(data):
    matches = data.split('\n')
    score = 0
    for matchup in matches:
        elf = matchup.split(" ")[0]
        me = matchup.split(" ")[1]
        score += scores.index(me) + 1
        score += outcomes[me].index(elf) * 3
        
    return score

def day2p2(data):
    matches = data.split('\n')
    score = 0
    for matchup in matches:
        elf = matchup.split(" ")[0]
        outcome = matchup.split(" ")[1]
        score += scores.index(outcome) * 3
        needToPick = outcomes[elf][2 - scores.index(outcome)]
        score += scores.index(needToPick) + 1
    return score
    
assert day2p1(utils.read(2, True)) == 15
assert day2p2(utils.read(2, True)) == 12
print(day2p1(utils.read(2)))
print(day2p2(utils.read(2)))