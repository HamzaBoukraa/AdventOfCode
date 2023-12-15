from aocd import get_data
import os

puzzule_date = __file__.split('\\')[-1].split('.')[0].split('D')
year = puzzule_date[0][3:]
day = puzzule_date[1]

input_directory_folder_path = '..\\input'
input_file_path = '{0}\\AOC{1}D{2}_input.txt'.format(input_directory_folder_path,year, day)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year),day=int(day))
    
    with open(input_file_path, 'w') as writer:
        writer.write(data)

# Get Puzzle Input
with open(input_file_path, 'r') as reader:
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')]

cards = [[c, len([s for s in c[2] if s in c[1]]), 1] for c in [[int(g[0][1]), g[1][0].split(), g[1][1].split()] for g in [[j[0].split(), j[1].split(' | ')] for j in [pi.split(': ') for pi in puzzle_input]]]]

def part_1():
    return sum([pow(2, c[1]- 1) for c in cards if c[1] > 0])

def part_2():
    for card_index in range(len(cards)):
        if cards[card_index][1] > 0:
            for i in range(card_index + 1, card_index + 1 + cards[card_index][1]):
                cards[i][2] += cards[card_index][2]
    return sum([c[2] for c in cards])

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
