hand_types = {
     "five of a kind": 7,
     "four of a kind": 6,
     "full house": 5,
     "three of a kind": 4,
     "two pair": 3,
     "one pair": 2,
     "high card": 1
}
card_weights = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "J" : 1
}

def Sort(sub_li, index):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][index] > sub_li[j + 1][index]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
     
    return sub_li


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    hands = []
    for line in lines:
        hand = []
        split_line = line.strip().split(" ")
        hand.append(int(split_line[1]))

        three_of_a_kind = False
        pair = False
        second_pair = False
        saved_char = 0
        if "J" in split_line[0]:
            num_of_j = split_line[0].count("J")
            for c in split_line[0]:
                if c == "J" or c == saved_char:
                    continue
                num_of_c = split_line[0].count(c)
                if num_of_c + num_of_j == 5:
                    hand.append(hand_types["five of a kind"])
                    break
                if num_of_c + num_of_j == 4:
                    hand.append(hand_types["four of a kind"])
                    break
                if num_of_c == 2:
                    if pair:
                        hand.append(hand_types["full house"])
                        break
                    pair = True
                    saved_char = c
            if len(hand) == 1 and num_of_j == 5:
                hand.append(hand_types["five of a kind"])
            if len(hand) == 1 and pair:
                hand.append(hand_types["three of a kind"])
            if len(hand) == 1 and num_of_j == 2:
                hand.append(hand_types["three of a kind"])
            if len(hand) == 1:
                hand.append(hand_types["one pair"])
        else:
            for c in split_line[0]:
                if c == saved_char:
                    continue
                num_of_c = split_line[0].count(c)
                if num_of_c == 5:
                    hand.append(hand_types["five of a kind"])
                    break
                if num_of_c == 4:
                    hand.append(hand_types["four of a kind"])
                    break
                if num_of_c == 3:
                    if pair:
                        hand.append(hand_types["full house"])
                        break
                    three_of_a_kind = True
                    saved_char = c
                if num_of_c == 2:
                    if three_of_a_kind:
                        hand.append(hand_types["full house"])
                        break
                    if pair:
                        hand.append(hand_types["two pair"])
                        break
                    pair = True
                    saved_char = c
            if len(hand) == 1 and pair:
                hand.append(hand_types["one pair"])
            if len(hand) == 1 and three_of_a_kind:
                hand.append(hand_types["three of a kind"])
            if len(hand) == 1:
                hand.append(hand_types["high card"])
        for c in split_line[0]:
            hand.append(card_weights[c])
        hands.append(hand)
       
    for i in range(6, 0, -1):
        Sort(hands, i)
    
    print(hands)
    sum_num = 0
    for i in range(len(hands)):
        sum_num += hands[i][0] * (i+1)
    print(sum_num)
        
