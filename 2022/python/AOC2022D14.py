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

def move_sand(moved_sand_position):
    if radar[moved_sand_position[0] + 1][moved_sand_position[1]] == '.':
        return (moved_sand_position[0] + 1, moved_sand_position[1])
    elif radar[moved_sand_position[0] + 1][moved_sand_position[1] - 1] == '.':
        return (moved_sand_position[0] + 1, moved_sand_position[1] - 1)
    elif radar[moved_sand_position[0] + 1][moved_sand_position[1] + 1] == '.':
        return (moved_sand_position[0] + 1, moved_sand_position[1] + 1)
    else:
        return moved_sand_position

def get_rocks(start_rock, end_rock):
    rocks_line = [start_rock]
    next_rock = (start_rock[0], start_rock[1])
    if start_rock[0] == end_rock[0]:
        if start_rock[1] > end_rock[1]:
            while next_rock[1] > end_rock[1]:
                next_rock = (next_rock[0], next_rock[1] - 1)
                rocks_line += [next_rock]
        elif start_rock[1] < end_rock[1]:
            while next_rock[1] < end_rock[1]:
                next_rock = (next_rock[0], next_rock[1] + 1)
                rocks_line += [next_rock]
    if start_rock[1] == end_rock[1]:
        if start_rock[0] > end_rock[0]:
            while next_rock[0] > end_rock[0]:
                next_rock = (next_rock[0] - 1, next_rock[1])
                rocks_line += [next_rock]
        elif start_rock[0] < end_rock[0]:
            while next_rock[0] < end_rock[0]:
                next_rock = (next_rock[0] + 1, next_rock[1])
                rocks_line += [next_rock]
    return rocks_line

# Part 1 :
rocks = []
for input_line in puzzle_input:
    stones = input_line.split(' -> ')
    for stone in range(1, len(stones)):
        s_stone = (int(stones[stone - 1].split(',')[1]), int(stones[stone - 1].split(',')[0]))
        e_stone = (int(stones[stone].split(',')[1]), int(stones[stone].split(',')[0]))
        rocks += get_rocks(s_stone, e_stone)
rocks = sorted(list(set(rocks)))
max_depth = max([rp[0] for rp in rocks]) + 1
max_position = max([rp[1] for rp in rocks]) + 1

radar = [['.' for position in range(max_position + 10)] for depth in range(max_depth + 1)]
radar[0][500] = '+'
for rock in rocks:
    radar[rock[0]][rock[1]] = '#'

sands = []
try:
    sand_position = (0, 500)
    while sand_position[0] < max_depth:
        sand_position = (0, 500)
        sand_moved = True
        while sand_moved:
            moved_sand_position = move_sand(sand_position)
            if moved_sand_position != sand_position:
                sand_position = moved_sand_position
            else:
                sand_moved = False
                sands += [sand_position]
                radar[sand_position[0]][sand_position[1]] = 'o'
except:
    pass

print('{0}{1} - Part 1 answer : {2}'.format(year, day, len(sands)))

# Part 2 :
radar = [['.' for position in range(max_position + 1000)] for depth in range(max_depth + 1)]
radar += [['#' for position in range(max_position + 1000)]]

radar[0][500] = '+'
for rock in rocks:
    radar[rock[0]][rock[1]] = '#'

sands = []

sand_position = (0, 500)
while radar[0][500] == '+':
    sand_position = (0, 500)
    sand_moved = True
    while sand_moved:
        moved_sand_position = move_sand(sand_position)
        if moved_sand_position != sand_position:
            sand_position = moved_sand_position
        else:
            sand_moved = False
            sands += [sand_position]
            radar[sand_position[0]][sand_position[1]] = 'o'
print('{0}{1} - Part 2 answer : {2}'.format(year, day, len(sands)))