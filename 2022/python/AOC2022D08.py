from aocd import get_data
import os

year = '2022'
day = '08'

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

# Part 1 :
visible_trees = 0
row_index = 0
while row_index < len(puzzle_input):
    column_index = 0
    while column_index < len(puzzle_input[row_index]):
        if column_index == 0 or row_index == 0 or column_index == (len(puzzle_input[row_index]) - 1) or row_index == (len(puzzle_input) -1):
            visible_trees += 1
        else:
            visible_tree_up = True
            temp_row_index = 0
            while temp_row_index < row_index and visible_tree_up:
                if int(puzzle_input[row_index][column_index]) <= int(puzzle_input[temp_row_index][column_index]):
                    visible_tree_up = False
                temp_row_index += 1
            if visible_tree_up:
                visible_trees += 1
            else:
                visible_tree_down = True
                temp_row_index = len(puzzle_input) - 1
                while temp_row_index > row_index and visible_tree_down:
                    if int(puzzle_input[row_index][column_index]) <= int(puzzle_input[temp_row_index][column_index]):
                        visible_tree_down = False
                    temp_row_index -= 1
                if visible_tree_down:
                    visible_trees += 1
                else:
                    visible_tree_left = True
                    temp_column_index = 0
                    while temp_column_index < column_index and visible_tree_left:
                        if int(puzzle_input[row_index][column_index]) <= int(puzzle_input[row_index][temp_column_index]):
                            visible_tree_left = False
                        temp_column_index += 1
                    if visible_tree_left:
                        visible_trees += 1
                    else:
                        visible_tree_right = True
                        temp_column_index = len(puzzle_input[row_index]) - 1
                        while temp_column_index > column_index and visible_tree_right:
                            if int(puzzle_input[row_index][column_index]) <= int(puzzle_input[row_index][temp_column_index]):
                                visible_tree_right = False
                            temp_column_index -= 1
                        if visible_tree_right:
                            visible_trees += 1

        column_index += 1
    row_index += 1
print('{0}{1} - Part 1 answer : {2}'.format(year, day, visible_trees))

# Part 2 :
highest_scenic_score = 0
row_index = 1
while row_index < len(puzzle_input):
    column_index = 1
    while column_index < len(puzzle_input[row_index]):
        scenic_score = 0

        visible_tree_up = True
        visible_trees_up = 0
        temp_row_index = row_index - 1
        while temp_row_index > -1 and visible_tree_up:
            if int(puzzle_input[row_index][column_index]) > int(puzzle_input[temp_row_index][column_index]):
                visible_trees_up += 1
            else:
                visible_trees_up += 1
                visible_tree_up = False
            temp_row_index -= 1

        visible_tree_down = True
        visible_trees_down = 0
        temp_row_index = row_index + 1
        while temp_row_index < len(puzzle_input) and visible_tree_down:
            if int(puzzle_input[row_index][column_index]) > int(puzzle_input[temp_row_index][column_index]):
                visible_trees_down += 1
            else:
                visible_trees_down += 1
                visible_tree_down = False
            temp_row_index += 1
            
            visible_tree_left = True
            visible_trees_left = 0
            temp_column_index = column_index - 1
            while temp_column_index > -1 and visible_tree_left:
                if int(puzzle_input[row_index][column_index]) > int(puzzle_input[row_index][temp_column_index]):
                    visible_trees_left += 1
                else:
                    visible_trees_left += 1
                    visible_tree_left = False
                temp_column_index -= 1
           
            visible_tree_right = True
            visible_trees_right = 0
            temp_column_index = column_index + 1
            while temp_column_index < len(puzzle_input[row_index]) and visible_tree_right:
                if int(puzzle_input[row_index][column_index]) > int(puzzle_input[row_index][temp_column_index]):
                    visible_trees_right += 1
                else:
                    visible_trees_right += 1
                    visible_tree_right = False
                temp_column_index += 1
        
        scenic_score = visible_trees_up * visible_trees_down * visible_trees_left * visible_trees_right

        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

        column_index += 1
    row_index += 1
print('{0}{1} - Part 2 answer : {2}'.format(year, day, highest_scenic_score))