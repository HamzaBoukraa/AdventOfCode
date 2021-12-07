year = '2021'
day = '04'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [entry for entry in reader.read().split('\n')]

bingo_grids = []
bingo_grid = []
result = 0
for line_index in range(len(puzzle_input)):
    if line_index == 0:
        numbers = [int(n) for n in puzzle_input[line_index].split(",")]
    else:
        if line_index % 6 != 1:
            # print(line_index, puzzle_input[line_index])
            bingo_line = puzzle_input[line_index].replace(" ","0")
            bingo_grid += [[(int(bingo_line[n]+bingo_line[n+1]),False) for n in range(13) if (n+2)%3==2]]

            if len(bingo_grid) == 5:
                bingo_grid += [False]
                bingo_grids += [bingo_grid]
                bingo_grid = []

# print(bingo_grids)
grids = len(bingo_grids)
bingo = False

num = 0
results = []
while not bingo and num < len(numbers) and len([bingo_grids[g][1] for g in range(grids) if bingo_grids[g][-1] == False]) > 0:
    number = numbers[num]
    n = 0
    while n < grids:
        if not bingo_grids[n][-1]:
            row = 0
            while row < 5 and not bingo:
                column = 0
                while column < 5 and not bingo:
                    if number == bingo_grids[n][row][column][0]:
                        bingo_grids[n][row][column] = (number, True)
                        b = False
                        c_t = 0
                        for c in range(5):
                            if (bingo_grids[n][row][c][1] == True):
                                c_t += 1
                        if c_t == 5:
                            b = True
                        else:
                            c_t = 0
                            for c in range(5):
                                if (bingo_grids[n][c][column][1] == True):
                                    c_t += 1
                            if c_t == 5:
                                b = True
                        
                        if b:
                            results += [number * sum([bingo_grids[n][r][c][0] for r in range(5) for c in range(5) if bingo_grids[n][r][c][1] == False])]
                            bingo_grids[n][-1] = True

                    column += 1
                row += 1
        n +=1
    num += 1


# Part 1 :
print('Part 1 answer :', results[0])

# Part 2 :
print('Part 2 answer :', results[-1])
