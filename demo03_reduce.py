"""
The reduce function is used to reduce a collection into a single value
unlike built in functions like map and filter, the reduce function is not built directly into python
"""

from functools import reduce

grades = [98, 72, 71, 65, 88]

# Reduce syntax:
#reduce(function, collection)
def sum(x, y):
    return x + y

total_scores = reduce(sum, grades)
#essentially, it is calling sum(sum(sum(sum(98, 72), 51), 84), 68)
print(total_scores)
total_scores_ugly = sum(sum(sum(sum(98, 72), 51), 84), 68)
print(total_scores_ugly)

def all_passed(x, y):
    return (x > 70 or (x == True)) and y > 70
everybody_passed = reduce(all_passed, grades)
print(everybody_passed)