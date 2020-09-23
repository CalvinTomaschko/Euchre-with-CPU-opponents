import pdb
import random


list_of_suit_values = [8,10,8,8]
# 10 10 8 8 
# 8 8 8 2
# 10 8 8 8 
# 10 8 8 2
suit_names = ["hearts", "diamonds", "spades", "clubs"]
values_by_suit_trump = zip(suit_names,list_of_suit_values)

#reorder the list based on second value
ordered_values_by_suit_trump = sorted(values_by_suit_trump, key=lambda x: x[1], reverse = True)
# Ex: [[diamonds,12],[spades,8],[hearts,3],[clubs,0]]

# randomize results if theirs tied entries
# do any scores match other scores? 
matching_scores = False
matches = []
for i in range(len(ordered_values_by_suit_trump)):
    for j in range(i+1,len(ordered_values_by_suit_trump)): # compare each to others
        # if there's a score match
        if  ordered_values_by_suit_trump[i][1]==ordered_values_by_suit_trump[j][1]:
            matching_scores = True
            if matches == []:
                # equal to max then add to the list, otherwise leave off
                matches.append(ordered_values_by_suit_trump[i])
                print("empty add")
                print(ordered_values_by_suit_trump[i])
                matches.append(ordered_values_by_suit_trump[j])
                print("empty add")
                print(ordered_values_by_suit_trump[j])
            else:
                print (f"max matches x[1] {max(matches, key=lambda x: x[1])}")
                print (f"ordered_values_by_suit_trump[][1]{ordered_values_by_suit_trump}")
                if ordered_values_by_suit_trump[i][1] == max(matches, key=lambda x: x[1])[1]:
                    # or ordered_values_by_suit_trump[j][1] == max(matches, key=lambda x: x[1])[1] (J being the differnece)
                    matches.append(ordered_values_by_suit_trump[i])
                    print("max add")
                    print(ordered_values_by_suit_trump[i])
                    
                    matches.append(ordered_values_by_suit_trump[j])
                    print("max add")
                    print(ordered_values_by_suit_trump[j])
                
                    
print(f"matches --> {matches} \n")

# matches_suits_only

if matching_scores == True:
    to_scramble_list = []
    # randomize the matches
    # pull values out of list at a spot, randomize them, then insert them back in at index
    matches_set = set(matches) # set makes matching items unique
    print(f"matches_set --> {matches_set}")
    matches_set_suits_only = []
    for x in matches_set:
        matches_set_suits_only.append(x[0])
    print (ordered_values_by_suit_trump)
    # Ex [[diamonds,10],[spades,10]]
    index_extract_point = -1
    for spot,suit_and_score in enumerate(ordered_values_by_suit_trump):
    # # Ex: [[diamonds,12],[spades,8],[hearts,3],[clubs,0]]
        # NOTE: Look here again
        the_suit = suit_and_score[0]
        if the_suit in matches_set_suits_only:
            # now pull how ever many matches there are scramble and put back
            index_extract_point = spot
            for number in range(len(matches_set)):
                to_scramble_list.append(ordered_values_by_suit_trump.pop(index_extract_point))
            # scramble
            print(f"with max repeat taken out {ordered_values_by_suit_trump}")
            print(f"Scramble_list {to_scramble_list}")
            random.shuffle(to_scramble_list)
            print(f"now scrambled {to_scramble_list}")
            print (f"insert point index {index_extract_point}")            
            # now put back in
            for scrambled_egg in to_scramble_list:
                ordered_values_by_suit_trump.insert(index_extract_point, scrambled_egg)
            # python debugger 
            print (f"back to full list {ordered_values_by_suit_trump}")
            break
