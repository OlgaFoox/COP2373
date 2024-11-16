import random


class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]


# Functions to convert card number to rank and suit
def card_to_rank_suit(card):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    r = card % 13
    s = card // 13
    return ranks[r], suits[s]


def print_hand(hand):
    for card in hand:
        rank, suit = card_to_rank_suit(card)
        print(f"{rank} of {suit}")


def main():
    my_deck = Deck(52)

    # Deal initial hand of five cards
    hand = [my_deck.deal() for _ in range(5)]
    print("Your initial hand:")
    print_hand(hand)

    # Prompt user for which cards to replace
    replace_indices = input(
        "Enter the card numbers to replace (1-5, separated by commas, or 'no' to keep all): ").strip()

    if replace_indices.lower() != 'no':
        indices = [int(x) - 1 for x in replace_indices.split(",") if x.strip().isdigit() and 0 < int(x) <= 5]

        # Replace the selected cards
        for index in indices:
            hand[index] = my_deck.deal()

    # Print the final hand
    print("\nYour final hand after drawing:")
    print_hand(hand)


# Run the game
if __name__ == "__main__":
    main()
