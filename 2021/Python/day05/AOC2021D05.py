from aocd import get_data
import os

year = '2021'
day = '05'

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

vent_lines_coordinate_raw = [
    [int(line.split(' -> ')[0].split(',')[0]),
    int(line.split(' -> ')[0].split(',')[1]),
    int(line.split(' -> ')[1].split(',')[0]),
    int(line.split(' -> ')[1].split(',')[1])] for line in puzzle_input]

vent_lines_coordinate = []

for l in range(len(vent_lines_coordinate_raw)):
    s = vent_lines_coordinate_raw[l]
    if s[0] == s[2]:
        if s[1] < s[3]:
            start = s[1]
            end = s[3]+1
        if s[1] > s[3]:
            start = s[3]
            end = s[1]+1
        for y in range(start,end):
            vent_lines_coordinate += [["V",s[0],y]]
    if s[1] == s[3]:
        if s[0] < s[2]:
            start = s[0]
            end = s[2]+1
        if s[0] > s[2]:
            start = s[2]
            end = s[0]+1
        for x in range(start,end):
            vent_lines_coordinate += [["H",x,s[1]]]
    if s[0] < s[2] and s[1] < s[3]:
        start = s[0]
        end = s[2]+1
        for x in range(end - start):
            vent_lines_coordinate += [["D1",s[0] + x,s[1] + x]]
    if s[0] > s[2] and s[1] > s[3]:
        start = s[2]
        end = s[0]+1
        for x in range(end - start):
            vent_lines_coordinate += [["D1",s[2] + x,s[3] + x]]
    if s[0] < s[2] and s[1] > s[3]:
        start = s[0]
        end = s[2]+1
        for x in range(end - start):
            vent_lines_coordinate += [["D2",s[0] + x,s[1] - x]]
    if s[0] > s[2] and s[1] < s[3]:
        start = s[2]
        end = s[0]+1
        for x in range(end - start):
            vent_lines_coordinate += [["D2",s[0] - x,s[1] + x]]

_puzzle_map = [[]]

def _map_size()->int:
    return max([vent_lines_coordinate_raw[i][j] for i in range(len(vent_lines_coordinate_raw)) for j in range(4)]) + 1

map_size = _map_size()

# Prepare the map
def _init_map():
    return [['.' for r in range(map_size)] for c in range(map_size)]

def _print_map():
    for m in range(map_size):
        row = ""
        for n in range(map_size):
            position = _puzzle_map[n][m]
            row += position
        print(row)

_puzzle_map = _init_map()

def process_map(all)->int:
    for l in vent_lines_coordinate:
        if all == False and (l[0]=="V" or l[0]=="H"):
            if _puzzle_map[l[1]][l[2]] == '.':
                _puzzle_map[l[1]][l[2]] = '1'
            else:
                _puzzle_map[l[1]][l[2]] = str(int(_puzzle_map[l[1]][l[2]])+1)

        elif all == True and (l[0]=="D1" or l[0]=="D2"):
            if _puzzle_map[l[1]][l[2]] == '.':
                _puzzle_map[l[1]][l[2]] = '1'
            else:
                _puzzle_map[l[1]][l[2]] = str(int(_puzzle_map[l[1]][l[2]])+1)

    danger = 0
    for m in range(map_size):
        for n in range(map_size):
            position = _puzzle_map[n][m]
            if position != '.' and int(position) > 1:
                danger += 1    
    return danger

# Part 1 :
print('Part 1 answer :', process_map(all=False))

# Part 2 :
print('Part 2 answer :', process_map(all=True))
