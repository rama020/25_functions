'''
DATE:20TH DEC 2022
DAY: TUESDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
''' 
def factorial(n):
    if n==0:
        return 1
    else:
        r=n*factorial(n-1)
        return r
n=abs(int(input("enter any number:")))
print(f"{n}! =" ,factorial(n))
import math
print(math.factorial(3))
def num_sum(lis):
    lis.sort()
    for i in lis: print(i,end=" ")
print("enter number: ")
v=[int(x) for x in input().split()]
num_sum(v)
a=50
def number():
    b=30
    a=40
    print(a)
    print('local variable(b):',b)
    print('global var a:',a)
print('global var a:',a)
number()
print('global var a:',a)