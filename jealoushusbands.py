'''
Created on 29.10.2014

@author: Lorenzo Ritter
'''
from copy import deepcopy
import time

class Shore:
    state = None
    boat = 0
    depth = 0                           # equals path cost in this example because unit step cost = 1
    path = None
    
    def __init__(self, s=[], b=0):
        self.state = s
        self.boat = b
        self.depth = 0
        self.path = []
        
    def f(self):                        # evaluation function
        return self.depth + h(self)
          

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

def expand(shore):
    good_people = isGood(shore)                                     # people on the same side as the boat are "good"
        
    for i in range(0, len(shore.state)):                            # iterate through all possible state changes
        for j in range(i, len(shore.state)):
            following = deepcopy(shore)
            if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                following.state[i]=alterbit(following.state[i])     # move first person
                if(i != j):                                         # move second person if different from first person
                    following.state[j]=alterbit(following.state[j])
                following.boat = alterbit(following.boat)           # move boat
                if visited(following, searched):                    # check if state was already visited
                    True
                elif jealousy(following):                           # check if there is jealousy
                    searched.append(following)
                elif True:
                    following.depth = following.depth + 1           # increase depth
                    following.path.append(shore)                    # add the parent node to the path
                    queue.append(following)                         # add the node to the queue
            else:
                True


def BFS(inode):

    d = -1                                      # current depth
    
    queue.append(inode)
    noStates = 0
    
    while True:
        noStates = noStates + 1
        
        current = queue.pop(0)
        
        current.heur = h(current)
        if current.heur == 0                                    # goal check
            print("\nVisited states: ", noStates)               # if heuristic function equals 0, the goal is reached
            return current
        
        if current.depth != d:                                  # print depth if changed
            d = current.depth
            print("current depth: ", d, "\tcalculating...")
        
        expand(current)                                         # expand and add to queue (frontier)
        searched.append(current)                                # add the current node to the closed list

def DFS(inode):
    queue.append(inode)
    noStates = 0
    
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        current = queue.pop()
        
        current.heur = h(current)
        if current.heur == 0:                                           # goal check
            return current                                              # if heuristic function equals 0, the goal is reached
        
        good_people = isGood(current)                                   # people on the same side as the boat are "good"
        
        for i in range(0, len(current.state)):                          # iterate through all possible state changes
            for j in range(i, len(current.state)):
                following = deepcopy(current)
                if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                    following.state[i]=alterbit(following.state[i])     # move first person
                    if(i != j):                                         # move second person if different from first person
                        following.state[j]=alterbit(following.state[j])
                    following.boat = alterbit(following.boat)           # move boat
                    if visited(following, searched):                    # check if state was already visited
                        True
                    elif jealousy(following):                           # check if there is jealousy
                        searched.append(following)
                    elif True:
                        following.depth = following.depth + 1           # increase depth
                        following.path.append(current)                  # add the parent node to the path
                        queue.append(following)                         # add the node to the queue
                else:
                    True
        searched.append(current)                                        # add the current node to the closed list

def GBEST(inode):
    queue = []                                  # open list (frontier)
    searched = []                               # closed list
    
    queue.append(inode)
    noStates = 0
    
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        queue.sort(key=lambda Shore: Shore.f())
        
        current = queue.pop()
        
        current.heur = h(current)
        if current.heur == 0:                                           # goal check
            return current                                              # if heuristic function equals 0, the goal is reached
        
        good_people = isGood(current)                                   # people on the same side as the boat are "good"
        
        for i in range(0, len(current.state)):                          # iterate through all possible state changes
            for j in range(i, len(current.state)):
                following = deepcopy(current)
                if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                    following.state[i]=alterbit(following.state[i])     # move first person
                    if(i != j):                                         # move second person if different from first person
                        following.state[j]=alterbit(following.state[j])
                    following.boat = alterbit(following.boat)           # move boat
                    if visited(following, searched):                    # check if state was already visited
                        True
                    elif jealousy(following):                           # check if there is jealousy
                        searched.append(following)
                    elif True:
                        following.depth = following.depth + 1           # increase depth
                        following.path.append(current)                  # add the parent node to the path
                        queue.append(following)                         # add the node to the queue
                else:
                    True
        searched.append(current)                                        # add the current node to the closed list
        
def ASTAR(inode):
    queue = []                                  # open list (frontier)
    searched = []                               # closed list
    
    queue.append(inode)
    noStates = 0
    
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        queue.sort(key=lambda Shore: h(Shore))
        
        current = queue.pop()
        
        current.heur = h(current)
        if current.heur == 0:                                           # goal check
            return current                                              # if heuristic function equals 0, the goal is reached
        
        good_people = isGood(current)                                   # people on the same side as the boat are "good"
        
        for i in range(0, len(current.state)):                          # iterate through all possible state changes
            for j in range(i, len(current.state)):
                following = deepcopy(current)
                if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                    following.state[i]=alterbit(following.state[i])     # move first person
                    if(i != j):                                         # move second person if different from first person
                        following.state[j]=alterbit(following.state[j])
                    following.boat = alterbit(following.boat)           # move boat
                    if visited(following, searched):                    # check if state was already visited
                        True
                    elif jealousy(following):                           # check if there is jealousy
                        searched.append(following)
                    elif True:
                        following.depth = following.depth + 1           # increase depth
                        following.path.append(current)                  # add the parent node to the path
                        queue.append(following)                         # add the node to the queue
                else:
                    True
        searched.append(current)                                        # add the current node to the closed list
                
if __name__ =='__main__':
    noCouples = int(input("Enter the number of couples: "))
    
    time.perf_counter()
    
    couple = [0,0]
    initial = Shore([], 0)
    goal = Shore([], 0)
    path = []
    
    for i in range(0,noCouples):                    # add couples on left side of the river
        initial.state.extend(couple)                # the state will be treated as wife1, wife2, wife3, ... husband1, husband2, husband3, ...
    
    queue = []                                      # open list (frontier)
    searched = []                                   # closed list
    
    queue.append(initial)
                                                
    goal = ASTAR(initial)                           # search
    
    print("\nSuccess: ", goal.state, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.state)
    print("Path: ", path)
    print("elapsed time: %.2fs" % time.perf_counter())
