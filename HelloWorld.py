import random
import os
import sys


villain={'Batman':'Joker',
            'The Prison Break':'T-Bag'}

print(villain['Batman'])
print(len(villain))


my_tuple = (1,2,3,4,5)


print(my_tuple)

new_list=list(my_tuple)

print(new_list)


for x in range(0,10):
    print(x, ' ', end="")
print('\n')
print('Hey')

list1=[1,2,3]
list2=[10,20,30]
my_list=[list1,list2]
print(my_list)

myString="Hello"
name=sys.stdin.readline()
print("Hey")