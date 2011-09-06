#Copyright (c) <2011> <Nathaniel Caldwell>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import BaseOptions
import random

#settings = 
class TourneySelect(BaseOptions.BaseSelect):
    def __init__(self, settings):
        BaseOptions.BaseSelect.__init__(self, settings)
    
    def getSelection(self, objectlist):
        numtomake = self.settings
        templist = []
        highesti = 0
        highestval = None
        for x in range(numtomake):
            a = random.randint(0, len(objectlist)-1)
            templist.append((objectlist[a][0], objectlist[a][1], a))
            if objectlist[a][0] > highestval:
                highestval = objectlist[a][0]
                highesti = len(templist)-1
        #templist.sort()
        #print templist
        return templist[highesti][2]
    
    def getSettingsInfo(self):
        return ["tourney size - the size of the tournament",]
    
class TourneyLowSelect(BaseOptions.BaseSelect):
    def __init__(self, settings):
        BaseOptions.BaseSelect.__init__(self, settings)
        
    def getSelection(self, objectlist):
        numtomake = self.settings
        templist = []
        lowesti = 0
        lowestval = ()
        for x in range(numtomake):
            a = random.randint(0, len(objectlist)-1)
            templist.append((objectlist[a][0], objectlist[a][1], a))
            if objectlist[a][0] < lowestval:
                lowestval = objectlist[a][0]
                lowesti = len(templist)-1
        #templist.sort()
        return templist[lowesti][2]
    
    def getSettingsInfo(self):
        return ["tourney size - the size of the tournament",]
    
#a = [(1.1, "yukkuri"), (4, "shitte"), (3.3, "itte"), (2.3, "ne"), (7, "touhou"), (2.7, "patchy"), (1.5, "aya"), (4.4, "suwako")] 