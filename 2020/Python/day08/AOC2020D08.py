year = '2020'
day = '08'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input = [[instruction[0], instruction[1]] for instruction.split(' ') in [input_line for input_line in reader.read().split('\n')]]

steps_part1 = [0 for s in range(len(puzzle_input))]

def process_step(program, step, accumulator, steps):
    if steps[step] == 0:
        print(step, program[step])
        steps[step] += 1
        instruction = program[step].split(' ')
        if instruction[0] == 'nop':
            return process_step(program, step + 1, accumulator, steps)
        elif instruction[0] == 'acc':
            return process_step(program, step + 1, accumulator + int(instruction[1]), steps)
        elif instruction[0] == 'jmp':
            return process_step(program, step + int(instruction[1]), accumulator, steps)
    else:
        print('Already visited :', step, program[step])
        return accumulator

# Part 1 :
print('Part 1 answer :', process_step(puzzle_input, 0, 0, steps_part1))

steps_part2 = [0 for s in range(len(puzzle_input))]

# Part 2 :
print('Part 2 answer :', process_step(puzzle_input, 0, 0, steps_part2))
