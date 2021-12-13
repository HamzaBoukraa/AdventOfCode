from aocd import get_data
import os

year = '2021'
day = '06'

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

lanterns = sorted([int(lantern) for lantern in [l.split(',') for l in puzzle_input][0]])

fishes_map =[[s,len([l for l in lanterns if l==s])] for s in range(9)]

def process(fishes_map,days)->int:
    for day in range(1,days+1):
        a = []
        a += [[f[0]-1,f[1]] for f in fishes_map if f[0] > 0]
        a += [[6,f[1]] for f in fishes_map if f[0] == 0]
        a += [[8,f[1]] for f in fishes_map if f[0] == 0]

        fishes_map = [[s,0] for s in range(9)]
        for e in range(len(fishes_map)):
            fishes_map[e][1] = sum([ax[1] for ax in a if ax[0]==e])

        fishes = sum([f[1] for f in fishes_map])
    return fishes

# Part 1 :
print('Part 1 answer :', process(fishes_map,80))

# Part 2 :
print('Part 2 answer :', process(fishes_map,256))
