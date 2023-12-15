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

from math import ceil, floor

def go_dist(time, button):
    return button * (time - button)

def part_1():
    times = [int(x) for x in puzzle_input[0].split(':')[1].split(' ') if x != '']
    dists = [int(x) for x in puzzle_input[1].split(':')[1].split(' ') if x != '']

    ways_all = 1
    for x in range(4):
        ways = 0
        t = times[x]
        d = dists[x]

        for button_time in range(t):
            g = go_dist(t, button_time)
            if g > d:
                ways += 1
        ways_all *= ways

    return ways_all

def part_2():
    time = int(puzzle_input[0].split(':')[1].replace(' ','').strip())
    dist = int(puzzle_input[1].split(':')[1].replace(' ','').strip())

    a = -1
    b = time
    c = -dist

    coeff = (pow(b, 2) - 4 * a * c) / (4 * a * a)

    sol1 = -b / (2 * a) + pow(coeff, 0.5)
    sol2 = -b / (2 * a) - pow(coeff, 0.5)

    if sol1 > sol2:
        sol1, sol2 = sol2, sol1

    sol1 = ceil(sol1)
    sol2 = floor(sol2)

    assert go_dist(time, sol1) >= dist
    assert go_dist(time, sol1 - 1) < dist
    assert go_dist(time, sol2) >= dist
    assert go_dist(time, sol2 + 1) < dist

    return sol2 - sol1 + 1

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
