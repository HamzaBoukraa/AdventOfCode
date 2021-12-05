year = '2021'
day = '03'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [map_row for map_row in reader.read().split('\n')]

gamma_rate = ""
epsilon_rate = ""
for pos in range(len(puzzle_input[0])):
    zeroes = 0
    ones = 0
    for input in puzzle_input:
        if input[pos] == "0":
            zeroes += 1
        elif input[pos] == "1":
            ones += 1
    if zeroes > ones:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
    
# Part 1 : 
print('Part 1 answer :', int(gamma_rate,2)*int(epsilon_rate,2))

# Part 2 :
puzzle_oxygen = puzzle_input.copy()
puzzle_co2 = puzzle_input.copy()
while len(puzzle_oxygen)>1 or len(puzzle_co2)>1:
    for pos in range(len(puzzle_input[0])):

        zeroes_o = 0
        ones_o = 0

        for input in puzzle_oxygen:
            if input[pos] == "0":
                zeroes_o += 1
            elif input[pos] == "1":
                ones_o += 1

        zeroes_co = 0
        ones_co = 0

        for input in puzzle_co2:
            if input[pos] == "0":
                zeroes_co += 1
            elif input[pos] == "1":
                ones_co += 1

        puzzle_index = 0
        while puzzle_index < len(puzzle_oxygen) and len(puzzle_oxygen) > 1:
            if (zeroes_o > ones_o and puzzle_oxygen[puzzle_index][pos] == "1") or (zeroes_o <= ones_o and puzzle_oxygen[puzzle_index][pos] == "0"):
                puzzle_oxygen.pop(puzzle_index)
                puzzle_index -= 1
            puzzle_index += 1

        puzzle_index = 0
        while puzzle_index < len(puzzle_co2) and len(puzzle_co2) > 1:
            if (zeroes_co > ones_co and puzzle_co2[puzzle_index][pos] == "0") or (zeroes_co <= ones_co and puzzle_co2[puzzle_index][pos] == "1"):
                puzzle_co2.pop(puzzle_index)
                puzzle_index -= 1
            puzzle_index += 1

print('Part 2 answer :', int(puzzle_oxygen[0],2)*int(puzzle_co2[0],2))