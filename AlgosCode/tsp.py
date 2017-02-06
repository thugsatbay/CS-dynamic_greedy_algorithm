import itertools
import random
import sys


def print_graph(graph):
    print "***===Travelling Salesman Problem Held-Karp Algorithm===***"
    print ""
    print "Nodes:",len(graph)
    print ""

    print "Weights of graph"

    for i in xrange(len(graph)):
        print graph[i] 

    print ""
    #Printing the weights / distance of each path
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                print "%i-->%i: %i" % (i, j, graph[i][j])



def held_karpDP(graph):
    distDic={}
    nodes=len(graph)
    

    #Initialize the initial distance from 0 to rest of nodes
    for x in range(1,nodes):
        distDic[(x,(0,))]=[graph[0][x],0]


    for n in range(1,nodes-1,1):
        #Forming subsets of n length
        for subset in tuple(itertools.combinations(range(1,nodes), n)):
            #To find all nodes from a route/path which are not covered yet
            for visitingNodes in range(1,nodes,1):
                #TSP does not allow to move twice over a single node
                if visitingNodes not in subset:
                    if len(subset) == 1:
                        distDic[(visitingNodes,(subset[0],))]=[graph[subset[0]][visitingNodes]+distDic[(subset[0],(0,))][0],subset[0]]
                    else:
                        #Multiple paths can exist, algorithm to find minimum path
                        minDist=float('inf')
                        nodeMinDist=-1
                        for eachNode in subset:
                            remainingSubset = list(subset)
                            del remainingSubset[remainingSubset.index(eachNode)]
                            remainingSubset = tuple(remainingSubset)
                            tempMinDist = graph[eachNode][visitingNodes]+distDic[(eachNode,remainingSubset)][0]
                            if minDist >= tempMinDist:
                                minDist = tempMinDist
                                nodeMinDist = eachNode
                        distDic[(visitingNodes,tuple(subset))]=[minDist,nodeMinDist]

    
    #Finding the returning path
    completeSubset=tuple(itertools.combinations(range(1,nodes), nodes-1))[0]
    minDist=float('inf')
    nodeMinDist=0
    for eachNode in completeSubset:
        remainingSubset = list(completeSubset)
        del remainingSubset[remainingSubset.index(eachNode)]
        remainingSubset = tuple(remainingSubset)
        tempMinDist = graph[eachNode][0]+distDic[(eachNode,remainingSubset)][0]
        if minDist >= tempMinDist:
            minDist = tempMinDist
            nodeMinDist = eachNode

    
    #Finding the final path in TSP
    subsetList=list(completeSubset)
    path=[0,nodeMinDist]
    del subsetList[subsetList.index(nodeMinDist)]
    while len(subsetList)>0:
        path.append(distDic[(path[-1],tuple(subsetList))][1])
        del subsetList[subsetList.index(path[-1])]
    path.append(0)


    print "Path Taken",list(reversed(path))
    print "Minimum Distance Required To Travel All Cities is",minDist


def greedyTSP(graph):
    
    nodesVisited=[0]
    totalDist=0
    nodes=len(graph)
    for x in xrange(nodes-1):
        minDist=float('inf')
        node=-1
        for y in xrange(nodes):
            if y not in nodesVisited:
                if graph[nodesVisited[x]][y]<minDist:
                    minDist=graph[nodesVisited[x]][y]
                    node=y
        nodesVisited.append(node)
        totalDist=totalDist+minDist
    nodesVisited.append(0)

    print "Path Taken",nodesVisited
    print "Minimum Distance Required To Travel All Cities is",totalDist+graph[nodesVisited[-2]][0]




def TSP():
    #Weight of distances of the graph
    graph=[[0,1,15,6],[2,0,7,20],[9,6,0,12],[10,4,8,0]]
    print_graph(graph)
    print ""
    print "---Dynamic Approach---"
    print ""
    held_karpDP(graph)
    print ""
    print "---Greedy Approach---"
    print ""
    greedyTSP(graph)
    print ""
    graph=[[0,1,15,6],[2,0,7,3],[9,6,0,12],[10,4,8,0]]
    print_graph(graph)
    print ""
    print "---Dynamic Approach---"
    print ""
    held_karpDP(graph)
    print ""
    print "---Greedy Approach---"
    print ""
    greedyTSP(graph)

TSP()