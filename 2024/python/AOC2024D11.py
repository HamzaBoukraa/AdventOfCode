from aocd import get_data
import os
from collections import Counter

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

def part_1():
    blinks = 25
    queue = puzzle_input[0].split(" ")

    while blinks > 0:
        new_queue = []

        for number in queue:
            if number == "0":
                new_queue.append("1")
            elif len(number) % 2 == 0:
                half = len(number) // 2
                left_number = number[:half]
                right_number = number[half:]
                new_queue.extend([str(int(left_number)), str(int(right_number))])
            else:
                multiplied = str(int(number) * 2024)
                new_queue.append(multiplied)

        queue = new_queue
        blinks -= 1

    return len(queue)

def part_2():
    def count_occurrences(arr):
        return Counter(arr)

    stones = count_occurrences(list(map(int, puzzle_input[0].split(" "))))

    for blinks in range(1, 76):
        new_stones = Counter()

        for n, num_stone in stones.items():
            str_n = str(n)
            mid = len(str_n) // 2
            rem = len(str_n) % 2

            if n == 0:
                new_stones[1] += num_stone
            elif rem:
                key = 2024 * n
                new_stones[key] += num_stone
            else:
                first_part = n // (10 ** mid)
                second_part = n % (10 ** mid)
                new_stones[first_part] += num_stone
                new_stones[second_part] += num_stone

        stones = new_stones

        if blinks == 75:
            return sum(new_stones.values())

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
