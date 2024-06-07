import random
from typing import Any, Optional
from matplotlib.backend_bases import KeyEvent
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import matplotlib as mpl

def periodic(d, i, j, v, offsets):
    n = d.shape[0] - 1

    res = 0
    for p, q in offsets:
        res += d[(i + p * v) % n, (j + q * v) % n]
    return res / 4.0


def single_diamond_square_step( w, d, s, avg, *, x_transform = 0, y_transform = 0):
    n = d.shape[0]
    v = w // 2
    diamond = [(-1 , -1 ), (-1 , 1 ), (1 , 1 ), (1 , -1 )]
    square = [(-1 , 0 ), (0 , -1 ), (1 , 0 ), (0 , 1 )]
    for i in range(v, n, w):
        for j in range(v, n, w):
            d[i, j] = avg(d, i, j, v, diamond) + random.uniform(-s, s)

    for i in range(v, n, w):
        for j in range(0, n, w):
            d[i, j] = avg(d, i, j, v, square) + random.uniform(-s, s)

    for i in range(0, n, w):
        for j in range(v, n, w):
            d[i, j] = avg(d, i, j, v, square) + random.uniform(-s, s)


def make_terrain(n, ds, bdry):
    d = np.zeros(n * n).reshape(n, n)
    w, s = n - 1, 1.0
    while w > 1:
        single_diamond_square_step(w,d, s, bdry)
        w //= 2
        s *= ds
    return d

def key_event(e: KeyEvent):
    global POINTS, START_IDX, d, n, ds
    print(e.key)
    if str(e.key) == 'r':
        print("r")
    elif str(e.key) == 'right':
        START_IDX += 64
        bdry = periodic  
        new_points = make_terrain(n, ds, bdry)
        POINTS = new_points + POINTS
        plt.imshow(POINTS, cmap="terrain")
        plt.show()  
        print("right")
    elif str(e.key) == 'left':
        START_IDX += 64
        bdry = periodic  
        POINTS = make_terrain(n, ds, bdry)
        plt.imshow(POINTS, cmap="terrain")
        plt.show()  
    elif str(e.key) == 'up':
        START_IDX += 64
        bdry = periodic  
        new_points = make_terrain(n, ds, bdry)
        plt.imshow(POINTS + new_points, cmap="terrain")
        plt.show()  
    elif str(e.key) == 'down':
        START_IDX += 64
        bdry = periodic  
        new_points = make_terrain(n, ds, bdry)
        POINTS += new_points
        plt.imshow(POINTS, cmap="terrain")
        plt.show()  


def main():
    global POINTS, FIG, n, d, ds
    n = 1 + 2**9
    d = np.zeros(n * n).reshape(n, n)
    ds = 0.5
    ds = float(input("input param R ="))
    bdry = periodic  
    POINTS = make_terrain(n, ds, bdry)
    FIG = plt.figure(figsize=(n / 100, n / 100), dpi=200).canvas.mpl_connect('key_press_event', key_event)
    plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    plt.imshow(POINTS, cmap="terrain")
    plt.savefig("diamond.png")
    plt.show()    
      


if __name__ == '__main__':
    ds = 0
    d = np.array([])
    n = 0
    POINTS = np.array([])
    FIG: Optional[Any] = None
    START_IDX: int = 0
    main()
