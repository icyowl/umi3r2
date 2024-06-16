import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom

p = 1/6

fig, ax = plt.subplots(1, 1)

x = np.arange(geom.ppf(0.01, p), geom.ppf(0.99, p))
print(1 - geom.cdf(26, p))
ax.plot(x, geom.pmf(x, p), 'o', ms=8)
ax.vlines(x, 0, geom.pmf(x, p), lw=2)

ax.set_title('Geometric distribution')
plt.show()
