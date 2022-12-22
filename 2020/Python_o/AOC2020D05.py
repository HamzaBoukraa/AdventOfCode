year = '2020'
day = '05'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    seats = [int(s[:-3], 2) * 8 + int(s[-3:], 2) for s in [seat.strip().replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0') for seat in reader.read().split('\n')]]

# Part 1 :
print('Part 1 answer :', max(seats))

# Part 2 :
print('Part 2 answer :', [s for s in range(min(seats), max(seats)) if s not in seats][0])
