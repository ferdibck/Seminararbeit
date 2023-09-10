import matplotlib.pyplot as plt
import numpy as np
import math

"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = ["Times New Roman"]
"""

def V(V0, x, a, b):
    while x <= 0:
        x += (a + b)
    if 0 < x < a:
        return 0
    elif a <= x <= a + b:
        return 5
    else:
        while a+b < x:
            x -= (a+b)

        if 0 < x < a:
            return 0
        elif a <= x <= a + b:
            return 5

def plot_topf(V0, a, b):
    x = np.linspace(-10, 50, 1000)
    y = [V(V0, xi, a, b) for xi in x]

    # Kasten
    plt.plot(x, y, color="blue", alpha=1.00)
    plt.fill_between(x, y, 0, color="blue", alpha=0.1)

    # Visuell

    plt.xlabel("x", fontsize=15)
    plt.ylabel("V(x)", fontsize=15)
    plt.title("Periodisches Potential", fontsize=15)
    #plt.xlim(-10, a+10)
    #plt.ylim(-1, 10)
    #plt.yticks([0])
    #plt.legend()

    ax = plt.subplot()
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_xticks([0, a, a+b])
    ax.set_xticklabels(["0", "a", "a+b"])
    ax.set_yticks([0, V0])
    ax.set_yticklabels(["0", "V0"])

    plt.show()


plot_topf(5, 10, 5)