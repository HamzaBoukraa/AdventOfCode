from aocd import get_data
import os

year = '2021'
day = '02'

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
print('Part 1 answer :', sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "forward"])*(sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "down"])-sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "up"])))

# Part 2 :
depth = 0
horizontal_position = 0
aim = 0
for input in puzzle_input:
    instruction = input.split(" ")[0]
    command = int(input.split(" ")[1])
    if instruction == "forward":
        horizontal_position += command
        depth += aim * command
    elif instruction == "down":
        aim += command
    elif instruction == "up":
        aim -= command
print('Part 2 answer :', horizontal_position * depth)