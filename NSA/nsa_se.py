import json
from typing import List
from Priority_queue_v import Priority_queue as pq


def build_categories():
    ...


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


def build_first(categories: List[List], applicant: List, k: int) -> List:
    # given list of k categories, returns the extension with euclidean distance squared.
    for i in range(k):
        categories[i] += norm2(categories[i], applicant)
    return categories


def applicable(applicant: List, Job) -> bool: ...


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


def search_engine(Q: pq, categories: List[List], applicant: List) -> List:
    # Q already has the first k elements.
    for i in range(len(categories)):
        add = []
        if i >= k:
            add = [norm2(applicant, categories[i])]
        Q.insert(categories[i]+add)
        Q.remove_max()
    return Q.queue_to_list()


def num_jobs(Q: pq) -> List:
    p = Q.prob_vector()
    num_jobs = []
    for i in range(len(p)):
        num_jobs.append(int(p[i]*Q.size()))
    return num_jobs


def x_applicable_jobs(v: List, applicant: List, x: int) -> List:
    i = 0
    k = 0
    jobs = []
    while i < x and k < len(v):
        if applicable(applicant, v[i]):
            jobs += v[i]
            i += 1
        k += 1
    return jobs


def def_joblist(Q: pq, applicant: List) -> List:
    l = Q.queue_to_list()
    num_job = num_jobs(Q)
    job_list = []
    # M should be a map from category id to list of jobs in the category.
    M = []
    for i in range(len(l)):
        v = M[l[i][-2]]
        job_list += x_applicable_jobs(v, applicant, num_job[i])
    return job_list

# elements in the queue will be [v,'id', d(v,u)**2] where u is the application.
# the application has format [u,w,0] where w is the vector containing applicable information.
# compare with d(u,v)**2

# TO DO:
# Applicable function
# API
