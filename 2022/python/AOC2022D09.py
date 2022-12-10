from aocd import get_data
import os

year = '2022'
day = '09'

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


def process(knots_count):
    for input_instruction in puzzle_input:
        direction = input_instruction.split(' ')[0]
        steps = int(input_instruction.split(' ')[1])
        
        for step in range(steps):
            if direction == 'L':
                knots_positions[0] = (knots_positions[0][0], knots_positions[0][1] - 1)
            elif direction == 'R':
                knots_positions[0] = (knots_positions[0][0], knots_positions[0][1] + 1)
            elif direction == 'U':
                knots_positions[0] = (knots_positions[0][0] - 1, knots_positions[0][1])
            elif direction == 'D':
                knots_positions[0] = (knots_positions[0][0] + 1, knots_positions[0][1])
            knots_position_history[0] += [knots_positions[0]]

            for knot in range(1, knots_count):

                if knots_positions[knot - 1][0] == knots_positions[knot][0] - 2:
                    if knots_positions[knot - 1][1] == knots_positions[knot][1] - 2:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] - 1:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1]:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1])
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 1:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] + 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 2:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] + 1)

                elif knots_positions[knot - 1][0] == knots_positions[knot][0] - 1:
                    if knots_positions[knot - 1][1] == knots_positions[knot][1] - 2:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 2:
                        knots_positions[knot] = (knots_positions[knot][0] - 1, knots_positions[knot][1] + 1)

                elif knots_positions[knot - 1][0] == knots_positions[knot][0]:
                    if knots_positions[knot - 1][1] == knots_positions[knot][1] - 2:
                        knots_positions[knot] = (knots_positions[knot][0], knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 2:
                        knots_positions[knot] = (knots_positions[knot][0], knots_positions[knot][1] + 1)

                elif knots_positions[knot - 1][0] == knots_positions[knot][0] + 1:
                    if knots_positions[knot - 1][1] == knots_positions[knot][1] + 2:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] + 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] - 2:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] - 1)

                elif knots_positions[knot - 1][0] == knots_positions[knot][0] + 2:
                    if knots_positions[knot - 1][1] == knots_positions[knot][1] - 2:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] - 1:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] - 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1]:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1])
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 1:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] + 1)
                    elif knots_positions[knot - 1][1] == knots_positions[knot][1] + 2:
                        knots_positions[knot] = (knots_positions[knot][0] + 1, knots_positions[knot][1] + 1)

                knots_position_history[knot] += [knots_positions[knot]]
            
# Part 1 :
knots_count = 2
initial_position = (0, 0)
knots_positions = [initial_position for k in range(knots_count)]
knots_position_history = [[initial_position] for k in range(knots_count)]
process(knots_count)
print('{0}{1} - Part 1 answer : {2}'.format(year, day, len(set(knots_position_history[knots_count - 1]))))

# Part 2 :
knots_count = 10
initial_position = (0, 0)
knots_positions = [initial_position for k in range(knots_count)]
knots_position_history = [[initial_position] for k in range(knots_count)]
process(knots_count)
print('{0}{1} - Part 1 answer : {2}'.format(year, day, len(set(knots_position_history[knots_count - 1]))))