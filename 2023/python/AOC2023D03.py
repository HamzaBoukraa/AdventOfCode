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

numbers_list = []
symbols_list = []

for line_index in range(len(puzzle_input)):
    for char_index in range(len(puzzle_input[line_index])):
        char = puzzle_input[line_index][char_index]
        if char != ".":
            if char.isdigit():
                if numbers_list and numbers_list[-1][1] == line_index and numbers_list[-1][3] == char_index - 1:
                    numbers_list[-1] = [int(char) + (numbers_list[-1][0] * 10), line_index, numbers_list[-1][2], char_index]
                else:
                    numbers_list += [[int(char), line_index, char_index, char_index]]
            else:
                symbols_list += [[char, line_index, char_index]]

for i in range(len(numbers_list)):
    numbers_list[i] = [i, numbers_list[i][0], numbers_list[i][1], numbers_list[i][2], numbers_list[i][3], False]

gear_parts_sum = 0
for symbol in symbols_list:
    parts = []
    for number_item in [n for n in numbers_list if n[5] == False]:
        if ((symbol[1] == number_item[2] and ((symbol[2] == number_item[4] + 1) or (symbol[2] == number_item[3] - 1))) \
            or (((symbol[1] == number_item[2] - 1) or (symbol[1] == number_item[2] + 1)) and ((symbol[2] == number_item[3] - 1) or (symbol[2] == number_item[4] + 1))) \
                or (((symbol[1] == number_item[2] - 1) or (symbol[1] == number_item[2] + 1)) and (symbol[2] >= number_item[3]) and (symbol[2] <= number_item[4]))) \
                    and number_item[5] == False:
            numbers_list[number_item[0]][5] = True
            parts += [numbers_list[number_item[0]][1]]
    if len(parts) == 2 and symbol[0] == '*':
        gear_parts_sum += parts[0] * parts[1]

def part_1():
    return sum([n[1] for n in numbers_list if n[5] == True])

def part_2():
    return gear_parts_sum

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
