from aocd import get_data
import os

year = '2022'
day = '10'

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
x = 1
cycle = 1
signal_strength = 0
cycles_strength = [20 + (s * 40) for s in range(6)]
for instruction_line in puzzle_input:
    instructions = instruction_line.split(' ')
    if len(instructions) == 1:
        cycle += 1
        if cycle in cycles_strength:
            signal_strength += x * cycle
    else:
        cycle += 1
        if cycle in cycles_strength:
            signal_strength += x * cycle
        
        x += int(instructions[1])
        cycle += 1
        if cycle in cycles_strength:
            signal_strength += x * cycle
print('{0}{1} - Part 1 answer : {2}'.format(year, day, signal_strength))

# Part 2 :
x = 1
cycle = 0
screen_sprites = [['.' for s in range(40)] for l in range(6)]
for instruction_line in puzzle_input:
    instructions = instruction_line.split(' ')
    
    if len(instructions) == 1:
        cycle += 1
        if ((cycle - 1)  % 40) in range(x - 1, x + 2):
            screen_sprites[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
    else:
        cycle += 1
        if ((cycle - 1)  % 40) in range(x - 1, x + 2):
            screen_sprites[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
        
        cycle += 1
        if ((cycle - 1)  % 40) in range(x - 1, x + 2):
            screen_sprites[(cycle - 1) // 40][(cycle - 1)  % 40] = '#'
        x += int(instructions[1])
print('{0}{1} - Part 2 answer : '.format(year, day))
for line in screen_sprites:
    print(''.join([p for p in line]))