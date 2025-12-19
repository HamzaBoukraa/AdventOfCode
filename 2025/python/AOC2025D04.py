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
    puzzle_input = [puzzle_line for puzzle_line in reader.read().split('\n')]


def _parse_grid(grid_lines):
    """Return a set of (r,c) coordinates for '@' cells and the number of rows.

    Rows may have varying lengths; checks will use row lengths per row.
    """
    coords = set()
    for r, row in enumerate(grid_lines):
        for c, ch in enumerate(row):
            if ch == '@':
                coords.add((r, c))
    return coords


def _neighbor_counts(coords, grid_lines):
    """Return a dict mapping coordinates to number of neighboring '@' cells.

    Only neighbors inside the original grid bounds are considered.
    """
    counts = {}
    nrows = len(grid_lines)
    for (r, c) in coords:
        for nr in range(r - 1, r + 2):
            if nr < 0 or nr >= nrows:
                continue
            row_len = len(grid_lines[nr])
            for nc in range(c - 1, c + 2):
                if nc < 0 or nc >= row_len:
                    continue
                if (nr, nc) == (r, c):
                    continue
                counts[(nr, nc)] = counts.get((nr, nc), 0) + 1
    return counts

def part_1():
    coords = _parse_grid(puzzle_input)
    counts = _neighbor_counts(coords, puzzle_input)
    # For each '@' cell, counts.get(coord, 0) gives number of neighbouring '@' cells
    return sum(1 for coord in coords if counts.get(coord, 0) < 4)

def part_2():
    coords = _parse_grid(puzzle_input)
    total = 0
    while True:
        counts = _neighbor_counts(coords, puzzle_input)
        to_remove = {coord for coord in coords if counts.get(coord, 0) < 4}
        if not to_remove:
            break
        total += len(to_remove)
        coords -= to_remove
    return total

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
