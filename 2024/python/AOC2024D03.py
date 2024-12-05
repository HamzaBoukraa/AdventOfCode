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
    puzzle_input =  [puzzle_line for puzzle_line in reader.read()]

def part_1():
    index = 0
    current_sequence=''
    valid_sequences=[]
    last_char = ''
    while index < len(puzzle_input):
        current_char=puzzle_input[index]
        if current_sequence == '' and current_char == 'm':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'm' and current_char == 'u':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'mu' and current_char == 'l':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'mul' and current_char == '(':
            last_char = current_char
            current_sequence += last_char
            operands = []
        elif current_sequence == 'mul(' and current_char.isdigit():
            last_char = current_char
            current_sequence += last_char
            operands += [last_char]
        elif last_char.isdigit() and current_char.isdigit() and len(operands) == 1 and len(operands[0]) < 3:
            last_char = current_char
            current_sequence += last_char
            operands[0] += last_char
        elif last_char.isdigit() and current_char == ',' and len(operands) == 1:
            last_char = current_char
            current_sequence += last_char
        elif last_char == ',' and len(operands) == 1 and current_char.isdigit():
            last_char = current_char
            current_sequence += last_char
            operands += [last_char]
        elif last_char.isdigit() and current_char.isdigit() and len(operands) == 2 and len(operands[1]) < 3:
            last_char = current_char
            current_sequence += last_char
            operands[1] += last_char
        elif last_char.isdigit() and current_char == ')' and len(operands) == 2:
            last_char = current_char
            current_sequence += last_char
            if len(current_sequence) > 7:
                valid_sequences += [current_sequence]
            current_sequence = ''
            operands = []
        else:
            last_char = current_char
            current_sequence = ''
        index+=1

    return sum([int(i[0]) * int(i[1]) for i in [v[4:-1].split(',') for v in valid_sequences]])

def part_2():
    index = 0
    enabled_mul = True
    current_sequence=''
    valid_sequences=[]
    last_char = ''
    while index < len(puzzle_input):
        current_char=puzzle_input[index]
        if current_sequence == '' and current_char == 'm':
            last_char = current_char
            current_sequence += last_char
        elif last_char == 'd' and current_char == 'o':
            last_char = current_char
            current_sequence += "do"
        elif current_sequence == 'm' and current_char == 'u':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'mu' and current_char == 'l':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'mul' and current_char == '(':
            last_char = current_char
            current_sequence += last_char
            operands = []
        elif current_sequence == 'do' and current_char == '(':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'do' and current_char == 'n':
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'don' and current_char == "'":
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == "don'" and current_char == "t":
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == "don't" and current_char == "(":
            last_char = current_char
            current_sequence += last_char
        elif current_sequence == 'do(' and current_char == ')':
            last_char = current_char
            enabled_mul = True
            current_sequence = ''
        elif current_sequence == "don't(" and current_char == ')':
            last_char = current_char
            enabled_mul = False
            current_sequence = ''
        elif current_sequence == 'mul(' and current_char.isdigit():
            last_char = current_char
            current_sequence += last_char
            operands += [last_char]
        elif last_char.isdigit() and current_char.isdigit() and len(operands) == 1 and len(operands[0]) < 3:
            last_char = current_char
            current_sequence += last_char
            operands[0] += last_char
        elif last_char.isdigit() and current_char == ',' and len(operands) == 1:
            last_char = current_char
            current_sequence += last_char
        elif last_char == ',' and len(operands) == 1 and current_char.isdigit():
            last_char = current_char
            current_sequence += last_char
            operands += [last_char]
        elif last_char.isdigit() and current_char.isdigit() and len(operands) == 2 and len(operands[1]) < 3:
            last_char = current_char
            current_sequence += last_char
            operands[1] += last_char
        elif last_char.isdigit() and current_char == ')' and len(operands) == 2:
            last_char = current_char
            current_sequence += last_char
            if len(current_sequence) > 7 and enabled_mul == True:
                valid_sequences += [current_sequence]
            current_sequence = ''
            operands = []
        else:
            last_char = current_char
            current_sequence = ''
            operands = []
        index+=1

    return sum([int(i[0]) * int(i[1]) for i in [v[4:-1].split(',') for v in valid_sequences]])

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
