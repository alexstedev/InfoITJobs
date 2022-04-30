import json
from typing import List
from Priority_queue_v import Priority_queue as pq


def build_categories():
    ...


def divide(v: List, n: int):
    for i in range(len(v)):
        v[i] /= n
    return v


def sum_vec(v1: List, v2: List):
    v = []
    for i in range(len(v1)):
        v += [v1[i]+v2[i]]
    return v


def norm2(v1: List, v2: List):
    s = 0
    for i in range(len(v1)-1):
        s += (v1[i]-v2[i])**2
    return s


def add_activity(v: List, new_v: List):
    return sum_vec(v, new_v)


def applicant_vector(profile: List, activity: List, n: int):
    return profile + divide(activity, n)


def build_first(categories: List[List], applicant: List, k: int):
    # given list of k categories, returns the extension wiht euclidean distance squared.
    for i in range(k):
        categories[i] += norm2(categories[i], applicant)
    return categories


skills = []
profile = []
activity = []
category_matrix = [[]]
act_num = 1
k = 10
n = len(skills)  # number of skills
applicant = applicant_vector(profile, activity, act_num)
first_k = build_first(category_matrix, applicant, k)
Q = pq(first_k, k)

# Layer 1.


def search_engine(Q: pq, categories: List[List], applicant: List):
    # Q already has the first k elements.
    for i in range(len(categories)):
        Q.insert(categories[i]+norm2(applicant, categories[i]))
        Q.remove_max()
    return Q.queue_to_list()


def discard_unapp(Q: pq):
    ...


def recomm_jobs(Q: pq):
    p = Q.prob_vector()


def sort_most_recent(v: List): ...

# elements in the queue will be [v,'id', d(v,u)**2] where u is the application.
# compare with d(u,v)**2


# TO DO:
# Discard unapp
# recomm jobs probabilistically
# filter by recency
