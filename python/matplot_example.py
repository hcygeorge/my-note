#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
X = np.linspace(0, 4*np.pi, 1000)
Y = np.sin(X)

#%%
X
#%%
fig, ax = plt.subplots()
ax.plot(X, Y)
fig.show()

# %%
