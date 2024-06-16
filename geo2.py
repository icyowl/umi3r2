import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
import numpy as np
from scipy.stats import geom


def divied0(sq, p):
    x, y, w, h = sq
    w1 = p / h
    w2 = w - w1
    return (x, y, w1, h), (x + w1, y, w2, h)

def divied1(sq, p):
    x, y, w, h = sq
    h1 = p / w
    h2 = h - h1
    return (x, y + h2, w, h1), (x, y, w, h2)

def divied2(sq, p):
    x, y, w, h = sq
    w1 = p / h
    w2 = w - w1
    return (x + w2, y, w1, h), (x, y, w2, h)

def divied3(sq, p):
    x, y, w, h = sq
    h1 = p / w
    h2 = h - h1
    return (x, y, w, h1), (x, y + h1, w, h2)

p = 1/99.9
q = np.reciprocal(p)
n = 400

sq2 = 0, 0, 1, 1

fig, ax = plt.subplots(1, 1)

for i in range(n):
    m = i%4
    pmf = p*(1-p)**i
    if not m:
        sq1, sq2 = divied0(sq2, pmf)
        x, y, w, h = sq1
    if m == 1:
        sq1, sq2 = divied1(sq2, pmf)
        x, y, w, h = sq1
    if m == 2:
        sq1, sq2 = divied2(sq2, pmf)
        x, y, w, h = sq1
    if m == 3:
        sq1, sq2 = divied3(sq2, pmf)
        x, y, w, h = sq1
    r = patches.Rectangle(xy=(x, y), width=w, height=h, fc=cm.Blues_r(i/n))
    # r = patches.Rectangle(xy=(x, y), width=w, height=h, fc=cm.twilight(i/n))
    ax.add_patch(r)

x, y, w, h = sq2
r = patches.Rectangle(xy=(x, y), width=w, height=h, fc='hotpink')
ax.add_patch(r)

ax.set_title(f'Geometric Distribution, p=1/{q}, n={n}')
ax.set_aspect('equal')
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
plt.show()