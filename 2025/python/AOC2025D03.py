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

def part_1():
    """Find the maximum two-digit number formed by two digits in order for each battery.

    Replace O(n^2) nested loops with an O(n) pass that tracks the best suffix digit.
    """
    total = 0
    for battery in puzzle_input:
        if len(battery) < 2:
            continue
        # best digit to the right of each position
        best_right = [''] * len(battery)
        best = battery[-1]
        best_right[-1] = best
        for i in range(len(battery) - 2, -1, -1):
            if battery[i + 1] > best:
                best = battery[i + 1]
            best_right[i] = best

        maximum = 0
        for i in range(len(battery) - 1):
            candidate = int(battery[i] + best_right[i])
            if candidate > maximum:
                maximum = candidate
        total += maximum
    return total

def _max_k_digits(battery: str, k: int) -> int:
    """Return the maximum k-digit number obtainable by selecting k digits from battery in order.

    Greedy algorithm: for each selection pick the largest digit possible while leaving
    enough digits to complete the remaining selections. O(n*k) time.
    """
    n = len(battery)
    if k <= 0 or k > n:
        return 0
    res = []
    start = 0
    for remaining in range(k, 0, -1):
        # we can pick from start up to n - remaining (inclusive)
        end = n - remaining
        best_digit = '0'
        best_pos = start
        for pos in range(start, end + 1):
            d = battery[pos]
            if d > best_digit:
                best_digit = d
                best_pos = pos
                if best_digit == '9':
                    break
        res.append(best_digit)
        start = best_pos + 1
    return int(''.join(res))


def part_2():
    total = 0
    K = 12
    for battery in puzzle_input:
        total += _max_k_digits(battery, K)
    return total

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
