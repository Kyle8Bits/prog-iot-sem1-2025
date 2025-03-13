thislist = list(("Homer", "Marge", "Bart")) # note the double round-brackets
#thislist = ["Homer", "Marge", "Bart"]
print(thislist)
print(id(thislist))
thislist.append("Nelson")
print(thislist)
print(id(thislist))
thislist.remove("Nelson")
print(thislist)

# Stack (LIFO)
stack = [1, 2, 3, 4, 5] 
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)
stack.pop()
print(stack)

# Queue (FIFO)
q = []

q.append('eat')
q.append('sleep')
q.append('code')
print(q)
q.pop(0)
print(q)


# Tuples
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# add items to tuples

#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
print(id(tuplex))
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
print(id(tuplex))
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
print(id(tuplex))
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

# you cannot remove items from tuples

#create a tuple
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)
