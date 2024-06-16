import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
from scipy.stats import geom

p = 1/6
n = 26

fig, ax = plt.subplots(1, 1)

x, y, w, h = 0, 1, 1, 1
pre_h = 0
for i in range(n):
    if not i%2:
        h = y
        w = p*(1-p)**i / h
        y = 0
        pre_h = h
    else:
        x = x + w
        w = 1 - x
        h = p*(1-p)**i / w
        y = pre_h - h
    if i < n - 1:
        fc = cm.Blues_r(i/n)
    else:
        fc = 'red'
    r = patches.Rectangle(xy=(x, y), width=w, height=h, fc=fc)
    ax.add_patch(r)
    if i == n - 1:
        print(w * h, w * y)

ax.set_title('Geometric Distribution (p=1/6)')
ax.set_aspect('equal')
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
plt.show()

