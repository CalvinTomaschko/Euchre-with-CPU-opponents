# Euchre, Capstone challenge
# Written by Calvin Tomaschko
# Aug 24th, 2019 
# Made as final capstone to 
# Udemy:Complete Python Bootcamp: Go from zero to hero in Python 3
# Created with guidance from the Black Jack game module


import random
import pdb





################################

### Classes ###
### Classes ###
### Classes ###

#Class Definitions
# NOTE: original class moved to storage 

#Dev Class Definitions

class Dev_Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Dev_Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Dev_Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def shuffle_bottom(self):
        to_shuffle = self.deck[6:]
        random.shuffle(to_shuffle)
        self.deck = self.deck[:6]+to_shuffle
        
    def hearts_for_dealer(self):
        list_o_ranks = ["Jack","Ace","King","Queen","Ten"]
        list_o_tcards = []
        nine_for_top = []
        for count,card in enumerate(self.deck):
            if card.rank in list_o_ranks and card.suit == 'Hearts': 
                tcard = self.deck.pop(count)  # there may be a lucky strike here with pop and insert
                self.deck.insert(0,tcard) # this messed up the for loop observing the list in other trys
            if card.rank == "Nine" and card.suit == 'Hearts':
                nine_for_top = self.deck.pop(count)
        
        self.deck.insert(20,nine_for_top)
        
    def hearts_for_2nd(self):
        
    ## New list swapping
        list_o_ranks = ["Jack","Ace","King","Queen","Ten"]
        list_o_five_tcards = []
        nine_for_top = []
        new_list = []    
        
    ## Pull the desired cards   

        for card in self.deck:
            if card.rank in list_o_ranks and card.suit == 'Hearts':  
                list_o_five_tcards.append(card)
            if card.rank == "Nine" and card.suit == 'Hearts':
                nine_for_top = card

    ## Make new list leaving out the five tcards and the nine

        for card in self.deck:
            if card.rank == "Nine" and card.suit == 'Hearts':
                continue
            if card not in list_o_five_tcards:
                new_list.append(card)


#         print ("same list, no tcards or tnine, new_list is")
    
    ## quick print as objects need to be called directly for print string
#         for card in new_list:
#             print (card)

        for card in list_o_five_tcards:
            new_list.insert(5,card)

    ## Add tNine to 4th spot

        if nine_for_top != []:
            new_list.insert(-3,nine_for_top)

    ## Return final list   
    
    ## quick print to check, as card objects won't print unless directly called on
#         for card in new_list:
#             print (card)
        
        self.deck = new_list


    def hearts_for_2nd_and_one_off_suited(self):
            
        ## New list swapping
            list_o_ranks = ["Jack","Ace","King","Queen","Ten"]
            list_o_five_tcards = []
            nine_for_top = []
            new_list = []    
            
        ## Pull the desired cards   

            for card in self.deck:
                if card.rank in list_o_ranks and card.suit == 'Hearts':  
                    list_o_five_tcards.append(card)
                if card.rank == "Nine" and card.suit == 'Hearts':
                    nine_for_top = card

        ## Make new list leaving out the five tcards and the nine

            for card in self.deck:
                if card.rank == "Nine" and card.suit == 'Hearts':
                    continue
                if card not in list_o_five_tcards:
                    new_list.append(card)
        
        ## Here's where I pull one random card and will add it later
            random_card = random.choice(new_list)
            new_list.remove(random_card)
            # list is now one shorter


    #         print ("same list, no tcards or tnine, new_list is")
        
        ## quick print as objects need to be called directly for print string
    #         for card in new_list:
    #             print (card)

            for card in list_o_five_tcards:
                new_list.insert(5,card)

        ## Now I'm adding a random card to their hand
            new_list.insert(5,random_card)

        ## Add tNine to 4th spot

            if nine_for_top != []:
                new_list.insert(-3,nine_for_top)

        ## Return final list   
        
        ## quick print to check, as card objects won't print unless directly called on
    #         for card in new_list:
    #             print (card)
            
            self.deck = new_list
    
    # Future goal: Deals must be dealt by going around the table twice 
    # giving everyone at least one card each time around   
    
    def deal(self):
        single_card = self.deck.pop(0)
        return single_card
    
    def put_back(self,card):
        self.deck.insert(0,card)
    

class Dev_Hand:
    
    def __init__(self,name):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.name = name
        self.color = ''
        
    def __str__(self):
        
        return self.name
    
    def add_card(self,card):
        self.cards.append(card)


### Classes ###
### Classes ###
### Classes ###

################################

### Functions ###
### Functions ###
### Functions ###


## Setup ##
## Setup ##

# How many human players

def how_many_humans():
    num_humans = int(input("How many human players are there?"))
    ### place exception error catch here
    return table_positions(num_humans)

# Which positions are the human players? 
# They can be on the same team or opposing teams depending on where they sit

def table_positions(output_num): 
    table_position_dict = table_position_dict_default.copy()
#     for seat in table_position_dict_default:
#         table_position_dict.update(seat[0]:seat[1])
    print (f"testing to see if table copied well {table_position_dict}")
    print ("The positioning is around a table \n position 1 is on the south and then it goes clockwise \n up to the 4th position to the east")
    print ("\n   p3  \n p2  p4\n   p1  ")
    
    # While loop until we get the right positions out
    correct = False
    while correct == False:
        
        # Passed from how_many_humans
        for n in range(output_num): 
            player_num = n + 1
            print ("player "+str(player_num))
            
            num_to_swap = int(input("what position would you like to take? 1-4 \n"))
            
            # Based on the input we will alter the base table_position_dict of all pc players
            keyval_swap = "chair_"+str(num_to_swap)
            table_position_dict[keyval_swap] = 'hu player '+str(player_num)
            ### error exception here
            
            print ('this is table_position_dict')
            print (table_position_dict)
        
        print (table_position_dict)
        final_ans = input("Now is all the positioning correct? Y or N")
        if final_ans[0].lower() == 'y':
            team_a = table_position_dict['chair_1'] + " & " +table_position_dict['chair_3']
            team_b = table_position_dict['chair_2'] + " & " +table_position_dict['chair_4']
            print (f"Team A is {team_a}")
            print (f"Team B is {team_b}")
            correct = True
        else:
            print ("Ok, we'll reset and restart")
            table_position_dict = table_position_dict_default.copy()
#             for seat in table_position_dict_default:
#                 table_position_dict.update(seat[0]:seat[1])
            print("This is the reset dict")
            print(table_position_dict)
    return (table_position_dict)
        

def print_teams(table_position_dict):
    tdict = table_position_dict
    south = tdict["chair_1"]
    north = tdict["chair_3"]
    west = tdict["chair_2"]
    east = tdict["chair_4"]
    print (f"Team North & South is {south} and {north}")
    print (f"Team East & West is {west} and {east}")  
    
    
# who's dealer, randomly pick a dealer

def whos_first_dealer():
    choice = random.randint(1,4)
    first_dealer = "chair_"+ str(choice)
    player = table_position_dict[first_dealer]
    print (f'First deal is {player}')
    return first_dealer   

# Deal out 5 cards 
    
def deal_cards(whos_hand,given_deck):
    deck = given_deck
    whos_hand.add_card(deck.deal())
    whos_hand.add_card(deck.deal())
    whos_hand.add_card(deck.deal())
    whos_hand.add_card(deck.deal())
    whos_hand.add_card(deck.deal())

def top_card_suit(deck):
    top_card = deck.deal()
    print (f"The top card is {top_card}")
    one_and_done_suit = top_card.suit
    deck.put_back(top_card)
    print (one_and_done_suit)
    return one_and_done_suit 
#   Card(suit,rank)

## Setup ##
## Setup ##

###################

## PC functions, trump picking ##
## PC functions, trump picking ##

# Tells the numerical value of a given hand with trump as the signifier 

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
    



## PC functions, trump picking ##
## PC functions, trump picking ##

###################

## PC and HU Decision functions ##
## PC and HU Decision functions ##

# Decide on suit
# who's left of the dealer
# then player selection on puting card away if trump is called

def select_trump_after_flip():
    print ("\n SELECT TRUMP AFTER FLIP FUNCTION")
    
    ## Dealers turn counts 0,1,2,3 
    print (f"STAF Here's dealers turn {dealers_turn}")
    trump_picker = table_position_list.index(dealers_turn)+1 # if dealer is chair 1, trump picker is 1
    # trump_picker represents a player to point at, there's no player 0 only 1-4
    print (f"STAF Here's trump picker {trump_picker}")
    
    
    
    
    trump_picker = table_position_list.index(dealers_turn)+1 # trump picker points at a player, 
    # no player 0
    trump = ''
    trump_chosen = False
    
    screw_dealer_counter = 0 # if it gets to 4 it should make the dealer choose
    print (f"Top area of STAF: trump_picker is {trump_picker}, trump is '{trump}', screw dealer is {screw_dealer_counter}")
    # For use in the big while loop
    count_for_next_player = 0
    #This is the BIG while loop waiting for trump to be decided
    while trump_chosen == False:
        
        if count_for_next_player == 0:
            print ("\n First player's decision time! \n")
        else:
            print("\n NEXT PLAYER! \n")
        count_for_next_player += 1
        ### Screw Dealer count, at 4 this says 'no more pass'
        screw_dealer_counter += 1
        print (f"screw_dealer_counter is {screw_dealer_counter}")
        
        ### Trump picker count, increase each cycle to move to next player around the table clockwise
        ### starts equal to dealer but then gets one added here
        ### Actual count is 1,2,3,4
        

        trump_picker += 1
        if trump_picker == 5:
            trump_picker = 1
        
        
        # Based on trump picker this sets the chair in question from our list of positions

        chair = table_position_list[trump_picker-1]
        print (f"table position is player {table_position_dict[chair]} in {chair}")
        
    
        # now we see if that chair is a pc or hu player
        # This IF ELSE statement is the gate for getting back through the BIG while loop


        ## The IF is for PC players ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if table_position_dict[chair][:2] == "pc":

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

        
        ## The ELSE is for  HU players

        else:
            print ("activated human decision time")

            #Now an acceptable decision must be made to escape back up to the while loop
            decision = False

            # This while loop is waiting for a decision
            while decision == False:

                print (f'it is human player in {chair} turn')    
                response = input("It's on you to choose trump or pass, respond with 's','d','h', or 'c', otherwise type 'p' for pass")

                # Blank check
                # if response is left blank then this loop will insist that it be filled in
                if response == '':
                    while response == '':
                         response = input("respond with 's','d','h', or 'c', otherwise type 'p' for pass")
                

                # Answer check
                # Insisting that the answers first letter be that of a suit or to pass
                while response[0].lower() not in ['s','d','h','c','p']:
                    print ('sorry we did not understand your input')
                    response = input(f"{chair} choose trump or pass, respond with 's','d','h', or 'c', otherwise type 'p' for pass")
                    
                    print (f"player response is {response}")
                    
                # Answer processing
                # now that we have an acceptable answer let's see if it means trump was selected

                # first if "pass"
                if response[0].lower() == "p":

                    # Checking if pass is acceptable, otherwise we change the answer to
                    # keep us in the decision while loop
                    if screw_dealer_counter >= 4:
                        print ("sorry you can not choose to pass, you must select a suit to be trump")
                        response = "failed pass"
                        print (f"player response is {response}")
                    # Player can pass if screw dealer is not in effect, allowing us to exit decision loop
                    else:
                        print ("hu player chose to pass")
                        decision = True

                # Decision making!
                # If trump is chosen by the human player then we can declare two things
                # 1. decision made, and 2. trump chosen thereby exiting the BIG loop at the top
                
                ##### Make these return two values Suit and who called to kick it back out the the main game 
                #### OTHER EXIT HERE OTHER EXIT HERE
                elif response[0].lower() == one_and_done_suit[0].lower():
                    print("sorry, you can not choose the same suit that was flipped over")
                    # Do not return do not pass go do not collect $200
                elif response[0].lower() == "s":
                    trump_chosen = True 
                    trump = "Spades"
                    print ('trump is Spades')
                    decision = True
                    return trump, chair;
                elif response[0].lower() == "d":
                    trump_chosen = True
                    trump = "Diamonds"
                    print ('trump is Diamonds')
                    decision = True
                    return trump, chair;
                elif response[0].lower() == "h":
                    trump_chosen = True
                    trump = "Hearts"
                    print ('trump is Hearts')
                    decision = True
                    return trump, chair;
                elif response[0].lower() == "c":
                    trump_chosen = True
                    trump = "Clubs"
                    print ('trump is Clubs')
                    decision = True
                    return trump, chair;
                # To let players know what trump is for this deal print response
                print (response)
                    




def pass_or_order_up(suit_of_up_card):
    print("\n PASS OR ORDER UP FUNCTION")
    suit = suit_of_up_card

# Decide on if top card will be trump or not, 
# the dealer gets to pick up this card
# whom is left of the dealer gets to make the first call
# then it goes clockwise around the table of

# whos_first_deal, and in that function should change dealers_turn = to seat number 1-4
# whos_first_deal needs to output dealers_turn = random, then call new func
# def next_deal
# next function?

# This function returns both true or false on if trump selected 
# and who called in a form of string

    ## Dealers turn counts 0,1,2,3 
    print (f"Passoou Here's dealers turn {dealers_turn}")
    trump_picker = table_position_list.index(dealers_turn)+1 # if dealer is chair 1, trump picker is 1
    # trump_picker represents a player to point at, there's no player 0 only 1-4
    print (f"Passoou Here's trump picker {trump_picker}")
    trump_chosen = False
    
    flip_card_over_counter = 0 ## if this gets to 5 then it's on to select_trump 
    print ("Passoou This line is up at start")
    #for use in the big while loop
    count_for_next_player = 0
    #This is the BIG while loop waiting for trump to be decided
    while trump_chosen == False:
        
        
        if count_for_next_player == 0:
            print ("\n First player's decision time! \n")
        else:
            print("\n NEXT PLAYER! \n")
        count_for_next_player += 1
        ### 3. flip card over count, at 5 we break and go to select_trump
        ### this is if no one selected that card and it was "turned over"
        flip_card_over_counter += 1
        print (f"PassOOUflip_card_over_counter is {flip_card_over_counter}")
        if flip_card_over_counter >= 5:
            trump = ''
            
            
            # EXIT 1: we go around the table and get to dealer, dealer flips over the card
            return [False,"no one, all passed, flip card over"];
        
        #OR
        
#         run select_trump_after_flip() 
#         break
        
        ### Trump picker count, increase each cycle to move to next 
        ### player around the table clockwise
        ### starts equal to dealer but then gets one added here
        ### Actual count is 1,2,3,4
        

        trump_picker += 1 # this steps it one left of dealer to start, up further they were equal 
        # chair 1 and trump picker position 1 
        if trump_picker == 5:
            trump_picker = 1
        print (f"Passoou trump_picker is {trump_picker}")
        
        # Based on trump picker this sets the chair in question from our list of positions

        chair = table_position_list[trump_picker-1]
        # Make chair position pull the hand object from list of hand objects
        hand = list_of_hand_objects[trump_picker-1]
        print (f"Passoou table position is {chair}")
        print (table_position_dict)
        
    
        # now we see if that chair is a pc or hu player
        # This IF ELSE statement is the gate for getting back through the BIG while loop


        ## The IF is for PC players ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if table_position_dict[chair][:2] == "pc":
           
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
            

        
        ## The ELSE is for  HU players ~~~~~~~~~~~~~~~~~~~~~~~~~

        else:
            print ("activated human decision time")

            #Now an acceptable decision must be made to escape back up to the while loop
            decision = False
            ### Future note, I could rewrite this as a counter = 0 then while loop, counter += 1
            ### if counter is greater than 1 then do the "sorry, didn't understand"
            # This while loop is waiting for a decision
            while decision == False:

                print (f'\n HUMAN DECISION TIME: it is human player in {chair} turn')    
                response = input("It's on you to have dealer pick up trump or pass, respond with 'o' for 'order up' or 'p' for 'pass'")

                # Blank check
                # if response is left blank then this loop will insist that it be filled in
                if response == '':
                    while response == '':
                         response = input("respond with 'o' for 'order up' or 'p' for 'pass'")
                

                # Answer check
                # Insisting that the answers first letter be that of a suit or to pass
                while response[0].lower() not in ['o','p']:
                    print ('sorry we did not understand your input')
                    response = input(f"{chair} choose for dealer to pick up trump or pass, respond with 'o' for 'order up' or 'p' for 'pass'")
                    
                    print (f"player response is {response}")
                    
                # Answer processing
                # now that we have an acceptable answer let's see if it means trump was selected

                # first if "pass"
                if response[0].lower() == "p":

                    # Checking if pass is acceptable, otherwise we change the answer to
                    # keep us in the decision while loop
                   
                    # Player can pass if screw dealer is not in effect, allowing us to exit decision loop
                    
                    print ("hu player chose to pass")
                    if trump_picker == table_position_list.index(dealers_turn)+1:
                        print ("dealer flips card over, now left of dealer is first to pick trump that's not what was just turned down")
                    decision = True
                    
                    
                        

                # Decision making!
                # If trump is chosen by the human player then we can declare two things
                # 1. decision made, and 2. trump chosen thereby exiting the BIG loop at the top
                elif response[0].lower() == "o":
                    
                    trump = one_and_done_suit
                    print (f'trump is {one_and_done_suit}') 
                    decision = True
                    trump_chosen = True
                    
                    # EXIT 3: Trump is ordered up by Human, dealer gets that top card and swaps
                    return [True,chair];
                else:
                    # Why is this here? Because if there's still something off about the answer 
                    # then the while loop will run again
                    pass
             
                # To let players know what trump is for this deal print response
                print (response)

        
  

def pick_up_and_switch(player,name_hand,trump,deck,card = ''):
    # the PC player or human player may have been ordered to pick it up or have chosen this on 
    # their own but either way pc must choose one card to set down and one card to pick up
    our_index = table_position_list.index(name_hand)
    # input hand and trump arguments and then if it's from a pc that chose trump it may have 
    hand = list_of_hand_objects[our_index]
    # card_to_drop = ?
    chosen_card_to_drop = []
    if card != '':
        # pc already chose a card to drop and passed along that argument! 
        # card_to_drop = This one!
        pass
    else:
        decision = False
        while decision == False:
        # a decision must be made
        
        # card_to_drop = ?
           
        # PC DECISION TIME START -------------------------------------            
            
            print (f"PC CHECKING {table_position_dict[player][:2]}")
            if table_position_dict[player][:2] == "pc":
                
                
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
                        if "Diamonds" == trump:
                            has_trump = True
                        elif card.rank == "Ace":
                            pass
                        else:
                            card_count_list[1][1] += 1
                    if card.suit == "Spades":
                        if "Spades" == trump:
                            has_trump = True
                        elif card.rank == "Ace":
                            pass
                        else:
                            card_count_list[2][1] += 1
                    if card.suit == "Clubs":
                        if "Clubs" == trump:
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
 
            else:
        # HU DECISION TIME START ------------------------------------- 
            # if human do this
            
            # print hand
                counter = 1
                for card in hand.cards:
                    print (f"{card} is card #{counter}")
                    counter += 1
            # ask player which card to drop
                poss_ans = [1,2,3,4,5]
                card_selection = int(input("Which card would you like to drop? 1,2,3,4, or 5 "))
                card_selected = False # until we prove there was a proper selection
                if card_selection in poss_ans:
                    card_selected = True
                if card_selected == False:
                    while card_selected == False:
                        print ("sorry, your entry wasn't 1,2,3,4, or 5")
                        card_selection = int(input("Which card would you like to drop? please answer 1,2,3,4 or 5 "))
                        if card_selection in poss_ans:
                            card_selected = True
            # drop this card at this index
                chosen_card_to_drop = hand.cards[card_selection-1]
                decision = True
                print (f"hand object refrence{hand.cards[card_selection-1]}")
                print (f"chosen_card_to_drop should be -->{chosen_card_to_drop}")
                decision = True
        ### While loop exit, decision True 
            
        # HU DECISION TIME END ------------------------------------- 
    #back to function indent
    card_for_deck = None
#     ['Ten', 'Hearts', 8]
#     self.rank + ' of ' + self.suit
#     chosen_card_to_drop[0] + ' of ' + chosen_card_to_drop[1]
    for this_card in hand.cards:
        if this_card.rank == chosen_card_to_drop.rank and this_card.suit == chosen_card_to_drop.suit:
            card_index = hand.cards.index(this_card)
            card_for_deck = hand.cards.pop(card_index)
            print (f"card to be put in deck {card_for_deck} \n")
    new_card = deck.deal()
    deck.put_back(card_for_deck)
    hand.cards.append(new_card)
    
    for card in hand.cards:
        print (card)
    
#     top_card = deck.deal()
#     print (f"The top card is {top_card}")
#     one_and_done_suit = top_card.suit
#     deck.put_back(top_card)
#     deal
#     ef deal(self):
#         single_card = self.deck.pop()
#         return single_card
    
#     def put_back(self,card):

def card_object_is_left_bower(card_object,trump):
    trump_color = colors[trump]
    if card.rank == "Jack" and colors[card.suit] == trump_color:
        return True
    else:
        return False

def card_is_left_bower(card,trump):
    trump_color = colors[trump]
    if card[0] == "Jack" and colors[card[1]] == trump_color:
        return True
    else:
        return False



## PC and HU Decision functions ##
## PC and HU Decision functions ##

###################

## Play Phase ##
## Play Phase ##


def left_of_dealer_plays_first(position_on_table, who_called, whats_trump, table):
    
    print ("\n In left of dealer")
    chair = table_position_list[position_on_table]
    # the hand objects as of Jan 16, 2020 can only be called through the list_of_hand_objects
    this_hand = list_of_hand_objects[position_on_table]
    print (f"this should be 'this hand' object gabbledygooc {this_hand}")
    if table_position_dict[chair][0:2] == "pc":
        print ("chair was pc")
        return pc_plays_a_card(chair, whats_trump, who_called, this_hand,table)

    else:
        print ("chair was hu")
        # hu_plays_a_card()
        pass

def pc_plays_a_card(chair, trump, who_called, hand, table):
    
    # if who_called == "chair_1" or who_called == "chair_3":
    #     team_that_called = "team_ns"
    # else:
    #     team_that_called = "team_ew"
    
    # left_bowers_suit = 
    
    print ("\n In pc plays a card" )
    if who_called in team_ns:
        team_that_called = team_ns
    else:
        team_that_called = team_ew
    
    print (f"this is 'team that called' -->{team_that_called}")


    if table == []:
        #pc_plays_first_card():
        # their team called
        print ("a")
        if chair in team_that_called:
            if chair == who_called:
                # play aggressive, this ordered up or called and wants to take the lead
                card_list = []
                print ("b")
                for card in hand.cards:
                # for card in hand make list with accurate rank and value
                # now that trump is locked in
                    if card.suit == trump:
                        rank = "t" + str(card.rank)
                        value = values[rank]
                    else:
                        rank = card.rank
                        value = values[rank]
                    card_list.append([card, rank, card.suit, value])

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
                
                # table.append(card_to_play)
                hand.cards.remove(card_to_play)
                print (hand.cards)
                for card in table:
                    print (card)
                # return [chair, card_to_play, table];
                return [chair, card_to_play];
                
            else:
                # this pc's partner called trump
                # play conservative (off but high)
                highest_value_card_block = max(card_list, key=lambda x: x[3] and x[3] <=6)
                
                highest_value = highest_value_card_block[3]
                choices_for_card_to_play = []
                for card in card_list:
                    if card[3] == highest_value:
                        choices_for_card_to_play.append(card)
                if len(choices_for_card_to_play) == 1:
                    highest_value_card = choices_for_card_to_play[0]
                    card_to_play = highest_value_card[0]
                if len(choices_for_card_to_play) == 0:
                    highest_value_card_block = max(card_list, key=lambda x: x[3])
                    card_to_play = highest_value_card_block[0]
                else:
                    selected_highest_value_card = random.choice(choices_for_card_to_play)
                    card_to_play = selected_highest_value_card[0]
                
                # table.append(card_to_play)
                hand.cards.remove(card_to_play)
                print (hand.cards)
                for card in table:
                    print (card)
                # return [chair, card_to_play, table];
                return [chair, card_to_play];


        else:
            # this pc's team did not call trump, the opponents did
            # play conservative (off but high)
            highest_value_card_block = max(card_list, key=lambda x: x[3] and x[3] <=6)
            
            highest_value = highest_value_card_block[3]
            choices_for_card_to_play = []
            for card in card_list:
                if card[3] == highest_value:
                    choices_for_card_to_play.append(card)
            if len(choices_for_card_to_play) == 1:
                highest_value_card = choices_for_card_to_play[0]
                card_to_play = highest_value_card[0]
            if len(choices_for_card_to_play) == 0:
                highest_value_card_block = max(card_list, key=lambda x: x[3])
                card_to_play = highest_value_card_block[0]
            else:
                selected_highest_value_card = random.choice(choices_for_card_to_play)
                card_to_play = selected_highest_value_card[0]
            
            # table.append(card_to_play)
            hand.cards.remove(card_to_play)
            print (hand.cards)
            for card in table:
                print (card)
            # return [chair, card_to_play, table];
            return [chair, card_to_play];


    else:
        # table [] is not empty, previous cards have been played
        who_played_first_card = table[0][0]
        first_card_played = table[0][1]
        if card_object_is_left_bower(first_card_played,trump):
            suit_to_follow = trump
        else: 
            suit_to_follow = first_card_played.suit
        # follow suit
        # who's winning
        # has partner played?
        # did they call trump
        # if partner winning is it with rank king or higher = T/F
        # if yes, then play low off
        # if no, play highest you can
        suit_to_follow = first_card_played.suit
        have_card_of_that_suit = False
        for card in hand.cards:
            if card.suit == suit_to_follow:
                have_card_of_that_suit = True 
        if have_card_of_that_suit == True:
            # follow suit, play highest to beat or lowest to lose
            pass
        else:
            # if you have trump 
            card_to_play = selected_highest_value_card[0]
            # table.append(card_to_play)
            hand.cards.remove(card_to_play)
            print (hand.cards)
            for card in table:
                print (card)
            # return [chair, card_to_play, table];
            return [chair, card_to_play];
            # table is not empty
            #pc_plays_another_card()
            # what is suit to follow
            # look at previous cards to see who has it and with what
            
        
    

    # Makes a choice based on offense or defense if their team called or not
    # if not lead: follow suit
        # if suit can't beat lead, then throw lower of that suit
        # if first round
            # if partner called: throw low trump 
            # unless other team picked up the right bauer 
            # elif opponents picked up: through highest non-trump
            # else lead with highest trump
        # elif (not first round): 
# Left of dealer go
#   Make decision on card and play
# Next player
#   what is suit to follow
#   Make decision on card and play
# Repeat Next player twice
# Mark Trick winner
# Trick winner plays next card
# repeat Next player Thrice


def next_player(current_player_position, table_position_list):

    print (f"last player was {current_player_position+1}")

    if current_player_position == len(table_position_list)-1:
        current_player_position = 0
    else:
        current_player_position +=1

    print (f"now next player is {current_player_position+1}")

    



def hu_plays_a_card(trump,suit_to_follow,hand):
    print ("\n HPAC FUNCTION")
    # make list of cards in hand, labeled 1-5(or less), have player pick one of the 5 (or less each round) 
    # must follow suit if not lead
    
    pass



def check_trick_for_points(who_called):
    print ("\n CTFP FUNCTION")
   
    # walk through played_cards list, if rank is highest then keep otherwise
    # move to next card, then get highest of 4 cards, what was it's position in 
    # played_cards, if 2 for example then that was the second card after the lead
    # so walking through table_positions starting at lead and going 1 more step gets you the team 
    # whom won the trick. 
    # looks at the trick and assesses in order whom won, 
    # adding up trick_scores for each team
    # Then assigns who leads next turn by changing whos_next variable
    
    pass







def check_for_team_win():
    pass



def suit_to_follow(round):
    if 2 >1:
        pass

## Play Phase ##
## Play Phase ##

### Functions ###
### Functions ###
### Functions ###

######################################

### GAME SETUP perameters ###
### GAME SETUP perameters ###
### GAME SETUP perameters ###

team_ns_score = 0
team_ew_score = 0 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Nine':1, 'Ten':2, 'Jack':3, 'Queen':4, 'King':5, 'Ace':6, 'tNine':7, 'tTen':8, 'tJick':12, 'tJack':13, 'tQueen': 9, 'tKing': 10, 'tAce':11}
colors = {"Hearts":"red", "Diamonds":"red", "Clubs":"black", "Spades":"black"}
table_position_dict_default = {'chair_1':'pc South', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'}
# table_position_dict = {'chair_1':'pc South', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'} # default all pcs

# Once trump is decided then values can be assigned more permanently



# table_position_list = ["chair_1","chair_2","chair_3","chair_4"]
# list_of_hand_objects = ["chair_1","chair_2","chair_3","chair_4"]

### GAME SETUP perameters ###
### GAME SETUP perameters ###
### GAME SETUP perameters ###

######################################

# DEV GAME Execution
# DEV GAME Execution
# DEV GAME Execution

# NOTE: regular game execution moved to storage

# how_many_humans() -->table_positions()
table_position_dict = how_many_humans()

table_position_list = [] 

for chair in table_position_dict:
    table_position_list.append(chair)

print_teams(table_position_dict)

dealers_turn = "chair_1"

list_of_hand_objects = []

for chair in table_position_list:
    # CHECK print (f"here's chair: {chair}")
    name = str(chair)
    chair = Dev_Hand(name)
    list_of_hand_objects.append(chair)


dev_deck = Dev_Deck() 
### euchre_deck.
# print ("1")
# print (dev_deck)

dev_deck.shuffle()

### DEV NOTE: Below is where I stack the deck for a particular chair based on
### which method I call from the dev classes

# dev_deck.hearts_for_dealer()

## dev_deck.hearts_for_2nd()

dev_deck.hearts_for_2nd_and_one_off_suited()

# print (f"printing dev_deck{dev_deck}")

# The below is if you want to only shuffle from a certain number down in the deck
# dev_deck.shuffle_bottom()
# print ("2")
# print (dev_deck)


for player_hand in list_of_hand_objects:
    deal_cards(player_hand,dev_deck)
    
for player_hand in list_of_hand_objects:
    print("\n")
    print (table_position_dict[str(player_hand)])
    print (f"Cards in {player_hand}'s hand")
    for card in player_hand.cards:
        print (card)
print ("\n")
one_and_done_suit = top_card_suit(dev_deck)


## TRUMP SELECTION ##
## TRUMP SELECTION ##


two_part_response = pass_or_order_up(one_and_done_suit)
# PassOOU returns a 2 list value of [true/false,str(chair) that called]
ordered_up_qm = two_part_response[0]
who_called = two_part_response[1]
print(f"Ordered up is --> {ordered_up_qm}")
if who_called[0].lower() == 'c':
    print(f"{table_position_dict[who_called]},{who_called}, ordered up")
   
    print (dealers_turn)
    print (one_and_done_suit)
## TESTING HERE
    pick_up_and_switch(dealers_turn,dealers_turn,one_and_done_suit,dev_deck,card = '')
    whats_trump = one_and_done_suit
    ### Hidden pass along to grab_top_card
### TESTING HERE

else:
    print(f"Who ordered up? --> {who_called} ")



if not ordered_up_qm: 
    whats_trump_who_called = select_trump_after_flip()
    whats_trump = whats_trump_who_called[0]
    who_called = whats_trump_who_called[1]
    print (f"what_trump is --> {whats_trump}")
    print (f"who_called is --> {who_called}")

team_ns = ["chair_1","chair_3"]
team_ew = ["chair_2","chair_4"]

# NOTE: may have to add in that when dealer is screwed their team is the one that called

## TRUMP SELECTION ##
## TRUMP SELECTION ##

########################

## Trick play ##
## Trick play ##

# point to left of dealer

# the position in the table_position_list
dealer_position = table_position_list.index(dealers_turn)

if table_position_list.index(dealers_turn) == 3:
    player_left_of_dealer = 0
else:
    player_left_of_dealer = table_position_list.index(dealers_turn)+ 1

trick_counter = 0
table = []

# trump_card_list will hold all the cards and their current value based on the 
# selected trump, looks like 
# [card rank, card suit, Trump T/F, actual value]
trump_card_list = []
for suit in suits:
    for rank in ranks:
        trump_card_list.append([rank,suit])

for card in trump_card_list:
    if card[1] == whats_trump:
        trank = 't' + card[0]
        value = values[trank]
        card.append(True)
        card.append(value)
        
    elif card_is_left_bower(card,whats_trump):
        value = values['tJick']
        card.append(True)
        card.append(value)
    else:
        value = values[card[0]]
        card.append(False)
        card.append(value)

# print([x for x in a_list])

print ([x for x in trump_card_list])


# do the sort one last time and have it for the round, 
# giving a [card.rank,actual_suit,card.value] and reference that 
# for winning or not. Also actual suit is for the left bower jumping ship  

# python debugger 
# pdb.set_trace()

while trick_counter < 6:



    if trick_counter == 0:
        chair_and_card = []
        print ("trick_counter is zero")
        chair_and_card = left_of_dealer_plays_first(player_left_of_dealer, who_called, whats_trump, table)
        print (f"this is the returned {chair_and_card}")
        who_played_it = chair_and_card[0]
        one_selected = chair_and_card[1]
        table.append(chair_and_card)
        # table = chair_and_card[2]
        print (one_selected)
        print (table)
        current_player_position = player_left_of_dealer
         # Next player x3
        next_player(current_player_position, table_position_list)

        trick_counter += 1
        # NOTE: do I want this to be whocalled or which team called?
       
        # which team won the trick, add 
    if trick_counter >= 1:
        print ("trick_counter is greater or equal to one")
        pdb.set_trace()
        break
        # trick_winner_plays_next_card()
        # Next player x3
        # which team won the trick, add

# who gets points, add
# did anybody win the game? 

# Dealer and left of dealer now have a position number in table_position_dict

### Play Functions ###
### Play Functions ###
### Play Functions ###



    
### DEV GAME execution
### DEV GAME execution
### DEV GAME execution

# To see variables, picked up from here in stackoverflow from jamk 
# https://stackoverflow.com/questions/633127/viewing-all-defined-variables
#----------------------------------------------
# def printvars():

#    tmp = globals().copy()
#    [print(k,'  :  ',v,' type:' , type(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]

# printvars()
#----------------------------------------------
# this one also kinda works, needs tinckering 
# from same site by Brian R. Bondy

# for name in vars().keys():#     print (name)# for value in vars().values():#     print (value)














