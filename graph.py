import random

class graph:
    def __init__(self,size):
        self.matrix=[[]]
        for i in range(size):
            self.addNode()

    def addNode(self):
        if(len(self.matrix[0])==0):
            self.matrix[0]=[0]
        else:
            #add new column
            self.matrix.append([])
            for i in range(len(self.matrix)-1):
                self.matrix[len(self.matrix)-1].append(random.randint(0,100))
            #add bottom row
            for edge,node in zip(self.matrix[len(self.matrix)-1],range(len(self.matrix)-1)):
                self.matrix[node].append(edge)
            #add last element
            self.matrix[len(self.matrix)-1].append(0)

if __name__=="__main__":
    g=graph(10)
    print g.matrix
    for i in range(len(g.matrix)-1):
        for j in range(len(g.matrix)-1):
            if g.matrix[i][j] != g.matrix[j][i]:
                print "Error: non-symmetric graph"
        if g.matrix[i][i] != 0:
            print "Error: distance to self !=0"

    
