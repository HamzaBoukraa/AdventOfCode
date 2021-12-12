from aocd import get_data
import os

year = '2021'
day = '09'

input_directory_folder_path = '..\..\Input\day{0}'.format(day)
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

# Part 1 :
print('Part 1 answer :', puzzle_input)

# Part 2 :
print('Part 2 answer :', puzzle_input)
