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

#interface:
#getNodeByLocation(x, y) - returns nodeID
#splitNode(id)
#getNodeRegion(id)
#getNumNodes
#getWorldRegion - simply returns node 0 region
#getHierarchy - returns list of all nodes in hierarchy
#joinNodes(id) - joins nodes and all of their siblings. Collapses everything under.
#getChildren(id)
#getParent(id)
#getAllLeafNodes()

#add data like in the GraphEngine

from collections import deque

#for each node, save region, parent, children

#quadrant lookup
#quadlook[leftofhalfx?, abovehalfy?]

#have max depth, and also max hits contained in a leaf before it splits itself
quadlook = []
quadlook.append([4, 1])
quadlook.append([3, 2])

#should return (in region?, is edge?)
def fPoint(p, region):
    return ((p[0] <= region[2]) and (p[0] >= region[0]) and (p[1] <= region[3]) and (p[1] >= region[1]), True) 

class QuadTree:
    #region = (x1, y1, x2, y2) in float
    #bucketsize is the maximum number of objects in a particular section.
    #any more and they will be split.
    #objfunc is a function that takes (obj, region), and should return True if
    #that region contains the object (or a piece of it), or False if it does not.
    def __init__(self, region, bucketsize=4, edgeres=6, objfunc=fPoint):
        self.x1, self.y1, self.x2, self.y2 = self.region = region
        self.nodes = {}
        self.top = 0
        self.root=0
        self.bucketsize = bucketsize
        self.edgeres = edgeres
        self.objfunc = objfunc
        self.__makeNode(None, region, 0)
        self.leafnodes = set() #points to all of the lead nodes
        self.leafnodes.add(0)
        self.object_nodes = {}
        return
    
    #obj if the actual object to contain.
    #test_data should be None to use the objfunc, or
    #the function to use to test this object
    def addObject(self, obj, test_func=None, bucket=True, edge=False):
        self.object_nodes[obj] = set()
        o = (obj, test_func)
        nodec = self.__findContainingNodes(obj, self.objfunc if test_func is None else test_func)
        for n in nodec:
            self.__putInNode(o, n, bucket=bucket, edge=edge)
        #if edge:
        #    drop_list = [x for x in self.object_nodes[obj]]
        #    for n in drop_list:
                
        return
    
    #given an object and a region test function, efficiently
    #find all of the leaf nodes that it fits in
    def __findContainingNodes(self, obj, test_func, start_node=0):
        q = deque()
        containing = []
        q.append(start_node)
        while len(q) > 0:
            check = q.popleft()
            if check in self.leafnodes:
                tf = test_func(obj, self.nodes[check].region)
                if tf[0]:
                    containing.append((check, tf[1]))
            else:
                n = self.nodes[check]
                if test_func(obj, self.nodes[n.childQ1].region):
                    q.append(n.childQ1)
                if test_func(obj, self.nodes[n.childQ2].region):
                    q.append(n.childQ2)
                if test_func(obj, self.nodes[n.childQ3].region):
                    q.append(n.childQ3)
                if test_func(obj, self.nodes[n.childQ4].region):
                    q.append(n.childQ4)
        return containing
    
    #puts the given ocontainer in the given node, and cascades if the
    #node is over the bucketsize
    def __putInNode(self, ocontainer, node, bucket=True, edge=False):
        self.object_nodes[ocontainer[0]].add(node[0])
        self.nodes[node[0]].objectcontainers.add((ocontainer, node[1]))
        if bucket and (len(self.nodes[node[0]].objectcontainers) > self.bucketsize):
            self.__cascade(node[0], bucket, edge)
        elif edge and node[1] and (self.nodes[node[0]].depth < self.edgeres):
            self.__cascade(node[0], bucket, edge)
        return
    
    #
    def __cascade(self, node, bucket, edge):
        self.splitNode(node)
        for c in self.nodes[node].objectcontainers:
            self.object_nodes[c[0][0]].remove(node)
            tf = self.objfunc if c[0][1] is None else c[0][1]
            nn = self.__findContainingNodes(c[0][0], tf, node)
            for n in nn:
                self.__putInNode(c[0], n, bucket, edge)
        self.nodes[node].objectcontainers = set()
        return
   
    #You can only split a leaf node. (That node has no children/is pointed to by leafnodes)   
    def splitNode(self, nid):
        if nid not in self.leafnodes: return #was not a leaf node
        #get the node info
        node = self.nodes[nid]      #the node
        noder = node.getRegion()    #the node's region
        nx1, ny1, nx2, ny2 = noder  #the individual elements
        #calculate the halfway points
        hx = ((nx2 - nx1) / 2.0) + nx1 #X halfway mark
        hy = ((ny2 - ny1) / 2.0) + ny1 #Y halfway mark
        #the node's depth
        depth = node.depth + 1
        #make the nodes
        q1 = self.__makeNode(nid, (hx, ny1, nx2, hy), depth) #upper right (Quadrant 1)
        q2 = self.__makeNode(nid, (nx1, ny1, hx, hy), depth) #upper left  (Quadrant 2)
        q3 = self.__makeNode(nid, (nx1, hy, hx, ny2), depth) #lower left  (Quadrant 3)
        q4 = self.__makeNode(nid, (hx, hy, nx2, ny2), depth) #lower right (Quadrant 4)
        #set them as the children of the split node
        node.setChildren( (q1, q2, q3, q4) )
        #change leafnode info
        self.leafnodes.remove(nid) #remove old
        self.leafnodes.add(q1)
        self.leafnodes.add(q2)
        self.leafnodes.add(q3)
        self.leafnodes.add(q4)
        return (q1, q2, q3, q4)
      
    def getNodeRegion(self, nid):
        return self.nodes[nid].getRegion() 
      
    def getNodeDepth(self, nid):
        #pid = self.nodes[nid].getParent()
        #depth = 0
        #while pid != None:
        #    pid = self.nodes[pid].getParent()
        #    depth += 1
        return self.nodes[nid].depth 
   
    def getNodeByLocation(self, location):
        #test if location is out of origin region first...
        currentnode = 0
        while currentnode not in self.leafnodes:
            q = self.__getQuadrant(location, self.nodes[currentnode].getRegion())
            currentnode = self.getNodeChildren(currentnode)[q-1]
        return currentnode
      
    #returns in form of (q1, q2, q3, q4), or none if a leaf
    def getNodeChildren(self, nid):
        if nid in self.leafnodes : return None
        node = self.nodes[nid]
        return node.getChildren()
      
    def getLeafNodes(self):
        return tuple([x for x in self.leafnodes])
   
    def __getQuadrant(self, location, region):
        hx = ((region[2] - region[0]) / 2.0) + region[0] #X halfway mark
        hy = ((region[3] - region[1]) / 2.0) + region[1] #Y halfway mark
        lx = location[0] < hx
        ay = location[1] < hy
        return quadlook[lx][ay]
      
    def __makeNode(self, parent, region, depth):
        self.nodes[self.top] = Node(parent, region, depth)
        #self.nodes[self.top].setChildren
        out = self.top
        self.top += 1
        return out

#region is (x1, y1, x2, y2)      
class Node:
    def __init__(self, parentid, region, depth):
        self.parentid = parentid
        self.region = region
        self.childQ1 = None
        self.childQ2 = None
        self.childQ3 = None
        self.childQ4 = None
        self.objectcontainers = set()
        self.depth = depth
        return
   
    def getRegion(self):
        return self.region
   
    def getParent(self):
        return self.parentid
   
    #give as [Q1, Q2, Q3, Q4]
    def setChildren(self, childrenids):
        self.childQ1, self.childQ2, self.childQ3, self.childQ4 = childrenids
        return
      
    def getChildren(self):
        return (self.childQ1, self.childQ2, self.childQ3, self.childQ4)
      
    def setChildQ1(self, q1):
        self.childQ1 = q1
        return
      
    def setChildQ2(self, q2):
        self.childQ2 = q2
        return
      
    def setChildQ3(self, q3):
        self.childQ3 = q3
        return
      
    def setChildQ4(self, q4):
        self.childQ4 = q4
        return
      
    def clearChildren(self):
        self.childQ1 = None
        self.childQ2 = None
        self.childQ3 = None
        self.childQ4 = None
        return
       
