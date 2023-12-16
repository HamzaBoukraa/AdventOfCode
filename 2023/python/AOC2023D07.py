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

hands = [[h[0], int(h[1])] for h in [c.split() for c in puzzle_input]]

cards_value_part1 ={'A' : 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,'2': 2}
cards_value_part2 ={'A' : 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,'2': 2}

def get_hand_power(hand, with_joker):
    cards = [c for c in hand]
    unique_cards = list(set(cards))
    tc = [[unique_cards[c], len([ci for ci in cards if ci == unique_cards[c]])] for c in range(len(unique_cards))]
    
    if len(unique_cards) == 1 \
        or (len(unique_cards) == 2 and with_joker and 'J' in unique_cards):
        return 6 # Five of a kind
    elif (len(unique_cards) == 2 and len([t for t in tc if t[1] == 4]) > 0) \
        or (len(unique_cards) == 3 and with_joker and 'J' in unique_cards and ((len([t for t in tc if t[1] == 3]) > 0) or (len([t for t in tc if t[0] == 'J' and t[1] == 2]) > 0))):
        return 5 # Four of a kind
    elif (len(unique_cards) == 2) \
        or (len(unique_cards) == 3 and with_joker and 'J' in unique_cards):
        return 4 # Full house
    elif (len(unique_cards) == 3 and len([t for t in tc if t[1] == 3]) > 0) \
        or (len(unique_cards) == 4 and with_joker and 'J' in unique_cards):
        return 3 # Three of a kind
    elif (len(unique_cards) == 3):
        return 2 # Two pairs
    elif (len(unique_cards) == 4) \
        or (with_joker and 'J' in unique_cards):
        return 1 # One pair
    else:
        return 0 # High card

def compare_hands(h1, h2, with_joker, cards_value):
    h1_power = get_hand_power(h1, with_joker)
    h2_power = get_hand_power(h2, with_joker)
    if h1_power > h2_power:
        return 1
    elif h1_power < h2_power:
        return -1
    else:
        c = 0
        while c < 5:
            cv1 = cards_value[h1[c]]
            cv2 = cards_value[h2[c]]
            if cv1 > cv2:
                return 1
            elif cv1 < cv2:
                return -1
            c+= 1
        return 0

def sort_hands(with_joker):
    if not with_joker:
        cards_value = cards_value_part1
    else:
        cards_value = cards_value_part2

    for h1 in range(len(hands) - 1):
        for h in range(h1 + 1, len(hands)):
            if compare_hands(hands[h1][0], hands[h][0], with_joker, cards_value) > 0:
                hands[h1], hands[h] = hands[h], hands[h1]

def part_1():
    sort_hands(with_joker=False)
    return sum([(h + 1) * hands[h][1] for h in range(len(hands))])

def part_2():
    sort_hands(with_joker=True)
    return sum([(h + 1) * hands[h][1] for h in range(len(hands))])

if __name__ == '__main__':
    print('{0}{1} - Part 1 answer : {2}'.format(year, day, part_1()))
    print('{0}{1} - Part 2 answer : {2}'.format(year, day, part_2()))
