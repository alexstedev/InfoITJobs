from pq_function import *
from typing import List


def _bubble_up(v: List, i: int):
    work = True
    ind = i
    while (work == True):
        work = comp(v[ind], v[ind//2])
        if work:
            swap(v, ind//2, ind)
            ind = i//2
        if ind == 0:
            work = False


def _build_heap(initial_k: List, k: int):
    Heap = [None]
    for i in range(len(initial_k)):
        Heap.append(initial_k[i])
    for j in range(k//2, 0, -1):
        _bubble_down(Heap, j)
    return Heap


def _bubble_down(v: List, i: int):
    ind = i
    work = True
    while 2*ind+1 < len(v) and work:
        if comp(v[2*ind], v[2*ind+1]):
            if comp(v[2*ind], v[ind]):
                swap(v, ind, 2*ind)
                ind *= 2
            else:
                work = False
        else:
            if comp(v[2*ind+1], v[ind]):
                swap(v, ind, 2*ind+1)
                ind = 2*ind+1
            else:
                work = False
    if 2*ind < len(v) and comp(v[2*ind], v[ind]):
        swap(v, ind, 2*ind)


def _remove_min(v: List):
    aux = v[-1]
    v.pop()
    v[1] = aux
    _bubble_down(v, 1)


v = [[3], [11], [30], [2], [31], [8], [6], [13], [26], [30]]
print(v)
w = _build_heap(v, 10)
print(w)
_remove_min(w)
print(w)
