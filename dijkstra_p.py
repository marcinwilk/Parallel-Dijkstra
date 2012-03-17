from dijkstra import dijkstra,dijkstra_all
from graph import graph,graph_shapes
from time import time
from psim import PSim
import random 

def dijkstra_p(g,source,p):
    comm=PSim(p)
    myRank=comm.rank
    chunkSize=len(g)/p

    result=list(g[source])
    remaining=list(g[source])

    myGraphChunk = comm.one2all_scatter(0,g)
    localResultView=comm.one2all_scatter(0,result)
    localRemainView= comm.one2all_scatter(0,remaining)

    for q in range(len(result)):
        lowestLocalDist=min(localRemainView)
        lowestLocalDistIdx=localRemainView.index(lowestLocalDist)

        gatheredCandidatesDist=comm.all2one_collect(0,lowestLocalDist)
        gatheredCandidatesIdxs=comm.all2one_collect(0,lowestLocalDistIdx+myRank*chunkSize)
        
        processWithLowestDist=-1
        addedNodeIdx=-1
        lowestOverallDistance=-1

        if myRank==0:
            lowestOverallDistance=min(gatheredCandidatesDist)
            processWithLowestDist=gatheredCandidatesDist.index(lowestOverallDistance)
            addedNodeIdx=gatheredCandidatesIdxs[processWithLowestDist]

        receivedBroadcast = \
            comm.one2all_broadcast(0,\
            (processWithLowestDist,addedNodeIdx,lowestOverallDistance,))

        if myRank==receivedBroadcast[0]:
            indexToUpdate=receivedBroadcast[1]-myRank*chunkSize
            localRemainView[indexToUpdate]=''

        for iter in range(len(localResultView)):
            potentialNewDistance = \
                    myGraphChunk[iter][receivedBroadcast[1]]+receivedBroadcast[2]
            if potentialNewDistance < localResultView[iter]:
                localResultView[iter]=potentialNewDistance
                localRemainView[iter]=potentialNewDistance

    reassembled=comm.all2one_reduce(0,localResultView)
    if myRank==0:
        return reassembled
    else:
        return []

if __name__=="__main__":
    p=16
    g=graph(400,max_edge=10000,shape=graph_shapes.RANDOM).matrix

    i=random.randint(0,len(g)-1)
    time1=time()
    expected=dijkstra(g,i)
    time2=time()
    print "Linear execution time: ",time2-time1," seconds."
    timeA=time()
    result=dijkstra_p(g,i,p)
    if(result!=[]):
        timeB=time()    
        assert(expected==result)
        print "Parallel execution time: ",timeB-timeA," seconds."
