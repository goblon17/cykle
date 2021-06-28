class Graph:
    def __init__(self,n):
        self.v = n
        self.graph = [[] for i in range(n+1)]

    def get_succ(self,v):
        return self.graph[v]

    def add_edge(self,v,u):
        self.graph[v].append(u)
        self.graph[u].append(v)

    def rem_edge(self,v,u):
        self.graph[v].remove(u)
        self.graph[u].remove(v)

    def get_deg(self):
        w = []
        for i in self.graph:
            w.append(len(i))
        return w

    def chk_edge(self,v,u):
        return u in self.graph[v]