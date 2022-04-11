#!/usr/bin/python3
tuple1 = (1,6,3,9,5)
tuple2 = (1,6,3,9,5)
#tuple1[0] = 9   tuple object is immutable
print(tuple1,'=======',tuple2)
tupleSorted = sorted(tuple1)
print(tupleSorted)
print("hello world".split('o'))
list1 = [1,6,3,9,5]
list2 = list1 
list1[0] = 9
print(list1,'++++++',list2)