from aocd import get_data
import os, time

year = '2022'
day = '22'

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

path = []
path_raw = puzzle_input[-1]
temp = ''
for c in path_raw:
    if c != 'R' and c != 'L':
        temp += c
    else:
        path += [int(temp)]
        path += [c]
        temp = ''

map_tiles = []
map_tiles_lines = puzzle_input[:-2]
map_tiles_width = max([len(s) for s in map_tiles_lines])
position = (0, 0)
for map_tile_row_index in range(len(map_tiles_lines)):
    map_tile = []
    for map_tile_column_index in range(map_tiles_width):
        if map_tile_column_index < len(map_tiles_lines[map_tile_row_index]):
            map_tile += [map_tiles_lines[map_tile_row_index][map_tile_column_index]]
        else:
            map_tile += [' ']
        if position == (0, 0) and map_tile[-1] != ' ':
            position = (map_tile_row_index, map_tile_column_index)
    map_tiles += [map_tile]

facing = 0
for m in path:
    print(m, position, facing)
    time.sleep(5)

    if m == 'R':
        facing += 1
        if facing == 4:
            facing = 0
    elif m == 'L':
        facing -= 1
        if facing == -1:
            facing = 3
    else:
        blocked = False
        while m > 0 and not blocked:
            if facing == 0:
                if map_tiles[position[0]][position[1] + 1] == '#':
                    blocked = True
                elif map_tiles[position[0]][position[1] + 1] == '.':
                    m -= 1
                    position = (position[0], position[1] + 1)
            elif facing == 1:
                if map_tiles[position[0] + 1][position[1]] == '#':
                    blocked = True
                elif map_tiles[position[0] + 1][position[1]] == '.':
                    m -= 1
                    position = (position[0] + 1, position[1])
            elif facing == 2:
                if position[1] == 0:
                    position = (position[0], map_tiles_width - 1)
                    while map_tiles[position[0]][position[1]] == ' ':
                        position = (position[0], position[1] - 1)
                    if map_tiles[position[0]][position[1]] == '#':
                        blocked = True
                        position = (position[0], 0)
                    else:
                        position = (position[0], position[1] + 1)
                if map_tiles[position[0]][position[1] - 1] == '#':
                    blocked = True
                elif map_tiles[position[0]][position[1] - 1] == '.':
                    m -= 1
                    position = (position[0], position[1] - 1)
            elif facing == 3:
                if position[0] == 0:
                    position = (len(map_tiles_lines) - 1, position[1])
                    while map_tiles[position[0]][position[1]] == ' ':
                        position = (position[0] - 1, position[1])
                    if map_tiles[position[0]][position[1]] == '#':
                        blocked = True
                        position = (0, position[1])
                    else:
                        position = (position[0] + 1, position[1])
                if map_tiles[position[0] - 1][position[1]] == '#':
                    blocked = True
                elif map_tiles[position[0] - 1][position[1]] == '.':
                    m -= 1
                    position = (position[0] - 1, position[1])
            print(m, position, facing)
            time.sleep(1)

# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))