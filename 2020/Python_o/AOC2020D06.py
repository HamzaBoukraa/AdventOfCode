year = '2020'
day = '06'

with open('..\..\Input\day{1}\AOC{0}D{1}_input.txt'.format(year, day), 'r') as reader:
    groups_answers = [group_answers for group_answers in reader.read().split('\n\n')]

# Part 1 :
print('Part 1 answer :', sum([len(sorted(set(group_answers.replace('\n', '')))) for group_answers in groups_answers]))

# Part 2 :
sum_common_answers = 0
for groups_answers in [[set(sorted(person_answers)) for person_answers in groups_answers[group_number].split('\n')] for group_number in range(len(groups_answers))]:
    common_answers = groups_answers[0]
    for person_answers in groups_answers:
        common_answers = person_answers & common_answers
    sum_common_answers += len(common_answers)

print('Part 2 answer :', sum_common_answers)
