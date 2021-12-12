from aocd import get_data
import os

year = '2021'
day = '03'

input_directory_folder_path = '..\..\Input\day{0}'.format(day)
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

gamma_rate = ""
epsilon_rate = ""
for pos in range(len(puzzle_input[0])):
    zeroes = 0
    ones = 0
    for input in puzzle_input:
        if input[pos] == "0":
            zeroes += 1
        elif input[pos] == "1":
            ones += 1
    if zeroes > ones:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
    
# Part 1 : 
print('Part 1 answer :', int(gamma_rate,2)*int(epsilon_rate,2))

# Part 2 :
puzzle_oxygen = puzzle_input.copy()
puzzle_co2 = puzzle_input.copy()
while len(puzzle_oxygen)>1 or len(puzzle_co2)>1:
    for pos in range(len(puzzle_input[0])):

        zeroes_o = 0
        ones_o = 0

        for input in puzzle_oxygen:
            if input[pos] == "0":
                zeroes_o += 1
            elif input[pos] == "1":
                ones_o += 1

        zeroes_co = 0
        ones_co = 0

        for input in puzzle_co2:
            if input[pos] == "0":
                zeroes_co += 1
            elif input[pos] == "1":
                ones_co += 1

        puzzle_index = 0
        while puzzle_index < len(puzzle_oxygen) and len(puzzle_oxygen) > 1:
            if (zeroes_o > ones_o and puzzle_oxygen[puzzle_index][pos] == "1") or (zeroes_o <= ones_o and puzzle_oxygen[puzzle_index][pos] == "0"):
                puzzle_oxygen.pop(puzzle_index)
                puzzle_index -= 1
            puzzle_index += 1

        puzzle_index = 0
        while puzzle_index < len(puzzle_co2) and len(puzzle_co2) > 1:
            if (zeroes_co > ones_co and puzzle_co2[puzzle_index][pos] == "0") or (zeroes_co <= ones_co and puzzle_co2[puzzle_index][pos] == "1"):
                puzzle_co2.pop(puzzle_index)
                puzzle_index -= 1
            puzzle_index += 1

print('Part 2 answer :', int(puzzle_oxygen[0],2)*int(puzzle_co2[0],2))