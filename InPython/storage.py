
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Future goal: Deals must be dealt by going around the table twice 
    # giving everyone at least one card each time around   
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
    def put_back(self,card):
        self.deck.insert(0,card)
    

class Hand:
    
    def __init__(self,name):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.name = name
        self.color = ''
        
    def __str__(self):
        
        return self.name
    
    def add_card(self,card):
        self.cards.append(card)











        # # Game Execution

# # how_many_humans() -->table_positions()
# table_position_dict = how_many_humans()

# table_position_list = [] 

# for chair in table_position_dict:
#     table_position_list.append(chair)

# # CHECK print (f"Here's table position list {table_position_list}")
# print_teams(table_position_dict)

# dealers_turn = whos_first_dealer()
# print (f"dealer is, {dealers_turn}")
# # if I want to be first dealer then
# # first_dealer = 1, func makes random choice

# list_of_hand_objects = []

# for chair in table_position_list:
#     # CHECK print (f"here's chair: {chair}")
#     name = str(chair)
#     chair = Hand(name)
#     list_of_hand_objects.append(chair)
    
# # CHECK print ("Look here to check in list hand objects has stuff")
# # CHECK print (len(list_of_hand_objects))
    
# euchre_deck = Deck()
# print ("1")
# print (euchre_deck)
# euchre_deck.shuffle()
# print("2")
# print (euchre_deck)

# for player_hand in list_of_hand_objects:
#     deal_cards(player_hand,euchre_deck)
    
# for player_hand in list_of_hand_objects:
#     print (f"Cards in {player_hand}'s hand")
#     for card in player_hand.cards:
#         print (card)

# one_and_done_suit = top_card_suit(euchre_deck)

# #will it show top card? 








# Extra thought on player left of dealer function

# def left_of_dealer_plays_first_card():
#     # Check if PC is left of dealer
#     chair = dealer +1
#     if table_position_dict[chair] == "pc":
#         pass
#         # PC decision
#         # adds first card into played_cards[0].append
#     # Since not PC then human decision time!
#     else:
#         pass
#         #choose from hand a card to play.





# was used in pc_plays_a_card to make it print and to choose a random card

                random_position = random.randint(0,len(hand.cards)-1)
                print (f"random_position equals, {random_position}")
                card_to_play = hand.cards.pop(random_position)
                table.append(card_to_play)
                print ("1 \n")
                print (card_to_play)

                print ("table in funct")
                print (table)
                print (card_to_play)
                returnable_list = []
                returnable_list.append(card_to_play)
                returnable_list.append(table)
                print (f"this is returnable list {returnable_list}")
                print (f"length of hand.card {len(hand.cards)}")


# Here's what I used for aggressive play, going to attempt conservative play
# found this amazing max for given element of list
                # https://dbader.org/blog/python-min-max-and-nested-lists
                # max(nested_list, key=lambda x: x[1])
                # max(nested_list, key=lambda x: (position, len(), or other attribute))

                highest_value_card_block = max(card_list, key=lambda x: x[3])
                
                highest_value = highest_value_card_block[3]
                choices_for_card_to_play = []
                for card in card_list:
                    if card[3] == highest_value:
                        choices_for_card_to_play.append(card)
                if len(choices_for_card_to_play) == 1:
                    highest_value_card = choices_for_card_to_play[0]
                    card_to_play = highest_value_card[0]
                else:
                    selected_highest_value_card = random.choice(choices_for_card_to_play)
                    card_to_play = selected_highest_value_card[0]
                
                table.append(card_to_play)
                hand.cards.remove(card_to_play)
                print (hand.cards)
                for card in table:
                    print (card)
                return [card_to_play, table];
            else:
                # play conservative (off but high)
                card_to_play = random.choice(hand.cards)
                print ("2 \n")
                print (card_to_play)
               
                return card_to_play


# This one here is for conservative play

                highest_value_card_block = max(card_list, key=lambda x: x[3] and x[3] <=6)
                
                highest_value = highest_value_card_block[3]
                choices_for_card_to_play = []
                for card in card_list:
                    if card[3] == highest_value:
                        choices_for_card_to_play.append(card)
                if len(choices_for_card_to_play) == 1:
                    highest_value_card = choices_for_card_to_play[0]
                    card_to_play = highest_value_card[0]
                else:
                    selected_highest_value_card = random.choice(choices_for_card_to_play)
                    card_to_play = selected_highest_value_card[0]
                
                table.append(card_to_play)
                hand.cards.remove(card_to_play)
                print (hand.cards)
                for card in table:
                    print (card)
                return [card_to_play, table];