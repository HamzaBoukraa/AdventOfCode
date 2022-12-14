from aocd import get_data
import os

year = '2022'
day = '14'

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

def print_radar():
    for r in range(len(radar)):
        print(r, ''.join(radar[r]))

# Part 1 :
rocks = sorted(list(set([j for i in [[(int(rock_position.split(',')[1]), int(rock_position.split(',')[0])) for rock_position in rock_line.split(' -> ')] for rock_line in puzzle_input] for j in i])))
max_depth = max([rp[0] for rp in rocks]) + 1
max_position = max([rp[1] for rp in rocks]) + 1
radar = [['.' for position in range(max_position + 1)] for depth in range(max_depth + 1)]

radar[0][500] = '+'
for rock in rocks:
    radar[rock[0]][rock[1]] = '#'

print_radar()


print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))