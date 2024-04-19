x=[['32T3K',765],['T55J5',684],['KK677',28],['KTJJT',220],['QQQJA',483]]

VK= []
IVK = []
FH = []
IIVK = []
TP = []
OP = []
HC = []


def get_hand_type(hand):
    unique = set(hand)
    counts = []
    for letter in unique:
        counts.append(hand.count(letter))
    counts.sort(reverse=True)

    if counts[0] == 5:
        return 'Five of a Kind'
    elif counts[0] == 4:
        return 'Four of a Kind'
    elif counts[0] == 3 and counts[1] == 2:
        return 'Full House'
    elif counts[0] == 3:
        return 'Three of a Kind'
    elif counts.count(2) == 2:
        return 'Two Pairs'
    elif counts.count(2) == 1:
        return 'One Pair'
    else:
        return 'High Card'

for place, data in enumerate(x):
    hand = data[0]
    value = data[1]
    hand_type = get_hand_type(hand)
    print(hand, hand_type)
