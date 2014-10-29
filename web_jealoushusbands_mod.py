'''
Created on 28.10.2014

@author: Lorenzo Ritter
'''

#!/usr/bin/python3

# See https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# to-do: enter solution matrix to check solution to either puzzle

people_dict = {"h1": 0, "h2": 0, "h3": 0, "w1": 0, "w2": 0, "w3": 0, "b": 0}

queue = [people_dict]
searched = []
following = {}
currentShore = {}
current_names = list(currentShore.keys())

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

def goodside(good_people, move):
    for i in current_names:
        if i in move:
            if not (i in good_people):
                print("Cannot move " + i + "; the boat is on the wrong side!\n")
                return 0
    return 1



def turn():
    currentShore = queue.pop(0)
#    draw(currentShore)
    
    # people on the same side as the boat are "good"
    good_people = []
    for i in current_names:
        if currentShore[i] == currentShore[6]:
            good_people.append(i)
    print("Available to choose from: " + ', '.join(good_people))
    
    for a in current_names:
        move = a
        for b in current_names:
            move = a,b
            
            # check that people on a different side than the boat are not moved
            if(goodside(good_people, move)):            
                # perform the move
                counter = 0
                for i in current_names:
                    if i in move:
                        following[i] = alterbit(currentShore[i])
                        # check if there is jealousy
                        if jealousy(following):
                            print("A wife cannot be left with another man unless her husband is present. -> Discarded state ", following)
                            searched.append(following)
                            return 0
                        counter += 1
                if counter != 0:
                    following[6] = alterbit(following[6]) # don't move the boat if no one crossed
                queue.append(following)

def draw(position_dict):
    global boat
    not_crossed = []
    crossed = []
    for i in current_names:
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
while not (sum(currentShore[i] for i in current_names) == 6):
    turn()
    turn_number += 1
print("Congratulations! You won in " + str(turn_number) + " turns. (Minimum 11)")