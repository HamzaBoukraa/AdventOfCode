year = '2020'
day = '03'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input =  [map_row for map_row in reader.read().split('\n')]

tree = "#"
moves = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

def process(move_index):
    move = moves[move_index]
    
    down_progression = move[0]
    right_progression = move[1]
    
    cell_index = [0,0]
    
    trees_count = 0
    
    while cell_index[0] < len(puzzle_input) - 1:
        cell_index[1] += right_progression
        cell_index[0] += down_progression
        while len(puzzle_input[cell_index[0]]) < cell_index[1]:
            puzzle_input[cell_index[0]] += puzzle_input[cell_index[0]]
        position = puzzle_input[cell_index[0]][cell_index[1]]
        if position == tree:
            trees_count += 1
    
    return trees_count

# Part 1 : 
print('Part 1 answer :', process(1))

# Part 2 :
result = 1
for step in range(5):
    result *= process(step)
print('Part 2 answer :', result)
