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
    puzzle_input = [puzzle_line for puzzle_line in reader.read().split('\n')]

from itertools import cycle
from math import lcm

def read_puzzle():
    turns = puzzle_input[0]

    directions = {}
    for d in puzzle_input[2:]:
        node, dirs = d.split(' = ')
        dirs = dirs.split('(')[1].split(')')[0].split(', ')
        directions[node] = dirs

    return turns, directions

def part_1():
    turns, directions = read_puzzle()

    curr_node = 'AAA'
    cnt = 0
    for t in cycle(turns):
        curr_node = directions[curr_node][0 if t == 'L' else 1]
        cnt += 1
        if curr_node == 'ZZZ':
            break

    return cnt

def part_2():
    turns, directions = read_puzzle()

    start_nodes = [n for n in directions if n[2] == 'A']
    curr_nodes = [n for n in start_nodes]

    cycle1_counts = [0] * len(curr_nodes)
    cycle2_counts = [0] * len(curr_nodes)
    for t in cycle(turns):
        for i, node in enumerate(curr_nodes):
            if node[2] == 'Z':
                if cycle2_counts[i] == 0:
                    cycle2_counts[i] = cycle1_counts[i]
                    cycle1_counts[i] = 0
                else:
                    continue
            curr_nodes[i] = directions[node][0 if t == 'L' else 1]
            cycle1_counts[i] += 1
        if all(n[2] == 'Z' for n in curr_nodes):
            break

    all_steps_count = lcm(*cycle1_counts)
    return all_steps_count

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
