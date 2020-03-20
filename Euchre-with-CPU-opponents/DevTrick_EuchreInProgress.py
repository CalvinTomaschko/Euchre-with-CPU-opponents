# Euchre, Capstone challenge
# Written by Calvin Tomaschko
# Aug 24th, 2019 
# Made as final capstone to 
# Udemy:Complete Python Bootcamp: Go from zero to hero in Python 3
# Created with guidance from the Black Jack game module


import random
import pdb

from collections import Counter





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
            print (f"old rank was {old_rank} of {self.suit}") 
            print (f"new rank is {trump_rank} of {card.suit}")
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
        return pc_plays_a_card(position_on_table, whats_trump, who_called,table)

    else:
        print ("chair was hu")
        # hu_plays_a_card()
        pass

def whos_winning(table_list):
    '''Reply's with the chair that has played the highest value'''
   
    winning_chair_card = max(table_list, key=lambda x: x[1].value)
    print ("\n Here's the winning chair and card from the table")
    print (winning_chair_card)
    winning_chair = winning_chair_card[0]
    return winning_chair














def pc_plays_a_card(position_on_table, trump, who_called, table):
    


    chair = table_position_list[position_on_table]
    hand = list_of_hand_objects[position_on_table]
    
    print ("\nIn function pc_plays_a_card" )

    if len(table) != 0:
        print ("\nCards on table")
        for card in table:
            print (card[1])
    else:
        print ("\ntable is empty")

    if who_called in team_ns:
        team_that_called = team_ns
    else:
        team_that_called = team_ew
    
    print (f"\nthis is 'team that called' -->{team_that_called}")
    print (f"This is who called, {who_called}")
    
    # Making the card list to work with
    
    card_list = []
    for card in hand.cards:
            rank = card.rank
            value = values[rank]
            card_list.append([card, rank, card.suit, value])

    print (f"\nThis chairs--> {chair} <--cards")
    for card in hand.cards:
        print (card)


    if table == []:  # TABLE IS EMPTY, picks which "style" to play ___________
        print ("\nTable is empty\n")
        
        # Same team called
        if chair in team_that_called:
                    
            if chair == who_called: # This PC called

                # play aggressive, this ordered up or called and wants to take the lead
                
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
                
                hand.cards.remove(card_to_play)
                
                # return [chair, card_to_play, table];
                print ("\nend of, this PC called trump")
                return [chair, card_to_play];
                
            else:  # this pc's partner called trump
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

                # return [chair, card_to_play, table];
                print ("\nend of, this pc's partner called trump")
                return [chair, card_to_play];


        else: # THIS PC'S TEAM DID NOT CALL trump, the opponents did __________
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

            # return [chair, card_to_play, table];
            print ("\nend of, this PC's team did not call trump")
            return [chair, card_to_play];


    else:  # TABLE [] is NOT EMPTY, previous cards have been played __________
        print ("\nTable is not empty\n")

        # Placing all potentially needed factors here (Feb 5th 2020) for now
        # then putting some behind ifs to cut back on uncessary computations

        # F> WHO LEAD
        who_played_first_card = table[0][0]
        print (f"-->{who_played_first_card}<-- played first card")
        # F> WHAT CARD WAS LEAD
        first_card_played = table[0][1]
        print (f"-->{first_card_played}<-- was first card")

        # F> WHICH TEAM IS PC ON, help us see if partner has lead later
        
        if chair in team_ns:
            this_pcs_team = team_ns
        else:
            this_pcs_team = team_ew
        print (f"-->{this_pcs_team}<-- is this pc's team")
        
        # F> WHICH CHAIR IS WINNING 
        # F> WHAT CARD WAS PLAYED
        
        if len(table) == 1:
            winning_chair = who_played_first_card
            winning_card = first_card_played
        else: 
            winning_chair_and_card = max(table, key=lambda x: x[1].value)
            winning_chair = winning_chair_and_card[0]
            winning_card = winning_chair_and_card[1]

        # F> WINNING CARD SCORE

        winning_card_value = winning_card.value

        print(f"This is the winning card, {winning_card}")
        print(f"This is the winning card's value, {winning_card_value}")

        # F> WHICH TEAM IS WINNING
        # F> PARTNER_HAS_IT T/F

        partner_has_it = False
        if winning_chair in this_pcs_team:
            partner_has_it = True
        
        # Come back to!
        # if partner_has_it == True:
        #     partner_chair_and_card = lamba x: x[0] == 
            # Do a check if they used trump to do so
            # when lead is off and they used trump, then they "trumped"
            # when lead is trump then they just followed suit

        # F> SUIT TO FOLLOW
        
        suit_to_follow = first_card_played.suit # suit to follow, if player has it
        
        # F> LEAD SUIT WAS TRUMP Y/N

        lead_suit_was_trump = False
        if suit_to_follow == trump:
            lead_suit_was_trump = True
        print (f"Lead suit was trump?-->{lead_suit_was_trump}<--")

        # F> PC HAS LEAD SUIT
        # F> CARDS IN HAND OF LEAD SUIT

        # card_list.append([card, rank, card.suit, value])

        pc_has_lead_suit = True
        cards_in_hand_of_lead_suit = list(filter(lambda x: x[2] == suit_to_follow, card_list))

        if cards_in_hand_of_lead_suit == []:
            pc_has_lead_suit = False
        print (f"PC has lead suit?-->{pc_has_lead_suit}<--")

        # F> HAS TRUMP? T/F
        # F> CARDS IN HAND OF TRUMP

        has_trump = True
        cards_in_hand_of_trump = list(filter(lambda x: x[2] == trump, card_list))
        if len(cards_in_hand_of_trump) == 0:
            has_trump = False
        print (f"Has_trump? is -->{has_trump}<--")
        
        


        # Instances to call for 
        # These will all be made for if there is only 1 other card on the table, meaning it's simplified
        # No need to calibrate if partner has it or not
        # variables are:
        #  
        #   who_played_first_card
        #   first_card_played
        #   winning_chair
        #   winning_card   &&&   winning_card_value
        #   suit_to_follow
        #   pc_has_lead_suit t/f
        #   cards_in_hand_of_lead_suit [list]
        #   lead_suit_was_trump t/f
        #   partner_has_it t/f
        #   partner_trumped t/f
        #   has_trump
        #   cards_in_hand_of_trump 

        # card_list is build with these ([card, rank, card.suit, value])


        # IF LEN(TABLE) == 1:  ____________________________________

        # SCENARIO 1. Follow suit
        # Lead suit not trump, PC has lead suit
        # if lead suit != trump and PC has trump
        if suit_to_follow != trump and pc_has_lead_suit == True:
            print ("\nScenario 1: Lead is not trump, pc has that suit, follow suit")
            
            max_card_to_play = max(cards_in_hand_of_lead_suit, key=lambda x: x[3])
            min_card_to_play = min(cards_in_hand_of_lead_suit, key=lambda x: x[3])
            
            # default play lowest
            card_to_play = min_card_to_play
            
            # unless they have more than one?
            if len(cards_in_hand_of_lead_suit) > 1:
                
            # if yes, can you beat the winning card?
                if max_card_to_play[3] > winning_card_value:
                    card_to_play = max_card_to_play 

            card_to_remove = card_to_play[0]
            # this card to play is in [card, rank, card.suit, value] format
            hand.cards.remove(card_to_remove)
            print(f"This is the card_to_play, {card_to_remove} from Scenario 1")
            return [chair, card_to_play];


        # SCENARIO 2. Could Trump!
        # Lead suit not trump, PC does not have lead suit
        if suit_to_follow != trump and pc_has_lead_suit == False:
            print ("\nScenario 2: Lead is not trump, pc does not have that suit")
            
            # default
            min_value_cards = min(card_list, key=lambda x: x[3])
            if len(min_value_cards) > 1:
                card_to_play = random.choice(min_value_cards)
            else:
                card_to_play = min_value_cards

            if has_trump == True: 
                max_card_to_play = max(cards_in_hand_of_trump, key=lambda x: x[3])
                card_to_play = max_card_to_play
            
            # this card to play is in [card, rank, card.suit, value] format
            
            card_to_remove = card_to_play[0]
            hand.cards.remove(card_to_remove)
            print(f"This is the card_to_play, {card_to_remove} from Scenario 2")
            return [chair, card_to_play];


        # SCENARIO 3. Who has higher trump?
        # lead suit is trump, PC has
        if suit_to_follow == trump and pc_has_lead_suit == True:
            print ("\nScenario 3: Lead is indeed trump, pc has that suit")

            max_card_to_play = max(cards_in_hand_of_lead_suit, key=lambda x: x[3])
            min_card_to_play = min(cards_in_hand_of_lead_suit, key=lambda x: x[3])
            # do you have more than one?
            # if yes, can you beat the winning card?

            # default play lowest
            card_to_play = min_card_to_play    
            
            # can you beat the winning card?
            if max_card_to_play[3] > winning_card_value:
                card_to_play = max_card_to_play 

            
            # hand.cards.remove(card_to_play)
            card_to_remove = card_to_play[0]
            hand.cards.remove(card_to_remove)
            print(f"This is the card_to_play, {card_to_remove} from Scenario 3")
            return [chair, card_to_play];


   #   who_played_first_card
        #   first_card_played
        #   winning_chair
        #   winning_card   &&&   winning_card_value
        #   suit_to_follow
        #   pc_has_lead_suit t/f
        #   cards_in_hand_of_lead_suit [list]
        #   lead_suit_was_trump t/f
        #   partner_has_it t/f
        #   partner_trumped t/f
        #   has_trump
        #   cards_in_hand_of_trump 

        # card_list is build with these ([card, rank, card.suit, value])

        # SCENARIO 4. You lose, play a low card, narrow amount of suits, keep aces
        # lead suit is trump, PC does not have
        if suit_to_follow == trump and pc_has_lead_suit == False:
            print ("\nScenario 2 Lead is indeed trump, pc does not have that suit")

            # 9s=1, 10s=2, Js=3, Qs=3, Ks=4, As=5
            # Find single suits and get rid of one of those if it's not an ACE or KING

            # Checking for Single Suited
            # Checking for Single Suited
            
            # Guide for effective card to card checking

            # for i in range(len(card_list)):
            #     for j in range(i+1,len(card_list)):
            #         print (f"'i'&'j' is --> {i},{j}")

            if len(card_list) < 2:
            
                # Step 1: add all suits that are in hand
                
                suits_with_only_one = [] # Think "Hearts" and "Spades"

                for card in card_list:
                    if card[2] not in suits_in_hand:
                        suits_with_only_one.append(a_card[2])

                

                # example suits_with_only_one = ["Hearts","Spades","Clubs"]

                # Step 2: Compare cards, if one card matches another, remove that suit from suit_in_hand
                

                # go through each card to look at each card info block
                for i in range(len(card_list)):
                    # look at each other card info block
                    for j in range(i+1,len(card_list)):
                        # if card info block [2] matches
                        if card_list[i][2] == card_list[j][2]:
                            # if card info block [2] is in suits_with_only_one
                            if card_list[i][2] in suits_with_only_one:
                                print (card_list[i][2],card_list[j][2])
                                suits_with_only_one.remove(card_list[i][2])
                                # delete
                
                if suits_with_only_one != []
                    print(suits_with_only_one)

                    # Step: 3: go through cards in hand, grab the one with suits in suit_with_only_one 
                    
                    uniquely_suited_cards = []
                   
                    for card in card_list:
                        if card[2] in suits_with_only_one:
                            uniquely_suited_cards.append(card)

                    print (uniquely_suited_cards)

                    # Step 4: take out Aces as 
                    for card in uniquely_suited_cards:

                        if card[3] == 6 or card[3] == 5:
                            uniquely_suited_cards.remove(card)

                    print(uniquely_suited_cards)

                    if uniquely_suited_cards != []:
                        if len(uniquely_suited_cards) > 1:
                            card_to_play = random.choice(uniquely_suited_cards)
                        else:
                            card_to_play = uniquely_suited_cards[0]
                        
                        # REMOVE CARD HERE AND RETURN   
                        return [chair, card_to_play];

                    # END of checking for single suited, non Ace or King
                    # END of checking for single suited, non Ace or King
            
            # If there wasn't a single of a suit card to get rid of 
            # then thread continues here to find lowest valued card



            for card_info in card_list:
                if card_info[2] not in suits_remaining_list:
                    suits_remaining_list.append(card_info[2]

            suit_countdown_list = []
            for suit in suits_remaining_list:
                suit_countdown_list.append([suit,5])

            # [[Hearts,5][Diamonds,5]]

            for card in card_list:
                for item in suit_countdown_list:
                    if card[2] == item[0]:
                        item[1] -= 1


            suits_with_only_one = []
            for item in suit_countdown_list:
                if item[1] == 4:
                    suits_with_only_one.append(item[1])

            
            only_of_their_suit_list = []
            for card in card_list:




            only_of_their_suit_not_ace_or_king = list(filter(lambda x: x[3] < 4, only_of_their_suit_list))

            # hand.cards.remove(card_to_play)
            pass



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

# DEV GAME Setup
# DEV GAME Setup

# NOTE: regular game execution moved to storage

# how_many_humans() -->table_positions()

table_position_dict = {'chair_1':'hu player 1', 'chair_2':'pc West', 'chair_3':'pc North', 'chair_4':'pc East'}

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
    
# for player_hand in list_of_hand_objects:
#     print("\n")
#     # print (table_position_dict[str(player_hand)])
#     # print (f"Cards in {player_hand}'s hand")
#     for card in player_hand.cards:
#         # print (card)
# # print ("\n")
one_and_done_suit = top_card_suit(dev_deck)

# DEV GAME Setup
# DEV GAME Setup

## TRUMP SELECTION ##
## TRUMP SELECTION ##

whats_trump = 'Hearts'
who_called = 'chair 2'
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

# trump_card_list will hold all the cards and their current value based on the 
# selected trump, looks like 
# [card rank, card suit, actual value]
# to test if a card is trump, do an if value > 6

# Needs to go through all cards in each hand, not each card in dev deck
# March 2020

# # python debugger 
# pdb.set_trace()

# This for loop applies the new values of the now known suit of trump

trump_color = colors[whats_trump]

for hand in list_of_hand_objects:
    for card in hand.cards:
        if card.suit == whats_trump:
            card.make_rank_trump()
        if card.rank == "Jack" and colors[card.suit] == trump_color and card.suit != whats_trump:
            card.make_rank_trump(True)

# trump_card_list = []
# make_trump_card_list(trump_card_list) # old method as of Jan 27th 2020

# # print([x for x in a_list])

# print ([x for x in trump_card_list])

# point to left of dealer

# the position in the table_position_list
dealer_position = table_position_list.index(dealers_turn)

if table_position_list.index(dealers_turn) == 3:
    player_left_of_dealer = 0
else:
    player_left_of_dealer = dealer_position+1

trick_counter = 0
table = []




# do the sort one last time and have it for the round, 
# giving a [card.rank,actual_suit,card.value] and reference that 
# for winning or not. Also actual suit is for the left bower jumping ship  



current_player_position = -2

while trick_counter < 6:

    


    if trick_counter == 0:
        chair_and_card = []
        print ("trick_counter is zero")
        chair_and_card = left_of_dealer_plays_first(player_left_of_dealer, who_called, whats_trump, table)
        who_played_it = chair_and_card[0]
        one_selected = chair_and_card[1]
        print (f"\nthis is the returned chair, {who_played_it}, and card, {one_selected}")
        table.append(chair_and_card)
        # table = chair_and_card[2]
        print (f"current player position starts as {current_player_position}")
        current_player_position = player_left_of_dealer
        print (f"A. current player position is now {current_player_position}")
         # Next player x3
        next_player_answer = next_player(current_player_position, table_position_list)
        current_player_position = next_player_answer
        print (f"B. and now, after func next_player,is {current_player_position}")    
# python debugger 
        # pdb.set_trace()
        trick_counter += 1
        # NOTE: do I want this to be whocalled or which team called?
       
        # which team won the trick, add 
    if trick_counter >= 1:
        print ("trick_counter is greater or equal to one")

        # def pc_plays_a_card(position_on_table, trump, who_called, this_hand, table)
        pc_plays_a_card(current_player_position, whats_trump, who_called, table)
        
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














