#!/usr/bin/python3
a = 100
b = 12.00
c = 'second one'

d = e = f = 49  #allocate value 49 to variable d, e, and f
r, t = 'yyy',90  # allocate values to the variables respectively

#print(a, b, c, d, e, f, r, t)

str = 'Hello, Python!'

print(str)
print(str[0]) # the first character in string
print(str[2:6]) # the third character to the seventh character in the string
print(str[2:]) # from the third character to the end 
print(str * 2) # print the string two times
print(str + 'TEST')  # add a new string TEST to the end of the string variable


list = ['abcd', 786, 2.23, 'john', 70.2]  
tinylist = [123, 'john']
print(list)
print(list[0])
print(list[-1])
print(list[2:4])
print(list[2:])
print(list * 2)
print(list + tinylist)

#list type ,use brackets[] and commas; its elements and size can be changed
#tuples type, use parenthesis() and commas; its elements and size cannot be changed, 
# can be thought of as read-only list 

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tynituple = (123, 'john')
print('merge tuple and tinytuple')
print(tuple + tynituple)
print('change the second element of tuple as 3')
#tuple[1] = 2  #this is invalid, because tuple object does not support assignment. It can not be updated
print(tuple)

print('change the second element of list as 3')
list[1] = 3
print(list) # this is valid because list type supports update

#dictionary type enclosed by curly braces; consist of key-value pairs; 
# key can be any Python type, but usually numbers and strings
#value can be any arbitrary Python object
#values can be assigned and accessed using square braces[]

dict = {}
dict['one'] = 'This is one'  #assign value(This is one) to key(one) in dictionary dict
dict['2'] = 'This is two'  
tinydict = {'3':'three','name':'Lucy','code':23546,'size':'xlarge'}  #assign as key-value pairs
print(dict)
print(dict['one'])
print(dict.keys()) #access all keys in dict as a list
print(tinydict.values())  #access all values in dict as a list


#convert between types: use type-name as functions
print(int(12.0))
print(float(12))


