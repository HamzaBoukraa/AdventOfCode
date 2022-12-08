from aocd import get_data
import os

year = '2022'
day = '03'

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

def get_priority(item_type):
    item_priority = ord(item_type)-96
    if item_priority < 0:
        item_priority += 58
    return item_priority

# Part 1 :
item_types = []
for bag in puzzle_input:
    c1 = bag[:len(bag)//2]
    c2 = bag[len(bag)//2:]
    item_type = next(iter(set(sorted(c1)).intersection(set(sorted(c2)))))
    item_priority = get_priority(item_type)
    item_types += [[item_type,item_priority]]
print('{0}{1} - Part 1 answer : {2}'.format(year, day, sum([i[1] for i in item_types])))

# Part 2 :
item_types = []
temp_bags = []
for bag in puzzle_input:
    temp_bags += [bag]
    if len(temp_bags) == 3:
        item_type= next(iter(set(sorted(temp_bags[0])).intersection(set(sorted(temp_bags[1]))).intersection(set(sorted(temp_bags[2])))))
        item_priority = get_priority(item_type)
        item_types += [[item_type,item_priority]]
        temp_bags = []
print('{0}{1} - Part 2 answer : {2}'.format(year, day, sum([i[1] for i in item_types])))