x=[['32T3K',765],['T55J5',684],['KK677',28],['KTJJT',220],['QQQJA',483]]

VK= []
IVK = []
FH = []
IIVK = []
TP = []
OP = []
HC = []
types = [VK,IVK,FH,IIVK,TP,OP,HC]
names = ['VK','IVK','FH','IIVK','TP','OP','HC']

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

def sort_by_value(hands_list):
 values =['A','K','Q','J','T','9','8','7','6','5','4','3','2']
 return sorted(hands_list, key=lambda x: values.index(x[0][0]))


for place, data in enumerate(x):
    hand = data[0]
    bet = data[1]
    hand_type = get_hand_type(hand)
  
    if hand_type == 'Five of a Kind':
        VK.append([hand,bet])
    elif hand_type == 'Four of a Kind':
        IVK.append([hand,bet])
    elif hand_type == 'Full House':
        FH.append([hand,bet])
    elif hand_type == 'Three of a Kind':
        IIVK.append([hand,bet])
    elif hand_type == 'Two Pairs':
        TP.append([hand,bet])
    elif hand_type == 'One Pair':
        OP.append([hand,bet])
    else:
        HC.append([hand,bet])


for place,hand_type in enumerate(types):
  types[place] = sort_by_value(hand_type)
  print(names[place],':',types[place])

