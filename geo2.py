import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
import numpy as np
from scipy.stats import geom


def divided_left(sq, p):
    x, y, w, h = sq
    w1 = p / h
    w2 = w - w1
    return (x, y, w1, h), (x + w1, y, w2, h)

def divided_top(sq, p):
    x, y, w, h = sq
    h1 = p / w
    h2 = h - h1
    return (x, y + h2, w, h1), (x, y, w, h2)

def divided_right(sq, p):
    x, y, w, h = sq
    w1 = p / h
    w2 = w - w1
    return (x + w2, y, w1, h), (x, y, w2, h)

def divided_bottom(sq, p):
    x, y, w, h = sq
    h1 = p / w
    h2 = h - h1
    return (x, y, w, h1), (x, y + h1, w, h2)

p = 1/6
n = 25

sq2 = 0, 0, 1, 1  # x, y, w, h

fig, ax = plt.subplots(1, 1, figsize=(6, 6))

for i in range(n):
    m = i%4
    pmf = p*(1-p)**i
    if not m:
        sq1, sq2 = divided_left(sq2, pmf)
        x, y, w, h = sq1
    if m == 1:
        sq1, sq2 = divided_top(sq2, pmf)
        x, y, w, h = sq1
    if m == 2:
        sq1, sq2 = divided_right(sq2, pmf)
        x, y, w, h = sq1
    if m == 3:
        sq1, sq2 = divided_bottom(sq2, pmf)
        x, y, w, h = sq1

    fc = cm.Blues_r(i/n)
    r = patches.Rectangle(xy=(x, y), width=w, height=h, fc=fc)
    ax.add_patch(r)

# sf
x, y, w, h = sq2
r = patches.Rectangle(xy=(x, y), width=w, height=h, fc='hotpink')
ax.add_patch(r)

q = np.reciprocal(p)
q = int(q) if q.is_integer() else q
sf = w * h
ax.set_title(f'Geometric Dist. p=1/{q}, n={n}, sf={round(sf, 5)}')

ax.set_aspect('equal')
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
plt.show()