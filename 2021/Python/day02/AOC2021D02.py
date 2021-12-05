year = '2021'
day = '02'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [password for password in reader.read().split('\n')]

# Part 1 : 
print('Part 1 answer :', sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "forward"])*(sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "down"])-sum([item[1] for item in [[input.split(' ')[0],int(input.split(' ')[1])] for input in puzzle_input] if item[0] == "up"])))

# Part 2 :
depth = 0
horizontal_position = 0
aim = 0
for input in puzzle_input:
    instruction = input.split(" ")[0]
    command = int(input.split(" ")[1])
    if instruction == "forward":
        horizontal_position += command
        depth += aim * command
    elif instruction == "down":
        aim += command
    elif instruction == "up":
        aim -= command
print('Part 2 answer :', horizontal_position * depth)