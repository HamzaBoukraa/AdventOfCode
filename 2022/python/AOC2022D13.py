from aocd import get_data
import os, ast, time

year = '2022'
day = '13'

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

def compare_items(left_item, right_item):   
    if len(left_item) > 0 and len(right_item) == 0:
        return 'F'
    elif len(left_item) == 0 and len(right_item) > 0:
        return 'T'
    elif len(left_item) > 0 and len(right_item) > 0:
        if isinstance(left_item[0], int) and isinstance(right_item[0], int):
            if left_item[0] < right_item[0]:
                return 'T'
            elif left_item[0] > right_item[0]:
                return 'F'
        elif isinstance(left_item[0], list) and isinstance(right_item[0], int):
            check = compare_items(left_item[0], [right_item[0]])
            if check in ['T' , 'F']:
                return check
        elif isinstance(left_item[0], int) and isinstance(right_item[0], list):
            check = compare_items([left_item[0]], right_item[0])
            if check in ['T' , 'F']:
                return check
        elif isinstance(left_item[0], list) and isinstance(right_item[0], list):
            check = compare_items(left_item[0], right_item[0])
            if check in ['T' , 'F']:
                return check
        check = compare_items(left_item[1:], right_item[1:])
        if check in ['T' , 'F']:
            return check

signals = []
left_signal = ''
right_signal = ''
signal_strength = 0
signal_index = 1
for i in range(len(puzzle_input)):
    if len(puzzle_input[i]) != 0:
        signals += [ast.literal_eval(puzzle_input[i])]
        if left_signal == '':
            left_signal = ast.literal_eval(puzzle_input[i])
        else:
            right_signal = ast.literal_eval(puzzle_input[i])
            
            if 'T' == compare_items(left_signal, right_signal):
                signal_strength += signal_index

            left_signal = ''
            right_signal = ''
            signal_index += 1

# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, signal_strength))

# Part 2 :
signals += [[[2]]]
signals += [[[6]]]

for spi in range(len(signals) - 1):
    for ssi in range(spi, len(signals)):
        if 'F' == compare_items(signals[spi], signals[ssi]):
            aux_signal = signals[spi]
            signals[spi] = signals[ssi]
            signals[ssi] = aux_signal

s = [s+1 for s in range(len(signals)) if signals[s] == [[2]] or signals[s] == [[6]]]

print('{0}{1} - Part 2 answer : {2}'.format(year, day, s[0] * s[1]))