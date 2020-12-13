with open('AOC2020D05_input.txt', 'r') as reader:
    seats = [int(s[:-3], 2) * 8 + int(s[-3:], 2) for s in [seat.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0') for seat in reader.read().split('\n')]]

# Part 1 :
print(max(seats))

# Part 2 :
print('Missing seat is :', [s for s in range(min(seats), max(seats)) if s not in seats])
