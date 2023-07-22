import random
import matplotlib.pyplot as plt
import numpy as np

class Vertex:
    state = None
    pos = (None, None)

    def __init__(self, s, p):
        self.state = s
        self.pos = p

    def Γ(self):
        return self.pos
    
    def ω(self):
        return self.state
    
class Edge:
    v1 = (None, None)
    v2 = (None, None)

    def __init__(self, s, e):
        self.v1 = s
        self.v2 = e

    def Vertices(self):
        return (self.v1, self.v2)
    
    def Δx(self):
        return (self.v1.Γ()[0], self.v2.Γ()[0])
    
    def Δy(self):
        return (self.v1.Γ()[1], self.v2.Γ()[1])
    
class Grid:
    M = []
    V = [[]] # Knotenmenge
    E = [] # Kantenmenge
    probabilities = [] # Wahrscheinlichkeit

    def __init__(self, xmax, ymax, p): # Konstruktor
        E = self.E
        V = self.V
        M = self.M
        V = [[None] * xmax for _ in range(ymax)]
        probablilites = self.probabilities
        probabilities = [p, 1-p]

        for y in range(ymax):
            for x in range(xmax):
                V[y][x] = Vertex(random.choices([1,0], probabilities)[0], (x+1,y+1)) # Knoten
                if V[y][x].ω() == 1:
                    M.append(V[y][x])

                # Kanten
                if x > 0 and V[y][x].ω() == 1 and V[y][x-1].ω() == 1:
                    E.append(Edge(V[y][x],V[y][x-1]))
                    E.append(Edge(V[y][x-1],V[y][x]))
                    
                if y > 0 and V[y][x].ω() == 1 and V[y-1][x].ω() == 1:
                    E.append(Edge(V[y][x],V[y-1][x]))
                    E.append(Edge(V[y-1][x],V[y][x]))

        self.V = V
        self.M = M
        self.E = E
        self.probabilities = probabilities
        
    def visual(self):
        V = self.V
        E = self.E

        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        for x in range(len(self.V[0])):
            for y in range(len(self.V)):
                xpos = V[y][x].Γ()[0]
                ypos = V[y][x].Γ()[1]

                if V[y][x].ω() == 1:
                    ax.plot(xpos, ypos, "o", markersize = 10, color = "#1E3888")
                else:
                    ax.plot(xpos, ypos, "o", markersize = 10, color = "#FFBA59")
        
        for i in range(len(E)):
            xpos = E[i].Δx()
            ypos = E[i].Δy()
            ax.plot(xpos, ypos, linewidth = 2, color = "#1E3888")

        plt.xticks(range(1,len(V[0])+1))
        plt.yticks(range(1,len(V)+1))
        plt.grid(True)
        plt.show()
            
    def findEdges(self, v1):
        E = self.E
        vE = []

        for i in range(len(E)):
            if E[i].Vertices()[0] == v1:
                vE.append(E[i])
        
        return vE
    
    def exploration(self):
        M = self.M
        Clusters = []
        visited = set()

        def dfs(v, cluster):
            visited.add(v)

            for e in self.findEdges(v):
                neighbor = e.Vertices()[1]

                if neighbor not in visited:
                    dfs(neighbor, cluster)
            
            cluster.append(v)

        for v in M:
            if v not in visited:
                cluster = []
                dfs(v, cluster)
                Clusters.append(cluster)
            
        return Clusters
    
    def size(self):
        V = self.V

        return (len(V[0]), len(V)) # x, y

    def endtoend(self):
        V = self.V
        sX = []
        zX = []
        sY = []
        zY = []

        for x in range(self.size()[0]):
            for y in range(self.size()[1]):
                sX.append(V[y][0])
                zX.append(V[y][self.size()[0]-1])
                sY.append(V[0][x])
                zY.append(V[self.size()[1]-1][x])

        output = [False, False] # x, y

        Clusters = self.exploration()

        for cluster in Clusters:
            for sv in sX:
                for zv in zX:
                    if sv in cluster and zv in cluster:
                        output[0] = True

        for cluster in Clusters:
            for sv in sY:
                for zv in zY:
                    if sv in cluster and zv in cluster:
                        output[1] = True

        return output
    
def simulation(x, y, p, n):
    results = []

    for i in range(n):
        r = Grid(x, y, p)
        results.append(r.endtoend())
    
    return results

def multisimulation(x, y, p, n):
    resultset = []

    for i in range(len(p)):
        resultset.append(0)
        result = simulation(x, y, p[i], n)
        for r in result:
            if r[0] == True or r[1] == True:
                resultset[i] = resultset[i]+1

    def plot(x, y, p, n, resultset):
        ax = plt.subplots()

        barWidth = 0.5
        N = len(p)
        xloc = np.arange(N)

        p1 = plt.bar(xloc, resultset, width=barWidth, color = "#1E3888")

        plt.ylabel("Anzahl an perkolierten Rastern n")
        plt.xlabel("Wahrscheinlichkeit p")
        plt.title("Perkolation in "+str(x)+"x"+str(y)+" Rastern")
        plt.xticks(xloc, (p))
        plt.yticks(range(0, n+1))

        plt.savefig("plot04.png")

    plot(x, y, p, n, resultset)




x = 10
y = 10
n = 10

p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

multisimulation(10,10,p,20)