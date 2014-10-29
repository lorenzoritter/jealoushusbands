'''
Created on 28.10.2014

@author: Lorenzo Ritter
'''

noCouples = 3
 
class Person(object):
    def __init__(self, gender, shore):
        self.gender = gender
        self.shore = shore
        
class Shore:
    def __init__(self, h1=0, h2=0, h3=0, w1=0, w2=0, w3=0):
        self = [[h1,w1], [h2,w2],[h3,w3]]
    
    def jealousy(self):
        for i in range(0,noCouples-1):
            if(self[i][0] != self[i][1]):
            # husband is not with his wife
                for j in range(0,noCouples-1): 
                    if(self[j][0] == self[i][1]):
                        # another husband is with the wife, so jealousy occurs
                        return 1
        return 0

    def __str__(self):
        return "%a" % (self.__init__(0,0,0,0,0,0))

class State:
    near = None
    far = None
    onNearSide = True
    lastCross = None

    def __init__(self, n = Shore(), f = Shore()):
        self.near = n
        self.far = f

    def cross(self, people):
        self.lastCross = people
        if self.onNearSide:
            self.near -= people
            self.far += people
        else:
            self.near += people
            self.far -= people
        self.onNearSide = not self.onNearSide

    def isLegal(self):
        return self.near.isLegal() and self.far.isLegal()

    def isGoal(self):
        return not self.onNearSide and (self.near.missionaries == 0 and
                                        self.near.cannibals == 0)
        
    def __str__(self):
        nearness = lambda isNear: (isNear and ["n"] or ["f"])[0]
        legality = lambda isLegal: (isLegal and [""] or ["[i]"])[0]
        return "%s:%s%s:%s%s" % (nearness(self.onNearSide), self.near, legality(self.near.isLegal()),
                                 self.far, legality(self.far.isLegal()))

print(Shore())
    