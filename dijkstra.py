# Created by Marcin Wilk - BSD License

from graph import graph,graph_shapes
from time import time

def dijkstra_all(g):
    """
    Helper for iterative all-pairs shortest path using dijkstra's
    """
    distances=[]
    for i in range(len(g)):
        distances.append(dijkstra(g,i))
    return distances

def dijkstra(g,source):
    """
    Iterative dijkstra's shortest path algorithm
    """
    result=list(g[source])
    remaining=list(result)

    # Iterate q times, where q is number of nodes in graph
    for q in range(len(result)):
        # Get shortest path not yet included in result
        lowestDist=min(remaining)
        if(lowestDist==float('inf')):
            # No need to proceed if all remaining distances are inf
            break
        # Mark the new node with lowest distance as visited
        nodeIdWithLowestDist=remaining.index(lowestDist)
        remaining[nodeIdWithLowestDist]=''
        # Loop over all connections to this last visited node
        for distance,iter in zip(g[nodeIdWithLowestDist],range(len(result))):
            # If the distances through this node are less than what we know
            if distance+lowestDist < result[iter]:
                # Update the result list and remaining nodes to visit list
                result[iter]=distance+lowestDist
                assert(remaining[iter]!='')
                remaining[iter]=distance+lowestDist

    return result
            
if __name__=="__main__":
    inf=float('inf')

    # Unit tests or dijkstra function

    # Visual test of random graph
    g=graph(5,shape=graph_shapes.RANDOM).matrix
    print g
    print dijkstra_all(g) 

    # Various automated tests
    g1=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,1],[5,1,5,0,1],[5,5,1,1,0]]
    assert(dijkstra_all(g1)==[[0,1,1,2,2],[1,0,2,1,2],[1,2,0,2,1],[2,1,2,0,1],[2,2,1,1,0]])

    g2=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,5],[5,1,5,0,1],[5,5,5,1,0]]
    assert(dijkstra_all(g2)==[[0,1,1,2,3],[1,0,2,1,2],[1,2,0,3,4],[2,1,3,0,1],[3,2,4,1,0]])
 
    g3=[[0,1,1,5,2],[1,0,5,4,5],[1,5,0,5,5],[5,4,5,0,1],[2,5,5,1,0]]
    assert(dijkstra_all(g3)==[[0,1,1,3,2],[1,0,2,4,3],[1,2,0,4,3],[3,4,4,0,1],[2,3,3,1,0]])

    g4=[[0,inf,5,inf,1],[inf,0,inf,inf,inf],[5,inf,0,inf,1],[inf,inf,inf,0,5],[1,inf,1,5,0]]
    assert(dijkstra_all(g4)==\
        [[0,inf,2,6,1],[inf,0,inf,inf,inf],[2,inf,0,6,1],[6,inf,6,0,5],[1,inf,1,5,0]])

    # Large input test
    g_big=graph(300,shape=graph_shapes.TWO).matrix

    timeA=time()
    dijkstra_all(g_big)
    timeB=time()

    print "Time taken on big input: ", timeB-timeA, " seconds."
