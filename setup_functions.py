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


# who's dealer, randomly pick a dealer

def whos_first_dealer():
    choice = random.randint(1,4)
    first_dealer = "chair_"+ str(choice)
    player = table_position_dict[first_dealer]
    print (f'First deal is {player}')
    return first_dealer


# Deal out 5 cards


def print_teams(table_position_dict):
    tdict = table_position_dict
    south = tdict["chair_1"]
    north = tdict["chair_3"]
    west = tdict["chair_2"]
    east = tdict["chair_4"]
    print (f"Team North & South is {south} and {north}")
    print (f"Team East & West is {west} and {east}")
