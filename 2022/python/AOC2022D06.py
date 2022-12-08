from aocd import get_data
import os

year = '2022'
day = '06'

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
puzzle_input = puzzle_input[0]

def process_puzzle(marker_characters):
    marker_index = marker_characters
    marker_found = False
    while not marker_found and marker_index < len(puzzle_input):
        markers = list(puzzle_input[(marker_index - marker_characters): marker_index])
        if len(list(set(markers))) == marker_characters:
            marker_found = True
        else:
            marker_index += 1
    if marker_found:
        return marker_index
    else:
        return -1

# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, process_puzzle(4)))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, process_puzzle(14)))