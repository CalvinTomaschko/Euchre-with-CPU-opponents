
# #Class Definitions
#
# class Card:
#
#     def __init__(self,suit,rank):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return self.rank + ' of ' + self.suit
#

############################

# class Deck:
#
#     def __init__(self):
#         self.deck = []  # start with an empty list
#         for suit in suits:
#             for rank in ranks:
#                 self.deck.append(Card(suit,rank))
#
#     def __str__(self):
#         deck_comp = ''  # start with an empty string
#         for card in self.deck:
#             deck_comp += '\n '+card.__str__() # add each Card object's print string
#         return 'The deck has:' + deck_comp
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     # Future goal: Deals must be dealt by going around the table twice
#     # giving everyone at least one card each time around
#
#     def deal(self):
#         single_card = self.deck.pop()
#         return single_card
#
#     def put_back(self,card):
#         self.deck.insert(0,card)
#
#
# class Hand:
#
#     def __init__(self,name):
#         self.cards = []  # start with an empty list as we did in the Deck class
#         self.value = 0   # start with zero value
#         self.name = name
#         self.color = ''
#
#     def __str__(self):
#
#         return self.name
#
#     def add_card(self,card):
#         self.cards.append(card)
#
#

################################
