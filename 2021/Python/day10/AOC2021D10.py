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
    puzzle_input =  [[puzzle_line,[]] for puzzle_line in reader.read().split('\n')]

for line_index in range(len(puzzle_input)):
    valid = True
    line = puzzle_input[line_index][0]
    c = -1
    check = ""
    while valid and c < len(line) - 1:
        c += 1
        char = line[c]
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
                    puzzle_input[line_index][1]=[expected, char, 0, "corrupted"]
            else:
                valid = False

    score=0
    if not valid and puzzle_input[line_index][1][3]=="corrupted":
        if char == ")":
            score=3
        elif char == "]":
            score=57
        elif char == "}":
            score=1197
        elif char == ">":
            score=25137
        puzzle_input[line_index][1][2]=score
    elif len(check)>0:
        valid = False
        expected = ""
        for c in reversed(check):
            score *= 5
            if c == "{":
                expected += "}"
                score += 3
            elif c == "[":
                expected += "]"
                score += 2
            elif c == "(":
                expected += ")"
                score += 1
            elif c == "<":
                expected += ">"
                score += 4
        puzzle_input[line_index][1]=["", "", score, "incomplete"]

# Part 1 :
print('Part 1 answer :', sum([e[1][2] for e in puzzle_input if e[1] != [] and e[1][3] == "corrupted"]))

# Part 2 :
scores = sorted([e[1][2] for e in puzzle_input if e[1] != [] and e[1][3] == "incomplete"])
print('Part 2 answer :', scores[len(scores)//2])
