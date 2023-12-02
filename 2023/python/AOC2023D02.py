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

def get_puzzle_solution_1():
    return sum([game[0] for game in [(int(g[0].split(' ')[1]), [t for t in [[item for item in \
                                        [(int(i.split(' ')[0]), i.split(' ')[1]) for i in gi.split(', ')] \
                                        if (item[1] == 'red' and item[0] > 12) or (item[1] == 'green' and item[0] > 13) or (item[1] == 'blue' and item[0] > 14)] \
                                        for gi in g[1].split('; ')] if len(t)>0]) for g in [l.split(': ') for l in puzzle_input]] if len(game[1]) == 0])

def get_puzzle_solution_2():
    sum_of_powers = 0
    for line in puzzle_input:
        game = line.split(': ')[1]
        minimum_cubes = [0, 0, 0]
        for game_set in game.split('; '):
            for cubes in game_set.split(', '):
                cube = cubes.split(' ')
                color = cube[1]
                count = int(cube[0])
                if color == 'red' and count > minimum_cubes[0]:
                    minimum_cubes[0] = count
                elif color == 'green' and count > minimum_cubes[1]:
                    minimum_cubes[1] = count
                elif color == 'blue' and count > minimum_cubes[2]:
                    minimum_cubes[2] = count
        sum_of_powers += minimum_cubes[0] * minimum_cubes[1] * minimum_cubes[2]
    return sum_of_powers

# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, get_puzzle_solution_1()))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, get_puzzle_solution_2()))
