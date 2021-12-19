from aocd import get_data
import os

year = '2021'
day = '08'

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

puzzle_lines = [[[sorted(set(d)) for d in l.split(" | ")[0].split(" ")],
[sorted(set(d)) for d in l.split(" | ")[1].split(" ")],
["X" for x in range(4)]] for l in puzzle_input]

# Part 1 :
print('Part 1 answer :', sum([len([output for output in line[1] if output in [digit for digit in line[0] if len(digit) in [2,3,4,7]]]) for line in puzzle_lines]))

# Part 2 :
for line_index in range(len(puzzle_lines)):
    possible_wires = {}
    possible_wires["A"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,2,3,5,6,7,8,9]]
    possible_wires["B"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,4,5,6,8,9]]
    possible_wires["C"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,1,2,3,4,7,8,9]]
    possible_wires["D"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[2,3,4,5,6,8,9]]
    possible_wires["E"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,2,6,8]]
    possible_wires["F"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,1,3,4,5,6,7,8,9]]
    possible_wires["G"] = [chr(a) for a in range(ord("a"),ord("h"))]#,[0,2,3,5,6,8,9]]

    ind = 8

    while len([p for p in possible_wires if len(possible_wires[p]) == 1]) != 7 and ind >= 0:
        ind -= 1
        for digits_count in range(2,7):
            for input_index in range(len(puzzle_lines[line_index][0])):
                digits_i = puzzle_lines[line_index][0][input_index]

                if len(digits_i) == digits_count:
                    if len(digits_i) == 2:
                        for p in possible_wires:
                            for e in range(ord("a"),ord("h")):
                                if p not in ["C","F"] and chr(e) in possible_wires[p] and chr(e) in digits_i:
                                    possible_wires[p].remove(chr(e))
                                if p in ["C","F"] and chr(e) in possible_wires[p] and chr(e) not in digits_i:
                                    possible_wires[p].remove(chr(e))
                        for i_index in range(len(puzzle_lines[line_index][0])):
                            if len(puzzle_lines[line_index][0][i_index]) == digits_count:
                                puzzle_lines[line_index][0][i_index] = []
                    if len(digits_i) == 3:
                        for p in possible_wires:
                            for e in range(ord("a"),ord("h")):
                                if p not in ["A", "C","F"] and chr(e) in possible_wires[p] and chr(e) in digits_i:
                                    possible_wires[p].remove(chr(e))
                                if p in ["A", "C","F"] and chr(e) in possible_wires[p] and chr(e) not in digits_i:
                                    possible_wires[p].remove(chr(e))
                        for i_index in range(len(puzzle_lines[line_index][0])):
                            if len(puzzle_lines[line_index][0][i_index]) == digits_count:
                                puzzle_lines[line_index][0][i_index] = []
                    if len(digits_i) == 4:
                        for p in possible_wires:
                            for e in range(ord("a"),ord("h")):
                                if p not in ["B", "C", "D", "F"] and chr(e) in possible_wires[p] and chr(e) in digits_i:
                                    possible_wires[p].remove(chr(e))
                                if p in ["B", "C", "D", "F"] and chr(e) in possible_wires[p] and chr(e) not in digits_i:
                                    possible_wires[p].remove(chr(e))
                        for i_index in range(len(puzzle_lines[line_index][0])):
                            if len(puzzle_lines[line_index][0][i_index]) == digits_count:
                                puzzle_lines[line_index][0][i_index] = []
                    if len(digits_i) == 6:
                        missing = [chr(item) for item in range(ord("a"),ord("h")) if chr(item) not in digits_i][0]
                        done = False

                        if missing in possible_wires["C"]:
                            possible_wires["C"] = [missing]
                            if missing in possible_wires["F"]:
                                possible_wires["F"].remove(missing)
                            done = True
                        elif missing in possible_wires["E"]:
                            possible_wires["E"] = [missing]
                            if missing in possible_wires["G"]:
                                possible_wires["G"].remove(missing)
                            done = True
                        elif missing in possible_wires["D"]:
                            possible_wires["D"] = [missing]
                            if missing in possible_wires["B"]:
                                possible_wires["B"].remove(missing)
                            done = True

                        if done:
                            for i_index in range(len(puzzle_lines[line_index][0])):
                                if puzzle_lines[line_index][0][i_index] == digits_i:
                                    puzzle_lines[line_index][0][i_index] = []
    
    for output_index in range(len(puzzle_lines[line_index][1])):
        if puzzle_lines[line_index][1][output_index] == sorted([possible_wires["C"][0],possible_wires["F"][0]]):
            puzzle_lines[line_index][2][output_index] = "1"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["C"][0],possible_wires["D"][0],possible_wires["E"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "2"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["C"][0],possible_wires["D"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "3"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["B"][0],possible_wires["C"][0],possible_wires["D"][0],possible_wires["F"][0]]):
            puzzle_lines[line_index][2][output_index] = "4"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["B"][0],possible_wires["D"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "5"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["B"][0],possible_wires["D"][0],possible_wires["E"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "6"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["C"][0],possible_wires["F"][0]]):
            puzzle_lines[line_index][2][output_index] = "7"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["B"][0],possible_wires["C"][0],possible_wires["D"][0],possible_wires["E"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "8"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["B"][0],possible_wires["C"][0],possible_wires["D"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "9"
        elif puzzle_lines[line_index][1][output_index] == sorted([possible_wires["A"][0],possible_wires["B"][0],possible_wires["C"][0],possible_wires["E"][0],possible_wires["F"][0],possible_wires["G"][0]]):
            puzzle_lines[line_index][2][output_index] = "0"
    
print('Part 2 answer :', sum([int(''.join(puzzle_lines[line_index][2])) for line_index in range(len(puzzle_lines))]))
