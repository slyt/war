# A probably shitty implementation of the Game of War
# Authors: Lauren Mancewicz & Taylor Sly

import random

def initialize_deck():
    # Build a deck
    deck = [2,3,4,5,6,7,8,9,10,'J', 'K', 'Q', 'A']
    suits = ["-<3", "-<>", "-%", "-^"] # Hearts, Diamons, Clubs, Spades
    full_deck = []
    for card_value in deck:
        for suit in suits:
            full_deck.append(str(card_value) + suit) # Append suit

    return full_deck

def draw_cards(deck, n):
    # TODO: Randomly generate indexes to remove from list
    deck_size = len(deck)
    hand=[]

    if n > deck_size: # Validation
        print("ERROR: Cannot draw more cards than the deck has!")
        return -1

    if deck_size <= 0:
        print("ERROR: Cannot draw cards from empty deck")
        return -1

    # TODO: Random draw n indexes
    for i in range(0,n):
        card_index = random.randint(0, deck_size-1) 
        card = deck.pop(card_index)
        deck_size = len(deck)
        #print(f"card_index:{card_index} Chosen card: {card}, len_deck: {len(deck)}")
        hand.append(card)
    return hand # deck SHOULD be modified?
    

def war(player_1_hand, player_2_hand):

    # TODO: Validate that each player has 4 cards left

    player_1_war_hand = draw_cards(player_1_hand, 4)
    player_2_war_hand = draw_cards(player_2_hand, 4)

    player_1_war_card = player_1_war_hand.pop(0)
    player_2_war_card = player_2_war_hand.pop(0)

    print(f"player 1 war card: {player_1_war_card}")
    print(f"player 2 war card: {player_2_war_card}")

    war_winner = int(input("Who won, p2 or p2?"))

    if war_winner == 1:
        player_1_hand.append(player_1_war_hand) # Get cards back
        player_1_hand.append(player_1_war_card)
        player_1_hand.append(player_2_war_hand)
        player_1_hand.append(player_2_war_card)
    elif war_winner == 2:
        player_2_hand.append(player_1_war_hand) 
        player_2_hand.append(player_1_war_card)
        player_2_hand.append(player_2_war_hand) # Get cards back
        player_2_hand.append(player_2_war_card)
    else:
        print("Error: Double-War not implemented.") # TODO: Call war recursively with deck size validation.
    pass


def main():
    deck = initialize_deck()
    player_1_hand = draw_cards(deck, (int(len(deck)/2)))
    player_2_hand = draw_cards(deck, (len(deck)))
    print(f"deck: {deck}")
    print(f"player_1_hand: {player_1_hand}")
    print(f"player_2_hand: {player_2_hand}")


    while True:
        print("Player 1 plays a card from their hand")
        player_1_card = player_1_hand.pop(0)
        print(f"player_1_card: {player_1_card}")
        input("Continue?...")

        print("Player 2 plays a card from their hand")
        player_2_card = player_2_hand.pop(0)
        print(f"player_2_card: {player_2_card}")
        #input("Continue?...")
        

        winner = int(input("Which player won? 1 or 2?"))
    

        if winner == 1:
            player_1_hand.append(player_2_card)
            player_1_hand.append(player_1_card)
        elif winner == 2: # Cards go to player 2
            player_2_hand.append(player_2_card)
            player_2_hand.append(player_1_card)
        else: # WAR!
            # Winner gets player_1_card and player_2_card
            print("XXX !WAR! XXX")
            war(player_1_hand, player_2_hand)

        print(f"Player 1 has {len(player_1_hand)} cards left, Player 2 has {len(player_2_hand)} cards left")
        print(f"player 1 hand: {player_1_hand}")
        print(f"player 2 hand: {player_2_hand}")
        print("-----------")

        if len(player_1_hand) <= 0:
            print("Player 2 WINS! <3 <3 * XO XO XO!!!") 
            print("Player 1 LOOOOSES!!!! :( !!! ")
            break
        if len(player_2_hand) <= 0:
            print("Player 1 WINS! <3 <3 * XO XO XO!!!") 
            print("Player 2 LOOOOSES!!!! :( !!! ")
            break



if __name__ == "__main__":
    main()
