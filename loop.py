#!/sur/bin/python3
# In Python, all the statements indented by the same number of character spaces 
# after a programming construct are considered to be part of a single block of code. 
# Python uses indentation as its method of grouping statements.


# loop include while, for and 
count = 0
while(count < 9):
    print('The count is', count)
    count += 1

else:
    print('Good bye2')


list = ['Lucy','Lily','Sam','Jim','Jake']
for name in list:
    print("the person's name is", name)
print('Goodbye')

tuple = {'name':'Lucy','age':16,"tel":'16354635263','address':'致力陆'}
for key in tuple:
    print(tuple[key])
print('tuple is over')


# range() generates an iterator to progress integers starting with 0 upto n-1.