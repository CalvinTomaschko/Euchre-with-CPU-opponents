################################

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
                self.deck.append(Card(suit,rank))

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


##################################
