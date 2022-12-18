from aocd import get_data
import os

year = '2022'
day = '15'

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

def add_to_map(coordinates, map_position):
    if len([m for m in map_position if m[0] == coordinates[0]]) == 0:
        map_position += [[coordinates[0],[(coordinates[1], coordinates[1])]]]
        m_pos = [m for m in range(len(map_position)) if (map_position[m][0] == coordinates[0])][0]
    else:
        m_pos = [m for m in range(len(map_position)) if (map_position[m][0] == coordinates[0])][0]
        if len([s for m in range(len(map_position)) for s in map_position[m][1] if (map_position[m][0] == coordinates[0]) and (coordinates[1] <= s[1]) and (s[0] <= coordinates[1])]) > 0:
            pass
        else:
            pos1 = [(m, s) for m in range(len(map_position)) for s in range(len(map_position[m][1])) if (map_position[m][0] == coordinates[0]) and (coordinates[1] == (map_position[m][1][s][1] + 1))]
            if len(pos1) > 0:
                map_position[pos1[0][0]][1][pos1[0][1]] = (map_position[pos1[0][0]][1][pos1[0][1]][0], coordinates[1])
            else:
                pos1 = [(m, s) for m in range(len(map_position)) for s in range(len(map_position[m][1])) if (map_position[m][0] == coordinates[0]) and (coordinates[1] == (map_position[m][1][s][0] - 1))]
                if len(pos1) > 0:
                    map_position[pos1[0][0]][1][pos1[0][1]] = (coordinates[1],map_position[pos1[0][0]][1][pos1[0][1]][1])
                else:
                    map_position[m_pos][1] += [(coordinates[1], coordinates[1])]
    map_position[m_pos][1] = sorted(map_position[m_pos][1])
    positions = []
    m = 0
    while m < len(map_position[m_pos][1]):
        if m == 0:
            positions += [map_position[m_pos][1][m]]
        else:
            if (positions[-1][1] >= map_position[m_pos][1][m][0] - 1):
                positions[-1] = (positions[-1][0], map_position[m_pos][1][m][1])
            else:
                positions += [map_position[m_pos][1][m]]
        m += 1
    map_position[m_pos][1] = sorted(positions)
    return map_position

# Part 1 :
map_position = []
for input_line in puzzle_input:    
    line_components = input_line.split(' ')
    sensor_position = (int(line_components[3].removeprefix('y=').removesuffix(':')), int(line_components[2].removeprefix('x=').removesuffix(',')))
    beacon_position = (int(line_components[9].removeprefix('y=')), int(line_components[8].removeprefix('x=').removesuffix(',')))
    distance = abs(sensor_position[0] - beacon_position[0]) + abs(sensor_position[1] - beacon_position[1])
    # map_position = add_to_map(sensor_position, map_position)
    # map_position = add_to_map(beacon_position, map_position)
    
    if (2000000 >= sensor_position[0] - distance) and (2000000 <= sensor_position[0] + distance):
        for x in [2000000]:
            for y in range(sensor_position[1] - distance, sensor_position[1] + distance + 1):
                if ((abs(x - sensor_position[0]) + abs(y - sensor_position[1])) <= distance):
                    map_position = add_to_map((x,y), map_position)

print('{0}{1} - Part 1 answer : {2}'.format(year, day,sum([s[1]-s[0] for m in range(len(map_position)) for s in map_position[m][1] if map_position[m][0] == 2000000])))

# Part 2 :
map_position = []
for input_line in puzzle_input:    
    line_components = input_line.split(' ')
    sensor_position = (int(line_components[3].removeprefix('y=').removesuffix(':')), int(line_components[2].removeprefix('x=').removesuffix(',')))
    beacon_position = (int(line_components[9].removeprefix('y=')), int(line_components[8].removeprefix('x=').removesuffix(',')))
    distance = abs(sensor_position[0] - beacon_position[0]) + abs(sensor_position[1] - beacon_position[1])
    # map_position = add_to_map(sensor_position, map_position)
    # map_position = add_to_map(beacon_position, map_position)
    
    print(input_line, distance)
    if (4000000 >= sensor_position[0] - distance) and (0 <= sensor_position[0] + distance):
        for x in range(4000000):
            for y in range(4000000):
                if (y >= (sensor_position[1] - distance)) and (y <= (sensor_position[1] + distance + 1)) and ((abs(x - sensor_position[0]) + abs(y - sensor_position[1])) <= distance):
                    map_position = add_to_map((x,y), map_position)

for m in sorted(map_position):
    print(m)

print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))
