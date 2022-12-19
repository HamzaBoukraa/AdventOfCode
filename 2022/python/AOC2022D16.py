from aocd import get_data
import os

year = '2022'
day = '16'

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
    puzzle_input =  sorted([[p[0], int(p[1]), 'C', p[2:]] for p in [puzzle_line.replace(' tunnels lead to valves ','').replace(' tunnels lead to valve ','').replace(' tunnel leads to valve ','').replace('Valve ','').replace('has flow rate=','').replace(';',' ').replace(',','').split(" ") for puzzle_line in reader.read().split('\n')]])

valves = puzzle_input
open_valves = []
minutes = 1
release_pressure = 0
position = 'AA'
while minutes < 30:
    valve = [v for v in valves if v[0] == position][0]
    minutes += 1

# Part 1 :
print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))