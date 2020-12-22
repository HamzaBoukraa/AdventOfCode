year = '2020'
day = '08'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    puzzle_input = [input_line for input_line in reader.read().split('\n')]

steps_part1 = [0 for s in range(len(puzzle_input))]

def process_step(program, step, accumulator, steps):
    if step < len(program) and step < len(steps) and steps[step] == 0:
        # print(step, program[step], accumulator)
        steps[step] += 1
        instruction = program[step].split(' ')
        if instruction[0] == 'nop':
            return process_step(program, step + 1, accumulator, steps)
        elif instruction[0] == 'acc':
            return process_step(program, step + 1, accumulator + int(instruction[1]), steps)
        elif instruction[0] == 'jmp':
            return process_step(program, step + int(instruction[1]), accumulator, steps)
    else:
        if step >= len(program):
            # print('End Reached :', step)
            return (accumulator, False, step) 
        else:
            # print('Already visited :', step, program[step])
            return (accumulator, True, step, program[step]) 

# Part 1 :
print('Part 1 answer :', process_step(puzzle_input, 0, 0, steps_part1)[0])

# Part 2 :
last_changed_index = -1
step = 0
cyclic_loop = True

while cyclic_loop and step < len(puzzle_input): 
    puzzle_input_copy = puzzle_input.copy()
    steps_part2 = [0 for s in range(len(puzzle_input_copy))]
    instruction = puzzle_input_copy[step].split(' ')
    if instruction[0] == 'nop' or instruction[0] == 'jmp':
        if instruction[0] == 'nop':
            puzzle_input_copy[step] = 'jmp ' + instruction[1]
        elif instruction[0] == 'jmp':
            puzzle_input_copy[step] = 'nop ' + instruction[1]

        processing_results = process_step(puzzle_input_copy, 0, 0, steps_part2)
        cyclic_loop = processing_results[1]
    step += 1
print('Part 2 answer :', processing_results[0])
