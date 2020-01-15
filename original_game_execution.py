



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


# In[30]:
