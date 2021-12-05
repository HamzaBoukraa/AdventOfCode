year = '2020'
day = '02'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [password for password in reader.read().split('\n')]

# Part 1 : 
print('Part 1 answer :', len([p for p in [(password, len([l for l in password[1] if password[0] == l])) for password in [(input.split(' ')[-2].split(':')[0], input.split(" ")[-1], int(input.split(' ')[0].split('-')[0]), int(input.split(' ')[0].split('-')[1])) for input in puzzle_input]] if p[1] <= p[0][3] and p[1] >= p[0][2]]))

# Part 2 : 
print('Part 2 answer :', len([password[1] for password in [(input.split(' ')[-2].split(':')[0], input.split(" ")[-1], int(input.split(' ')[0].split('-')[0]), int(input.split(' ')[0].split('-')[1])) for input in puzzle_input] if password[1][password[2] - 1] != password[1][password[3] - 1] and (password[1][password[2] - 1] == password[0] or password[1][password[3] - 1] == password[0])]))
