def pc_hand_value(which_hand,trump='off'):
    print ("\n PcHandValue FUNCTION")
    total_card_values = 0
    print (which_hand)
    print (trump)
    trump_color = colors[trump]
    # print (trump_color)
    all_card_list = [] # this will eventually get wittled down to the lowest valued card or cards
    all_value_list = []
#     lowest_value = 14 # higher than any card value, right jack at 13

    # This for loop takes in all the cards in the hand and adjusts their temporary value, then adding
    # that value to all_card_list

    for card in which_hand.cards:
        print (f"{card.rank} of {card.suit}")

        if card.suit == trump:
            # print (f"1 card.rank {card.rank}")  # Ace or Jack
            temp_rank = 't'+str(card.rank)
            # print (f"trump temp_rank {temp_rank}")
            # print (f"3 values[card.rank] {values[card.rank]}") # a num like 6 or 3
            temp_value = values[temp_rank]
            # print (f"4 temp_value {temp_value}")
            total_card_values += temp_value
            all_card_list.append([card.rank,card.suit,temp_value])


        elif card.rank == "Jack" and colors[card.suit] == trump_color:
            temp_rank = 'tJick'
            # print (f"the Left temp_rank {temp_rank}")
            temp_value = values[temp_rank]
            all_card_list.append([card.rank,card.suit,temp_value])

        else:
            # print ("regular card")
            value = values[card.rank]
            total_card_values += values[card.rank]
            all_card_list.append([card.rank,card.suit,value])


    print (f"all_card_list --> {all_card_list}")


    # This is to test for if the pc player is the dealer, if they are then
    # the pc player will decide which card to discard, which will likely be a lowest value card
    # but could also be not the lowest value card, instead it could be the only card of a particular suit
    # in their hand, if pc player drops that card then they are more likley able to play trump when that
    # same suit is lead

    if dealers_turn == which_hand:
        total_card_values = pc_is_dealer_hand_value(all_card_list,which_hand,trump)



    print (f"total card values is {total_card_values}")
    return (total_card_values)



def pc_is_dealer_hand_value(all_card_list,hand,trump):
    print ("\n PcIsDealerHandValue")
    # all_card_list  -->  [ [card.rank,card.suit,temp_value] , [cr,cs,tv] , 3 more =5 cards total]
    # hand   --> 'Chair#'
    # trump  -->  string of a suit, "Spades"

    list_of_numbered_suits = pc_check_for_suits(hand)

    # list_of_numbered_suits --> [0,0,0,0] if 3 Hearts and 2 Spades [3,0,2,0], does not account
    # for Jick transfer to other suit, so Trump suit must still be filtered

    # Single suited swap?
    # Checking if pc player can get rid of an entire suit, if there's one single card of a suit
    # if it's not trump, and it's not an Ace, then it's better to lay it down so that
    # odds of "trumping" during play is more likely

    while chosen_card == '':
    # Major While loop until we pick a card to swap with the trump card we pick up

    # STEP 1 Check if there's a single card suit
    # on it's own, or multiple, then maybe pick one

        if 1 in list_of_numbered_suits:
            # meaning something like this [0,1,1,3]

            list_of_positions_numbered_one = []

            # Since we know there's at least one instance of a single card of a suit, let's grab all (up to 3)
            # and rule out those that are trump, and aces if possible, otherwise randomly choose one

            for count,num_of_suits in enumerate(list_of_positions_numbered_suits): # enumerate note at bottom of function
                if num_of_suits == 1:
                    list_of_positions_numbered_one.append(list_of_numbered_suits[count])

            # lopno will be possibly [0,2]
            # which in list of suits is [HdSc] position hearts and position Spades
            # if hearts is trump then we'd want to use the only other position in lopno
            # that is 2 and we would get rid of a whole suit from the pc hand

            for position in list_of_positions_numbered_one:
                # checks to make sure list is still there
                if len(list_of_positions_numbered_one) ==0:
                    break
                # checks for Trump
                if suit[position] == trump:
                    list_of_positions_numbered_one.pop(position)
                # now we find what rank this lone suit is, and if it's an ace we'll keep it in our hand for now
                # by popping it from the potential discard list
                the_rank = ''

                if len(list_of_positions_numbered_one) ==0:
                    break
                for each_card_list in all_card_list:
                    if each_card_list[1] == suit[position]:
                        the_rank = each_card_list[0]
                        break
                    else: continue
                if the_rank == 'Ace':
                    list_of_positions_numbered_one.pop(position)

                if len(list_of_positions_numbered_one) ==0:
                    break

                # Remember list_of_positions_numbered_one could like these
                # [0,1]  or  [2,3]  or  [0]  or  [1,2,3] (bad bad hand)
                # sH,sD      sS,sC      sH       sD,sS,sC      s = single
                # these numbers are positions, positions that relate to
                # list_of_numbered_suits --> [0,1,1,3]
                # aka this hand has no hearts, 1 of diamond & spades, 3 clubs
                # any final selection must be traslated out to the card in hand


            # now if this list still has stuff in it, like it's a farmers hand of 9c,9s,9d,Jd,Ah and the
            # card they would pick up is the right, then we'll select one of the 9 cards at random to get rid of it.

                if len(list_of_positions_numbered_one) >= 1:
                    if len(list_of_positions_numbered_one) == 1:
                        # translate this postion to the suit to the card of that suit
                        # make that card the chioce and then say while loop
                        # card_to_be_swapped_is = This one card!
                        suit_of_card_to_drop = list_of_numbered_suits[list_of_positions_numbered_one[0]]
                        # finds the card in the hand
                        for card in all_card_list:
                            if card[1] == suit_of_card_to_drop:
                                chosen_card = all_card_list[all_card_list.index(card)]

                            else:
                                pass
                        # EXIT 1 WHILE LOOP HERE

                    else:
                        # there's more than 1 single suited card that not trump or an Ace
                        # so let's pick 1 randomly
                        choice = random.randint(0,len(list_of_positions_numbered_one))
                        chosen_position = list_of_positions_numbered_one[choice]
                        # Translation
                        suit_of_card_to_drop = list_of_numbered_suits[list_of_positions_numbered_one[chosen_position]]
                        #_________________________________________________________________________________________________
                        for card in all_card_list:
                            if card[1] == suit_of_card_to_drop:
                                chosen_card = all_card_list[all_card_list.index(card)]
                                break
                            else:
                                continue
                        # EXIT 2 WHILE LOOP HERE


        else:


    # STEP 2 No single cards so we must find a
    # low value card to toss, still in while loop

            # all_card_list  -->  [ [card.rank,card.suit,temp_value] , [cr,cs,tv] , 3 more =5 cards total]
            # hand   --> 'Chair#'
            # trump  -->  string of a suit, "Spades"

            for card in all_card_list:
                all_value_list.append(card[2])
            lowest_value = min(all_value_list)

            for card in all_card_list:
                if card[2] == lowest_value:
                    continue
                else:
                    all_card_list.pop(card)

            # lowest value can not be trump, all tRank cards are higher, unless the hand was all trump
            # in that case trump being the lowest is fine. Player is about to have a great hand

            # In case the play has 2 9s
            # , this will choose one of them as lowest card. They would want to keep one if they had more of that
            # suit because then they would lower the number of suits in their hand, thereby letting them
            # trump on a turn where someone else lead a suit that they no long have and therefore don't have to
            # follow suit

            if len(all_card_list) >=2:
                choice = random.randint(0,len(all_card_list))
                chosen_card = all_card_list[choice]



            else:
                chosen_card = all_card_list[0]


    # EXIT 2 WHILE LOOP HERE

    # Now that we're out of that while

    return (chosen_card)
    # should be [card.rank,card.suit,temp_value]


    # NOTE to remember how enumerate works
    #   lst = ['a','b','c']
    #   for number,item in enumerate(lst):
    #   print(number)
    #   print(item)




def pc_best_playable_suit(hand,list_of_suit_values,trump_picker):
    # This function is for select_trump_after_flip only
    print ("\n PcBestPlayableSuits FUNCTION")
    print (f"this is hand {hand}")

    values_by_suit_trump = list_of_suit_values
    print(f"values by suit trump list \n -->{values_by_suit_trump}")
    chosen_suit = ''

    print (f"here's one_and_done_suit --> {one_and_done_suit}")

    # for loop to make one_and done 0 if needed lets see

    #######
    #######

    # list in order hdsc

    # now choose the highest valued trump suit to pursue,
    # if there's a tie randomly choose highest

    check_suit_list = []

    print (f"Max value in values_by_suit_trump is {max(values_by_suit_trump)}")

    indicy_walker = 0

    for val in values_by_suit_trump:
        if val == max(values_by_suit_trump):
            check_suit_list.append(indicy_walker)
        indicy_walker +=1

    print(f"This list is of suits (indicies) at max value h0,d1,s2,c3 {check_suit_list}")

    final_check = 0 # the indicy that we will choose in suits tuple

    if len(check_suit_list)>1:
        final_check = check_suit_list[random.randint(1,len(check_suit_list))-1]
        chosen_suit = suits[final_check]

    else:
        final_check = check_suit_list[0]
        chosen_suit = suits[final_check]
    print (f"Here's the final suit (indicies) check chosen h0,d1,s2,c3; {final_check} !")

    # value = pc_hand_value(hand,chosen_suit)

    # Now with a chosen suit we make a decision by returning the needed
    # values for call_pick_up()

    return (chosen_suit)

    # Now write program to call the suit or not like pc_call_pick_up does



def pc_call_pick_up(hand,maybe_trump,value,trump_picker):
    # This function is for pass_or_order_up only
    print ("\n PcCallPickUp FUNCTION")
    # need to pass through what is trump, suit?
    dealer_num = table_position_list.index(dealers_turn)+1 # their chair, not index
    print (f"here's dealer num, {dealer_num}")
    suit = ''

    if pc_single_suited(pc_check_for_suits(hand)):
        print ("back to PcCallPickUp FUNCTION" )
        # dealer is picking trump
        if dealer_num==trump_picker:
            if value >= 32:
                # suit = maybe_trump
                print ("found answer 1")
                return True
        # partner deal
        elif  abs(dealer_num-trump_picker) == 2:
            if value >= 37:
                # suit = maybe_trump
                print ("found answer 2")
                return True
        # else opponent deal
        else:
            if value >= 38:
                # suit = maybe_trump
                print ("found answer 3")
                return True
    else:
        if dealer_num==trump_picker:
            if value >= 36:
                # suit = maybe_trump
                print ("found answer 4")
                return True
        # partner deal
        elif abs(dealer_num-trump_picker) == 2:
            if value >= 38:
                # suit = maybe_trump
                print ("found answer 5")
                return True
        # else opponent deal
        elif value >= 43:
            # suit = maybe_trump
            print ("found answer 6")
            return True
    print ("found no answer couldn't call order up")
    return False


def pc_check_for_suits(hand_ob):
# This function does not account for the transferring same color Jack aka "Jick" becoming
# the same suit (effectively), that must be done within other functions
    print ("\n PcCheckForSuits FUNCTIONS")
    list_hand_suits = [0,0,0,0]

    # Oct 8th, NOTE should I just change this to sort Jicks over into the other same color suit?
    # check if that will affect how the other functions work

    for card in hand_ob.cards:
        if card.suit == "Hearts":
            list_hand_suits[0] += 1
        elif card.suit == "Diamonds":
            list_hand_suits[1] += 1
        elif card.suit == "Spades":
            list_hand_suits[2] += 1
        else:
            list_hand_suits[3] += 1
            #h d s c
    print (f"list_hand_suits h,d,s,c {list_hand_suits}")

    return (list_hand_suits)


def pc_single_suited(list_hand_suits):
    print ("\n PcSingleSuited FUNCTION")
    print (list_hand_suits)

#     single_suited = False
    num_suit = 4
    for num in list_hand_suits:
        if num == 0:
            num_suit -= 1
    if num_suit <=2:
        return True
    else:
        return False


def pc_plays_a_card(trump,who_called,trick_round,hand):
    print ("\n PPAC FUNCTION")
    pass
    # Makes a choice based on offense or defense if their team called or not
    # if not lead: follow suit
        # if suit can't beat lead, then throw lower of that suit
        # if first round
            # if partner called: throw low trump
            # unless other team picked up the right bauer
            # elif opponents picked up: through highest non-trump
            # else lead with highest trump
        # elif (not first round):

def pc_side_of_select_trump_after_flip():

    decision = False
    list_of_values = []
    for suit_type in suits:
        if suit_type == one_and_done_suit:
            list_of_values.append(0)
            continue
        print(f"Suit_type from the IF in choose trump {suit_type} for PHV to look into")
        list_of_values.append(pc_hand_value(list_of_hand_objects[trump_picker-1],suit_type))

    # suit_list = pc_check_for_suits(list_of_hand_objects[trump_picker-1]) ## I dont' think this is needed here
    # but rather inside of pc_best_playable_suit()

    #### PROMBLEM here: takes one suit away but offsets the list indexing then.
    print (f"heres the list of values {list_of_values} from PHV, still in STAF function to passed into PBPS")

    # for list of values the highest one over a certain number is chosen for their trump

    ### NEW THOUGHT!
    #if no value in list of values over certain number then don't bother checking:
    # else:
    suit_to_pursue = pc_best_playable_suit(list_of_hand_objects[trump_picker-1],list_of_values,trump_picker)

    # call function that uses the suit to pursue to choose yay or nay and give response

    print (f"suit to pursue selection is --> {suit_to_pursue}")
    value_for_this_suit = pc_hand_value(list_of_hand_objects[trump_picker-1],suit_type)


    if pc_call_pick_up(list_of_hand_objects[trump_picker-1],suit_to_pursue,value_for_this_suit,trump_picker):
        # The arguments are "hand", maybe_trump aka 'suit',value, and trump_picker
        trump_chosen == True
        return suit_to_pursue, chair;
        ### EXIT HERE EXIT HERE

    if trump_chosen == False:
        print (f"\n{table_position_dict[chair]} chooses to pass")


def pc_side_of_pass_or_order_up(suit_of_up_card):
    
    print ("activated pc decision time")
    # NOTE: make it a pcfunction to call trump or not

    # position 0. spades, 1. diamonds, 2. hearts, 3. clubs

    #             decision = False
    hand_value = pc_hand_value(list_of_hand_objects[trump_picker-1],one_and_done_suit)

    # print (f"heres the of value of their hand, {hand_value}")

    if pc_call_pick_up(hand,one_and_done_suit,hand_value,trump_picker):
        trump_chosen = True

        # EXIT 2: Trump is ordered up by PC, dealer gets that top card and swaps
        return [True, chair];

    # for list of values the highest one over a certain number is chosen for their trump



def pc_side_of_pick_up_and_switch():

    card_count_list = [["Hearts",0],["Diamonds",0],["Spades",0],["Clubs",0]]
    all_card_list = []
    has_trump = False

    for card in hand.cards:
        value = values[card.rank]

        # With this one for loop we'll create two separate lists for the purpose
        # of picking a good card to swap

    ##### Start: all_card_list section---------
    #This section makes a list of cards with rank,suit,and accurate value
        if card.suit == trump:
            # print (f"1 card.rank {card.rank}")  # Ace or Jack
            temp_rank = 't'+str(card.rank)
            # print (f"trump temp_rank {temp_rank}")
            # print (f"3 values[card.rank] {values[card.rank]}") # a num like 6 or 3
            temp_value = values[temp_rank]
            # print (f"4 temp_value {temp_value}")
            all_card_list.append([card.rank,card.suit,temp_value])

        elif card.rank == "Jack" and colors[card.suit] == trump_color:
            temp_rank = 'tJick'
            # print (f"the Left temp_rank {temp_rank}")
            temp_value = values[temp_rank]
            all_card_list.append([card.rank,card.suit,temp_value])

        else:
            # print ("regular card")
            value = values[card.rank]
            all_card_list.append([card.rank,card.suit,value])
    ##### End: all_card_list section

    ##### Start: card_count_list section -------
    # This section only grabs non-trump and non-Ace values. Taking those
    # and adding them into a list of cards that could be swapped towards getting
    # a suit out of your hand, thereby making it a stronger hand for trumping

        if card.suit == "Hearts":
            if "Hearts" == trump:
                has_trump = True
            elif card.rank == "Ace":
                pass
            else:
                card_count_list[0][1] += 1
        if card.suit == "Diamonds":
            if "Hearts" == trump:
                has_trump = True
            elif card.rank == "Ace":
                pass
            else:
                card_count_list[1][1] += 1
        if card.suit == "Spades":
            if "Hearts" == trump:
                has_trump = True
            elif card.rank == "Ace":
                pass
            else:
                card_count_list[2][1] += 1
        if card.suit == "Clubs":
            if "Hearts" == trump:
                has_trump = True
            elif card.rank == "Ace":
                pass
            else:
                card_count_list[3][1] += 1

    ##### End: card_count_list section


    ##### Start: Look for Single Card of Suit section #####---------

    # Now card_count_list will look something like
    #  [["Hearts",2],["Diamonds",1],["Spades",1],["Clubs",1]]
    # Going through this list for single suit checking
    chosen_suit_to_drop = "empty"
    if has_trump == True:
        # if there's no trump then there's no use trying to go single suited
        # for loop for ones! last loop took out trump cards for use in swap
        # so now only non-trump cards are up for grabs
        suits_with_one_list = []
        print (f"Looking at card_count_list {card_count_list}")


        for suit in card_count_list:
            if suit[1] == 1:
                suits_with_one_list.append(suit)
        print(f"let's see suits_with_one_list {suits_with_one_list} ")
        # now suits_with_one_list should look like this
        # [["Diamonds",1]["Spades",1],["Clubs",1]] or [["Spades",1]] or "empty" # no
        # suits with just one card
        if len(suits_with_one_list) != 0:
            if len(suits_with_one_list) == 1:
                print ("found len of 1")
                chosen_suit_to_drop = suits_with_one_list[choice][0]
                clear = True
            else:
                print ("found not len of 1")
                # len(suits_with_one_list) < 1
                # there's more than 1 single suited card that not trump or an Ace
                # so let's pick 1 randomly
                choice = random.randint(0,len(suits_with_one_list))
                chosen_suit_to_drop = suits_with_one_list[choice][0]

    if chosen_suit_to_drop != "empty":
    # use that suit looking through hand to choose the card
    # return the card to drop
        for card in hand: # may need to be hand.cards
            if card.suit == chosen_suit_to_drop:
                chosen_card_to_drop = card
                print (f"chosen card at single suit section, {chosen_card_to_drop}")
                decision = True
    ### While loop exit, decision True


    # chosen_card_to_drop = ??????????

    ##### End: Look for Single Card of Suit section #####



    else:
    ##### Start: Selecting low value card ------------

        # Now if there wasn't an answer from the single card of a suit pursuit then
        # we'll look to drop the lowest valued card!
        # all_card_list  -->  [ [card.rank,card.suit,temp_value] , [cr,cs,tv] , 3 more =5 cards total]
        # hand   --> 'Chair#'
        # trump  -->  string of a suit, "Spades"
        print (f"all_card_list{all_card_list}")

        all_value_list = []
        for card in all_card_list:
            all_value_list.append(card[2])

        print (f"all_value_list{all_value_list}")

        lowest_value = min(all_value_list)
        print (f"lowest_value{lowest_value}")

        print(all_card_list)
        ### Make new list here

        remain_list = []
        for count,card in enumerate(all_card_list):
            print (card)
            print (f"counting loop {count}")
            if card[2] == lowest_value:
                remain_list.append(card)
#                             print ("is getting popped due to being lowest value")
#                             all_card_list.pop(count)


        # lowest value can not be trump, all tRank cards are higher, unless the hand was all trump
        # in that case trump being the lowest is fine. Player is about to have a great hand

        # In case the play has 2 9s
        # , this will choose one of them as lowest card. They would want to keep one if they had more of that
        # suit because then they would lower the number of suits in their hand, thereby letting them
        # trump on a turn where someone else lead a suit that they no long have and therefore don't have to
        # follow suit
        print (f"what remains of all_card_list{remain_list}")
        
        if len(remain_list) >=2:
            print ("len greater than 2")
            choice = random.randint(0,len(remain_list))
            chosen_card_to_drop = remain_list[choice]
            print (f"chosen_card_to_drop{chosen_card_to_drop}")
            print (f"chosen card at lowest value section")
            decision = True
        ### While loop exit, decision True
        
        else:
            print ("len of 1")
            chosen_card_to_drop = remain_list[0]
            print (f"chosen_card_to_drop{chosen_card_to_drop}")
            print (f"chosen card at lowest value section")
            decision = True
    ### While loop exit, decision True
    ##### End: Selecting low value card #####

    decision = True
    # PC DECISION TIME END -------------------------------------
