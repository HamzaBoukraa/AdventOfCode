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

sensors_raw_inputs = [[[int(si) for si in sil.split()]] for sil in puzzle_input]
import copy

def part_1():
    sensors_inputs = copy.deepcopy(sensors_raw_inputs)
    for sensor_index in range(len(sensors_inputs)):
        sensor_inputs = sensors_inputs[sensor_index]
        while len([s for s in sensor_inputs[-1]]) != len([s for s in sensor_inputs[-1] if s == 0]):
            sensor_inputs += [[sensor_inputs[-1][si] - sensor_inputs[-1][si - 1] for si in range(1, len(sensor_inputs[-1]))]]
        sensor_inputs[-1] += [0]
        for l in range(2, len(sensor_inputs) + 1):
            ind = -1 * l
            sensor_inputs[ind] += [sensor_inputs[ind][-1] + sensor_inputs[ind + 1][-1]]
    return sum([s[0][-1] for s in sensors_inputs])

def part_2():
    sensors_inputs = copy.deepcopy(sensors_raw_inputs)
    for sensor_index in range(len(sensors_inputs)):
        sensor_inputs = sensors_inputs[-1*(sensor_index+1)]
        while len([s for s in sensor_inputs[-1]]) != len([s for s in sensor_inputs[-1] if s == 0]):
            sensor_inputs += [[sensor_inputs[-1][si] - sensor_inputs[-1][si - 1] for si in range(1, len(sensor_inputs[-1]))]]
        sensor_inputs[-1].insert(0, 0)
        for l in range(2, len(sensor_inputs) + 1):
            ind = -1 * l
            sensor_inputs[ind].insert(0, sensor_inputs[ind][0] - sensor_inputs[ind + 1][0])
    return sum([s[0][0] for s in sensors_inputs])


if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
