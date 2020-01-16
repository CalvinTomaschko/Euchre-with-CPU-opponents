
# Euchre, Capstone challenge
# Written by Calvin Tomaschko
# Aug 24th, 2019
# Made as final capstone to
# Udemy:Complete Python Bootcamp: Go from zero to hero in Python 3
# Created with guidance from the Black Jack game module

################################


import hu_functions
import pc_functions
#import original_game_execution


### Classes ###
### Classes ###
### Classes ###

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

        for card in self.deck: ## Pull the desired cards
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

        for card in list_o_five_tcards:
            new_list.insert(5,card)

        if nine_for_top != []: ## Add tNine to 4th spot
            new_list.insert(-3,nine_for_top)

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

##################################

### Functions ###
### Functions ###
### Functions ###



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

    # Tells the numerical value of a given hand with trump as the signifier


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

            ### RUN FUNC IN PC.PY
            ###
            ###

            pass

        ## The ELSE is for  HU players

        else:

            ### RUN FUNC IN HU.PY
            ###
            ###

            print ("activated human decision time")




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

            ### 
            # Sent to pc_functions
            ###

            pc_functions.pc_side_of_pass_or_order_up(suit)


        ## The ELSE is for  HU players ~~~~~~~~~~~~~~~~~~~~~~~~~

        else:
            print ("activated human decision time")

            ###
            # Sent to hu_functions
            ###

            hu_functions.hu_side_of_pass_or_order_up(suit)


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

                ### 
                # Sent to pc_functions
                ###

                pc_functions.pc_side_of_pick_up_and_switch()

                pass

            else:

                ### 
                # Sent to hu_functions
                ###

                hu_functions.hu_side_of_pick_up_and_switch

    #back to function indent
    card_for_deck = None
    #     ['Ten', 'Hearts', 8]
    #     self.rank + ' of ' + self.suit
    #     chosen_card_to_drop[0] + ' of ' + chosen_card_to_drop[1]
    for this_card in hand.cards:
        if this_card.rank == chosen_card_to_drop[0] and this_card.suit == chosen_card_to_drop[1]:
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


def left_of_dealer_play_first_card():
    # Check if PC is left of dealer
    chair = dealer +1
    if table_position_dict[chair] == "pc":
        pass
        # PC decision
        # adds first card into played_cards[0].append
    # Since not PC then human decision time!
    else:
        pass
        #choose from hand a card to play


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


def lead_player_starts(whos_next):
    if trick_counter >= 6:
        # check_tricks_for_score(who_called)
        return ("let's award team points")

    if table_position_dict[chair] == "pc":
        # pc_play_a_card()
        pass
    else:
        # hu_plays_a_card()
        pass


def check_for_team_win():
    pass


def suit_to_follow(round):
    if 2 >1:
        pass


##################################

### GAME SETUP ###
### GAME SETUP ###
### GAME SETUP ###

team_ns_score = 0
team_ew_score = 0
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Nine':1, 'Ten':2, 'Jack':3, 'Queen':4, 'King':5, 'Ace':6, 'tNine':7, 'tTen':8, 'tJick':12, 'tJack':13, 'tQueen': 9, 'tKing': 10, 'tAce':11}
colors = {"Hearts":"red", "Diamonds":"red", "Clubs":"black", "Spades":"black"}
table_position_dict_default = {'chair_1':'pc South', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'}
# table_position_dict = {'chair_1':'pc South', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'} # default all pcs

# table_position_list = ["chair_1","chair_2","chair_3","chair_4"]
# list_of_hand_objects = ["chair_1","chair_2","chair_3","chair_4"]

### GAME SETUP ###
### GAME SETUP ###
### GAME SETUP ###

##################################

### DEV GAME Execution ###
### DEV GAME Execution ###
### DEV GAME Execution ###



# how_many_humans() -->table_positions()
table_position_dict = how_many_humans()

table_position_list = []

for chair in table_position_dict:
    table_position_list.append(chair)

print_teams(table_position_dict)

dealers_turn = "chair_1"

list_of_hand_objects = []

for chair in table_position_list:
    name = str(chair)
    chair = Dev_Hand(name)
    list_of_hand_objects.append(chair)


### DEV NOTE: Below is where I stack the deck for a particular chair based on
### which method I call from the dev classes

# dev_deck.hearts_for_dealer()
# dev_deck.hearts_for_2nd()
# The below A.) is if you want to only shuffle from a certain number down in the deck
    # A.) dev_deck.shuffle_bottom() # print ("2") # print (dev_deck)

dev_deck = Dev_Deck() 

dev_deck.shuffle()

dev_deck.hearts_for_2nd()


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

#get_ipython().run_line_magic('whos', '')


# TRUMP SELECTION
# ordered_up_qm =

two_part_response = pass_or_order_up(one_and_done_suit)
# PassOOU returns a 2 list value of [true/false,str(chair) that called]
ordered_up_qm = two_part_response[0]
who_called = two_part_response[1]
print(f"Ordered up is --> {ordered_up_qm}")
if who_called[0].lower() == 'c':
    print(f"{table_position_dict[who_called]},{who_called}, ordered up")

    print (dealers_turn)
    print (dealers_turn)
    print (one_and_done_suit)
## TESTING HERE
    pick_up_and_switch(dealers_turn,dealers_turn,one_and_done_suit,dev_deck,card = '')
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




### DEV GAME Execution ###
### DEV GAME Execution ###
### DEV GAME Execution ###

