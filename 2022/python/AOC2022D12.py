from aocd import get_data
import os

year = '2022'
day = '12'

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

map_position = []
row_index = 0
entry_position = (0,0)
current_position = (0,0)
exit_position = (0,0)

path = []
for map_line in puzzle_input:
    map_row = []
    column_index = 0

    for p in map_line:
        if p == 'S':
            entry_position = (row_index, column_index)
            map_row += ['a']
            current_position = (row_index, column_index)
            path += []
        elif p == 'E':
            exit_position = (row_index, column_index)
            map_row += ['z']
        else:
            map_row += [p]
        column_index += 1
    
    map_position += [map_row]
    row_index += 1

    print(map_row, entry_position, exit_position)
if map_position[entry_position[0] + 1][entry_position[1]] - map_position[entry_position[0]][entry_position[1]] == 1:
    path += [()]
# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))