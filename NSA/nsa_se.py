import json
from typing import Dict, List
from Priority_queue_v import Priority_queue as pq


def divide(v: List, n: int) -> List:
    for i in range(len(v)):
        v[i] /= n
    return v


def sum_vec(v1: List, v2: List) -> List:
    v = []
    for i in range(len(v1)):
        v += [v1[i]+v2[i]]
    return v


def norm2(v1: List, v2: List) -> float:
    s = 0
    for i in range(len(v1)-1):
        s += (v1[i]-v2[i])**2
    return s


def add_activity(v: List, new_v: List) -> List:
    return sum_vec(v, new_v)


def applicant_vector(profile: List, activity: List, n: int) -> List:
    return divide(profile + divide(activity, n), 2)


def build_first(sc_matrix: List[List], applicant: List, k: int) -> List:
    # given list of k sc_matrix, returns the extension with euclidean distance squared.
    for i in range(len(sc_matrix)):
        sc_matrix[i] += [norm2(sc_matrix[i], applicant)]
    return sc_matrix


skills = []
profile = []
activity = []
k = 10
act_num = 1
# applicant = applicant_vector(profile, activity, act_num)

# Layer 1.


def keystoint(x):
    return {int(k): v for k, v in x.items()}


def retrieve_data():
    with open('sc_id_to_name.json') as file:
        M = json.load(file)
    with open('category_matrix.json') as file:
        sc_matrix = json.load(file)
    with open('skills_id_to_name.json') as file:
        v = json.load(file)
    return M, sc_matrix, len(v)


def search_engine(Q: pq, sc_matrix: List[List], applicant: List) -> List:
    # Q already has the first k elements.
    for i in range(len(sc_matrix)):
        Q.insert(sc_matrix[i])
        Q.remove_max()
    return Q.queue_to_list()


def exec():
    M, sc_matrix, n = retrieve_data()
    # print(M) works
    # print(sc_matrix) works
    applicant = []
    # generate an applicant profile
    K = 1
    for i in range(n):
        if K > 0:
            applicant.append(1)
        else:
            applicant.append(0)
        K *= -1
    # now we should have a real applicant

    Q = pq(build_first(sc_matrix, applicant, k), k)
    search_engine(Q, sc_matrix, applicant)
    v = Q.queue_to_list()
    rc_sc_id = {}
    for i in range(len(v)):
        rc_sc_id[M[str(v[i][-2])]] = 0
    return list(rc_sc_id)[:k]


print(exec())
# elements in the queue will be [v,'id', d(v,u)**2] where u is the application.
# the application has format [u,w,0] where w is the vector containing applicable information.
# compare with d(u,v)**2
