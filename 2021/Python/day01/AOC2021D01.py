year = '2021'
day = '01'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [int(entry) for entry in reader.read().split('\n')]

# Part 1 :
print('Part 1 answer :', len([puzzle_input[b] for a in range(len(puzzle_input)) for b in range(len(puzzle_input)) if b == a + 1 and puzzle_input[a] < puzzle_input[b]]))

# Part 2 :
print('Part 2 answer :',len([puzzle_input[a] for a in range(len(puzzle_input)-3) if puzzle_input[a]+puzzle_input[a+1]+puzzle_input[a+2]<puzzle_input[a+1]+puzzle_input[a+2]+puzzle_input[a+3]]))
