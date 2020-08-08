
table = [["player 1", "card 1"],["player 2", "card 2"]]

#["player 3", "card 3"]

print ("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
for i in range(4):
    if i >= len(table):
        print ("\n")
    else:
        print (f"{table[i][0]} played {table[i][1]}")
print ("\n|______________________________|")
print ("\n \n")

