#!/usr/bin/python3


# 4 + 5 = 9  4 and 5 are operands, and + is operator
#Python operators: arithmetic operators, comparison(relational) operators, assignment operators, 
# logical operators, bitwise(逐位，按位) operators, membership operators, identity operators

# Arithmetic Operators
# + addition   - subtraction   * multiplication  / division 
# % modulus  取相除之后的余数
# Divides left hand operand by right hand operand and returns remainder  4%3 = 1  5%3 = 2 
# ** exponent  指数运算 2的3次方 就是 2x2x2   2的3次方 +  2的4次方 = 2的7次方
# Performs exponential (power) calculation on operators 
# // floor division  向下取整
# The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
# quotient 商 divisor 除数  dividend 被除数  remainder 余数  ceiling division 向上取整

print(2+2)
print(2-2)
print(2*2)
print(2%2)
print(4%3)
print(5%3)
print('exponent')
print(3**2)
print(5**3)
print('floor division')
print(5//2) # this code means 2 goes into 5 two times 
# if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
# 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

#Comparasion Operators = Relational Operators
# if use comparasion operators, the result will be true or false
# == equal   != not equal    >   <   >=  <=


#Assignment Operators
# assign values from right side operands to left side operands 
#  = assign    c = a + b assigns value of a + b into c
# += add and assign    c += a is equivalent to c = c + a
# -+ sutract and assign  c -= a is equivalent to c = c - a
#  *= multiply and assign  c *= a is equivalent to c = c * a
#  /= divide and assign  c /= a is equivalent to c = c / a
#  %=  modulus and assign  
# **= exponent and assign  
# //= floor division and assign 
print('assignment operator')
a = 3
c = 8
c //= a  
print(c)

# Bitwise Operators  
# & Binary AND  | Binary OR   ^ Binary XOR  ~ Binary Ones Complement  << Binary Left Shift  >> Binary Right Shift 
# 

# Logical Operators  
# and     or    not
# Assume variable a holds True and variable b holds False then
#  (a and b) is FALSE   (a or b) is TURE   not(a and b) is TRUE
#     

# Membership Operators
# Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
#  in     not in

list = [2,3,4,5]
a = 4
b = 0
print('membership operators')
print(a in list)
print(b in list)
print(b not in list)





