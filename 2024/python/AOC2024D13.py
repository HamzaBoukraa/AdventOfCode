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


def get_cost(ax, ay, bx, by, p1, p2):
    cost = 0
    denom_k1 = bx * ay - by * ax
    if denom_k1 != 0 and bx != 0:  # if these are zero, the values would be undefined
        k1_num = p2 * bx - by * p1
        if k1_num % denom_k1 == 0:  # exact int check
            k1 = k1_num // denom_k1
            k2_num = p1 - (ax * k1)
            if k2_num % bx == 0:  # exact int check
                k2 = k2_num // bx
                cost = k1 * 3 + k2
    return cost

def get_min_token(offset = 0):
    claws = []
    for line in puzzle_input:
        if "Button A" in line:
            claws += [{}]
        if 'Button' in line:
            label = line.split(':')[0].split()[1].strip()
            x_effort = int(line.split(':')[1].split(',')[0].strip().split('+')[1])
            y_effort = int(line.split(':')[1].split(',')[1].strip().split('+')[1])
            claws[-1][label] = (x_effort, y_effort)
        if 'Prize' in line:
            label = 'prize'
            x_effort = int(line.split(':')[1].split(',')[0].strip().split('=')[1]) + offset
            y_effort = int(line.split(':')[1].split(',')[1].strip().split('=')[1]) + offset
            claws[-1][label] = (x_effort, y_effort)

    min_token = 0
    for claw in claws:
        a_x_effort, a_y_effort = claw['A']
        b_x_effort, b_y_effort = claw['B']
        prize_x, prize_y = claw['prize']
        min_token += get_cost(a_x_effort, a_y_effort, b_x_effort, b_y_effort, prize_x, prize_y)
    
    return min_token

def part_1():    
    return get_min_token()

def part_2():    
    return get_min_token(10000000000000)

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
