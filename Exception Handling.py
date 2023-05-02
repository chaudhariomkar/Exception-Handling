""""""
"""
Exception means error
eg. - NameError, ValueError, KeyError
Check all exceptions hierarchy
print(help('builtins'))

In Exception handling we have 4 blocks
1.try: test code
2.except: if exception in test code => come here
3.else: if NO exception in test code => come here in else block
4.finally: if exception occurs or not => i will execute
*try and except blocks are compulsory
*else and finally blocks are optional
"""
#using try and except blocks
try:
    print(9/'t')
except:
    print('Error Occured')
#---------------------------------------
#How to handle typical known exceptions
#1. Zero Divison Error
try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Error:',msg)
#2. Type Error
try:
    print(10/'2')
except TypeError as msg:
    print('Error:',msg)
#3. Name Error
try:
    d
except NameError as msg:
    print('Error:',msg)
#4. Other Error
k = [1,2]
try:
    print(k[20])
except:
    print('Other Error')

#How to combine multiple exception in one?
try:
    print(10/0)
except (ZeroDivisionError,NameError,TypeError) as msg: #Default exceptions must be written at the end
    print('Error:',msg)

#How to handle all exception in one
try:
    print(10/0)
except Exception as msg: #it will all exceptions because its a parent of all
    print('Error:',msg)

#Suppose if we have multiple in try?
try:
    print(a) #As we have exception control will move to except block
    print(99)
    print(23/2)
except Exception as msg:
    print('Error:',msg)
else:
    print('Python')
    a = [890.76,43]
#*Error => Go to except
#*No Error => Go to else