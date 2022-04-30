from tkinter import W
from pq_function import *
from typing import List
from Priority_queue_v import Priority_queue as pq

v = [[3], [11], [30], [2], [31], [8], [6], [13], [26], [30]]
w = [[i] for i in range(20)]
Q = pq(v+w, len(v+w))
Q.print_queue()


def divide(v: List, n: int) -> List:
    for i in range(len(v)):
        v[i] /= n
    return v


a = [i for i in range(8)]

print(divide(a, 2))
