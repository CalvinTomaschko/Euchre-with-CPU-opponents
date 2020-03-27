def pick_a_hand_give_cards_from_list(self):
        # If a certain card arrangement causes an error we need to be able to copy and paste
        # the results and have this method recreate it for us. So this takes the verticle unseparated result
        # and will distribute the cards in that manner. 


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

    big_list_final = []

    for string in big_list_minus_ofs:
        big_list_final.append(string.split())

    print (big_list_final)


    # NOW LISTED ITEMS ARE READY TO BE COMPARED TO CARD OBJECTS

    # find card objects that match text list parts
    # store those objects in this players hand
    # 
    # put this hand's current cards in a separate list
    # read all hands
    # find cards that match list
    # take those cards out of those hands, put them in this hand, replace missing cards with old cards from this hand
    # done! 

    # chair = -1
    # acceptable_answer = [1,2,3,4]
    # while chair not in acceptable_answer:
    #     chair = int(input("please select Chair # 1,2,3,or 4"))


    # copied_cards = "Eight of Circles"
    # acceptable_string_entered = False





# def acceptable_string_test(stringy):
#     print("testing string")
#     number_of_line_breaks = stringy.count("\n")
#     print (f"number of line breaks is, {number_of_line_breaks}")
#     number_of_ofs = stringy.count("of")
#     print (f"number of 'of's is, {number_of_ofs}")
#     if number_of_line_breaks == 4 and number_of_ofs == 5:
#         print ("You're probably good, but be ready for possible error exception")
#         return True
#     print ("Not quite lining up yet, try again")
#     return False



# while acceptable_string_entered == False:        
    
#     copied_cards = input("please enter copied string of cards")
#     count = 0
#     while True:
#         count += 1
#         input_text = input("Please insert a number of lines of text \n")
#         print("Count is " + str(count))
#         print("what the variable is set to first time its running the loop: ",input_text,"\n")
#     acceptable_string_entered = acceptable_string_test(copied_cards)


# turning this

# Nine of Diamonds
# Nine of Clubs
# King of Clubs
# Queen of Clubs
# Ten of Clubs

# into this

# [Nine of Diamonds,
# Nine of Clubs,
# King of Clubs,
# Queen of Clubs,
# Ten of Clubs]

# then walking through it and giving the hand those cards, filling in other cards
# into the voids left giving those cards. This could recreate every scenario of error in initial play

