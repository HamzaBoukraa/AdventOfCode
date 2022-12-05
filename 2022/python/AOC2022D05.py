from aocd import get_data
import os, copy

year = '2022'
day = '05'

input_directory_folder_path = '..\input'
input_file_path = '{0}\AOC{1}D{2}_input.txt'.format(input_directory_folder_path,year, day)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year),day=int(day))
    
    with open(input_file_path, 'w') as writer:
        writer.write(data)

# Get Puzzle Input
with open(input_file_path, 'r') as reader:
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')]


stacks = [[puzzle_input[j][i + (3 * (i -1))] for j in range(7, -1, -1) if puzzle_input[j][i + (3 * (i -1))] != ' '] for i in range(1, 10)]
instructions = [[int(t[1]), int(t[3]) - 1, int(t[5]) - 1] for t in [[i for i in s.split(' ')] for s in puzzle_input[10:]]]

# Part 1 :
stacks1 = copy.deepcopy(stacks)
for instruction in instructions:
    stacks1[instruction[2]] += reversed(stacks1[instruction[1]][(-1 * instruction[0]):])
    stacks1[instruction[1]] = stacks1[instruction[1]][:(-1 * instruction[0])]

print('Part 1 answer :', ''.join([s[-1] for s in stacks1]))

# Part 2 :
stacks2 = copy.deepcopy(stacks)
for instruction in instructions:
    stacks2[instruction[2]] += stacks2[instruction[1]][(-1 * instruction[0]):]
    stacks2[instruction[1]] = stacks2[instruction[1]][:(-1 * instruction[0])]

print('Part 2 answer :', ''.join([s[-1] for s in stacks2]))
