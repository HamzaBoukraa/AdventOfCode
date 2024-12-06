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

def search_horizontal():
    xmas_found = 0
    row = 0
    while row < len(puzzle_input):
        column = 0
        while column < len(puzzle_input[row]):
            if column + 3 < len(puzzle_input[row]):
                if puzzle_input[row][column] == "X" and puzzle_input[row][column+1] == "M" and puzzle_input[row][column+2] == "A" and puzzle_input[row][column+3] == "S":
                    xmas_found += 1
                    column+=4
                else:
                    column+=1
            else:
                column += 1
        row += 1

    return xmas_found

def search_horizontal_backwards():
    xmas_found = 0
    row = 0
    while row < len(puzzle_input):
        column = 0
        while column < len(puzzle_input[row]):
            if column + 3 < len(puzzle_input[row]):
                if puzzle_input[row][column] == "S" and puzzle_input[row][column+1] == "A" and puzzle_input[row][column+2] == "M" and puzzle_input[row][column+3] == "X":
                    xmas_found += 1
                    column+=4
                else:
                    column+=1
            else:
                column += 1
        row += 1

    return xmas_found

def search_vertical():
    xmas_found = 0
    column = 0
    while column < len(puzzle_input[0]):
        row = 0
        while row < len(puzzle_input):
            if row + 3 < len(puzzle_input):
                if puzzle_input[row][column] == "X" and puzzle_input[row + 1][column] == "M" and puzzle_input[row + 2][column] == "A" and puzzle_input[row + 3][column] == "S":
                    xmas_found += 1
                    row += 4
                else:
                    row += 1
            else:
                row += 1
        column += 1

    return xmas_found

def search_vertical_backwards():
    xmas_found = 0
    column = 0
    while column < len(puzzle_input[0]):
        row = 0
        while row < len(puzzle_input):
            # print(i, p[i])
            if row + 3 < len(puzzle_input):
                if puzzle_input[row][column] == "S" and puzzle_input[row + 1][column] == "A" and puzzle_input[row + 2][column] == "M" and puzzle_input[row + 3][column] == "X":
                    xmas_found += 1
                    row += 4
                else:
                    row += 1
            else:
                row += 1
        column += 1

    return xmas_found

def search_diagonal_1():
    xmas_found = 0
    starting_column = 0
    starting_row = len(puzzle_input) - 4

    while starting_row >= 0 and starting_column < len(puzzle_input[0]) - 3:
        row = starting_row
        column = starting_column

        while row < len(puzzle_input) and column < len(puzzle_input[0]):
            if row + 3 < len(puzzle_input) and column + 3 < len(puzzle_input[0]):
                if puzzle_input[row][column] == "X" and puzzle_input[row + 1][column + 1] == "M" and puzzle_input[row + 2][column + 2] == "A" and puzzle_input[row + 3][column + 3] == "S":
                    xmas_found += 1
                    row += 4
                    column += 4
                else:
                    row += 1
                    column += 1
            else:
                row += 1
                column += 1
        
        if starting_row > 0:
            starting_row -=1
        else:
            starting_column += 1

    return xmas_found

def search_diagonal_1_backwards():
    xmas_found = 0
    starting_column = 0
    starting_row = len(puzzle_input) - 4

    while starting_row >= 0 and starting_column < len(puzzle_input[0]) - 3:
        row = starting_row
        column = starting_column

        while row < len(puzzle_input) and column < len(puzzle_input[0]):
            if row + 3 < len(puzzle_input) and column + 3 < len(puzzle_input[0]):
                if puzzle_input[row][column] == "S" and puzzle_input[row + 1][column + 1] == "A" and puzzle_input[row + 2][column + 2] == "M" and puzzle_input[row + 3][column + 3] == "X":
                    xmas_found += 1
                    row += 4
                    column += 4
                else:
                    row += 1
                    column += 1
            else:
                row += 1
                column += 1
        
        if starting_row > 0:
            starting_row -=1
        else:
            starting_column += 1

    return xmas_found

def search_diagonal_2():
    xmas_found = 0
    starting_column = 3
    starting_row = 0

    while starting_row < len(puzzle_input) - 3 and starting_column < len(puzzle_input[0]):
        row = starting_row
        column = starting_column

        while row < len(puzzle_input) and column >= 0:
            if row + 3 < len(puzzle_input) and column - 3 >= 0:
                if puzzle_input[row][column] == "X" and puzzle_input[row + 1][column - 1] == "M" and puzzle_input[row + 2][column - 2] == "A" and puzzle_input[row + 3][column - 3] == "S":
                    xmas_found += 1
                    row += 4
                    column -= 4
                else:
                    row += 1
                    column -= 1
            else:
                row += 1
                column -= 1
        
        if starting_column < len(puzzle_input[0]) - 1:
            starting_column +=1
        else:
            starting_row += 1

    return xmas_found

def search_diagonal_2_backwards():
    xmas_found = 0
    starting_column = 3
    starting_row = 0

    while starting_row < len(puzzle_input) - 3 and starting_column < len(puzzle_input[0]):
        row = starting_row
        column = starting_column

        while row < len(puzzle_input) and column >= 0:
            if row + 3 < len(puzzle_input) and column - 3 >= 0:
                if puzzle_input[row][column] == "S" and puzzle_input[row + 1][column - 1] == "A" and puzzle_input[row + 2][column - 2] == "M" and puzzle_input[row + 3][column - 3] == "X":
                    xmas_found += 1
                    row += 4
                    column -= 4
                else:
                    row += 1
                    column -= 1
            else:
                row += 1
                column -= 1
        
        if starting_column < len(puzzle_input[0]) - 1:
            starting_column +=1
        else:
            starting_row += 1

    return xmas_found

def search_x_mas():
    x_mas_found = 0
    row = 1
    while row < len(puzzle_input) - 1:
        column = 1
        while column < len(puzzle_input[0]) - 1:
            if puzzle_input[row][column] == "A":
                if ((puzzle_input[row - 1][column - 1] == "M" and puzzle_input[row + 1][column + 1] == "S") or (puzzle_input[row - 1][column - 1] == "S" and puzzle_input[row + 1][column + 1] == "M")) \
                    and ((puzzle_input[row - 1][column + 1] == "M" and puzzle_input[row + 1][column - 1] == "S") or (puzzle_input[row - 1][column + 1] == "S" and puzzle_input[row + 1][column - 1] == "M")):
                    x_mas_found += 1
            column += 1
        row +=1
    return x_mas_found

def part_1():    
    return search_horizontal() + search_horizontal_backwards() + search_vertical() + search_vertical_backwards() + search_diagonal_1() + search_diagonal_1_backwards() + search_diagonal_2() + search_diagonal_2_backwards()

def part_2():
    return search_x_mas()

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
