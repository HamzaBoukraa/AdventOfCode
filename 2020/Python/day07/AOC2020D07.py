year = '2020'
day = '07'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    bags = [[rule.split(' contain ')[0],[[b[b.find(' '):].strip(),b[:b.find(' ')].strip()] for b in [r.strip() for r in rule.split(' contain ')[1].split(',')]]] for rule in [raw_rule for raw_rule in sorted(reader.read().replace('bags', 'bag').replace('.', '').replace('no other', '0 other').split('\n'))]]

empty_bag = 'other bag'
my_bag = 'shiny gold bag'

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
def number_of_bags(multiplier, requested_bag, level):
    for bag in [bag_candidate for bag_candidate in bags if bag_candidate[0] == requested_bag]:
        bags_count = 0
        for contained_bag in bag[1]:
            if contained_bag[0] == empty_bag:
                return multiplier
            else:
                bags_count += multiplier * number_of_bags(int(contained_bag[1]), contained_bag[0], level + 1)
        return bags_count + multiplier
print('Part 2 answer :', number_of_bags(1, my_bag, 1) - 1)
