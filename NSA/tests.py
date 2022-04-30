from pq_function import *
from typing import List
from Priority_queue_v import Priority_queue as pq

v = [[3], [11], [30], [2], [31], [8], [6], [13], [26], [30]]

Q = pq(v, 10)
Q.print_queue()
Q._remove_min()
Q.print_queue()
Q.insert([14])
Q.print_queue()
