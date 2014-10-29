'''
Created on 28.10.2014

@author: Lorenzo Ritter
'''

#!/usr/bin/python3

# See https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# to-do: enter solution matrix to check solution to either puzzle

people_dict = {"h1": 0, "h2": 0, "h3": 0, "w1": 0, "w2": 0, "w3": 0}
people_names = list(people_dict.keys())
boat = 0

def alterbit(bit):
    return abs(bit - 1)

def jealousy(current):
    for i in [1,2,3]:
        if current["h" + str(i)] != current["w" + str(i)]:
        # husband is not with his wife
            if (current["h1"] == current["w" + str(i)]) or (current["h2"] == current["w" + str(i)]) or (current["h3"] == current["w" + str(i)]):
            # another husband is with the wife, so jealousy occurs
                return 1
    return 0

queue = [people_dict]
searched = []

def turn():
    currentShore = queue[0]
    draw(currentShore)
    global boat
    # people on the same side as the boat are "good"
    good_people = []
    for i in people_names:
        if currentShore[i] == boat:
            good_people.append(i)
    print("Available to choose from: " + ', '.join(good_people))
    
    for a in people_names:
        move = a
        for b in people_names:
            move = a,b
            # check that people on a different side than the boat are not moved
            
            boat_other = 0
            for i in people_names:
                if i in move:
                    if not (i in good_people):
                        boat_other = 1
                        print("Cannot move " + i + "; the boat is on the wrong side!\n")
                        return 0

            # check that when the move is completed, there is no jealousy
            temp_current = dict(currentShore)
            # dry-run to see if there are any jealous husbands
            for i in people_names:
                if i in move:
                    temp_current[i] = alterbit(temp_current[i])
            if jealousy(temp_current):
                print("A wife cannot be left with another man unless her husband is present. -> Discarded state ", temp_current)
                return 0
            # perform the move for real
            counter = 0
            for i in people_names:
                if i in move:
                    currentShore[i] = alterbit(currentShore[i])
                    counter += 1
            if counter != 0:
                boat = alterbit(boat) # don't move the boat if no one crossed

def draw(position_dict):
    global boat
    not_crossed = []
    crossed = []
    for i in people_names:
        if position_dict[i] == 0:
            not_crossed.append(i)
        else:
            crossed.append(i)
    print("\n" + ' '.join(not_crossed))
    if not boat:
        print('''~~B~~~~~~~~~~~~~~
    R i v e r
~~~~~~~~~~~~~~~~~''')
    else:
        print('''~~~~~~~~~~~~~~~~~
    R i v e r
~~B~~~~~~~~~~~~~~''')
    print(' '.join(crossed) + "\n")

turn_number = 0
while not (sum(people_dict[i] for i in people_names) == 6):
    turn()
    turn_number += 1
print("Congratulations! You won in " + str(turn_number) + " turns. (Minimum 11)")