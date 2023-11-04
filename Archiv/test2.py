import matplotlib.pyplot as plt
import numpy as np

p = np.linspace(0, 1, 100)
p_c = 0.59

y = (p - p_c) ** 1.3

plt.plot(p, y, "-")
plt.xlabel("p")
plt.xticks([0, p_c, 1])
plt.yticks([])
plt.ylabel("Leitfähigkeit (σ)")

plt.show()
