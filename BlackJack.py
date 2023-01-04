import random

print("Hi, welcome to my first python game, it's called BLACKJACK!")
print("Please add your name:")
player1 = input()
print("Okay, " + player1 + ", let's play a game against the computer: ")


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
player_hand = []
dealer_hand = []
playerIn = True
dealerIn = True

def dealCard(turn):
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)

def total(turn):
    total = 0
    face = ["J", "K", "Q"]
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

def revealDealerHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

for i in range(2):
    dealCard(player_hand)
    dealCard(dealer_hand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealer_hand) > 16:
        dealerIn = False
    else:
        dealCard(dealer_hand)
    if stayOrHit == "1":
        playerIn = False
    else:
        dealCard(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

if total(player_hand) == 21:
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Blackjack! You win!")
elif total(dealer_hand) == 21:
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Blackjack! Dealer wins!")
elif total(player_hand) > 21:
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You bust! Dealer wins!")
elif total(dealer_hand) > 21:
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer busts! You win!")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer wins!")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\n You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You win!")
