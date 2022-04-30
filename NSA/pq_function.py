from typing import List


def comp(a: List, b: List):
    return a[-1] > b[-1]


def swap(v: List, i: int, j: int):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux
