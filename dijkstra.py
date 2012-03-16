from graph import graph

def dijkstra(g,source):
    result=list(g[source])
    remaining=list(result)

    #iterate over all nodes
    for q in range(len(result)):
        lowestDist=min(remaining)
        nodeIdWithLowestDist=remaining.index(lowestDist)
        remaining[nodeIdWithLowestDist]=''

        for distance,iter in zip(g[nodeIdWithLowestDist],range(len(result))):
            if distance+lowestDist < result[iter]:
                result[iter]=distance+lowestDist
                assert(remaining[iter]!='')
                remaining[iter]=distance+lowestDist
        print 'result=',result
        print 'remaining=',remaining

    return result
            
if __name__=="__main__":
    #Unit tests or dijkstra function
    g=graph(16).matrix
    print g
    distances=[]
    for i in range(len(g)):
        distances.append(dijkstra(g,i))
    print distances

    distances=[]
    g1=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,1],[5,1,5,0,1],[5,5,1,1,0]]
    for i in range(len(g1)):
        distances.append(dijkstra(g1,i))
    assert(distances==[[0,1,1,2,2],[1,0,2,1,2],[1,2,0,2,1],[2,1,2,0,1],[2,2,1,1,0]])

    distances=[]
    g2=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,5],[5,1,5,0,1],[5,5,5,1,0]]
    for i in range(len(g2)):
        distances.append(dijkstra(g2,i))
    assert(distances==[[0,1,1,2,3],[1,0,2,1,2],[1,2,0,3,4],[2,1,3,0,1],[3,2,4,1,0]])
 
    distances=[]
    g3=[[0,1,1,5,2],[1,0,5,4,5],[1,5,0,5,5],[5,4,5,0,1],[2,5,5,1,0]]
    print g3
    for i in range(len(g3)):
        distances.append(dijkstra(g3,i))
    print distances
    assert(distances==[[0,1,1,3,2],[1,0,2,4,3],[1,2,0,4,3],[3,4,4,0,1],[2,3,3,1,0]])

