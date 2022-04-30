# elements in the queue will be [v, d(v,u)**2] where u is the application.
# compare with d(u,v)**2

from typing import List
from pq_function import *


class Priority_queue:

    def __init__(self, initial_k: List, k: int) -> None:
        self._heap = []
        self._build_heap(initial_k, k)
        self._size = k

    def size(self):
        return self._size

    def insert(self, v):
        self._size += 1
        self._heap.append(v)
        self._bubble_up(self._size-1)

    def _build_heap(self, initial_k: List, k: int):
        self._heap = [None]
        for i in range(len(initial_k)):
            self._heap.append(initial_k[i])
        for j in range(k//2, 0, -1):
            self._bubble_down(j)

    def _bubble_down(self, i: int):
        ind = i
        work = True
        while 2*ind+1 < len(self._heap) and work:
            if comp(self._heap[2*ind], self._heap[2*ind+1]):
                if comp(self._heap[2*ind], self._heap[ind]):
                    swap(self._heap, ind, 2*ind)
                    ind *= 2
                else:
                    work = False
            else:
                if comp(self._heap[2*ind+1], self._heap[ind]):
                    swap(self._heap, ind, 2*ind+1)
                    ind = 2*ind+1
                else:
                    work = False
        if 2*ind < len(self._heap) and comp(self._heap[2*ind], self._heap[ind]):
            swap(self._heap, ind, 2*ind)

    def _bubble_up(self, i: int):
        work = True
        ind = i
        while (work == True):
            work = comp(self._heap[ind], self._heap[ind//2])
            if work:
                swap(self._heap, ind//2, ind)
                ind = i//2
            if ind == 0:
                work = False

    def remove_max(self):  # or remove_min according to comp
        aux = self._heap[self._size]
        self._heap.pop()
        self._heap[1] = aux
        self._bubble_down(1)
        self._size -= 1

    def print_queue(self):
        for e in self._heap:
            print(e, end=" ")
        print()

    def queue_to_list(self):
        l = []
        for i in range(1, len(self._heap)):
            l.append(self._heap[i][:len(self._heap)-1])
        return l

    def max_element(self):  # or min according to comp
        return self._heap[1][-1]

    def prob_vector(self):
        d = 0
        for i in range(1, len(self._heap)):
            d += self._heap[i][-1]
        assert(d != 0)
        c = self.max_element()
        l = self.queue_to_list()
        p = []
        for i in range(len(self._heap)-1):
            p.append(l[i][-1]/d)
        return p
