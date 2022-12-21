from aocd import get_data
import os, copy

year = '2022'
day = '20'

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
    puzzle_input =  [[int(puzzle_line),False] for puzzle_line in reader.read().split('\n')]


# Part 1 :
original_stacks = copy.deepcopy(puzzle_input)
for origin in original_stacks:
    item_index = [i for i in range(len(puzzle_input)) if puzzle_input[i][0] == origin[0] and puzzle_input[i][1] == False][0]
    moves = abs(puzzle_input[item_index][0])
    if moves > 0:
        direction = puzzle_input[item_index][0] / moves
        while moves > 0:
            if direction > 0:
                if item_index == len(puzzle_input) - 1:
                    puzzle_input = [puzzle_input[-1]] + puzzle_input[:-1]
                    item_index = 0
                aux_item = puzzle_input[item_index]
                puzzle_input[item_index] = puzzle_input[item_index + 1]
                puzzle_input[item_index + 1] = aux_item
                item_index += 1
            else:
                if item_index == 0:
                    puzzle_input = puzzle_input[1:] + [puzzle_input[0]]
                    item_index = len(puzzle_input) - 1
                aux_item = puzzle_input[item_index]
                puzzle_input[item_index] = puzzle_input[item_index - 1]
                puzzle_input[item_index - 1] = aux_item 
                item_index -= 1
            moves -= 1
    puzzle_input[item_index][1] = True

grove_coordinates = 0
zero_item_index = [i for i in range(len(puzzle_input)) if puzzle_input[i][0] == 0][0]
hl = ((10000//len(puzzle_input)) * puzzle_input)
for i in range(zero_item_index, zero_item_index + 3001):
    if ((i - zero_item_index) % 1000) == 0:
        grove_coordinates +=  hl[i][0]

print('{0}{1} - Part 1 answer : {2}'.format(year, day, grove_coordinates))

# Part 2 :
puzzle_input = copy.deepcopy(original_stacks)
for i in range(len(puzzle_input)):
    puzzle_input[i][0] *= 811589153
original_stacks = copy.deepcopy(puzzle_input)

for t in range(10):
    for i in range(len(puzzle_input)):
        puzzle_input[i][1] = False
    for origin in original_stacks:
        item_index = [i for i in range(len(puzzle_input)) if puzzle_input[i][0] == origin[0] and puzzle_input[i][1] == False][0]
        moves = abs(puzzle_input[item_index][0]) % (len(puzzle_input) - 1)
        if moves > 0:
            direction = puzzle_input[item_index][0] / moves
            while moves > 0:
                if direction > 0:
                    if item_index == len(puzzle_input) - 1:
                        puzzle_input = [puzzle_input[-1]] + puzzle_input[:-1]
                        item_index = 0
                    aux_item = puzzle_input[item_index]
                    puzzle_input[item_index] = puzzle_input[item_index + 1]
                    puzzle_input[item_index + 1] = aux_item
                    item_index += 1
                else:
                    if item_index == 0:
                        puzzle_input = puzzle_input[1:] + [puzzle_input[0]]
                        item_index = len(puzzle_input) - 1
                    aux_item = puzzle_input[item_index]
                    puzzle_input[item_index] = puzzle_input[item_index - 1]
                    puzzle_input[item_index - 1] = aux_item 
                    item_index -= 1
                moves -= 1
        puzzle_input[item_index][1] = True

grove_coordinates = 0
zero_item_index = [i for i in range(len(puzzle_input)) if puzzle_input[i][0] == 0][0]
hl = ((10000//len(puzzle_input)) * puzzle_input)
for i in range(zero_item_index, zero_item_index + 3001):
    if ((i - zero_item_index) % 1000) == 0:
        grove_coordinates +=  hl[i][0]

print('{0}{1} - Part 2 answer : {2}'.format(year, day, grove_coordinates))