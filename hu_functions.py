
def hu_side_of_select_trump_after_flip():

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



def hu_side_of_pass_or_order_up(suit_of_up_card):
    
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





def hu_side_of_pick_up_and_switch():

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
                    print (card_selected)
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
