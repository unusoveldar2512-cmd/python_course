import time
import matplotlib.pyplot as plt
import random
pole=[[random.randint(0,1) for _ in range(20)] for _ in range(20)]# 0="мертвая" 1="живая"
# pole = [[0]*20 for _ in range(20)]
# for x, y in [(0,1), (1,2), (2,0), (2,1), (2,2)]:
#     pole[x][y] = 1
def count_of_alive(pole,x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0: continue
            if 0 <= x + i < 20 and 0 <= y + j < 20 and pole[x + i][y + j] == 1:
                count += 1

    return count
def next_generation(pole):
    new_pole=[[0 for _ in range(20)] for _ in range(20)]
    for x in range(20):
        for y in range(20):
            count=count_of_alive(pole, x, y)
            if pole[x][y]==1:
                if count>3 or count<2:new_pole[x][y]=0
                else:
                    new_pole[x][y] = 1
            elif count==3:new_pole[x][y]=1
    return new_pole

def prnt(pole):
    for x in range(20):
        for y in range(20):
            if pole[x][y]==1:print("#",end="")
            else: print(".",end="")
        print()

for x in range(200):
    plt.imshow(pole, cmap="binary", vmin=0, vmax=1)
    pole=next_generation(pole)
    time.sleep(0.5)
    plt.show()