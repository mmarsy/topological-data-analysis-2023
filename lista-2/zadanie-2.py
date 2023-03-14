import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt
data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
barcode_data = ripser(data)['dgms'][0]
fig, ax = plt.subplots()
for i, b in enumerate(barcode_data):
    ax.plot([b[0], b[1]], [i, i], c='black')
ax.set_ylim(-1, len(barcode_data))
ax.set_xlabel('Persistence')
ax.set_ylabel('Interval')
plt.show()
diagrams = ripser(data)['dgms']
plot_diagrams(diagrams, show=True)