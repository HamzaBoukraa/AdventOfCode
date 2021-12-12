from aocd import get_data
import os

year = '2021'
day = '01'

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
    puzzle_input =  [int(puzzle_line) for puzzle_line in reader.read().split('\n')]

# Part 1 :
print('Part 1 answer :', len([puzzle_input[b] for a in range(len(puzzle_input)) for b in range(len(puzzle_input)) if b == a + 1 and puzzle_input[a] < puzzle_input[b]]))

# Part 2 :
print('Part 2 answer :',len([puzzle_input[a] for a in range(len(puzzle_input)-3) if puzzle_input[a]+puzzle_input[a+1]+puzzle_input[a+2]<puzzle_input[a+1]+puzzle_input[a+2]+puzzle_input[a+3]]))
