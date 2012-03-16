from graph import graph

def dijkstra(g,source):
    result=list(g[source])
    remaining=list(result)

    #skip first node (already have its neighbors)
    lowestDist=min(remaining)
    remaining[remaining.index(lowestDist)]=''

    #iterate over all nodes
    for q in range(len(result)-1):
        lowestDist=min(remaining)
        nodeIdWithLowestDist=remaining.index(lowestDist)
        remaining[nodeIdWithLowestDist]=''

        for distance,iter in zip(g[nodeIdWithLowestDist],range(len(result))):
            if distance+lowestDist < result[iter]:
                result[iter]=distance+lowestDist
                assert(remaining[iter]!='')
                remaining[iter]=distance+lowestDist
    return result
            
if __name__=="__main__":
    g=graph(16).matrix
    #g=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,1],[5,1,5,0,1],[5,5,1,1,0]]
    #g=[[0,1,1,5,5],[1,0,5,1,5],[1,5,0,5,5],[5,1,5,0,1],[5,5,5,1,0]]
    #g=[[0,1,1,5,2],[1,0,5,4,5],[1,5,0,5,5],[5,4,5,0,1],[2,5,5,1,0]]
    print g
    distances=[]
    for i in range(len(g)):
        distances.append(dijkstra(g,i))
   
    print distances

