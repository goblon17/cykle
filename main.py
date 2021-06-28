from graph_class import Graph
from sys import setrecursionlimit
from timeit import default_timer as timer

setrecursionlimit(1000000)

def Hamilt(graph,v,n,k,start):
    graph.O[v] = True
    n += 1
    #print(n)
    for i in graph.get_succ(v):
        if i == start and n == graph.v:
            graph.Path[k[0]] = v
            k[0] += 1
            return True
        if not graph.O[i]:
            if Hamilt(graph,i,n,k,start):
                graph.Path[k[0]] = v
                k[0] += 1
                return True
    graph.O[v] = False
    n -= 1
    return False


def Hamilton_RobertsFlores(graph):
    graph.O = [False for i in range(graph.v + 1)]
    graph.Path = [0 for i in range(graph.v + 2)]
    start = 1
    graph.Path[1] = start
    n = 0
    k = [2]
    w = Hamilt(graph, start, n, k, start)
    #graph.Path = graph.Path[:0:-1]
    return w

def DFS_Euler(graph, v, w):
    for u in graph.get_succ(v):
        graph.rem_edge(v,u)
        DFS_Euler(graph, u, w)
    w.append(v)

def Euler(graph):
    tmp = graph.get_deg()
    for i in tmp:
        if i % 2 != 0:
            return False
    graph2 = Graph(graph.v)
    graph2.graph = graph.graph[::]
    graph.w = []
    DFS_Euler(graph2, 1, graph.w)
    return True

timer()

n = 15

nazwyeu = ["1graf30%_{:d}eu.txt".format(n),"1graf50%_{:d}eu.txt".format(n),"1graf70%_{:d}eu.txt".format(n),"0graf30%_{:d}eu.txt".format(n),"0graf50%_{:d}eu.txt".format(n),"0graf70%_{:d}eu.txt".format(n)]

for i in nazwyeu:
    graf = Graph(n)

    file = open(i, "r")

    for lin in file:
        v,u = map(int, lin.split())
        graf.add_edge(v,u)
    file.close()

    start = timer()
    Euler(graf)
    end = timer()
    print("{}: {:f} ms".format(i,(end-start) * 1000))


nazwyham = ["1graf30%_{:d}ham.txt".format(n),"1graf50%_{:d}ham.txt".format(n),"1graf70%_{:d}ham.txt".format(n),"0graf30%_{:d}ham.txt".format(n),"0graf50%_{:d}ham.txt".format(n),"0graf70%_{:d}ham.txt".format(n)]

for i in nazwyham:
    graf = Graph(n)

    file = open(i, "r")

    for lin in file:
        v,u = map(int, lin.split())
        graf.add_edge(v,u)
    file.close()
    
    start = timer()
    Hamilton_RobertsFlores(graf)
    end = timer()
    print("{}: {:f} ms".format(i,(end-start) * 1000))
