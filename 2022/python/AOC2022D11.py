from aocd import get_data
import os, math, time

year = '2022'
day = '11'

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

# Part 1 :
puzzle_input_index = 0
monkeys = []
monkey_raw = {}
while puzzle_input_index < len(puzzle_input):
    input_line = puzzle_input[puzzle_input_index]
    while input_line.startswith(' '):
        input_line = input_line.removeprefix(' ')
    if len(input_line) == 0:
        monkeys += [monkey_raw]
        monkey_raw = {}
    else:
        if input_line.startswith('Monkey'):
            monkey_raw['number'] = int(input_line.split(' ')[1].replace(':',''))
        elif input_line.startswith('Starting'):
            monkey_raw['items'] = [int(i) for i in input_line.split(': ')[1].split(', ')]
        elif input_line.startswith('Operation'):
            monkey_raw['Operation'] = input_line.split(': ')[1]
        elif input_line.startswith('Test'):
            monkey_raw['Test'] = int(input_line.split(': ')[1].split(' ')[-1])
        elif input_line.startswith('If true'):
            monkey_raw['TrueDestination'] = int(input_line.split(': ')[1].split(' ')[-1])
        elif input_line.startswith('If false'):
            monkey_raw['FalseDestination'] = int(input_line.split(': ')[1].split(' ')[-1])
        monkey_raw['Inspections'] = 0
    puzzle_input_index += 1
monkeys += [monkey_raw]

round_index = 1
while round_index < 21:
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            item = monkey['items'][0]
            op = monkey['Operation'].split(' ')[-2]
            val = monkey['Operation'].split(' ')[-1]
            if val == 'old':
                val = item
            else:
                val = int(val)
            if op == '+':
                new_item_value = item + val
            elif op == '*':
                new_item_value = item * val
            new_item_value = new_item_value // 3
            test_result = ((new_item_value % monkey['Test']) == 0)
            if test_result:
                destination = monkey['TrueDestination']
            else:
                destination = monkey['FalseDestination']
            
            monkeys[destination]['items'] += [new_item_value]

            monkey['Inspections'] += 1
            monkey['items'] = monkey['items'][1:]
    
    round_index += 1

highest_iterations = sorted([m['Inspections'] for m in monkeys])[-2:]
print('{0}{1} - Part 1 answer : {2}'.format(year, day, highest_iterations[0] * highest_iterations[1]))

# Part 2 :
puzzle_input_index = 0
monkeys = []
monkey_raw = {}
while puzzle_input_index < len(puzzle_input):
    input_line = puzzle_input[puzzle_input_index]
    while input_line.startswith(' '):
        input_line = input_line.removeprefix(' ')
    if len(input_line) == 0:
        monkeys += [monkey_raw]
        monkey_raw = {}
    else:
        if input_line.startswith('Monkey'):
            monkey_raw['number'] = int(input_line.split(' ')[1].replace(':',''))
        elif input_line.startswith('Starting'):
            monkey_raw['items'] = [[int(i)%j for j in range(2, 24)] for i in input_line.split(': ')[1].split(', ')]
        elif input_line.startswith('Operation'):
            monkey_raw['Operation'] = input_line.split(': ')[1]
        elif input_line.startswith('Test'):
            monkey_raw['Test'] = int(input_line.split(': ')[1].split(' ')[-1])
        elif input_line.startswith('If true'):
            monkey_raw['TrueDestination'] = int(input_line.split(': ')[1].split(' ')[-1])
        elif input_line.startswith('If false'):
            monkey_raw['FalseDestination'] = int(input_line.split(': ')[1].split(' ')[-1])
        monkey_raw['Inspections'] = 0
    puzzle_input_index += 1
monkeys += [monkey_raw]

round_index = 1
while round_index < 10001:
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            item = monkey['items'][0]
            op = monkey['Operation'].split(' ')[-2]
            value = monkey['Operation'].split(' ')[-1]
            
            for i in range(len(item)):
                if op == '+':
                    val = int(value)
                    item[i] += val
                elif op == '*':
                    if value != 'old':
                        val = int(value)
                        item[i] *= val
                    else:
                        item[i] *= item[i]
                item[i] = item[i] % (i+2)

            test_result = ((item[monkey['Test'] - 2]) == 0)

            if test_result:
                destination = monkey['TrueDestination']
            else:
                destination = monkey['FalseDestination']
            monkey['Inspections'] += 1            
            monkeys[destination]['items'] += [item]
            monkey['items'] = monkey['items'][1:]    
    round_index += 1
highest_iterations = sorted([m['Inspections'] for m in monkeys])[-2:]
print('{0}{1} - Part 2 answer : {2}'.format(year, day, highest_iterations[0] * highest_iterations[1]))