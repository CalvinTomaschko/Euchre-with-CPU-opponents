list_of_cards = [("object_1", "suit_1", "rank_1", 1 ),("object_2", "suit_2", "rank_1", 1),("object_3", "suit_3", "rank_3", 3),("object_4", "suit_4", "rank_2", 2)]


# cards_in_hand_of_trump = list(filter(lambda x: x[2] == current_playset.trump, card_list))

a_card_with_lowest_value = list(min(list_of_cards, key=lambda x: x[3]))
# then filter based on that? 

all_cards_with_lowest_value = list(filter(lambda x: x[3] == a_card_with_lowest_value[3],list_of_cards))
                                          
print (a_card_with_lowest_value)
print(all_cards_with_lowest_value)



sorted_list = sorted(list_to_sort, key=lambda x: (x[1], x[0]))


new_list = sorted(old_list, key=lambda x: x[2])



ls2=[[0,1,'f'],[4,2,'t'],[9,4,'afsd']]
def thirdItem(ls):
    #return the third item of the list
    return ls[2]
#Sort according to what the thirdItem function return 
ls2.sort(key=thirdItem)