from aocd import get_data
import os

year = '2022'
day = '04'

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
    puzzle_input =  [[[int(p) for p in a.split('-')] for a in puzzle_line.split(',')] for puzzle_line in reader.read().split('\n')]

# Part 1 :
print('Part 1 answer :', len([p for p in puzzle_input if (p[0][0] <= p[1][0] and p[0][1] >= p[1][1]) or (p[0][0] >= p[1][0] and p[0][1] <= p[1][1])]))

# Part 2 :
print('Part 2 answer :', len([p for p in puzzle_input if (p[0][0] >= p[1][0] and p[0][0] <= p[1][1]) or (p[0][1] <= p[1][1] and p[0][1] >= p[1][0]) or (p[1][0] >= p[0][0] and p[1][0] <= p[0][1]) or (p[1][1] <= p[0][1] and p[1][1] >= p[0][0])]))
