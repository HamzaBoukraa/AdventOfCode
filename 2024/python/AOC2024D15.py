from aocd import get_data
import os
import copy

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

initial_map = []
break_found = False
p_index = 0
while not break_found:
    p = puzzle_input[p_index]
    if "#" in p:
        initial_map += [[i for i in p]]
    else:
        break_found = True
    p_index += 1

instructions = ""
while p_index < len(puzzle_input):
    i = puzzle_input[p_index]
    instructions += i
    p_index += 1


def is_box_move_possible_1(map_blocks, coordinates, direction_vertical, direction_horizontal):
    if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
        return True
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
        return False
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "O":
        return is_box_move_possible_1(map_blocks, [coordinates[0] + direction_vertical,coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
    return False

def move_box_1(map_blocks, coordinates, direction_vertical, direction_horizontal):
    if is_box_move_possible_1(map_blocks, coordinates, direction_vertical, direction_horizontal):
        if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
            map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] = \
            map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]]
            coordinates[0] += direction_vertical
            coordinates[1] += direction_horizontal
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
            pass
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "O":
            move_box_1(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
    return map_blocks, coordinates

def is_robot_move_possible_1(map_blocks, coordinates, direction_vertical, direction_horizontal):
    if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
        return True
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
        return False
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "O":
        return is_box_move_possible_1(map_blocks, [coordinates[0] + direction_vertical,coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
    return False

def move_robot_1(map_blocks, coordinates, direction = "", direction_horizontal = 0, direction_vertical = 0):
    if direction == "":
        pass
    else:
        if direction == "^":
            direction_vertical = -1
        elif direction == "v":
            direction_vertical = 1
        elif direction == ">":
            direction_horizontal = 1
        elif direction == "<":
            direction_horizontal = -1

    if is_robot_move_possible_1(map_blocks, coordinates, direction_vertical, direction_horizontal):
        if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
            map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] = \
            map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]]
            coordinates[0] += direction_vertical
            coordinates[1] += direction_horizontal
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
            pass
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "O":
            move_box_1(map_blocks, coordinates, direction_vertical, direction_horizontal)
            map_blocks, coordinates = move_robot_1(map_blocks, coordinates, direction_vertical=direction_vertical, direction_horizontal=direction_horizontal)
    return map_blocks, coordinates

def move_1(map_blocks, robot_coordinates, direction):
    map_blocks, robot_coordinates = move_robot_1(map_blocks, robot_coordinates, direction)
    return map_blocks, robot_coordinates

def part_1():
    map_blocks = copy.deepcopy(initial_map)
    robot_coordinates = [0,0]
    row_index = 0
    while row_index < len(map_blocks) and robot_coordinates == [0,0]:
        column_index = 0
        while column_index < len(map_blocks[row_index]) and robot_coordinates == [0,0]:
            if map_blocks[row_index][column_index] == "@":
                robot_coordinates = [row_index, column_index]
            column_index += 1
        row_index += 1
    
    for move in instructions:
        map_blocks, robot_coordinates = move_1(map_blocks, robot_coordinates, move)

    for m in map_blocks:
        print(''.join(m))
    
    GPS = 0
    row_index = 0
    while row_index < len(map_blocks):
        column_index = 0
        while column_index < len(map_blocks[row_index]):
            if map_blocks[row_index][column_index] == "O":
                GPS += (100 * row_index) + column_index
            column_index += 1
        row_index += 1    
    
    return GPS



def is_box_move_possible_2(map_blocks, coordinates, direction_vertical, direction_horizontal):
    if direction_vertical == 0:
        if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2] == ".":
            return True
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2] == "#":
            return False
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2] in ["[", "]"]:
            return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical,coordinates[1] + direction_horizontal * 2], direction_vertical, direction_horizontal)
    elif direction_horizontal == 0:
        if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
            and ((map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == ".") \
                 or (map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == ".")):
            return True
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
            return False
        elif map_blocks[coordinates[0]][coordinates[1] + direction_horizontal] == "]" and map_blocks[coordinates[0]][coordinates[1] + direction_horizontal - 1] == "[" and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "#":
            return False
        elif map_blocks[coordinates[0]][coordinates[1] + direction_horizontal] == "[" and map_blocks[coordinates[0]][coordinates[1] + direction_horizontal + 1] == "]" and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "#":
            return False
        elif map_blocks[coordinates[0]][coordinates[1] + direction_horizontal - 1] == "[" and map_blocks[coordinates[0]][coordinates[1] + direction_horizontal] == "]":
                if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "[" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]":
                    return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal)
                elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "]" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
                    return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 2], direction_vertical, direction_horizontal)
                elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "." \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[":
                    return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "]" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[":
                    return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 2], direction_vertical, direction_horizontal) \
                        and is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
        elif map_blocks[coordinates[0]][coordinates[1] + direction_horizontal] == "[" and map_blocks[coordinates[0]][coordinates[1] + direction_horizontal + 1] == "]":
            if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "]":
                return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "[":
                return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal + 1], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == ".":
                return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "[":
                return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal) \
                    and is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal + 1], direction_vertical, direction_horizontal)

    return False

def move_box_2(map_blocks, coordinates, direction_vertical, direction_horizontal):
    box_move_possible_2 = is_box_move_possible_2(map_blocks, coordinates, direction_vertical, direction_horizontal)
    if box_move_possible_2:
        if direction_vertical == 0:
            if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2] == ".":
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] = \
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2]
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]] = \
                map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal]
                coordinates[0] += direction_vertical
                coordinates[1] += direction_horizontal * 2
            elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2] == "#":
                pass
            elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal * 2]  in ["[", "]"]:
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal * 2], direction_vertical, direction_horizontal)
        elif direction_horizontal == 0:
            if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
                pass
            elif map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == ".":
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]] = \
                map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal]
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1], map_blocks[coordinates[0]][coordinates[1] - 1] = \
                map_blocks[coordinates[0]][coordinates[1] - 1], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1]
                coordinates[0] += direction_vertical
                coordinates[1] += direction_horizontal
            elif map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == ".":
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]] = \
                map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal]
                map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1], map_blocks[coordinates[0]][coordinates[1] + 1] = \
                map_blocks[coordinates[0]][coordinates[1] + 1], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1]
                coordinates[0] += direction_vertical
                coordinates[1] += direction_horizontal
            elif map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "[":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "]":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "]":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 2], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == ".":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "]" and map_blocks[coordinates[0]][coordinates[1] - 1] == "[" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "[" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal - 1] == "]":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 2], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "." \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "[":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal + 1], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == ".":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)
            elif map_blocks[coordinates[0]][coordinates[1]] == "[" and map_blocks[coordinates[0]][coordinates[1] + 1] == "]" \
                and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "]" \
                    and map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal + 1] == "[":
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal + 1], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal - 1], direction_vertical, direction_horizontal)
                move_box_2(map_blocks, [coordinates[0], coordinates[1]], direction_vertical, direction_horizontal)

            else:
                pass
            
    return map_blocks, coordinates

def is_robot_move_possible_2(map_blocks, coordinates, direction_vertical, direction_horizontal):
    if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
        return True
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
        return False
    elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] in ["[", "]"]:
        return is_box_move_possible_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
    return False

def move_robot_2(map_blocks, coordinates, direction = "", direction_horizontal = 0, direction_vertical = 0):
    if direction == "":
        pass
    else:
        if direction == "^":
            direction_vertical = -1
        elif direction == "v":
            direction_vertical = 1
        elif direction == ">":
            direction_horizontal = 1
        elif direction == "<":
            direction_horizontal = -1
    robot_move_possible_2 = is_robot_move_possible_2(map_blocks, coordinates, direction_vertical, direction_horizontal)
    if robot_move_possible_2:
        if map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == ".":
            map_blocks[coordinates[0]][coordinates[1]], map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] = \
            map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal], map_blocks[coordinates[0]][coordinates[1]]
            coordinates[0] += direction_vertical
            coordinates[1] += direction_horizontal
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] == "#":
            pass
        elif map_blocks[coordinates[0] + direction_vertical][coordinates[1] + direction_horizontal] in ["[", "]"]:
            if direction_vertical == 0:
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                map_blocks, coordinates = move_robot_2(map_blocks, coordinates, direction_vertical=direction_vertical, direction_horizontal=direction_horizontal)
            elif direction_horizontal == 0:
                move_box_2(map_blocks, [coordinates[0] + direction_vertical, coordinates[1] + direction_horizontal], direction_vertical, direction_horizontal)
                map_blocks, coordinates = move_robot_2(map_blocks, coordinates, direction_vertical=direction_vertical, direction_horizontal=direction_horizontal)

    return map_blocks, coordinates

def move_2(map_blocks, robot_coordinates, direction):
    map_blocks, robot_coordinates = move_robot_2(map_blocks, robot_coordinates, direction)
    return map_blocks, robot_coordinates

def part_2():
    the_new_map = []
    for row in initial_map:
        new_row = []
        for block in row:
            if block == "O":
                new_row += ["[", "]"]
            elif block == "@":
                new_row += ["@", "."]
            elif block == ".":
                new_row += [".", "."]
            elif block == "#":
                new_row += ["#", "#"]
        the_new_map += [new_row]

    robot_coordinates = [0,0]
    row_index = 0
    while row_index < len(the_new_map) and robot_coordinates == [0,0]:
        column_index = 0
        while column_index < len(the_new_map[row_index]) and robot_coordinates == [0,0]:
            if the_new_map[row_index][column_index] == "@":
                robot_coordinates = [row_index, column_index]
            column_index += 1
        row_index += 1

    for move in instructions:
        the_new_map, robot_coordinates = move_2(the_new_map, robot_coordinates, move)
    
    GPS = 0
    row_index = 0
    while row_index < len(the_new_map):
        column_index = 0
        while column_index < len(the_new_map[row_index]):
            if the_new_map[row_index][column_index] == "[":
                GPS += (100 * row_index) + column_index
            column_index += 1
        row_index += 1    
    
    return GPS


if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
