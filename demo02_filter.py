"""
Filter: Similar to map, only the function returns true of false
"""

names= ["issac", "david", "jace", "zach", "evan"]

def is_not_zach(name):
    return name.lower().strip() != "zach"

print(names)
cleaned_list = list(filter(is_not_zach, names)) #returns a filter object
print(cleaned_list)

even_better = list(filter(lambda name: name.lower().strip() != "jace", cleaned_list))
print(even_better)

grades = [
    {"student": "Evan", "score": 12},
    {"student": "Issac", "score": 83},
    {"student": "Kaine", "score": 90},
    {"student": "Blake", "score": 79},
    {"student": "Micheal", "score": 89},
    {"student": "Zach", "score": 4}
]

# Filter this list down to only passing students:
passing_students = list(filter(lambda grade: grade["score"] >= 60, grades))
print(passing_students)