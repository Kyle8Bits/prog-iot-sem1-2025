# dicts
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
thisdict["apple"] = "red"
print(thisdict)

# or

thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# add

thisdict =	dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)

# remove

thisdict =	dict(apple="green", banana="yellow", cherry="red")
del thisdict["banana"]
print(thisdict)


# sets

thisset = {"apple", "banana", "cherry"}
print(thisset)

# or

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# add a new item

thisset.add("damson")
print(thisset)
thisset.add("damson")
print(thisset)
thisset.add("apple")
print(thisset)
