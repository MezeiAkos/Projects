# Skipping Work
# =============
# Commander Lambda is all about efficiency, including using her the bunny workers for manual labor. But no one's been
# properly monitoring the labor shifts for a while and they've gotten quite mixed up. You've been given the task of
# fixing them, but after you wrote up new shifts you realized that some bunny workers had been transferred to a
# different area and aren't available for their assigned shifts. Manually sorting through each shift list to compare
# against work area lists will take forever -- remember, Commander Lambda loves efficiency! Given two almost
# identical lists of worker IDs x and y where one of the lists contains an additional ID, write a function solution(
# x, y) that compares the lists and returns the additional ID.
#
# For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) would return 6
# because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3,
# 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function solution(x, y) would return -4 because the list y contains
# the integer -4 and the list x doesn't.
#
# In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more
# than 99, and one of the lists will contain an additional unique integer which should be returned by the function.
# The same n non-unique integers will be present on both lists, but they might appear in a different order like in
# the examples above. Commander Lambda likes to keep the numbers short, so every worker ID will be between -1000 and
# 1000.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
# Output:
#     6
#
# Input:
# solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
# Output:
#     -4

import time
import random
from random import randrange


def solution(x, y):
    if len(y) > len(x):
        x, y = y, x
    for id in x:
        if id not in y:
            return id


# TODO optimize the shit out of it lmao

i = 1
timeTaken = []
while i != 1000:
    list1 = random.sample(xrange(-999, 995), 999)
    list2 = list1[:]
    list2.insert(randrange(len(list2) + 1), 999)

    t0 = time.time()
    solution(list1, list2)
    t1 = time.time()

    timeTaken.append(t1-t0)
    i+=1
print(sum(timeTaken)/len(timeTaken))
print(solution([0], [0, 1]))
