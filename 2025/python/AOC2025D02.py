from aocd import get_data
import os
from typing import Iterable, Optional, Set, Tuple


puzzule_date = __file__.split('\\')[-1].split('.')[0].split('D')
year = puzzule_date[0][3:]
day = puzzule_date[1]

input_directory_folder_path = '..\\input'
input_file_path = '{0}\\AOC{1}D{2}_input.txt'.format(input_directory_folder_path, year, day)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year), day=int(day))

    with open(input_file_path, 'w') as writer:
        writer.write(data)

# Get Puzzle Input: list of (low, high) ranges
with open(input_file_path, 'r') as reader:
    raw = reader.read().strip()
    puzzle_input: Iterable[Tuple[int, int]] = []
    if raw:
        puzzle_input = [tuple(map(int, r.split('-'))) for r in raw.split(',') if r]


def _divisors_ge_2(n: int) -> Set[int]:
    """Return all divisors k >= 2 of n."""
    divs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    if n >= 2:
        divs.add(n)
    return divs


def _sum_repeating_numbers_in_range(low: int, high: int, allowed_k: Optional[Set[int]] = None) -> int:
    """Efficiently generate numbers in [low, high] that equal k repetitions of some block.

    If allowed_k is provided, only consider those repetition counts (e.g., {2} for part 1).
    """
    results: Set[int] = set()
    max_len = len(str(high))
    for total_len in range(2, max_len + 1):
        for k in _divisors_ge_2(total_len):
            if allowed_k is not None and k not in allowed_k:
                continue
            block_len = total_len // k
            start = 10 ** (block_len - 1)
            end = 10 ** block_len
            # build numbers by repeating the block k times
            for block in range(start, end):
                s = str(block) * k
                n = int(s)
                if n > high:
                    # blocks increase monotonically, so we can break
                    break
                if n >= low:
                    results.add(n)
    return sum(results)


def part_1() -> int:
    # only repetition of two equal halves
    total = 0
    for low, high in puzzle_input:
        total += _sum_repeating_numbers_in_range(low, high, allowed_k={2})
    return total


def part_2() -> int:
    # any k >= 2 repetitions
    total = 0
    for low, high in puzzle_input:
        total += _sum_repeating_numbers_in_range(low, high, allowed_k=None)
    return total

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
