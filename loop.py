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
#list = [4,5,6,'ok','89']

name_list = ['Lucy','Lily','Jack']
for index in range(len(name_list)):
    print('Currrent element is ', name_list[index])
print('name_list is done')


numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2 == 0:
        print(num, 'is an even number')
    else:
        print(num, 'is not an even number')
print('the numbers is done')

numbers2 = [11,22,55,39,26,75,37,21,23,41,13]
for num in numbers2:
    if num%2 == 0:
        print(num, 'is an even number')
        break;
else:
    print('numbers2 does not contain an even number')
print('the numbers2 is done')


#nested if construct
num = int(input("enter number"))
if num%3 == 0:
    if num%2 == 0:
        print(num, 'is divisible by 3 and 2')
    else:
        print(num, 'is divisible by 3 not by 2') 
else:
    if num%2 == 0:
        print(num, 'is not divisible by 3 but divisible by 2')
    else:
        print(num, 'is not divisible by 3 and not divisible by2')


#single statement suits
# If the suite of an if clause consists only of a single line,
#  it may go on the same line as the header statement.

var = 100
if (var == 100) : print('value of expression is 100')


for i in range(1,5):
    for j in range(6,10):
        k = i * j
        print(k,'======')
    print('@@@@@@@')
print('&&&&&&&&')




print('well done')
