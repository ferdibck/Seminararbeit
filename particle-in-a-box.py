import matplotlib.pyplot as plt
import numpy as np
import math

#plt.rcParams['text.usetex'] = True

def V(x, a):
    if 0 < x < a:
        return 0
    else:
        return 100
    
def psi(x, n, a):
    if x <= 0 or x >= a:
        return 0
    else: return math.sqrt(2/a)*np.sin((n*math.pi)/a * x)

def E(x, n, m, a):
    return (6.626* 10**(-34))/(8*m*a**2)* n**2

def plot_topf(a):
    x = np.linspace(-10, a+10, 1000)
    x2 = np.linspace(0, a, 1000)

    n_values = [1, 2, 3, 4, 5, 6]

    y = [V(xi, a) for xi in x]

    # Kasten
    plt.plot(x, y, color = "blue", alpha=1.00)
    plt.fill_between(x, y, 0, color = "blue", alpha = 0.1)

    """
    # Wellenfunktion
    for n in n_values:
        psi_values = [psi(xi, n, a) for xi in x]
        plt.plot(x, psi_values, label=f"ψ_{n}(x)")
    """

    # Energiewerte
    for n in n_values:
        E_values = [E(xi, n, 9.11*10**(-31), a) for xi in x2]
        plt.plot(x2, E_values, label=f"n = {n}")

    # Visuell
    plt.xlabel("x", fontsize = 15)
    plt.ylabel("V(x)", fontsize = 15)
    plt.title("Unendlich hoher Potentialtopf", fontsize = 15)
    plt.xlim(-10, a+10)
    #plt.ylim(-1, 10)
    plt.ylim(0, (1+0.1)*E(0, n_values[-1], 9.11*10**(-31), a))
    plt.yticks([0])
    plt.legend()

    ax = plt.subplot()
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_xticks([0, a])
    ax.set_xticklabels(["0", "a"]) 

    plt.show()

plot_topf(20)