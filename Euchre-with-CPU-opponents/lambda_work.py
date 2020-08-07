list_of_cards = [("object_1", "suit_1", "rank_1", 1 ),("object_2", "suit_2", "rank_1", 1),("object_3", "suit_3", "rank_3", 3),("object_4", "suit_4", "rank_2", 2)]


# cards_in_hand_of_trump = list(filter(lambda x: x[2] == current_playset.trump, card_list))

a_card_with_lowest_value = list(min(list_of_cards, key=lambda x: x[3]))
# then filter based on that? 

all_cards_with_lowest_value = list(filter(lambda x: x[3] == a_card_with_lowest_value[3],list_of_cards))
                                          
print (a_card_with_lowest_value)
print(all_cards_with_lowest_value)

