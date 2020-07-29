import pdb



def pc_plays_a_card(position_on_table, trump, who_called, table, table_position_list, list_of_hand_objects, team_that_called):
    


    chair = table_position_list[position_on_table]
    hand = list_of_hand_objects[position_on_table]
    
    print ("\nIn function pc_plays_a_card" )

    # if len(table) != 0:
    #     print ("\nCards on table")
    #     for card in table:
    #         print (card[1])
    # else:
    #     print ("\ntable is empty")


    
    print (f"\nthis is 'team that called' -->{team_that_called}")
    print (f"This is who called, {who_called}")
    
    # python debugger 
    pdb.set_trace()


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
                # print ("\nend of, this PC called trump")
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
                # print ("\nend of, this pc's partner called trump")
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
            # print ("\nend of, this PC's team did not call trump")
            return [chair, card_to_play];
    
        print ("!_!_! First cards coming as of empty table")

    else:  # TABLE [] is NOT EMPTY, previous cards have been played __________
        print ("\nTable is not empty, decide with other cards in mind\n")

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
            print ("\n_!_!_SCENARIO 1: Lead is not trump, pc has that suit, follow suit")
            
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
            print(f"!_!_! This is the card_to_play, {card_to_remove} from Scenario 1")
            return [chair, card_to_remove];


        # SCENARIO 2. Could Trump!
        # Lead suit not trump, PC does not have lead suit
        if suit_to_follow != trump and pc_has_lead_suit == False:
            print ("\n_!_!_SCENARIO 2: Lead is not trump, pc does not have that suit")
            
            # default
            min_value_cards = min(card_list, key=lambda x: x[3])
            if len(min_value_cards) > 1:
                card_to_play = random.choice(min_value_cards)
            else:
                card_to_play = min_value_cards[0]


            # NOTE: belowin cards_in_hand_of_trump here's the problem

            if has_trump == True: 
                max_card_to_play = max(cards_in_hand_of_trump, key=lambda x: x[3])
                card_to_play = max_card_to_play
            
            # this card to play is in [card, rank, card.suit, value] format
            
            card_to_remove = card_to_play[0]
            hand.cards.remove(card_to_remove)
            print(f"!_!_! This is the card_to_play, {card_to_remove} from Scenario 2")
            return [chair, card_to_remove];


        # SCENARIO 3. Who has higher trump?
        # lead suit is trump, PC has
        if suit_to_follow == trump and pc_has_lead_suit == True:
            print ("\n_!_!_SCENARIO 3: Lead is indeed trump, pc has that suit")

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
            print(f"!_!_! This is the card_to_play, {card_to_remove} from Scenario 3")
            return [chair, card_to_remove];


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
            print ("\n_!_!_SCENARIO 4 Lead is indeed trump, pc does not have that suit")

            # 9s=1, 10s=2, Js=3, Qs=3, Ks=4, As=5
            # Find single suits and get rid of one of those if it's not an ACE or KING
           
           
            # python debugger 
            
           
           
            # Checking for Single Suited
            # Checking for Single Suited
            
            # Guide for effective card to card checking

            # for i in range(len(card_list)):
            #     for j in range(i+1,len(card_list)):
            #         print (f"'i'&'j' is --> {i},{j}")

            card_to_remove = "place holder"
            
            has_unique_ace = False
            has_unique_king = False
            
            
            # ________Find all uniquely suited cards

            if len(card_list) > 2:
                print ("\nArea 1\n")
            
                # Step 1: add all suits that are in hand
                
                suits_with_only_one = [] # Think "Hearts" and "Spades"

                for card in card_list:
                    if card[2] not in suits_with_only_one:
                        suits_with_only_one.append(card[2])

                uniquely_suited_cards = []

                if len(suits_with_only_one) <= 1:
                    print ("\nArea 2\n")
                
                    for card in card_list:
                        if card[2] in suits_with_only_one:
                            uniquely_suited_cards.append(card)

                #_______ Uniquely suited cards found, if any


                #________ Now if there are uniquely suited cards, check if they're aces or kings
                # remove if so becaue generally you want to keep those
                # check for aces first maybe?
                
                if uniquely_suited_cards != []:
                    print ("\nArea 3\n")
                
                    for card in uniquely_suited_cards:

                        if card[3] == 6:
                            has_unique_ace = True
                            uniquely_suited_cards.remove(card)
                        if card[3] == 5:
                            has_unique_king = True
                            uniquely_suited_cards.remove(card)

                    print(uniquely_suited_cards)

                    if uniquely_suited_cards != []:
                        print ("\nfound a uniquely suited card!\n")
                        if len(uniquely_suited_cards) > 1:
                            card_to_play = random.choice(uniquely_suited_cards)
                        else:
                            card_to_play = uniquely_suited_cards[0]
                        
                        card_to_remove = card_to_play[0]
                        hand.cards.remove(card_to_remove)
                        print(f"!_!_! This is the card_to_play, {card_to_remove} from Scenario 4")
                        return [chair, card_to_remove];

                    # END of checking for single suited, non Ace or King
                    # END of checking for single suited, non Ace or King
                
            # If there wasn't a single of a suit card to get rid of 
            # then thread continues here to find lowest valued card
            print ("\nArea 4\n")
            print (card_to_remove)
            if card_to_remove == "place holder":
            # ALSO, IF THERE'S ONLY 1 CARD REMAINING
                print ("\nArea 7\n")

                pdb.set_trace()
                # default
                card_details_of_min_value = (min(card_list, key=lambda x: x[3])) 
                # this finds only 1 min so you must find others if they match
                min_value = card_details_of_min_value[3]
                
                # find all cards with that low value, poss multiples
                # for card in hand if value == min_value
                cards_with_min_value = []
                
                for card in card_list:
                    if card[3]==min_value:
                        cards_with_min_value.append(card)

                if len(cards_with_min_value) > 1:
                    card_to_play = random.choice(cards_with_min_value)
                else:
                    card_to_play = cards_with_min_value[0]


                card_to_remove = card_to_play[0]
                hand.cards.remove(card_to_remove)
                print(f"!_!_! This is the card_to_play, {card_to_remove} from Scenario 4")
                return [chair, card_to_remove];
            
            print ("\nArea 5\n")
