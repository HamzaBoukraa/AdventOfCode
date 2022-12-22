year = '2020'
day = '10'
suffix = ''
# suffix = '_1'
# suffix = '_2'

with open('..\..\Input\day{1}\AOC{0}D{1}_input{2}.txt'.format(year, day, suffix), 'r') as reader:
    puzzle_input = [int(input_line) for input_line in reader.read().split('\n')]

puzzle_input += [0]
puzzle_input += [max(puzzle_input) + 3]
puzzle_input = sorted(puzzle_input)

jolt_differences = [puzzle_input[index] - puzzle_input[index - 1] for index in range(1, len(puzzle_input))]

# Part 1 :
print('Part 1 answer :', len([jolt for jolt in jolt_differences if jolt == 1]) * len([jolt for jolt in jolt_differences if jolt == 3]))

# Part 2 :
i = 0
multipliers = 1
while i < len(puzzle_input):
    if puzzle_input[i] + 1 in puzzle_input and puzzle_input[i] + 2 in puzzle_input and puzzle_input[i] + 3 in puzzle_input and puzzle_input[i] + 4 in puzzle_input:
        multipliers *= 7
        i += 3
    if puzzle_input[i] + 1 in puzzle_input and puzzle_input[i] + 2 in puzzle_input and puzzle_input[i] + 3 in puzzle_input:
        multipliers *= 4
        i += 2
    elif puzzle_input[i] + 1 in puzzle_input and puzzle_input[i] + 2 in puzzle_input:
        multipliers *= 2
        i += 1
    i += 1

print('Part 2 answer :', multipliers)
