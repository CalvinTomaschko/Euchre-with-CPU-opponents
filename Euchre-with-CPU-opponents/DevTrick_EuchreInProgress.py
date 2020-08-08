# Euchre, Capstone challenge
# Written by Calvin Tomaschko
# Aug 24th, 2019 
# Made as final capstone to 
# Udemy:Complete Python Bootcamp: Go from zero to hero in Python 3
# Created with guidance from the Black Jack game module


import random
import pdb

from collections import Counter


import pcPlaysACard


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
        self.value = values[self.rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
    def make_rank_trump(self,jick = False):
        if jick == True:
            old_rank = self.rank
            self.rank = "Jick"
            trump_rank = "t" + self.rank
            self.rank = trump_rank
            # print (f"old rank was {old_rank} of {self.suit}")
            # print (f"new rank is {trump_rank} of {whats_trump}")
            self.value = values[self.rank]    
            self.suit = whats_trump       
        else:
            old_rank = self.rank
            trump_rank = "t" + old_rank
            self.rank = trump_rank
            # print (f"old rank was {old_rank} of {self.suit}") 
            # print (f"new rank is {trump_rank} of {card.suit}")
            self.value = values[self.rank]


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
    
    def pick_a_hand_give_cards_from_list(self):
            # If a certain card arrangement causes an error we need to be able to copy and paste
            # the results and have this method recreate it for us. So this takes the verticle unseparated result
            # and will distribute the cards in that manner. 

        # SELECT WHICH CHAIR TO BE GIVEN THE CARDS
        chair = -1
        acceptable_answer = [1,2,3,4]
        while chair not in acceptable_answer:
            chair = input("Swapping cards from text file into \nselected chair \nplease select Chair # 1,2,3,or 4")
            if not (chair.isdigit()):
                chair = -1
                print ("That's not reading right, try again please")
            else: 
                chair = int(chair)
            # Error exception for empty string here, can't make empty string an integer

        # READ .TXT FILE WHERE OUTPUT CARDS WERE COPIED
        # THEN BREAK DOWN THE TEXT INTO LISTED ITEMS

        copy_card_file = open("Euchre-with-CPU-opponents\copyhere.txt","r")

        big_list = copy_card_file.readlines()
        copy_card_file.seek(0)
        print(copy_card_file.readlines())
        print (big_list)
        copy_card_file.close()

        # example from Kite, https://kite.com/python/answers/how-to-remove-newline-character-from-a-list-in-python

        # sample_list = ["a", "b\n", "c\n"]
        # converted_list = []
        # for element in sample_list:
        #     converted_list.append(element.strip())
        # print(converted_list)

        big_list_minus_returns = []

        for line in big_list:
            big_list_minus_returns.append(line.strip())

        print(big_list_minus_returns)

        big_list_minus_ofs = []

        for line in big_list_minus_returns:
            big_list_minus_ofs.append(line.replace(" of",''))

        print(big_list_minus_ofs)

        # https://mkyong.com/python/python-how-to-split-a-string/

        big_list_final = []


        for string in big_list_minus_ofs:
            big_list_final.append(string.split())

        print (big_list_final)

        # big_list_final looks like [['Nine', 'Diamonds'], ['Nine', 'Clubs'],...[]]

        # NOW LISTED ITEMS ARE READY TO BE COMPARED TO CARD OBJECTS

        # find card objects that match text list parts
        # store those objects in this players hand

        ## Pull the desired cards   
        desired_card_objects = []

        for card_object in self.deck:
            for card_deets in big_list_final:
                if card_object.rank == card_deets[0] and card_object.suit == card_deets[1]:  
                    desired_card_objects.append(card_object)

        # WITH A LIST OF DESIRED CARDS, make place holders where the same cards are in the deck

        for card in self.deck:
            if card in desired_card_objects:
                position = self.deck.index(card)# find card in the list using index
                self.deck[position] = "To be replaced"

       
        print ("\n")

        print (f"Length dev_deck {len(dev_deck.deck)}")
       
       
        for card in self.deck:
            print (card) 
                
        # Chair 1: 1-5
        # Chair 2: 6-10
        # Chair 3: 11-15
        # Chair 4: 16-20
        
        # NOW TO REPLACE ALL THE "TO BE REPLACED" PLACE HOLDERS 
        # take the last 5 cards and put them in

        five_cards_to_put_in = []
        five_cards_found_near_bottom = False
        i = (len(self.deck)-1) # position of last item
        
        print (f"Length self.deck-1 = {i}")

        print (f"Length dev_deck {len(dev_deck.deck)}")

        while five_cards_found_near_bottom == False:
            if self.deck[i] != "To be replaced":
                print ("found a card object")
                card_for_list = self.deck.pop(i)
                print (f"card to add {card_for_list}")
                five_cards_to_put_in.append(card_for_list)

            i -=1
            if len(five_cards_to_put_in) == 5:
                five_cards_found_near_bottom = True

        print ("\n")
        # INSERT DESIRED CARDS INTO THE DECK 
        for card in self.deck:
            print (card)
        print ("\n")
        print (five_cards_to_put_in)
        print ("\n")

        print (f"Length dev_deck {len(dev_deck.deck)}")

        for count,card in enumerate(self.deck):
            print (count)
            if card == "To be replaced":
                print("Match found")
                position = self.deck.index(card)# find card in the list using index
                swap_card = five_cards_to_put_in.pop(0)
                self.deck[position] = swap_card
                print (f"Cards left in five card list {len(five_cards_to_put_in)}")
        print ("\n")
        print (f"Length dev_deck {len(dev_deck.deck)}")

        for card in self.deck:
            print (card)

        insert_pos = 5*(chair-1)

        for card_object in desired_card_objects:
            self.deck.insert(insert_pos,card_object)
        
        print ("\n")
        print (f"Length dev_deck {len(dev_deck.deck)}")

        for card in self.deck:
            print (card)

        # print ("\ndev_deck card")
        # for card in dev_deck.deck:
            
        #     print (card)

        # turning this



        # Nine of Diamonds
        # Nine of Clubs
        # King of Clubs
        # Queen of Clubs
        # Ten of Clubs

        # into this

        # [["Nine","Diamonds"],
        # ["Nine","Clubs"],
        # ["King","Clubs"],
        # [Queen","Clubs],
        # [Ten","Clubs]]


    def repeat_deck_from_list(self):
            # If a certain card arrangement causes an error we need to be able to copy and paste
            # the results and have this method recreate it for us. So this takes the verticle unseparated result
            # and will distribute the cards in that manner. 


        # READ .TXT FILE WHERE OUTPUT CARDS WERE COPIED
        # THEN BREAK DOWN THE TEXT INTO LISTED ITEMS

        copy_card_file = open("Euchre-with-CPU-opponents\CopyDeckHere.txt","r")

        big_list = copy_card_file.readlines()
        copy_card_file.seek(0)
        # print(copy_card_file.readlines())
        # print (big_list)
        copy_card_file.close()

        # example from Kite, https://kite.com/python/answers/how-to-remove-newline-character-from-a-list-in-python

        # sample_list = ["a", "b\n", "c\n"]
        # converted_list = []
        # for element in sample_list:
        #     converted_list.append(element.strip())
        # print(converted_list)

        big_list_minus_returns = []

        for line in big_list:
            big_list_minus_returns.append(line.strip())

        # print(big_list_minus_returns)

        big_list_minus_ofs = []

        for line in big_list_minus_returns:
            big_list_minus_ofs.append(line.replace(" of",''))

        # print(big_list_minus_ofs)

        # https://mkyong.com/python/python-how-to-split-a-string/

        big_list_final = []


        for string in big_list_minus_ofs:
            big_list_final.append(string.split())

        # print (f"big_list_final is {len(big_list_final)}")

        # big_list_final looks like [['Nine', 'Diamonds'], ['Nine', 'Clubs'],...[]]

        # NOW LISTED ITEMS ARE READY TO BE COMPARED TO CARD OBJECTS
        # print (f"dev_deck.deck len is {len(self.deck)}")

        new_deck_to_replace = []

        
        for count, card_deets in enumerate(big_list_final):
            for card_object in self.deck:
                if card_object.rank == card_deets[0] and card_object.suit == card_deets[1]:
                    # pop that card out and put in desired_order_card_objects, to be put back in deck in order later 
                    position = self.deck.index(card_object)# find card in the list using index
                    card_for_new_deck = self.deck[position]
                    new_deck_to_replace.append(card_for_new_deck)
                    # print (f"found match, position {count}")
                    # Find card, pop card, insert in list where belong
                    # position = self.deck.index(card_object)# find card in the list using index
                    # card_to_move = self.deck.pop(position)
                    # self.deck.insert(count,card_to_move)
                    # self.deck.append(card_to_move)
        # Deck ought to be reorganized now
        
        # print (f"new_deck_to_replace len is {len(new_deck_to_replace)}")

        
        self.deck.clear()

        # print (f"dev.deck len is {len(self.deck)}")

        for card in new_deck_to_replace:
            self.deck.append(card)

        # print (f"dev.deck len is {len(self.deck)}")


        spacing_variables = [21,10,0]
        # print ("Mainlist        dev_deck")
        # for count, card_object in enumerate(self.deck):
        #     print (count)
        #     # print (f" {big_list_final[count]} should be --> {self.deck[count]}" )
            
        #     print("%-21s %-10s %-19s" %(big_list_final[count],"is -->",self.deck[count]))

        counter_list_suits = [0,0,0,0]
        counter_list_ranks = [0,0,0,0,0,0]

        for count, suit in enumerate(suits):
            for card in self.deck:
                if card.suit == suit:
                    counter_list_suits[count] = counter_list_suits[count] + 1
        # for count, card_deets in enumerate(big_list_final):
        for count,rank in enumerate(ranks): 
            for card in self.deck:
                if card.rank == rank:
                    counter_list_ranks[count] = counter_list_ranks[count] + 1
        # print (counter_list_suits)
        # print (counter_list_ranks)

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

class Playset:
    def __init__(self, name, who_called, trump, card_values, teams, table_position_list):
        self.name = name
        self.who_called = who_called
        self.trump = trump
        self.card_values = card_values
        self.teams = teams
        self.table_position_list = table_position_list



### Classes ###
### Classes ###
### Classes ###

################################

### Functions ###
### Functions ###
### Functions ###



def print_teams(table_position_dict):
    tdict = table_position_dict
    south = tdict["chair_1"]
    north = tdict["chair_3"]
    west = tdict["chair_2"]
    east = tdict["chair_4"]
    print (f"Team North & South is {south} and {north}")
    print (f"Team East & West is {west} and {east}")  

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
    


## PC and HU Decision functions ##
## PC and HU Decision functions ##

###################

## Play Phase ##
## Play Phase ##

def make_trump_card_list(trump_card_list):
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



def left_of_dealer_plays_first(position_on_table, who_called, whats_trump, table):
    
    print ("\n In left of dealer")
    chair = table_position_list[position_on_table]
    # the hand objects as of Jan 16, 2020 can only be called through the list_of_hand_objects
    this_hand = list_of_hand_objects[position_on_table]
    print (f"this is {this_hand}")
    if table_position_dict[chair][0:2] == "pc":
        print ("chair was pc")
        # playset_round_1 --> self, name, who_called, trump, card_values, teams_ns_ew
        # table_position_list? list_of_had_objects?
        return pcPlaysACard.pc_plays_a_card(position_on_table, table, list_of_hand_objects, current_playset)

    else:
        print ("left_of_dealer_plays_first function says, 'chair was hu'")
        hu_plays_a_card(position_on_table, whats_trump, who_called, table)


def whos_winning(table_list):
    '''Reply's with the chair that has played the highest value'''
   
    winning_chair_card = max(table_list, key=lambda x: x[1].value)
    print ("\n Here's the winning chair and card from the table")
    print (winning_chair_card)
    winning_chair = winning_chair_card[0]
    return winning_chair






# Moved massive mega function over into 


#   pc_plays_a_card(position_on_table, trump, who_called, table)
# pc_plays_a_card(position_on_table, trump, who_called, table, table_position_list, list_of_hand_objects)



                                # example suits_with_only_one = ["Hearts","Spades","Clubs"]

               
               


        # NOTHING BELOW THIS LINE FOR NOW
     ####################################################################   

        # Might use later

        # trump_cards_in_hand = list(filter(lambda x: x.suit == whats_trump, hand.cards))

     ####################################################





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

    return current_player_position

    



def hu_plays_a_card(position_on_table, trump, who_called, table):
    # previous arguments (trump,suit_to_follow,hand)
    print ("\n HPAC FUNCTION")
    # make list of cards in hand, labeled 1-5(or less), have player pick one of the 5 (or less each round) 
    # must follow suit if not lead

    
    chair = table_position_list[position_on_table]
    hand = list_of_hand_objects[position_on_table]
    
    print ("\nIn function hu_plays_a_card" )

    if who_called in team_ns:
        team_that_called = team_ns
    else:
        team_that_called = team_ew
    
    print (f"\nthis is 'team that called' -->{team_that_called}")
    print (f"This is who called, {who_called}")
    
    # NOTE have player pick a card then check 
    # if it's a legal play, follows suit if has that suit, 
    # future, if it trumps partner already winning, or if it loses when you could have won the hand

    # print the cards in hand out labeled 1-#ofcards, have player pick from those, check that card
   
    # Making the card list to work with
    card_list = []
    for card in hand.cards:
            rank = card.rank
            value = values[rank]
            card_list.append([card, rank, card.suit, value])

    table_is_empty = False
    
    # suit to follow
    if len(table) == 0: # so if table is empty
        table_is_empty = True
        suit_to_follow = "There is no suit to follow, the table is empty"
        print ("Table is empty, choose any card to lead")

    if len(table) > 0: # if table is not empty
        first_card_played = table[0][1]
        print (f"-->{first_card_played}<-- was first card")
        suit_to_follow = first_card_played.suit # suit to follow, if player has it


    # does hu player need to follow suit? 
    hu_has_lead_suit = False

    if table_is_empty == False: # if there are cards to compare to
        cards_in_hand_of_lead_suit = list(filter(lambda x: x[2] == suit_to_follow, card_list))

        if len(cards_in_hand_of_lead_suit) >= 1:
            hu_has_lead_suit = True
            print ("Player must follow suit")
        
        if hu_has_lead_suit == False:
            print ("Player does not have the leading suit and can play 'off suit'")
    
    
    print ("Choose a card to play by it's number")

    print (f"\nThis chairs--> {chair} <--cards")

    for count, card in enumerate(hand.cards,1):
        print (f"#{count} {card}")


    print (f"trump is {trump}")

    print (f"suit_to_follow is {suit_to_follow}") 

    acceptable_answer = list(range(1,len(card_list)+1))
    print (f"acceptable_answer = {acceptable_answer}")
    



    card_meets_criteria = False # we have to test if it follows the rules
    selected_number_card = -1 # inialized as a not acceptable answer
    # If hu player won last hand then they'd be starting this next one
    if table_is_empty == True:
        card_meets_criteria = True

        # Repeat of text could be made into a function call! Aug 2nd 2020 (below)
        
        while selected_number_card not in acceptable_answer: # Can't pick the 5th card if you only have 4
                # selected_number_card = (input("Which numbered card do you choose ex: '2'"))
                
                # placed in to speed up play and test if the rounds work aug 7th 2020
                
                selected_number_card = random.choice(acceptable_answer)

                ######## commented for testing aug 7th 2020
                # if not (selected_number_card.isdigit()):
                #     selected_number_card = -1
                #     print ("That number is not reading right, try again please")
    
                # else: 
                #     selected_number_card = int(selected_number_card)

                # if selected_number_card not in acceptable_answer:
                #     print("Looks like the number you chose was not in the acceptable range")
                
                # Error exception for empty string here, can't make empty string an integer
        
        card_chosen = card_list[selected_number_card-1]

        card_to_return = card_chosen[0]

        hand.cards.remove(card_to_return)
        
        return [chair,card_to_return];

    if table_is_empty == False: # different rules apply than if hu player was playing the first card
        
        while card_meets_criteria == False:
        
            while selected_number_card not in acceptable_answer: # Can't pick the 5th card if you only have 4
                # selected_number_card = (input("Which numbered card do you choose (ex: '2')"))
                
                # placed in to speed up play and test if the rounds work aug 7th 2020
                
                selected_number_card = random.choice(acceptable_answer)
                print (selected_number_card)
                
                ######## commented for testing aug 7th 2020
                
                # if not (selected_number_card.isdigit()):
                #     selected_number_card = -1
                #     print ("That number is not reading right, try again please")
    
                # else: 
                #     selected_number_card = int(selected_number_card)

                # if selected_number_card not in acceptable_answer:
                #     print("Looks like the number you chose was not in the acceptable range")

                # Error exception for empty string here, can't make empty string an integer

            # If they have suit to follow? did they
            # if not then card meets criteria is False
            
            card_check_good = True

            if hu_has_lead_suit == True:
                if card_list[selected_number_card-1][2] != suit_to_follow:
                    print ("Selected card is not the correct suit, please choose a card that follows suit")
                    card_check_good = False
                    print ("shuffling random choice again")
                    selected_number_card = random.choice(acceptable_answer)
                    print (selected_number_card)
                
            if card_check_good == True:
                card_meets_criteria = True    

        card_chosen = card_list[selected_number_card-1]

        card_to_return = card_chosen[0]

        hand.cards.remove(card_to_return)
        
        return [chair,card_to_return];

   
def print_table(table):
    print ("\n\nTable")
    print ("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    for i in range(4):
        if i >= len(table):
            print ("\n")
        else:
            print (f"{table[i][0]} played {table[i][1]}")
    print ("\n|______________________________|")
    print ("\n \n")



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

# DEV GAME Setup
# DEV GAME Setup---------------------------------------------------------------------------------------------

# NOTE: regular game execution moved to storage

# how_many_humans() -->table_positions()

table_position_dict = {'chair_1':'hu player 1', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'}

table_position_list = [] 

for chair in table_position_dict:
    table_position_list.append(chair)

print_teams(table_position_dict)

dealers_turn = "chair_1"

list_of_hand_objects = []
# call below "chair" chair_spot instead, as chair variable is used again
for chair in table_position_list:
    # CHECK print (f"here's chair: {chair}")
    name = str(chair)
    chair = Dev_Hand(name)
    list_of_hand_objects.append(chair)

team_ns_score = 0
team_ew_score = 0 

round_number = 0




# # #
# GAME PLAY LEVEL WORK
# # #


while team_ns_score < 10 and team_ew_score < 10: 

    # # python debugger 
    pdb.set_trace()

    round_number +=1

    print (f"\nTHIS IS ROUND NUMBER {round_number}!\n")
    print (f"\nTHIS IS ROUND NUMBER {round_number}!\n")
    print (f"\nTHIS IS ROUND NUMBER {round_number}!\n")
    print (f"\nTHIS IS ROUND NUMBER {round_number}!\n")

    print (team_ew_score)
    print (team_ns_score)

    team_ns = ["chair_1","chair_3"]
    team_ew = ["chair_2","chair_4"]

    teams_ns_ew = [team_ns, team_ew]

    dev_deck = Dev_Deck() 

    dev_deck.shuffle()

    ### DEV NOTE: Below is where I stack the deck for a particular chair based on
    ### which method I call from the dev classes

    # dev_deck.hearts_for_dealer()

    ## dev_deck.hearts_for_2nd()

    dev_deck.hearts_for_2nd_and_one_off_suited()

    # dev_deck.pick_a_hand_give_cards_from_list()

    dev_deck.repeat_deck_from_list()

    # print("Out of pick_a_hand_give_cards_from_list")

    # python debugger 
    # pdb.set_trace()

    # print (f"printing dev_deck{dev_deck}")

    # The below is if you want to only shuffle from a certain number down in the deck
    # dev_deck.shuffle_bottom()
    # print ("2")
    # print (dev_deck)


    for player_hand in list_of_hand_objects:
        deal_cards(player_hand,dev_deck)
        

    one_and_done_suit = top_card_suit(dev_deck)


    # DEV GAME Setup--------------------------------------------------------------------------
    # DEV GAME Setup



    ###########################



    ## TRUMP SELECTION ##
    ## TRUMP SELECTION ##

    whats_trump = 'Hearts'
    who_called = 'chair 2'
    print (f"what_trump is --> {whats_trump}")
    print (f"who_called is --> {who_called}")

    if who_called in team_ns:
        team_that_called = team_ns
    else:
        team_that_called = team_ew

    # NOTE: may have to add in that when dealer is screwed their team is the one that called



 
 
 
 
 
 
    ## TRUMP SELECTION ##
    ## TRUMP SELECTION ##




    ########################





    ## Trick play ##
    ## Trick play ##

    # trump_card_list will hold all the cards and their current value based on the 
    # selected trump, looks like 
    # [card rank, card suit, actual value]
    # to test if a card is trump, do an if value > 6

    # Needs to go through all cards in each hand, not each card in dev deck
    # March 2020

    # This for loop applies the new values of the now known suit of trump

    trump_color = colors[whats_trump]

    list_of_cards_in_hands = []

    for hand in list_of_hand_objects:
        for card in hand.cards:
            # changing ranks
            if card.suit == whats_trump:
                card.make_rank_trump()
            # The "Jick"
            if card.rank == "Jack" and colors[card.suit] == trump_color and card.suit != whats_trump:
                card.make_rank_trump(True)
            # For playset_round objects each card object has suit, rank, and value accurate to the round now
            list_of_cards_in_hands.append(card)
            


    team_ew_tricks_won = 0 # Both teams start at 0 tricks won
    team_ns_tricks_won = 0


    # the position in the table_position_list
    dealer_position = table_position_list.index(dealers_turn)

    if table_position_list.index(dealers_turn) == 3:
        player_left_of_dealer = 0
    else:
        player_left_of_dealer = dealer_position+1


    # do the sort one last time and have it for the round, 
    # giving a [card.rank,actual_suit,card.value] and reference that 
    # for winning or not. Also actual suit is for the left bower jumping ship  

            # # python debugger 
            # pdb.set_trace()

    current_player_position = -2

    

    tricks_played = 0

    
    
    # Call on Class Playset

    # position_on_table, table, list_of_hand_objects, current_playset

    # class Playset:
    # def __init__(self, name, who_called, trump, card_values, teams_ns_ew):
    #     self.name = name
    #     self.who_called = who_called
    #     self.trump = trump
    #     self.card_values = card_values
    #     self.teams = teams
    playset_name = "playset_round_" + str(round_number)
    playset_name = Playset("round "+ str(round_number),  who_called,  whats_trump, list_of_cards_in_hands,  teams_ns_ew , table_position_list)
    current_playset = playset_name




    while tricks_played < 5:

    # # #
    # TRICK LEVEL WORK
    # # #

        cards_played_counter = 0
        table = []

        while cards_played_counter < 4:



            # # #
            # CARD LEVEL WORK
            # # #


            # IF FIRST CARD   !!!!!ONLY FIRST ROUND!!!!!! BECAUSE PERSON LEFT OF DEALER MUST START
            if tricks_played == 0 and cards_played_counter == 0:
                
                
                chair_and_card = []
                
                # FIRST CARD
                
                chair_and_card = left_of_dealer_plays_first(player_left_of_dealer, who_called, whats_trump, table)
                who_played_it = chair_and_card[0]
                one_selected = chair_and_card[1]
                table.append(chair_and_card) # table = chair_and_card[2]
                
                # MOVING TO NEXT PLAYER
                
                current_player_position = player_left_of_dealer

                next_player_answer = next_player(current_player_position, table_position_list)
                current_player_position = next_player_answer
               
                # Show what's on the table
                print_table(table)

                # END OF IF
            
            
            
            # IF NOT THE FIRST CARD OF ENTIRE ROUND, IE START OF NEXT HAND, OR MID-HAND
            else:   
                
                # def pc_plays_a_card(position_on_table, trump, who_called, this_hand, table
                
                # NEXT CARD
                if table_position_dict[table_position_list[current_player_position]][0:2] == "pc":

                    chair_and_card = pcPlaysACard.pc_plays_a_card(current_player_position, table, list_of_hand_objects, current_playset)
                else:

                    # Add "Playset" object here 

                    chair_and_card = hu_plays_a_card(current_player_position, whats_trump, who_called, table) 
                
                who_played_it = chair_and_card[0]
                one_selected = chair_and_card[1]
                
                table.append(chair_and_card)
                
                # Show what's on the table
                print_table(table)
                # MOVING TO NEXT PLAYER 
                next_player_answer = next_player(current_player_position, table_position_list)
                current_player_position = next_player_answer
                
                print ("\n")

                # END OF IF


            cards_played_counter += 1
            print (f"cards played counter is {cards_played_counter}")
        

            

            # END OF WHILE cards_played_counter < 4

            # # #
            # CARD LEVEL WORK
            # # #
        # python debugger 
        # pdb.set_trace()
        
        print ("\n All 4 cards have been played \n")
        # Which team won the trick

        # which card won 
        winning_chair_and_card = max(table, key=lambda x: x[1].value)
        winning_chair = winning_chair_and_card[0]
        winning_card = winning_chair_and_card[1]
        # then what team were they on

        if winning_chair in team_ns:
            team_ns_tricks_won += 1
        else:
            team_ew_tricks_won += 1
        # add 1 to the team trick counter

        print (f"Team NS {team_ns_tricks_won} tricks" )
        print (f"Team EW {team_ew_tricks_won} tricks" )
        
        winning_chair_position = table_position_list.index(winning_chair)
        print (f"{winning_chair} won the last hand and gets to lead the next hand \n")
        current_player_position = winning_chair_position

        tricks_played += 1
        print (f"tricks_played is {tricks_played}")
        # print (f"IMPORTANT!!! tricks_played is {tricks_played}")

        




    # # #
    # TRICK LEVEL WORK
    # # #

    




    # After every trick is played we assess which team is awarded team points and how many
    
    print ("\n you have exited the trickplay level loop \n")

    if team_ns_tricks_won > team_ew_tricks_won:
        team_ns_score += 1
        print ("Team North South won the most tricks and gets 1 team point")
        if team_ns_tricks_won == 5 and who_called not in team_ew :
            team_ns_score += 1
            print ("Team North South won all 5 tricks and won 2 pts total")
        if who_called in team_ew:
            team_ns_score += 1
            print ("Team North South 'Euchred' since Team East West called trump and won 2 pts total!")
        if team_ns_tricks_won == 5 and who_called in team_ew:
            team_ns_score += 2
            print ("Team North South also won all 5 tricks while 'Euchreing' earning 4 Team points total! ")
    else:
        team_ew_score += 1
        print ("Team East West won the most tricks and gets 1 team point")
        if team_ew_tricks_won == 5:
            team_ew_score += 1
            print ("Team East West won all 5 tricks and won 2 pts total")
        if who_called in team_ns:
            team_ew_score += 1
            print ("Team East West 'Euchred' since Team East West called trump and won 2 pts total!")
        if team_ew_tricks_won == 5 and who_called in team_ns:
            team_ew_score += 1
            print ("Team East West also won all 5 tricks while 'Euchreing' earning 4 Team points total! ")
    
    

    print (f"team_ew_score is now {team_ew_score}")
    print (f"team_ns_score is now {team_ns_score}")

    if team_ew_score >= 10:
        print (f"\n We \n   Have \n       A \n            WINNER! \n                  Team EW with a score of {team_ew_score} ")

    if team_ew_score >= 10:
        print (f"\n We \n   Have \n       A \n            WINNER! \n                  Team NS with a score of {team_ns_score} ")

# GAME PLAY LEVEL WORK
# # #

# team_ns_score < 10 and team_ew_score < 10: 



print ("\n you have exited the gameplay loop \n")
print ("\n a team has won! \n")




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














