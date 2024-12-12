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

the_map = [[int(i) for i in p] for p in puzzle_input]

end_of_trail = []
for row in range(len(the_map)):
    for column in range(len(the_map[0])):
        if the_map[row][column] == 9:
            end_of_trail += [[[the_map[row][column], (row, column), []]]]

def get_trail(eoti):
    current_item = eoti[-1]
    if current_item[0] > 0:
        next_item = current_item[0] - 1

        if current_item[1][0] > 0:
            if the_map[current_item[1][0] - 1][current_item[1][1]] == next_item:
                current_item[2] += get_trail([[next_item, (current_item[1][0] - 1, current_item[1][1]), []]])

        if current_item[1][0] < len(the_map) - 1:
            if the_map[current_item[1][0] + 1][current_item[1][1]] == next_item:
                current_item[2] += get_trail([[next_item, (current_item[1][0] + 1, current_item[1][1]), []]])

        if current_item[1][1] > 0:
            if the_map[current_item[1][0]][current_item[1][1] - 1] == next_item:
                current_item[2] += get_trail([[next_item, (current_item[1][0], current_item[1][1] - 1), []]])

        if current_item[1][1] < len(the_map[0]) - 1:
            if the_map[current_item[1][0]][current_item[1][1] + 1] == next_item:
                current_item[2] += get_trail([[next_item, (current_item[1][0], current_item[1][1] + 1), []]])

    return eoti

score_1 = 0
score_2 = 0
for e in end_of_trail:
    paths = []
    for p9 in get_trail(e):
        for p8 in p9[2]:
            for p7 in p8[2]:
                for p6 in p7[2]:
                    for p5 in p6[2]:
                        for p4 in p5[2]:
                            for p3 in p4[2]:
                                for p2 in p3[2]:
                                    for p1 in p2[2]:
                                        for p0 in p1[2]:
                                            paths += [[(p9[0],p9[1]), (p8[0], p8[1]), (p7[0], p7[1]), (p6[0],p6[1]), (p5[0],p5[1]), (p4[0],p4[1]), (p3[0],p3[1]), (p2[0],p2[1]), (p1[0], p1[1]), (p0[0], p0[1])]]

    heads = sorted([p[9][1] for p in paths])

    score_1 += len(set(heads))
    score_2 += len(paths)


def part_1():
    return score_1

def part_2():
    return score_2

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
