def pc_left_of_dealer():
	pass

# since trump won't change anymore then I could stop using the hands objects and use
# lists instead? or should I stick with hand? and have that card pop from each hand, 
# maybe I assign a value to the cards now that trump is decided, make that part of 
# the class and write in that "method?"


# default rule pick the highest none trump card

card_list = []

# for card in hand make list
for card in hand:
	if card.suit == trump:
		rank = "t" + str(card.rank)
		value = values[rank]
	else:
		rank = card.rank
		value = values[rank]
	card_list.append([rank, card.suit, card.value])

def highest_none_trump_in_hand(card_list,rule = 0):
	# rule 0 means there is trump, if there's no trump then we'll make rule = 1
	for card_block in card_list:
		# card list looks like:
		# [[card 1 info],[card 2 info],[card 3 info],[card 4 info],[card 5 info]]
		# add a 4th info part to card info [rank, suit, value, __YES__ ]
		# default is "yes" and mark "no" as we check for conditions
		# trying to get to one card chosen that is still "yes"
				
		card_block.append("yes")
	
	highest_value = 1 	
	
	for card_block in card_list:
		# each "card block" is:
		# [rank, suit, value, yes/no]
		#    0    1      2      3 
		# First sort out values higher than trump starting at 7 and up 
		if rule == 0:
			if card_block[2] > 6: # meaning value is as high as only trump can be
				card_block[3] = "no"
				break
		# this if finds the highest value of non-trump cards so betweenin range 1-6
		if card_block[2] > highest_value:
			highest_value = card_block[2]
	# now if any valued 1-6 cards are less than the highest value they are marked "no"			
	for card_block in card_list:
		if card_block[2] < highest_value:
			card_block[3] = "no"
	
	highest_valued_none_trump_cards = []		
	
	# Usually there'll be just one high card like an off suit Ace
	# but there could be 2, or even 3, aces that would still be marked "yes"
	for card_block in card_list:
		if card_block[3] = "yes":
			highest_valued_none_trump_cards += card_block
			
	if len(highest_valued_none_trump_cards) > 1:
		which_one = randint(0,len(highest_valued_none_trump_cards)) 
	    return highest_valued_none_trump_cards[which_one][0-2]
	else:
		return highest_valued_none_trump_cards[0][0-2] 
		
	# next would be to ignore the trump sorting, I could use a 3rd perameter for this
	# 		
	
	# Now that card can be played, what's the rules for the next card
	# read cards on table in order
	# define suit to follow	
	# figure out who's winning thus far
	# if your partner is winning did he trump it?
	# if you can beat it, beat it the highest you can 
	# if you can't beat it then play the lowest following suit that you can
	# if you don't have a card of that suit do you need to trump it? 			
	# if you only have trump left then play the highest trump, 
	#  
	