from aocd import get_data
import os, time

year = '2022'
day = '23'

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

map_positions = [[puzzle_input[x][y] for y in range(len(puzzle_input[x]))] for x in range(len(puzzle_input))]
elves = [[(x, y), (x, y), ['N', 'S', 'W', 'E']] for x in range(len(puzzle_input)) for y in range(len(puzzle_input[x])) if puzzle_input[x][y] == '#']

# Part 1 :

suggested_moves = 1
round = 1
while suggested_moves > 0:
    print("\n\n")
    print(elves)
    suggested_moves = 0
    for e in range(len(elves)):
        suggested = False
        if (((elves[e][0][0] == 0) or (elves[e][0][1] == 0) or map_positions[elves[e][0][0] - 1][elves[e][0][1] - 1] == '.')
        and ((elves[e][0][0] == 0) or map_positions[elves[e][0][0] - 1][elves[e][0][1]] == '.' )
        and ((elves[e][0][0] == 0) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] - 1][elves[e][0][1] + 1] == '.')
        and ((elves[e][0][1] == 0) or map_positions[elves[e][0][0]][elves[e][0][1] - 1] == '.')
        and ((elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0]][elves[e][0][1] + 1] == '.')
        and ((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == 0) or map_positions[elves[e][0][0] + 1][elves[e][0][1] - 1] == '.')
        and ((elves[e][0][0] == len(map_positions) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1]] == '.')
        and ((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1] + 1] == '.')):
            suggested = True
            pass
        else:
            move_index = 0
            while (not suggested) and move_index < 4:
                if elves[e][2][move_index] == 'N':
                    if (((elves[e][0][0] == 0) or (elves[e][0][1] == 0) or map_positions[elves[e][0][0] - 1][elves[e][0][1] - 1] == '.')
                    and ((elves[e][0][0] == 0) or map_positions[elves[e][0][0] - 1][elves[e][0][1]] == '.')
                    and ((elves[e][0][0] == 0) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] - 1][elves[e][0][1] + 1] == '.')):
                        suggested_moves += 1
                        elves[e][2] = elves[e][2][1:] + [elves[e][2][0]]
                        suggested = True
                        elves[e][1] = (elves[e][0][0] - 1, elves[e][0][1])
                elif elves[e][2][move_index] == 'S':
                    if (((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == 0) or map_positions[elves[e][0][0] + 1][elves[e][0][1] - 1] == '.')
                    and ((elves[e][0][0] == len(map_positions) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1]] == '.')
                    and ((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1] + 1] == '.')):
                        suggested_moves += 1
                        elves[e][2] = elves[e][2][1:] + [elves[e][2][0]]
                        suggested = True
                        elves[e][1] = (elves[e][0][0] + 1, elves[e][0][1])
                elif elves[e][2][move_index] == 'W':
                    if (((elves[e][0][0] == 0) or (elves[e][0][1] == 0) or map_positions[elves[e][0][0] - 1][elves[e][0][1] - 1] == '.')
                    and ((elves[e][0][1] == 0) or map_positions[elves[e][0][0]][elves[e][0][1] - 1] == '.')
                    and ((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1] - 1] == '.')):
                        suggested_moves += 1
                        elves[e][2] = elves[e][2][1:] + [elves[e][2][0]]
                        suggested = True
                        elves[e][1] = (elves[e][0][0], elves[e][0][1] - 1)
                elif elves[e][2][move_index] == 'E':
                    if (((elves[e][0][0] == 0) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] - 1][elves[e][0][1] + 1] == '.')
                    and ((elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0]][elves[e][0][1] + 1] == '.')
                    and ((elves[e][0][0] == len(map_positions) - 1) or (elves[e][0][1] == len(map_positions[0]) - 1) or map_positions[elves[e][0][0] + 1][elves[e][0][1] + 1] == '.')):
                        suggested_moves += 1
                        elves[e][2] = elves[e][2][1:] + [elves[e][2][0]]
                        suggested = True        
                        elves[e][1] = (elves[e][0][0], elves[e][0][1] + 1)
                move_index += 1

    print(elves)

    for m_r in range(len(map_positions)):
        for m_c in range(len(map_positions)):
            el = [e for e in elves if e[1] == (m_r, m_c)]
            if len(el) == 1:
                map_positions[el[0][0][0]][el[0][0][1]] = '.'
                map_positions[el[0][1][0]][el[0][1][1]] = '#'
                el[0][0] = el[0][1]
            else:
                for e in el:
                    e[1] = e[0]

    print(elves)

    for m_r in range(len(map_positions)):
        print(''.join(map_positions[m_r]))
    
    print(round, len([map_positions[x][y] for x in range(len(map_positions)) for y in range(len(map_positions[x])) if map_positions[x][y] == '.']))
    

    round += 1

    time.sleep(10)

print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))