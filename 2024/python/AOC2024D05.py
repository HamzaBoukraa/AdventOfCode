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

order_rules = [[int(r) for r in p.split('|')] for p in puzzle_input if '|' in p]
page_orders = [[int(r) for r in p.split(',')] for p in puzzle_input if ',' in p]

def check_validity(pages):
    first_page_index = 0
    valid = True
    while first_page_index < len(pages) - 1 and valid == True:
        second_page_index = first_page_index + 1
        while second_page_index < len(pages) and valid == True:
            rules = [r for r in order_rules if pages[first_page_index] in r and pages[second_page_index] in r][0]
            if len(rules) > 0:
                if pages[first_page_index] != rules[0] or pages[second_page_index] != rules[1]:
                    valid = False
            second_page_index +=1
        first_page_index += 1
    
    return valid

def part_1(pages_list):
    ordered_pages = []
    unordered_pages = []
    printed_pages=0
    for pages_index in range(len(pages_list)):
        pages = pages_list[pages_index]

        validity = check_validity(pages)

        if validity:
            ordered_pages += [pages]
            middle_page=pages[int(len(pages)//2)]
            printed_pages+=middle_page
        else:
            unordered_pages += [pages]
            
    return printed_pages, ordered_pages, unordered_pages

def part_2(pages_list):
    printed_pages=0
    for pages_index in range(len(pages_list)):
        pages = pages_list[pages_index]

        validity = check_validity(pages)

        while validity == False:
            first_page_index = 0
            while first_page_index < len(pages) - 1 and validity == False:
                second_page_index = first_page_index + 1
                while second_page_index < len(pages) and validity == False:
                    rules = [r for r in order_rules if pages[first_page_index] in r and pages[second_page_index] in r][0]
                    if len(rules) > 0:
                        if pages[first_page_index] != rules[0] or pages[second_page_index] != rules[1]:
                            pages_list[pages_index][first_page_index],pages_list[pages_index][second_page_index]=pages_list[pages_index][second_page_index],pages_list[pages_index][first_page_index]
                            validity = check_validity(pages)
                    second_page_index +=1
                first_page_index += 1

            
        if validity:
            middle_page=pages_list[pages_index][int(len(pages_list[pages_index])//2)]
            printed_pages+=middle_page

    return printed_pages

if __name__ == '__main__':
    part_1_answer = part_1(page_orders)
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1_answer[0]))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2(part_1_answer[2])))
