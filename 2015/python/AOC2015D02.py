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

boxes_dimensions = [sorted([int(dimension) for dimension in box.split("x")]) for box in puzzle_input]

def part_1():
    paper_dimensions = [(b[0] * b[1]) + (2 * (b[0] * (b[1] + b[2]) + (b[1] * b[2])))  for b in boxes_dimensions]
    return sum(paper_dimensions)

def part_2():
    ribbon_dimensions = [2 * (b[0] + b[1]) + (b[0] * b[1] * b[2])  for b in boxes_dimensions]
    return sum(ribbon_dimensions)

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
