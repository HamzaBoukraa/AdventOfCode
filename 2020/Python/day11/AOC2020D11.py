year = '2020'
day = '11'
suffix = ''
# suffix = '_1'

with open('..\..\Input\day{1}\AOC{0}D{1}_input{2}.txt'.format(year, day, suffix), 'r') as reader:
    puzzle_input = [input_line for input_line in reader.read().split('\n')]

# Part 1 :
new_seats = puzzle_input.copy()
seats = new_seats.copy()

def occupied_seats(seats):
    return sum([len([s for s in row if s == '#']) for row in seats])

def occupied_neighbor_seat(seats, row, seat, direction, radius):
    occupied = 0
    if radius > 0:
        if direction == 'north':
            if row > 0 and seats[row - 1][seat] == '#':
                occupied += 1
            elif row > 0 and seats[row - 1][seat] == '.':
                occupied += occupied_neighbor_seat(seats, row - 1, seat, direction, radius - 1)
        elif direction == 'south':
            if row < len(seats) - 1 and seats[row + 1][seat] == '#':
                occupied += 1
            elif row < len(seats) - 1 and seats[row + 1][seat] == '.':
                occupied += occupied_neighbor_seat(seats, row + 1, seat, direction, radius - 1)
        elif direction == 'east':
            if seat < len(seats[0]) - 1 and seats[row][seat + 1] == '#':
                occupied += 1
            elif seat < len(seats[0]) - 1 and seats[row][seat + 1] == '.':
                occupied += occupied_neighbor_seat(seats, row, seat + 1, direction, radius - 1)
        elif direction == 'west':
            if seat > 0 and seats[row][seat - 1] == '#':
                occupied += 1
            elif seat > 0 and seats[row][seat - 1] == '.':
                occupied += occupied_neighbor_seat(seats, row, seat - 1, direction, radius - 1)
        elif direction == 'northwest':
            if row > 0 and seat > 0 and seats[row - 1][seat - 1] == '#':
                occupied += 1
            elif row > 0 and seat > 0 and seats[row - 1][seat - 1] == '.':
                occupied += occupied_neighbor_seat(seats, row - 1, seat - 1, direction, radius - 1)
        elif direction == 'southwest':
            if row < len(seats) - 1 and seat > 0 and seats[row + 1][seat - 1] == '#':
                occupied += 1
            elif row < len(seats) - 1 and seat > 0 and seats[row + 1][seat - 1] == '.':
                occupied += occupied_neighbor_seat(seats, row + 1, seat - 1, direction, radius - 1)
        elif direction == 'northeast':
            if row > 0 and seat < len(seats[0]) - 1 and seats[row - 1][seat + 1] == '#':
                occupied += 1
            elif row > 0 and seat < len(seats[0]) - 1 and seats[row - 1][seat + 1] == '.':
                occupied += occupied_neighbor_seat(seats, row - 1, seat + 1, direction, radius - 1)
        elif direction == 'southeast':
            if row < len(seats) - 1 and seat < len(seats[0]) - 1 and seats[row + 1][seat + 1] == '#':
                occupied += 1
            elif row < len(seats) - 1 and seat < len(seats[0]) - 1 and seats[row + 1][seat + 1] == '.':
                occupied += occupied_neighbor_seat(seats, row + 1, seat + 1, direction, radius - 1)
    return occupied

def map(seats, occupied_neighbor_threshold, radius):
    unstable = True

    while unstable:
        changes = 0

        new_seats = seats.copy()

        max_row_coordinates = len(seats)
        max_seat_coordinates = len(seats[0])

        for r in range(max_row_coordinates):
            for c in range(max_seat_coordinates):
                neighbor_occupied_chairs = 0

                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'north', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'northwest', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'west', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'southwest', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'south', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'southeast', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'east', radius)
                neighbor_occupied_chairs += occupied_neighbor_seat(seats, r, c, 'northeast', radius)


                if seats[r][c] == 'L' and neighbor_occupied_chairs == 0:
                    new_seats[r] = new_seats[r][:c] + '#' + new_seats[r][c+1:]
                    changes += 1
                if seats[r][c] == '#' and neighbor_occupied_chairs >= occupied_neighbor_threshold:
                    new_seats[r] = new_seats[r][:c] + 'L' + new_seats[r][c+1:]
                    changes += 1

        seats = new_seats.copy()

        if changes == 0:
            unstable = False

    return occupied_seats(new_seats)


print('Part 1 answer :', map(seats, 4, 1))

# Part 2 :
print('Part 2 answer :', map(seats, 5, len(seats)))
