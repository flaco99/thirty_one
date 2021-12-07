# Naomi Weissberg
# Created: nov 16, 2021
# card game: thirty one

import random

#########################################################
# returns a pretty string representing a card
#########################################################
def pretty_card(c):
    pretty_suits = {'spades':'♠', 'clubs':'♣', 'hearts':'♥', 'diamonds':'♦'}
    pretty_suit = pretty_suits[c[1]]
    new_card = f'|{c[0]}{pretty_suit}| '
    return new_card

#########################################################
# calculate and returns a player's current score
#########################################################
def get_score(player_handV):
    scores = {'spades':0, 'clubs':0, 'hearts':0, 'diamonds':0, 'threes':0}
    nums = []
    for n in range(1,len(player_handV)):
        num = player_handV[n][0]
        nums.append(num)
        if num == 'A':
            num_value = 11
        elif num in 'JQK':
            num_value = 10
        else:
            num_value = int(num)
        suit = player_handV[n][1]
        scores[suit] += num_value
    if (nums[0] == nums[1]) and (nums[0] == nums[2]):
        scores['threes'] = 30
    return max(scores.values())

#########################################################
# figures out who won and returns the player as a list
#########################################################
def find_winner(players):
    players_scores = {}
    for P in players:
        players_scores[get_score(P)] = P
    highest_score = max(players_scores.keys())
    winner = players_scores.get(highest_score)
    return winner

#########################################################
# shuffles the discard pile and adds it to the deck
#########################################################
def refill(deckV, open_pileV):
    if len(deckV) == 0:
        top_open_card = open_pileV.pop(-1)
        random.shuffle(open_pileV)
        deckV += open_pileV
        open_pileV = top_open_card
    return (deckV, open_pileV)

#########################################################
# checks if a player has 31 points
#########################################################
def check_thirtyone(player):
    score = get_score(player)
    if score == 31:
        return True
    else:
        return False


#########################################################
# Main code; thirty one (without chips)
#########################################################

# initialize the suits and labels
suits = ["clubs", "diamonds", "hearts", "spades"]
labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# populate the deck
deck = []
for suit in suits:
    for label in labels:
        deck.append([label, suit])

# shuffle the deck
random.shuffle(deck)

# print the rules / objective of the game
print('THIRTY ONE GAME - RULES / OBJECTIVE'
      '\n'
      '\nThe objective of the game is to get thirty one points.'
      '\nThe sum of the digits of your cards is the number of points that you have.'
      '\n(Ace is worth 11 points, and all face cards are worth 10 points.)'
      '\n(Also, if all three of your cards have the same label (example: 2 clubs, 2 spades, 2 hearts), it counts as 30 points.)'
      '\n'
      '\nEveryone starts and ends with exactly three cards each.'
      '\nWhen you start your turn, you have three options.'
      '\n1: take a card from the deck'
      '\n2: take the top card from the discard pile (the cards in this pile are faced up so everyone can see it)'
      '\n3: knock (if you knock, your turn is over, and then everyone else gets to play one last turn. '
      '\nThen, everyone reveals their cards and the player with the most points wins. Once someone has knock, no one else can knock.)'
      '\nAfter you take a card, you have to get rid of one card from your hand. It goes faced up on the top of the discard pile.'
      '\nThen your turn is over and the next person plays.'
      '\n'
      '\nThis repeats until someone knocks or gets thirty one points.'
      '\nIf anyone gets thirty one points at any point in the game, they win.'
      '\n'
      '\nOK then good luck!'
      '\n')

# get the number of players (p)
p = 0
while p < 2:
    p = int(input("How many players? "))
# set up p players, each with a hand of n cards - value 0 for now
hands = []
for i in range(1,p+1):
    hand = []
    #put in player name
    hand.append("Player "+str(i))
    for j in range(1, 4):
        hand.append(0)
    hands.append(hand)

# deal out the p hands with 3 cards each, handing one card at a time to each player
for i in range (0, 3):
    for j in range (0, p):
        #take card off top of deck, deal to each player
        card = deck.pop(0)
        hands[j][i+1] = card


# the top card on the deck is opened
open_pile = []
open_pile.append(deck.pop(0))
top_open_card = open_pile[-1]
pretty_toc = pretty_card(top_open_card)
print('current open card:', pretty_toc)

# initialize the variables
num_players = p
knocked = False
knocked_player_num = -1
thirtyone = False
current_player_num = 0

while thirtyone is False:

    # decide on who's turn it is
    current_player_num = (current_player_num % num_players) + 1
    # when it is PlayerX's turn, current_player_num equals X.
    current_player = hands[current_player_num - 1]


    # make sure to exit the while loop and end the game so that the player who has knocked doesn't play again
    if knocked and current_player_num == knocked_player_num:
        break

    # play a turn

    # set up turn

    # check if the deck is empty, and refill it (with discard pile) if necessary
    (deck, open_pile) = refill(deck, open_pile)


    # start turn (tell the player how many points they have currently)
    print('\n' + current_player[0] + ", it's your turn.")
    pretty_hand = ''
    for c in current_player[1:]:
        pretty_hand += pretty_card(c)
    print('This is your hand:', pretty_hand)
    # tell the player his/her current score
    score = get_score(current_player)
    print('You have', score, 'points.')


    # check if the player has 31. (if yes, exit the while loop)
    # despite how rare it is, the player might have 31 points to begin with.
    hold_thirtyone = check_thirtyone(current_player)
    thirtyone = hold_thirtyone


    # player takes a card (or knocks)
    choice = '0'
    top_open_card = open_pile[-1]
    pretty_toc = pretty_card(top_open_card)
    while choice not in '123':
        if not knocked:
            choice = input('Would you like to pick the open card ' + pretty_toc +
                           '(enter "1"), pick a random card from the deck (enter "2"), or knock (enter "3")? ')
        else:
            choice = input('Would you like to pick the open card ' + pretty_toc +
                           '(enter "1") or pick a random card from the deck (enter "2")? ')
    if choice == '1':  # the player chose to pick the open card from the discard pile
        card = open_pile.pop(-1)
        current_player.append(card)
    elif choice == '2':  # the player chose to pick a random card from the deck
        card = deck.pop(-1)
        current_player.append(card)
        pc = pretty_card(card)
        print('You drew ' + pc)
    elif choice == '3':  # the player chose to knock
        knocked = True
        knocked_player_num = current_player_num
        print(current_player[0], 'has knocked. The final round starts now.')
        continue


    # make the player discard one card from their hand and add the card to the discard pile
    print('Now you must discard one card from your hand. Which card would you like to discard? \noptions:')
    for card_number in range(1, 5):
        pc = pretty_card(current_player[card_number])
        print(str(card_number) + ': ' + pc)
    discard_choice = ''
    while discard_choice not in ('1', '2', '3', '4'):
        discard_choice = input('Enter "1", "2", "3" or "4": ')
    # remove the discard_choice from the player's hand
    discard_card = current_player.pop(int(discard_choice))
    # add the discard card to the discard pile (open cards pile)
    open_pile.append(discard_card)
    # print the open card at the end of each turn
    pdc = pretty_card(discard_card)
    print(current_player[0], 'has discarded', pdc)


    # check if the player has 31. (if yes, exit the while loop)
    hold_thirtyone = check_thirtyone(current_player)
    thirtyone = hold_thirtyone


    # tell the player how many points they have currently
    score = get_score(current_player)
    print(current_player[0], 'you have completed your turn. You have', score, 'points.')


# Determine the winner and end the game
winner = find_winner(hands)
print('\n')
print(winner[0], 'wins!')
# reveal everyone's scores
for player in hands:
    score = get_score(player)
    print(player[0] + ': ' + str(score) + ' points')
