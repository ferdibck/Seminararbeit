import random
import matplotlib.pyplot as plt


def grid(x, y, p):
    state = [0, 1]
    probabilities = [1 - p, p]
    A = [[None] * y for _ in range(x)]
    edges = []
    dashededges = []

    for n in range(x):
        for m in range(y):
            # Kanten
            A[n][m] = random.choices(state, probabilities)[0]
            if n > 0 and A[n][m] == 1 and A[n - 1][m] == 1:
                edges.append(((n, m), (n - 1, m)))
            if m > 0 and A[n][m] == 1 and A[n][m - 1] == 1:
                edges.append(((n, m), (n, m - 1)))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for edge in edges:
        start, end = edge
        ax.plot([start[0], end[0]], [start[1], end[1]],
                'k-', linewidth=2, color='red')

    for n in range(x):
        for m in range(y):
            if A[n][m] == 1:
                ax.plot(n, m, 'o', markersize=5, color="red")
            else:
                ax.plot(n, m, 'o', markersize=5, color='black')

    plt.xticks([])
    plt.yticks([])
    plt.xlim(-0.5, x - 0.5)
    plt.ylim(-0.5, y - 0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


grid(15, 10, 0.7)