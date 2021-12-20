# -- coding: utf-8 --
"""
Created on Mon Nov  1 22:56:53 2021

@author: ekrut
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np

def generateBoard(h,w):
    b = np.zeros(h*w)
    b.shape = (h,w)
    return (b)


def performIter(b):
    bcopy = b.copy()
    for row in range(b.shape[0]):
        for col in range(b.shape[0]):
            val = b[row,col]
            numN = countNeighbors(b, row, col)

            if val == 1:

                if numN > 3 or numN < 2:
                    bcopy[row,col] = 0

            else:
                if numN == 3:
                    bcopy[row,col] = 1
    return bcopy

def countNeighbors(b, row, col):
    # n = 2 oder n = 3 -> Zelle bleibt am Leben
    # n > 3 oder n < 2 -> Zelle stirbvt
    # wenn leer und n = 3 Zelle wird geboren


    ADJACENTS = {(-1, 1), (0, 1), (1, 1), (-1, 0),
             (1, 0), (-1, -1), (0,-1), (1,-1)}
    sum = 0
    for i in ADJACENTS:
        
        nr = (row + i[0]) % b.shape[0]
        nc = (col + i[1]) % b.shape[1]
        t = col + i[1]
        #print(nr, nc)
        v = b[nr][nc]
        if row==0 and col == 0:
            print(nr,nc, v)
        sum += v
    return sum   


if __name__ == "__main__":
    """
    b = generateBoard(10, 10)
    b[1:4,2] = 1
    print(b)
    for i in range(0,10):
        b = performIter(b)
        print(b)
        """
    b = np.array([[0, 1, 0],
       [0, 1, 0],
       [0, 1, 0]])
    b = performIter(b)
