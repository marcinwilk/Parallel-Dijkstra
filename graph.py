# Created by Marcin Wilk - BSD License

import random

class graph_shapes:
    # Fully connected (complete) graph
    FULL=0
    # Each node connected to at least one other node, no cycles
    TREE=1
    # Each node is added with connection to two other nodes
    TWO=2
    # About 50% probability that any two nodes will be connected
    # (disconnected graph possible)
    RANDOM=3

class graph:

    def __init__(self,size,max_edge=100,shape=graph_shapes.FULL):
        """
        Constructor - creates a random graph based on specified parameters
        """
        self.matrix=[[]]
        for i in range(size):
            self.addNode(shape,max_edge)

    def addNode(self,shape,max_edge):
        """
        Adds a node to the graph based on specified parameters
        """
        if(len(self.matrix[0])==0):
            # If matrix is empty, initialize with one vertex
            self.matrix[0]=[0]
        else:
            # Add new column
            # This is done differently, depending on the specified shape
            # See class graph_shapes for descriptions
            if shape==graph_shapes.FULL:
                self.matrix.append([])
                for i in range(len(self.matrix)-1):
                    self.matrix[len(self.matrix)-1].append(random.randint(0,max_edge))
            elif shape==graph_shapes.TREE:
                connectedToNode=random.randint(0,len(self.matrix)-1)
                self.matrix.append([])
                for i in range(len(self.matrix)-1):
                    if i==connectedToNode:
                        self.matrix[len(self.matrix)-1].append(random.randint(0,max_edge))
                    else:
                        self.matrix[len(self.matrix)-1].append(float('inf'))
            elif shape==graph_shapes.TWO:
                connectedToNodeA=0
                connectedToNodeB=0
                if(len(self.matrix)==2):
                    connectedToNodeB=1
                elif(len(self.matrix)>2):
                    connectedToNodeA=random.randint(0,len(self.matrix)-1)
                    connectedToNodeB=random.randint(0,len(self.matrix)-1)
                    while connectedToNodeA==connectedToNodeB:
                        connectedToNodeB=random.randint(0,len(self.matrix)-1)
                self.matrix.append([])
                for i in range(len(self.matrix)-1):
                    if i==connectedToNodeA or i==connectedToNodeB:
                        self.matrix[len(self.matrix)-1].append(random.randint(0,max_edge))
                    else:
                        self.matrix[len(self.matrix)-1].append(float('inf'))
            elif shape==graph_shapes.RANDOM:
                self.matrix.append([])
                for i in range(len(self.matrix)-1):
                    if random.randint(0,1)==0:
                        self.matrix[len(self.matrix)-1].append(random.randint(0,max_edge))
                    else:
                        self.matrix[len(self.matrix)-1].append(float('inf'))
            else:
                assert(False and 'undefined shape')

            # Add bottom row based on new column (undirected graph)
            for edge,node in zip(self.matrix[len(self.matrix)-1],range(len(self.matrix)-1)):
                self.matrix[node].append(edge)

            # Add last element (distance to self)
            self.matrix[len(self.matrix)-1].append(0)

if __name__=="__main__":
    # Simple unit tests for graph generation
    g=graph(64,shape=graph_shapes.RANDOM)
    for i in range(len(g.matrix)-1):
        for j in range(len(g.matrix)-1):
            if g.matrix[i][j] != g.matrix[j][i]:
                print "Error: non-symmetric adjecency matrix"
                print "(directed graph not yet supported)"
                assert(False) 
        if g.matrix[i][i] != 0:
            print "Error: distance to self !=0"
            assert(False)

    
