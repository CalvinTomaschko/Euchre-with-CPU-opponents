

 # card_list is build with these ([card, rank, card.suit, value])
x9x0sdf909 = "Cardy 1"
x9x0sdf908 = "Cardy 2"
x9x0sdf907 = "Cardy 3"
x9x0sdf906 = "Cardy 4"
x9x0sdf905 = "Cardy 5"


#clubs is trump

card_list = [
[x9x0sdf909, "King", "Hearts", 5],
[x9x0sdf908, "Queen", "Hearts", 4],
[x9x0sdf907, "Nine", "Hearts", 1],
[x9x0sdf906, "Ten", "Diamonds", 2],
[x9x0sdf905, "Ace", "Spades", 6]
]

the_length = len(card_list)
print (f"the_length is --> {the_length}\n")

the_range = range(len(card_list))
print (f"the_range is --> {the_range}\n")

for i in range(len(card_list)):
    for j in range(i+1,len(card_list)):
        print (f"'i'&'j' is --> {i},{j}")

test_card_list = []


for thingy in card_list:
    test_card_list.append(thingy)

suits_with_only_one = []

for a_card in card_list:
    if a_card[2] not in suits_with_only_one:
        suits_with_only_one.append(a_card[2])

# example suits_with_only_one = ["Hearts","Spades","Clubs"]


uniquely_suited_cards = []

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

print(suits_with_only_one)

for card in card_list:
    if card[2] in suits_with_only_one:
        uniquely_suited_cards.append(card)

print (uniquely_suited_cards)

for card in uniquely_suited_cards:
    if card[3] == 6 or card[3] == 5:
        uniquely_suited_cards.remove(card)

print(uniquely_suited_cards)

# copy card_list
# empty list

# card_list = [
# [x9x0sdf909, "King", "Hearts", 5],
# [x9x0sdf908, "Queen", "Hearts", 4],
# [x9x0sdf907, "Nine", "Hearts", 1],
# [x9x0sdf906, "10", "Diamonds", 2],
# [x9x0sdf905, "Ace", "Spades", 6]
# ]




print ("\n")

# for i,card in enumerate(card_list):
#     print (i,card[2])





