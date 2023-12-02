from aocd import get_data
import os
import re

year = '2023'
day = '01'

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

# def get_first_digit(line):
#     return int(next((character for character in line if character.isdigit()), None))

literals = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}   

def get_first_and_last_digit_or_literal(line, digits_only = True):
    first = last = None

    pattern = r'\d' if digits_only else r'(?=('+ '|'.join(literals.keys()) + r'|\d))'

    digits = re.findall(pattern, line)

    for word in digits:
        if word.isdigit() or word in literals:
            if first is None:
                first = word if word.isdigit() else literals[word]
            last = word if word.isdigit() else literals[word]
    return (int(first) * 10) + int(last)

def get_puzzle_answer(digits_only = True):
    puzzle_answer = 0
    for input in puzzle_input:
        puzzle_answer += get_first_and_last_digit_or_literal(input, digits_only)
    return puzzle_answer


# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, get_puzzle_answer()))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, get_puzzle_answer(False)))
