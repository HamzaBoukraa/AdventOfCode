from aocd import get_data
import os

puzzule_date = __file__.split('\\')[-1].split('.')[0].split('D')
year = puzzule_date[0][3:]
day = puzzule_date[1]

input_directory_folder_path = '..\\input'
input_file_path = '{0}\\AOC{1}D{2}_input.txt'.format(input_directory_folder_path,year, day)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year),day=int(day))
    
    with open(input_file_path, 'w') as writer:
        writer.write(data)

# Get Puzzle Input
with open(input_file_path, 'r') as reader:
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')]
char_swap = {'F': '\u250c', 'J': '\u2518',
                     '7': '\u2510', 'L': '\u2514',
                     '-': '\u2500', '|': '\u2502',
                     'S': 'x',      '@': 'o'}
import copy

map = []
for row_index in range(len(puzzle_input)):
    for column_index in range(len(puzzle_input[row_index])):
        map += [[[row_index, column_index], puzzle_input[row_index][column_index], [0, 0, 0, 0], -1]]
        if map[-1][1] == 'L':
            map[-1][2][0] = map[-1][2][1] = 1
        elif map[-1][1] == 'J':
            map[-1][2][0] = map[-1][2][3] = 1
        elif map[-1][1] == 'F':
            map[-1][2][1] = map[-1][2][2] = 1
        elif map[-1][1] == '7':
            map[-1][2][2] = map[-1][2][3] = 1
        elif map[-1][1] == '-':
            map[-1][2][1] = map[-1][2][3] = 1
        elif map[-1][1] == '|':
            map[-1][2][0] = map[-1][2][2] = 1
        elif map[-1][1] == 'S':
            map[-1][3] = 0

def part_1():
    current_step = 0
    start_node = [m for m in map if m[3] == 0]
    current_nodes = start_node
    current_step += 1
    while len(current_nodes) > 0:
        nodes = copy.deepcopy(current_nodes)
        current_nodes = []
        for node in nodes:
            if node[2][0] == 1 or node[3] == 0:
                north_node = [m for m in map if m[0][0] == node[0][0] - 1 and m[0][1] == node[0][1] and m[2][2] == 1 and node[3] == current_step - 1 and m[3] == -1]
                if len(north_node) > 0:
                    north_node[0][3] = current_step
                    current_nodes += [north_node[0]]
            if node[2][2] == 1 or node[3] == 0:
                south_node = [m for m in map if m[0][0] == node[0][0] + 1 and m[0][1] == node[0][1] and m[2][0] == 1 and node[3] == current_step - 1 and m[3] == -1]
                if len(south_node) > 0:
                    south_node[0][3] = current_step
                    current_nodes += [south_node[0]]
            if node[2][1] == 1 or node[3] == 0:
                east_node = [m for m in map if m[0][0] == node[0][0] and m[0][1] == node[0][1] + 1 and m[2][3] == 1 and node[3] == current_step - 1 and m[3] == -1]
                if len(east_node) > 0:
                    east_node[0][3] = current_step
                    current_nodes += [east_node[0]]
            if node[2][3] == 1 or node[3] == 0:
                west_node = [m for m in map if m[0][0] == node[0][0] and m[0][1] == node[0][1] - 1 and m[2][1] == 1 and node[3] == current_step - 1 and m[3] == -1]
                if len(west_node) > 0:
                    west_node[0][3] = current_step
                    current_nodes += [west_node[0]]
            
        current_step += 1

    return max([m[3] for m in map])


def part_2():
    return 0

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
