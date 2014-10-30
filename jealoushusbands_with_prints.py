'''
Created on 29.10.2014

@author: Lorenzo Ritter
'''
from copy import deepcopy
import time

class Shore:
    state = None
    boat = 0
    depth = 0
    path = None
    
    def __init__(self, s=[], b=0, d=0):
        self.state = s
        self.boat = b
        self.depth = d
        self.path = []
          

def jealousy(current):
    for i in range(0,noCouples):
        if current.state[i] != current.state[noCouples+i]:          # husband is not with his wife
            for j in range(noCouples, noCouples*2): 
                    if(current.state[j] == current.state[i]):       # another husband is with the wife, so jealousy occurs
                        return 1
    return 0

def alterbit(bit):
    return abs(bit - 1)

def isGood(shore):                                                  # people on the same side as the boat are "good"
    good_people = deepcopy(initial.state)
    for i in range(0, len(shore.state)):
        if shore.state[i] == shore.boat:
            good_people[i] = 1
    return good_people

def h(shore):
    result = len(shore.state)
    for i in shore.state:
        result = result - i
    return result

def visited(shore, searched):
    for k in range(0, len(searched)):
        if shore.state == searched[k].state and shore.boat == searched[k].boat:
            return True
    return False


def BFS(inode):
    queue = []                                  # open list (frontier)
    searched = []                               # closed list
    
    queue.append(inode)
    round = 0
    
    while True:
        round = round + 1
        print("\nVisited state: ", round)
        print("Queue:")
        for i in range(0, len(queue)):
            print(queue[i].state, queue[i].boat)
            
        if h(queue[0]) == 0:                                            # goal check
            return queue[0]
        
        current = queue.pop(0)
        print("current: ", current.state, current.boat)
        
        good_people = isGood(current)                                   # people on the same side as the boat are "good"
        
        for i in range(0, len(current.state)):
           # move = a
            for j in range(i, len(current.state)):
                move = i,j
                print("move: ", move)
                following = deepcopy(current)
                following.parent = current
                if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                    following.state[i]=alterbit(following.state[i])     # move first person
                    if(i != j):                                         # move second person if different from first person
                        following.state[j]=alterbit(following.state[j])
                    following.boat = alterbit(following.boat)           # move boat
                    if visited(following, searched):                    # check if state was already visited
                        print("break: ", following.state, following.boat, " already searched.")
                    elif jealousy(following):                           # check if there is jealousy
                        print("break: ", following.state, " not possible. A wife cannot be left with another man unless her husband is present.")
                        searched.append(following)
                    elif True:
                        following.depth = following.depth + 1           # increase depth
                        following.path.append(current)                  # add the parent node to the path
                        queue.append(following)                         # add the node to the queue
                        print(following.state, following.boat,  " added to queue")
                else:
                    print("break: not possible because boat is on the other side.")
        searched.append(current)                                        # add the current node to the closed list
                
if __name__ =='__main__':
    noCouples = 3
    couple = [0,0]
    initial = Shore([], 0, 0)
    goal = Shore([], 0, 0)
    path = []

    for i in range(0,noCouples):                # add couples on left side of the river
        initial.state.extend(couple)            # the state will be treated as wife1, wife2, wife3, ... husband1, husband2, husband3, ...
                                                
    goal = BFS(initial)                        # search
    
    print("\nSuccess: ", goal.state)
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.state)
    print("Path: ", path)
