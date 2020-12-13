year = '2020'
day = '01'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [int(entry) for entry in reader.read().split('\n')]

# Part 1 :
print('Part 1 answer :', [puzzle_input[a] * puzzle_input[b] for a in range(200) for b in range(200) if b > a and puzzle_input[a] + puzzle_input[b] == 2020][0])

# Part 2 :
print('Part 2 answer :', [puzzle_input[a] * puzzle_input[b] * puzzle_input[c] for a in range(200) for b in range(200) for c in range(200) if c > b and b > a and puzzle_input[a] + puzzle_input[b] + puzzle_input[c] == 2020][0])
