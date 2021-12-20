from aocd import get_data
import os

year = '2021'
day = '10'

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

errors = [[] for line_index in range(len(puzzle_input))]

for line_index in range(len(puzzle_input)):
    valid = True
    c = -1
    check = ""
    while valid and c < len(puzzle_input[line_index]) - 1:
        c += 1
        char = puzzle_input[line_index][c]
        if char in ["<","{","(","["]:
            check += char
        else:
            if char in [">","}",")","]"]:
                expected = ""
                if check[-1] == "{":
                    expected = "}"
                elif check[-1] == "[":
                    expected = "]"
                elif check[-1] == "(":
                    expected = ")"
                elif check[-1] == "<":
                    expected = ">"
                if char == expected:
                    check = check[:-1]
                else:
                    valid = False
    if valid:
        errors[line_index]=[]
    else:
        score=0
        if char == ")":
            score=3
        elif char == "]":
            score=57
        elif char == "}":
            score=1197
        elif char == ">":
            score=25137
        errors[line_index]=[expected, char, score]

# Part 1 :
print('Part 1 answer :', sum([e[2] for e in errors if e != []]))

# Part 2 :
print('Part 2 answer :', puzzle_input)
