
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

