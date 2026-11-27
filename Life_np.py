import time
import matplotlib.pyplot as plt
import numpy as np
pl= np.random.randint(0,2,(20,20))
def next_generation1():
    p = np.pad(pl, pad_width=1)
    c=sum(p[1 + i:1 + i + 20, 1 + j:1 + j + 20] for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0)
    return (((pl==0) & (c==3)) | ((pl==1) &((c>=2)&(c<=3)))).astype(int)
for x in range(200):
    plt.imshow(pl, cmap="binary",vmin=False,vmax=True)
    pl=next_generation1()
    time.sleep(0.2)
    plt.title(x)
    plt.show()
