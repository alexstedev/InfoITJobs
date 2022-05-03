import requests
import pandas as pd
import json
from typing import Dict, List
from Priority_queue_v import Priority_queue as pq
from retrieve_data_2 import *

payload = {}
headers = {
    'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
    'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
}


def norm2(v1: List, v2: List) -> float:
    s = 0
    for i in range(len(v1)-1):
        s += (v1[i]-v2[i])**2
    return s


def build_first(sc_matrix: List[List], applicant: List, k: int) -> List:
    # given list of k sc_matrix, returns the extension with euclidean distance squared.
    for i in range(len(sc_matrix)):
        sc_matrix[i] += [norm2(sc_matrix[i], applicant)]
    return sc_matrix


k = 10
act_num = 1
#applicant = applicant_vector(profile, activity, act_num)

# Layer 1.


def search_engine(Q: pq, sc_matrix: List[List], applicant: List) -> List:
    # Q already has the first k elements.
    for i in range(len(sc_matrix)):
        Q.insert(sc_matrix[i])
        Q.remove_max()
    return Q.queue_to_list()


def num_jobs(Q: pq) -> List:
    p = Q.prob_vector()
    num_jobs = []
    for i in range(len(p)):
        num_jobs.append(int(p[i]*Q.size()))
    return num_jobs


def x_jobs(v: List, x: int) -> List:
    i = 0
    jobs = []
    while i < x and i < len(v):
        jobs += v[i]
        i += 1
    return jobs


def def_joblist(Q: pq, M: Dict) -> List:
    l = Q.queue_to_list()
    num_job = num_jobs(Q)
    job_list = []
    # M should be a map from category id to list of jobs in the category.
    for i in range(len(l)):
        v = []
        if l[i][-2] in M.keys():
            v = M[l[i][-2]]
        job_list += x_jobs(v, num_job[i])
    return job_list


def exec():
    M, sc_matrix, n = retrieve_data()
    applicant = []
    K = 1
    for i in range(n):
        if K > 0:
            applicant.append(1)
        else:
            applicant.append(0)
        K *= -1
    Q = pq(build_first(sc_matrix, applicant, k), k)
    search_engine(Q, sc_matrix, applicant)
    return def_joblist(Q, M)


print(exec())
