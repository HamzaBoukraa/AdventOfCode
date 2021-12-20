from aocd import get_data
import os, math

year = '2021'
day = '09'

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

puzzle_map = []
for i in range(len(puzzle_input)):
    puzzle_map += [[int(s) for s in puzzle_input[i]]]

points = []
for r in range(len(puzzle_map)):
    for c in range(len(puzzle_map[r])):
        if (c == len(puzzle_map[r]) - 1 or puzzle_map[r][c] < puzzle_map[r][c + 1]) \
            and (c == 0 or puzzle_map[r][c] < puzzle_map[r][c - 1]) \
            and (r == len(puzzle_map) - 1 or puzzle_map[r][c] < puzzle_map[r + 1][c]) \
            and (r == 0 or puzzle_map[r][c] < puzzle_map[r - 1][c]):
            points += [[r,c,[(r,c)],0]]

# Part 1 :
print('Part 1 answer :', sum(puzzle_map[p[0]][p[1]] + 1 for p in points))

# Part 2 :
for p in range(len(points)):
    points[p] = [points[p][0],points[p][1],[(points[p][0],points[p][1])],0]

    added = 1
    while added > 0:
        added = 0
        for c in points[p][2]:
            if c[0]<(len(puzzle_map)-1) and (c[0]+1,c[1]) not in points[p][2] and puzzle_map[c[0]+1][c[1]]!= 9 and abs(puzzle_map[c[0]+1][c[1]]-puzzle_map[c[0]][c[1]]) >= 1:
                points[p][2] += [(c[0]+1,c[1])]
                added += 1
            if c[0]>0 and (c[0]-1,c[1]) not in points[p][2] and puzzle_map[c[0]-1][c[1]]!= 9 and abs(puzzle_map[c[0]-1][c[1]]-puzzle_map[c[0]][c[1]]) >= 1:
                points[p][2] += [(c[0]-1,c[1])]
                added += 1
            if c[1]<(len(puzzle_map[0])-1) and (c[0],c[1] + 1) not in points[p][2] and puzzle_map[c[0]][c[1]+1]!= 9 and abs(puzzle_map[c[0]][c[1] + 1]-puzzle_map[c[0]][c[1]]) >= 1:
                points[p][2] += [(c[0],c[1]+1)]
                added += 1
            if c[1]>0 and (c[0],c[1] - 1) not in points[p][2] and puzzle_map[c[0]][c[1]-1]!= 9 and abs(puzzle_map[c[0]][c[1] - 1]-puzzle_map[c[0]][c[1]]) >= 1:
                points[p][2] += [(c[0],c[1]-1)]
                added += 1
    points[p][3] = len(points[p][2])

print('Part 2 answer :', math.prod(sorted([points[x][3] for x in range(len(points)) if points[x][3] != 0])[-3:]))
