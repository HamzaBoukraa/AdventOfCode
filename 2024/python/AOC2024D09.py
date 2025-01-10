from aocd import get_data
import os
import copy

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
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')][0]

file_blocks = []
file_id = 0
block_id = 0
for block in puzzle_input:
    if (block_id % 2) == 0:
        file_blocks += int(block) * [(len(file_blocks), str(file_id), int(block))]
        file_id += 1
    else:
        file_blocks += int(block) * [(len(file_blocks), '.', int(block))]
    block_id += 1
    
def part_1():
    block_format = copy.deepcopy(file_blocks)
    
    block_index = 0
    while block_index < len(block_format):
        # print(block_index, ''.join(block_format))
        # print(block_index, block_format[block_index])
        if block_format[block_index][1] == ".":
            exchange_block_index = len(block_format) - 1
            while exchange_block_index > block_index and block_format[exchange_block_index][1] == ".":
                exchange_block_index -= 1

            if exchange_block_index != block_index:
                # print(block_index, exchange_block_index, block_format[block_index], block_format[exchange_block_index])
                block_format[block_index],block_format[exchange_block_index] = block_format[exchange_block_index],block_format[block_index]
        block_index += 1

    checksum = 0
    block_index = 0
    while block_index < len(block_format) and block_format[block_index][1] != ".":
        if block_format[block_index][1] != ".":
            checksum += block_index * int(block_format[block_index][1])
            # print(block_index, checksum, block_format[block_index])
        block_index += 1

    return checksum

def part_2():
    block_format = copy.deepcopy(file_blocks)

    # last_file_id = max([int(p[1]) for p in block_format if p[1] != "."])
    # print(last_file_id)

    # while last_file_id > 0:
    #     block_to_move_index = min([i for i in range(len(block_format)) if block_format[i][1] == str(last_file_id)])
    #     block_size = [int(p[2]) for p in block_format if p[1] == str(last_file_id)][0]
    #     print(last_file_id, block_to_move_index, block_size)
        
    #     temp_block_size = 0        
    #     free_place_index = -1

    #     temp_free_block_index = 0
    #     while temp_free_block_index < block_to_move_index and free_place_index == -1:
    #         if block_format[temp_free_block_index][1] == ".":
    #             temp_block_size += 1
    #         else:
    #             temp_block_size = 0
            
    #         if temp_block_size == block_size:
    #             free_place_index = temp_free_block_index + 1 - block_size
    #         temp_free_block_index += 1
    #     if temp_free_block_index < block_to_move_index:
    #         for i in range(block_size):
    #             block_format[block_to_move_index + i], block_format[free_place_index + i] = block_format[free_place_index + i], block_format[block_to_move_index + i]
    #             # print(block_to_move_index, block_format[block_to_move_index])
    #     last_file_id -= 1

    checksum = 0
    # block_index = 0
    # while block_index < len(block_format):
    #     if block_format[block_index][1] != ".":
    #         checksum += block_index * int(block_format[block_index][1])
    #         # print(block_index, checksum, block_format[block_index])
    #     # print(block_format[block_index], block_index, checksum, ''.join([p[1] for p in block_format]))
    #     block_index += 1

    return checksum


if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
