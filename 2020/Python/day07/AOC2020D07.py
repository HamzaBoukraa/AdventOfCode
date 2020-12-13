year = '2020'
day = '07'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    bags = [[rule.split(' contain ')[0],[[b[b.find(' '):].strip(),b[:b.find(' ')].strip()] for b in [r.strip() for r in rule.split(' contain ')[1].split(',')]]] for rule in [raw_rule for raw_rule in sorted(reader.read().replace('bags', 'bag').replace('.', '').replace('no other', '0 other').split('\n'))]]

empty_bag = 'other bag'
my_bag = 'shiny gold bag'
my_bag = 'dark blue bag'
# my_bag = 'dark green bag'

# Part 1 :
bags_list = []
added_bags = 1
while added_bags > 0:
    added_bags = 0

    for bag in bags:
        for contained in bag[1]:
            if (contained[0] in bags_list or contained[0] == my_bag) and not (bag[0] in bags_list):
                bags_list += [bag[0]]
                added_bags += 1
print('Part 1 answer :', len(bags_list))

# Part 2 :
def number_of_bags(multiplier, requested_bag):
    for bag in [bag_candidate for bag_candidate in bags if bag_candidate[0] == requested_bag]:
        for contained_bag in bag[1]:
            print(bag[0], contained_bag[1])

    # if requested_bag == empty_bag:
    #     print('empty bag')
    #     return 0
    # else:
    #     for bag in [bag_candidate for bag_candidate in bags if bag_candidate[0] == requested_bag]:
    #         bags_count = 1
    #         for contained_bag in bag[1]:
    #             # print(contained_bag[1], contained_bag[0])
    #             print(multiplier * int(contained_bag[1]), contained_bag[0])
    #             bags_count += multiplier * number_of_bags(int(contained_bag[1]), contained_bag[0])
    #         print(bags_count, bag[0])
    #     return bags_count

number_of_bags(1, my_bag)
