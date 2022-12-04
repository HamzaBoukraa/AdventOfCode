from aocd import get_data
import os

year = '2022'
day = '02'

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
    puzzle_input =  [puzzle_line.split(' ') for puzzle_line in reader.read().split('\n')]


# Part 1 :
total_score = 0
for index in range(len(puzzle_input)):
    first = puzzle_input[index][0]
    second = puzzle_input[index][1]
    score = 0
    score += ord(second) - 87
    if ord(first) == ord(second) - 23:
        score += 3
    elif (ord(first) == ord(second) - 23 - 1) or (ord(first) == ord(second) - 23 + 2):
        score += 6
    total_score += score 

print('Part 1 answer :', total_score)


# Part 2 :
total_score = 0
for index in range(len(puzzle_input)):
    first = puzzle_input[index][0]
    second = puzzle_input[index][1]
    score = 0
    score += (ord(second) - 88) * 3
    
    if (first == 'A' and second == 'Y') \
        or (first == 'B' and second == 'X') \
        or (first == 'C' and second == 'Z'):
        score += 1
    elif (first == 'A' and second == 'Z') \
        or (first == 'B' and second == 'Y') \
        or (first == 'C' and second == 'X'):
        score += 2
    elif (first == 'A' and second == 'X') \
        or (first == 'B' and second == 'Z') \
        or (first == 'C' and second == 'Y'):
        score += 3
    
    total_score += score

print('Part 2 answer :', total_score)
