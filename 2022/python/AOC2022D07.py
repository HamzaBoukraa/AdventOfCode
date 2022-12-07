from aocd import get_data
import os

year = '2022'
day = '07'

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



def process_line(instruction_line, current_path):
    if instruction_line[0] == '$':
        current_path = process_instruction(instruction_line, current_path)
    else:
        current_path = process_folder_content(instruction_line, current_path)
    
    return current_path

def process_folder_content(content_line, current_path):
    if content_line[0] == 'dir':
        child_directory_path = current_path + content_line[1] + '/'
        
        if child_directory_path not in directories:
            directories[child_directory_path] = 0
    else:
        file_path = current_path + content_line[1]
        
        directory_weight_path = file_path

        while len(directory_weight_path) > 1:
            directories[directory_weight_path[:directory_weight_path.rindex('/') + 1]] += int(content_line[0])
            directory_weight_path = directory_weight_path[:directory_weight_path.rindex('/')]
           
    return current_path

def process_instruction(instruction_arguments, current_path):    
    if instruction_arguments[1] == 'cd':
        if instruction_arguments[2] == '/':
            current_path += '/'
        elif instruction_arguments[2] == '..':
            current_path = '/'.join(current_path.split('/')[:-2]) + '/'
        else:
            current_path += instruction_arguments[2] + '/'
        
        if current_path not in directories:
            directories[current_path] = 0
    elif instruction_arguments[1] == 'ls':
        pass
    
    return current_path

directories = {}
directory_path = ""

input_position = 0
while input_position < len(puzzle_input):
    directory_path = process_line(puzzle_input[input_position].split(' '), directory_path)
    input_position += 1

# Part 1 :
print('Part 1 answer :', sum([directories[directory] for directory in directories if directories[directory] <= 100000]))

# Part 2 :
required_space = 30000000 - (70000000 - [directories[directory] for directory in directories if directory == '/'][0])
print('Part 2 answer :', min([directories[directory] for directory in directories if directories[directory] >= required_space]))
