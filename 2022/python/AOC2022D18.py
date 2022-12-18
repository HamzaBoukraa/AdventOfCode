from aocd import get_data
import os

year = "2022"
day = "18"

input_directory_folder_path = "..\input"
input_file_path = "{0}\AOC{1}D{2}_input.txt".format(
    input_directory_folder_path, year, day
)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year), day=int(day))

    with open(input_file_path, "w") as writer:
        writer.write(data)

# Get Puzzle Input
with open(input_file_path, "r") as reader:
    puzzle_input = [puzzle_line for puzzle_line in reader.read().split("\n")]

cubes = []
for line_input in puzzle_input:
    cube_raw = line_input.split(",")
    xyz = (int(cube_raw[0]), int(cube_raw[1]), int(cube_raw[2]))
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    cube = [
        ((x, y, z), (x, y + 1, z), (x + 1, y + 1, z), (x + 1, y, z)),
        ((x, y, z), (x, y + 1, z), (x, y + 1, z + 1), (x, y, z + 1)),
        ((x, y, z), (x + 1, y, z), (x + 1, y, z + 1), (x, y, z + 1)),
        ((x + 1, y, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x + 1, y, z + 1)),
        ((x, y + 1, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x, y + 1, z + 1)),
        ((x, y, z + 1), (x, y + 1, z + 1), (x + 1, y + 1, z + 1), (x + 1, y, z + 1)),
    ]
    cubes += [cube]


# Part 1 :
total_uncovered = 0
for cube_index in range(len(cubes)):
    total_uncovered += len(cubes[cube_index])

    for cube_index_compare in range(len(cubes)):
        if cube_index < cube_index_compare:
            if (cubes[cube_index][0] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][5] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][5] == cubes[cube_index][0]):
                cubes[cube_index_compare][5] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][0] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2
            elif (cubes[cube_index][1] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][3] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][3] == cubes[cube_index][1]):
                cubes[cube_index_compare][3] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][1] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2
            elif (cubes[cube_index][2] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][4] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][4] == cubes[cube_index][2]):
                cubes[cube_index_compare][4] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][2] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2
            elif (cubes[cube_index][3] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][1] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][1] == cubes[cube_index][3]):
                cubes[cube_index_compare][1] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][3] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2
            elif (cubes[cube_index][4] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][2] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][2] == cubes[cube_index][4]):
                cubes[cube_index_compare][2] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][4] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2
            elif (cubes[cube_index][5] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][0] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][0] == cubes[cube_index][5]):
                cubes[cube_index_compare][0] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][5] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

print("{0}{1} - Part 1 answer : {2}".format(year, day, total_uncovered))

# Part 2 :
for cube_index in range(len(cubes)):
    for cube_index_compare in range(len(cubes)):
        if False and cube_index < cube_index_compare:
            if (
                cubes[cube_index][0] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][5] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][5][0][2] < cubes[cube_index][0][0][2]
                and (
                    cubes[cube_index_compare][5][0][0],
                    cubes[cube_index_compare][5][0][1],
                    cubes[cube_index_compare][5][1][0],
                    cubes[cube_index_compare][5][1][1],
                    cubes[cube_index_compare][5][2][0],
                    cubes[cube_index_compare][5][2][1],
                    cubes[cube_index_compare][5][3][0],
                    cubes[cube_index_compare][5][3][1],
                )
                == (
                    cubes[cube_index][0][0][0],
                    cubes[cube_index][0][0][1],
                    cubes[cube_index][0][1][0],
                    cubes[cube_index][0][1][1],
                    cubes[cube_index][0][2][0],
                    cubes[cube_index][0][2][1],
                    cubes[cube_index][0][3][0],
                    cubes[cube_index][0][3][1],
                )
            ):
                cubes[cube_index_compare][5] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][0] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

            elif (
                cubes[cube_index][1] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][3] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][3][0][0] < cubes[cube_index][1][0][0]
                and (
                    cubes[cube_index_compare][3][0][1],
                    cubes[cube_index_compare][3][0][2],
                    cubes[cube_index_compare][3][1][1],
                    cubes[cube_index_compare][3][1][2],
                    cubes[cube_index_compare][3][2][1],
                    cubes[cube_index_compare][3][2][2],
                    cubes[cube_index_compare][3][3][1],
                    cubes[cube_index_compare][3][3][2],
                )
                == (
                    cubes[cube_index][1][0][1],
                    cubes[cube_index][1][0][2],
                    cubes[cube_index][1][1][1],
                    cubes[cube_index][1][1][2],
                    cubes[cube_index][1][2][1],
                    cubes[cube_index][1][2][2],
                    cubes[cube_index][1][3][1],
                    cubes[cube_index][1][3][2],
                )
            ):
                cubes[cube_index_compare][3] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][1] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

            elif (
                cubes[cube_index][2] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][4] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][4][0][1] < cubes[cube_index][2][0][1]
                and (
                    cubes[cube_index_compare][4][0][0],
                    cubes[cube_index_compare][4][0][2],
                    cubes[cube_index_compare][4][1][0],
                    cubes[cube_index_compare][4][1][2],
                    cubes[cube_index_compare][4][2][0],
                    cubes[cube_index_compare][4][2][2],
                    cubes[cube_index_compare][4][3][0],
                    cubes[cube_index_compare][4][3][2],
                )
                == (
                    cubes[cube_index][2][0][0],
                    cubes[cube_index][2][0][2],
                    cubes[cube_index][2][1][0],
                    cubes[cube_index][2][1][2],
                    cubes[cube_index][2][2][0],
                    cubes[cube_index][2][2][2],
                    cubes[cube_index][2][3][0],
                    cubes[cube_index][2][3][2],
                )
            ):
                cubes[cube_index_compare][4] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][2] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

            elif (
                cubes[cube_index][3] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][1] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][1][0][0] > cubes[cube_index][3][0][0]
                and (
                    cubes[cube_index_compare][1][0][1],
                    cubes[cube_index_compare][1][0][2],
                    cubes[cube_index_compare][1][1][1],
                    cubes[cube_index_compare][1][1][2],
                    cubes[cube_index_compare][1][2][1],
                    cubes[cube_index_compare][1][2][2],
                    cubes[cube_index_compare][1][3][1],
                    cubes[cube_index_compare][1][3][2],
                )
                == (
                    cubes[cube_index][3][0][1],
                    cubes[cube_index][3][0][2],
                    cubes[cube_index][3][1][1],
                    cubes[cube_index][3][1][2],
                    cubes[cube_index][3][2][1],
                    cubes[cube_index][3][2][2],
                    cubes[cube_index][3][3][1],
                    cubes[cube_index][3][3][2],
                )
            ):
                cubes[cube_index_compare][1] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][3] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

            elif (
                cubes[cube_index][4] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][2] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][2][0][1] > cubes[cube_index][4][0][1]
                and (
                    cubes[cube_index_compare][2][0][0],
                    cubes[cube_index_compare][2][0][2],
                    cubes[cube_index_compare][2][1][0],
                    cubes[cube_index_compare][2][1][2],
                    cubes[cube_index_compare][2][2][0],
                    cubes[cube_index_compare][2][2][2],
                    cubes[cube_index_compare][2][3][0],
                    cubes[cube_index_compare][2][3][2],
                )
                == (
                    cubes[cube_index][4][0][0],
                    cubes[cube_index][4][0][2],
                    cubes[cube_index][4][1][0],
                    cubes[cube_index][4][1][2],
                    cubes[cube_index][4][2][0],
                    cubes[cube_index][4][2][2],
                    cubes[cube_index][4][3][0],
                    cubes[cube_index][4][3][2],
                )
            ):
                cubes[cube_index_compare][2] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][4] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

            elif (
                cubes[cube_index][5] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][0] != (("-"), ("-"), ("-"), ("-"))
                and cubes[cube_index_compare][0][0][2] > cubes[cube_index][5][0][2]
                and (
                    cubes[cube_index_compare][0][0][0],
                    cubes[cube_index_compare][0][0][1],
                    cubes[cube_index_compare][0][1][0],
                    cubes[cube_index_compare][0][1][1],
                    cubes[cube_index_compare][0][2][0],
                    cubes[cube_index_compare][0][2][1],
                    cubes[cube_index_compare][0][3][0],
                    cubes[cube_index_compare][0][3][1],
                )
                == (
                    cubes[cube_index][5][0][0],
                    cubes[cube_index][5][0][1],
                    cubes[cube_index][5][1][0],
                    cubes[cube_index][5][1][1],
                    cubes[cube_index][5][2][0],
                    cubes[cube_index][5][2][1],
                    cubes[cube_index][5][3][0],
                    cubes[cube_index][5][3][1],
                )
            ):
                cubes[cube_index_compare][0] = (("-"), ("-"), ("-"), ("-"))
                cubes[cube_index][5] = (("-"), ("-"), ("-"), ("-"))
                total_uncovered -= 2

    # total_uncovered += len(
    #     [f for f in cubes[cube_index] if f != (("-"), ("-"), ("-"), ("-"))]
    # )

    print(cubes[cube_index], total_uncovered)
print("{0}{1} - Part 2 answer : {2}".format(year, day, 0))
