from aocd import get_data
import os

year = '2022'
day = '01'

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
puzzle_input += ['']


elf_carriage = 0
elf_carriages = []
for puzzle_line in puzzle_input:
    if len(puzzle_line)==0:
        elf_carriages += [elf_carriage]
        elf_carriage = 0
    else:
        elf_carriage += int(puzzle_line)


# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, max(elf_carriages)))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, sum(sorted(elf_carriages)[-3:])))