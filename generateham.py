from graph_class import Graph
from random import randint

counter = 0
n = 15
gest = 0.7
liczba = n*(n-1) / 2

cykl = 1

gr = []

def random_u_v_sequence(u,v):
    w = []
    for i in range(v-u+1):
        a = randint(u,v)
        while a in w:
            a = randint(u,v)
        w.append(a)
    return w

def write_seq(graph,u,v):
    global counter
    t = random_u_v_sequence(u,v)
    first = t[-1]
    for i in range(v-u+1):
        second = t[i]
        graph.add_edge(first,second)
        gr.append([first, second])
        counter += 1
        first = second

g = Graph(n)
write_seq(g,1,n)

while(counter < gest * liczba):
    a = randint(1,n)
    b = randint(1,n)
    if not g.chk_edge(a,b):
        g.add_edge(a,b)
        gr.append([a,b])
        counter += 1

tttt = []
if not cykl:
    for i in range(len(gr)):
        x,y = gr[i]
        if x == 1 or y == 1:
            tttt.append(i)
    for i in tttt[::-1]:
        gr.pop(i)
    gr.append([1,2])


print(gest * liczba)
print(counter)

file = open("{:d}graf{:d}%_{:d}ham.txt".format(cykl, (int)(gest*100), n), "w")
for i in gr:
    file.write("{} {}\n".format(i[0], i[1]))
file.close()