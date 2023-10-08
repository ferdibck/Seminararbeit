import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lattice(xmax, ymax, zmax, p):
    state = [0,1]
    probabilities = [p, 1-p]
    L = [[[None] * zmax for _ in range(ymax)] for _ in range(xmax)]
    edges = []

    for x in range(xmax):
        for y in range(ymax):
            for z in range(zmax):
                L[x][y][z] = random.choices(state, probabilities)[0] # Knoten

                # Kanten 
                if x > 0 and L[x][y][z] == 1 and L[x - 1][y][z] == 1:
                    edges.append(((x+1, y+1, z+1), (x - 1+1, y+1, z+1)))
                if y > 0 and L[x][y][z] == 1 and L[x][y - 1][z] == 1:
                    edges.append(((x+1, y+1, z+1), (x+1, y - 1+1, z+1)))
                if z > 0 and L[x][y][z] == 1 and L[x][y][z - 1] == 1:
                    edges.append(((x+1, y+1, z+1), (x+1, y+1, z - 1+1)))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Knoten
    for x in range(xmax):
        for y in range(ymax):
            for z in range(zmax):
                if L[x][y][z] == 1:
                    ax.scatter(x+1, y+1, z+1, c='#1E3888', marker='o', s=20)
                else:
                    ax.scatter(x+1, y+1, z+1, c='#FFBA59', marker='o', s=20)

    # Kanten
    for edge in edges:
        start, end = edge
        ax.plot([start[0], end[0]], [start[1], end[1]],
                [start[2], end[2]], 'k-', linewidth=2, color='#1E3888')
        

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xticks(range(1, xmax+1))
    ax.set_yticks(range(1, ymax+1))
    ax.set_zticks(range(1, zmax+1))
    ax.grid(True)

    plt.show()


lattice(3, 3, 3, 0.5)