# test out how to reference the new dictionary to a winning card

import pdb



print ("poo")

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Nine':1, 'Ten':2, 'Jack':3, 'Queen':4, 'King':5, 'Ace':6, 'tNine':7, 'tTen':8, 'tJick':12, 'tJack':13, 'tQueen': 9, 'tKing': 10, 'tAce':11}
colors = {"Hearts":"red", "Diamonds":"red", "Clubs":"black", "Spades":"black"}
table_position_dict_default = {'chair_1':'pc South', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'}

trump_card_list = []
whats_trump = "Hearts"

def the_trump_card_list(trump_card_list, whats_trump):
    for suit in suits:
        for rank in ranks:
            trump_card_list.append([rank,suit])

    for card in trump_card_list:
        if card[1] == whats_trump:
            trank = 't' + card[0]
            value = values[trank]
            card.append(value)

        elif card_is_left_bower(card,whats_trump):
            value = values['tJick']
            card.append(value)
        else:
            value = values[card[0]]
            card.append(value)

grass = "green"

def card_is_left_bower(card,trump):
    trump_color = colors[trump]
    if card[0] == "Jack" and colors[card[1]] == trump_color:
        return True
    else:
        return False

tea = "grey"
the_trump_card_list(trump_card_list, whats_trump)
print (trump_card_list)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]


    def make_rank_trump(self,jick = False):
        if jick == True:
            old_rank = self.rank
            self.rank = "Jick"
            trump_rank = "t" + self.rank
            self.rank = trump_rank
            print (f"old rank was {old_rank} of {self.suit}")
            print (f"new rank is {trump_rank} of {whats_trump}")
            self.value = values[self.rank]
            self.suit = whats_trump           
        else:
            old_rank = self.rank
            trump_rank = "t" + old_rank
            self.rank = trump_rank
            print (f"old rank was {old_rank} of {self.suit}") 
            print (f"new rank is {trump_rank} of {card.suit}")
            self.value = values[self.rank]



card_object1 = Card("Jack", "Hearts")
card_object2 = Card("Jack", "Diamonds")
card_object3 = Card("Ace", "Spades")
print (card_object1.value)
print (card_object2.value)
print (card_object3.value)


# Ok, now, who won? 
# I need to give the cards a value

# card_object1.make_rank_trump()
trump_color = colors[whats_trump]

table_list = [["chair_1",card_object2],["chair_2",card_object1],["chair_3",card_object3]]

for card_played in table_list:
    card = card_played[1]
    if card.suit == whats_trump:
        card.make_rank_trump()
    if card.rank == "Jack" and colors[card.suit] == trump_color and card.suit != whats_trump:
        card.make_rank_trump(True)



    
print (card_object1.rank)
print (card_object2.rank)
print (card_object3.rank)

print (card_object1.value)
print (card_object2.value)
print (card_object3.value)

# 

# def whos_winning(table_list):
#     card_value_list
#     for chair_card in table_list:

winning_value = max(table_list, key=lambda x: x[1].value)
print (winning_value)

# now value is the 2nd position in the table_list
# looks like ["chair_1",card_object1, actual_value]

# to see who won, look through the list with lamda fun
# and then print the 0th position

cards_in_hand = [card_object1,card_object2,card_object3]

# 3 cards are H,D,S then H,H,S, no clubs
suit_to_follow = "Hearts"

cards_of_suit_to_follow = list(filter(lambda x: x.suit == suit_to_follow, cards_in_hand))

print ("here's the list version")
if cards_of_suit_to_follow == []:
    print ("cards_of_suit_to_follow is empty list")
else:
    print (len(cards_of_suit_to_follow))
    for card in cards_of_suit_to_follow:
        print (card.rank) 
        print (card.suit)
        

# has_suit_to_follow = bool(lambda card: False if card.suit != suit_to_follow)
# print ("here's the true and false version")

doesnt_have_any_of_suit = any(card.suit != suit_to_follow for card in cards_in_hand)

print (doesnt_have_any_of_suit)

winning_number_to_beat = 12

cards_that_beat_it = list(filter(lambda x: x.value > winning_number_to_beat, cards_in_hand))

print (cards_that_beat_it)



# any card in hand of .suit trump 

trump_cards_in_hand = list(filter(lambda x: x.suit == whats_trump, cards_in_hand))

print (trump_cards_in_hand)


team_ns = ["chair_1","chair_3"]
team_ew = ["chair_2","chair_4"]

# if pc is chair 2 how do I test if winning chair is their partner

# is winner_chair on same team
# this pc's team is 
pc_chair = "chair_2"






pdb.set_trace()
# highest_value = max(key = lambda card.rank: values[card.rank])


