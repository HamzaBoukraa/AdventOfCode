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
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')]

reports = [[int(level) for level in report.split()] for report in puzzle_input]

def test_report_safety_part_1(report):
    report_direction = "init"
    report_status = "safe"

    for level_index in range(len(report) - 1):
        if level_index == 0:
            if report[level_index] < report[level_index + 1]:
                report_direction = "increase"
            elif report[level_index] > report[level_index + 1]:
                report_direction = "decrease"
            else:
                report_status = "unsafe"

        if (report_status != "unsafe") and \
            (((report_direction == "increase") and ((report[level_index] >= report[level_index + 1]) or ((report[level_index] + 3) < report[level_index + 1]))) \
                or ((report_direction == "decrease") and ((report[level_index] <= report[level_index + 1]) or ((report[level_index] - 3) > report[level_index + 1])))):
                    report_status = "unsafe"

    return report_status


def test_report_safety_part_2(report):
    report_status = test_report_safety_part_1(report)

    level_to_remove = 0
    while report_status != "safe" and level_to_remove < len(report):
        subreport = copy.deepcopy(report)
        subreport.pop(level_to_remove)
        report_status = test_report_safety_part_1(subreport)
        level_to_remove += 1

    return report_status


def part_1():
    safe_reports = 0
    for report in reports:
        report_status = test_report_safety_part_1(report)

        if report_status == "safe":
            safe_reports += 1

    return safe_reports

def part_2():
    safe_reports = 0
    for report in reports:
        report_status = test_report_safety_part_2(report)

        if report_status == "safe":
            safe_reports += 1

    return safe_reports


if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
