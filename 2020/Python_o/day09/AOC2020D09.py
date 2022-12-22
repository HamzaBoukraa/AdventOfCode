year = '2020'
day = '09'
suffix = ''
# suffix = '_1'

with open('..\..\Input\day{1}\AOC{0}D{1}_input{2}.txt'.format(year, day, suffix), 'r') as reader:
    puzzle_input = [int(input_line) for input_line in reader.read().split('\n')]

preamble_size = 25
# preamble_size = 5

# Part 1 :
matched = True
c = preamble_size - 1
indexes = set([c for c in range(len(puzzle_input)) if c >= preamble_size])
while matched and c < len(puzzle_input):
    c += 1
    matched = False
    if c >= preamble_size:
        b = c - preamble_size + 1
        while b < c and not matched:
            a = c - preamble_size
            while a < b and not matched:
                if c > b and c > a and b >= c - preamble_size and a >= c - preamble_size and b > a and puzzle_input[c] == puzzle_input[a] + puzzle_input[b]:
                    matched = True
                a += 1
            b += 1

invalid_number = puzzle_input[c]
print('Part 1 answer :', invalid_number)

# Part 2 :
start_item_index = -1
matched = False
while not matched and start_item_index < c:
    contiguous_sum = 0
    start_item_index += 1
    item_index = start_item_index
    items = []
    while item_index < c and contiguous_sum < invalid_number and not matched:
        contiguous_sum += puzzle_input[item_index]
        items += [puzzle_input[item_index]]
        if contiguous_sum == invalid_number:
            matched = True
        item_index += 1
print('Part 2 answer :', min(items) + max(items))
