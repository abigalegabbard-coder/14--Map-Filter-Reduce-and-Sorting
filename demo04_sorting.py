names = ["Evan", "Jace", "Zach", "Mykyta", "Isaac", "allyn"]
# We can sort the list with the .sort method
# note: this changes the actual order of your list
print(names)
names.sort() # defaults to alphabetical (all capitals first)
print(names)

# Sort in reverse order:
names.sort(reverse = True)
print(names)

other_names = ("blake", "micheal", "abigale", "josie", "ryan", "josh", "duane", "john")

# We can't change a tuple!
# but we can sort a tuple if we use sorted

sorted_other_names = sorted(other_names)
# sorted returns a new list, instead of sorting in place
print(sorted_other_names)
# my own notes: when using .sort(), you want to use a list: [], not a tuple: ()
# OTHER THINGS:
print(dict(enumerate(sorted_other_names)))
print(dict(zip(["A", "B", "C", "D", "E", "F", "G", "H"], other_names)))

# Sort by length of string:
len_of_names_sorted = sorted(other_names, key = len)
print(len_of_names_sorted)

#count_vowels = lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s)))
#print(count_vowels("dog"))
most_vowels = sorted(other_names, key = lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s))), reverse=True)
print(most_vowels)

def get_last_letter(word):
    return word[-1]

sorted_by_last_letter = sorted(other_names, key = get_last_letter)
print(sorted_by_last_letter)