from aocd import get_data
import os, copy

year = '2022'
day = '21'

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
original_stacks = copy.deepcopy(puzzle_input)

monkeys = []
for i in puzzle_input:
    input_components = i.split(': ')
    monkey = [input_components[0]]
    if len(input_components[1].split(' ')) > 1:
        monkey += ['-', [input_components[1].split(' ')[0], input_components[1].split(' ')[1], input_components[1].split(' ')[2]]]
    else:
        monkey += [int(input_components[1]),'']
    monkeys += [monkey]

monkeys = sorted(monkeys)
original_monkeys = copy.deepcopy(monkeys)


# Part 1 :
while len([mon for mon in monkeys if mon[0] == 'root' and mon[1] != '-']) == 0:
    for m in range(len(monkeys)):
        if monkeys[m][1] != '-':
            for m1 in range(len(monkeys)):
                if len(monkeys[m1][2]) > 0:
                    if monkeys[m1][2][0] == monkeys[m][0]:
                        monkeys[m1][2][0] = monkeys[m][1]
                    if monkeys[m1][2][2] == monkeys[m][0]:
                        monkeys[m1][2][2] = monkeys[m][1]
                    if isinstance(monkeys[m1][2][0], int) and isinstance(monkeys[m1][2][2], int):
                        if monkeys[m1][2][1] == '+':
                            monkeys[m1][1] = monkeys[m1][2][0] + monkeys[m1][2][2]
                            monkeys[m1][2] = ''
                        elif monkeys[m1][2][1] == '-':
                            monkeys[m1][1] = monkeys[m1][2][0] - monkeys[m1][2][2]
                            monkeys[m1][2] = ''
                        elif monkeys[m1][2][1] == '*':
                            monkeys[m1][1] = monkeys[m1][2][0] * monkeys[m1][2][2]
                            monkeys[m1][2] = ''
                        elif monkeys[m1][2][1] == '/':
                            monkeys[m1][1] = monkeys[m1][2][0] // monkeys[m1][2][2]
                            monkeys[m1][2] = ''

print('{0}{1} - Part 1 answer : {2}'.format(year, day, [mon[1] for mon in monkeys if mon[0] == 'root' and mon[1] != '-'][0]))

# Part 2 :
human_value = 3509819803060
root_equals = False
while not root_equals:
    human_value += 1
    monkeys = copy.deepcopy(original_monkeys)
    root_index = [mon for mon in range(len(monkeys)) if monkeys[mon][0] == 'root'][0]
    monkeys[root_index][2][1] = '=='
    human_index = [mon for mon in range(len(monkeys)) if monkeys[mon][0] == 'humn'][0]
    monkeys[human_index][1] = human_value
    while len([mon for mon in monkeys if mon[0] == 'root' and mon[1] != '-']) == 0:
        for m in range(len(monkeys)):
            if monkeys[m][1] != '-':
                for m1 in range(len(monkeys)):
                    if len(monkeys[m1][2]) > 0:
                        if monkeys[m1][2][0] == monkeys[m][0]:
                            monkeys[m1][2][0] = monkeys[m][1]
                        if monkeys[m1][2][2] == monkeys[m][0]:
                            monkeys[m1][2][2] = monkeys[m][1]
                        if isinstance(monkeys[m1][2][0], int) and isinstance(monkeys[m1][2][2], int):
                            if monkeys[m1][2][1] == '+':
                                monkeys[m1][1] = monkeys[m1][2][0] + monkeys[m1][2][2]
                                monkeys[m1][2] = ''
                            elif monkeys[m1][2][1] == '-':
                                monkeys[m1][1] = monkeys[m1][2][0] - monkeys[m1][2][2]
                                monkeys[m1][2] = ''
                            elif monkeys[m1][2][1] == '*':
                                monkeys[m1][1] = monkeys[m1][2][0] * monkeys[m1][2][2]
                                monkeys[m1][2] = ''
                            elif monkeys[m1][2][1] == '/':
                                monkeys[m1][1] = monkeys[m1][2][0] // monkeys[m1][2][2]
                                monkeys[m1][2] = ''
                            elif monkeys[m1][2][1] == '==':
                                monkeys[m1][1] = (monkeys[m1][2][0] == monkeys[m1][2][2])
                                monkeys[m1][2] = ''
    root_equals = [mon for mon in monkeys if mon[0] == 'root' and mon[1] != '-'][0][1]

print('{0}{1} - Part 2 answer : {2}'.format(year, day, human_value))