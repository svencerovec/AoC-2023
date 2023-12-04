class Card:
    def __init__(self, index, winning_numbers, card_numbers):
        self.index = index
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        first_match = True
        self.points = 0
        self.matches = 0
        for number in self.card_numbers:
            if number in self.winning_numbers and number.isdigit():
                self.matches += 1
                if first_match:
                    self.points += 1
                    first_match = False
                else:
                    self.points *= 2

def calculate_total_number_of_cards(index, cards, total_number_of_cards):
    if index < len(cards):
        total_number_of_cards += 1
        for i in range(1, cards[index].matches + 1):
            total_number_of_cards = calculate_total_number_of_cards(i + index, cards, total_number_of_cards)
    return total_number_of_cards


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    cards = []
    for line in lines:
        line = line.strip()
        line_split_by_colon = line.split(":")
        index = line_split_by_colon[0].split(" ")[1]
        numbers = line_split_by_colon[1].split("|")
        winning_numbers = numbers[0].strip(" ").split(" ")
        card_numbers = numbers[1].strip(" ").split(" ")
        cards.append(Card(index,winning_numbers, card_numbers))

    sum_of_points = 0

    for card in cards:
        sum_of_points += card.points

    total_cards = 0
    sum_of_cards = 0

    for card in cards:
        sum_of_cards += calculate_total_number_of_cards(cards.index(card), cards, 0)
    print(sum_of_cards)