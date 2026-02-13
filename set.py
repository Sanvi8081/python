#set
collection={1,2,3,4,4,5,6}
print(collection)

print(type(collection))
#empty set
collection=set()
print(type(collection))

#set methods
collection=set()
collection.add(5)
collection.add(10)
collection.add(15)
collection.add(20)
print(collection)
collection.remove(15)
print(collection)
collection.pop()
print(collection)
collection.clear()
print(collection)
set1={1,2,3,}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

#Find a way to store 9 and 9.0 as seperate values in a set
value={9,"9.0"}
print(value)
#using built in datatypes
values={
    ("float",9.0),
    ("int",9)
}
print(values)