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

from math import log10, ceil

def apply_maps(maps, seed):
    pre_map = seed
    for m in maps:
        for ds, ss, rl in m:
            if ss <= pre_map < ss + rl:
                pre_map = ds + (pre_map - ss)
                break
    return pre_map

def parse(seed_ranges = False):
    seeds = [int(x) for x in puzzle_input[0].split(': ')[1].split(' ')]

    if seed_ranges:
        seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    maps = []
    curr_map = []
    for d in puzzle_input[3:]:
        if d == '':
            continue
        if ':' in d:
            maps += [curr_map]
            curr_map = []
        else:
            curr_map += [tuple(int(x) for x in d.split(' '))]

    maps += [curr_map]

    return seeds, maps

def part_1():
    seeds, maps = parse(seed_ranges = False)
    locs = {apply_maps(maps, s): s for s in seeds}
    min_loc = min(locs.keys())

    return min_loc

def part_2():
    seeds, maps = parse(seed_ranges = True)

    step_size = int(pow(10, ceil(log10(max(s[1] for s in seeds) / 100))))
    search_vals = {(ss, ss + sl, s): apply_maps(maps, s) for ss, sl in seeds for s in range(ss, ss + sl, step_size)}
    rough_est = min(search_vals.items(), key = lambda x: x[1])

    seed_range_start, seed_range_end, best_estimation = rough_est[0]

    while step_size > 1:
        left_search  = max(best_estimation - step_size, seed_range_start)
        right_search = min(best_estimation + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {s: apply_maps(maps, s) for s in range(left_search, right_search, step_size)}
        best_estimation, best_location = min(search_vals.items(), key = lambda x: x[1])
    return best_location

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
