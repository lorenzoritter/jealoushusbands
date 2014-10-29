'''
Created on 29.10.2014

@author: Lorenzo Ritter
'''


class Shore:
    state = None
    boat = 0
    
    def __init__(self, s=[], b=0):
        self.state = s
        self.boat = b
          

def jealousy(current):
    for i in range(0,noCouples):
        if current.state[i] != current.state[noCouples+i]:                  # husband is not with his wife
            for j in range(noCouples, noCouples*2): 
                    if(current.state[j] == current.state[i]):     # another husband is with the wife, so jealousy occurs
                        return 1
    return 0

def alterbit(bit):
    return abs(bit - 1)

def isGood(current):                            # people on the same side as the boat are "good"
    good_people = initial.state
    for i in current.state:
        if current.state[i] == current.boat:
            good_people[i] = 1
    return good_people

def h(current):
    result = len(current.state)
    for i in current.state:
        result = result - i
    return result


def BFS():
    current = queue.pop(0)
    print("current: ", current)
    
    good_people = isGood(current)                    # people on the same side as the boat are "good"
    
    for a in range(0, len(current.state)):
       # move = a
        for b in range(0, len(current.state)):
            move = a,b
            print("move: ", move)
            following = current
            if(good_people[a]==1 and good_people[b]==1):        # check that people on a different side than the boat are not moved
                counter = 0
                for i in current.state:
                    if i in move:
                        following.state[i] = alterbit(current.state[i])     # perform the move
                        if following in searched:                           # check if state was already visited
                            print("break: ", following.state, " already searched")
                        elif jealousy(following):                         # check if there is jealousy
                            print("break: ", following.state, " not possible. A wife cannot be left with another man unless her husband is present.")
                            searched.append(following)
                            break
                        counter += 1
                if counter != 0:                                # don't move the boat if no one crossed
                    following.boat = alterbit(current.boat)     # move the boat
                    queue.append(following)
                    print(following.state, " added to queue")
                
if __name__ =='__main__':
    noCouples = 3
    couple = [0,0]
    initial = Shore([], 0)

    for i in range(0,noCouples):
        initial.state.extend(couple)    # add couples on left side
                                        # the state will be treated as wife1, wife2, wife3, ... husband1, husband2, husband3, ...
    queue = []
    queue.append(initial)                # open list
    searched = []                       # closed list
    
    round = 0
             
    while(h(queue[0]) != 0):
        round = round + 1
        print("\nRound: ", round)
        BFS()
    print("Success: ", queue[0].state)
