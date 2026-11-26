import time
import matplotlib.pyplot as plt
import random
import numpy as np
pl=np.array([[random.randint(0,1) for x in range(20)] for y in range(20)])
def count_of_alive(x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==j==0: continue
            if  pl[(x+i)%20][(y+j)%20]==1:
                count += 1
    return count
def next_generation():
    new_pl=np.array([[0 for x in range(20)]for y in range(20)])
    for x in range(20):
        for y in range(20):
            c=count_of_alive(x,y)
            if pl[x][y]==1 and (c>3 or c<2):new_pl[x][y]=0
            elif pl[x][y]==0 and c==3:new_pl[x][y]=1
            else: new_pl[x][y]=pl[x][y]
    return new_pl
for x in range(200):
    plt.imshow(pl, cmap="binary")
    pl=next_generation()
    time.sleep(0.2)
    plt.show()