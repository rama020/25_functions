'''
DATE:20TH DEC 2022
DAY: TUESDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
''' 
def fun():
    x=7;y=8;z=9
    print(x+y)
fun()
a=2
def bm():
    a=4
    b=3;c=5
    print(a)
    print(b)
print(a)
bm()
print(a)
c=4
def fun():
    a=3
    global c,b
    b=8
    c=9
    print(b)
print(c)
fun()
print(c)
print(b)
print(c)
def fn(st):
    c=0
    for i in st:
        c+=1
    return c
print(fn('python'))
def sc():
    school='josh'
    print(f'name in school is {school}')
def cl():
    college='max'
    print(f'name in collega is {college}')
def wk():
    work='peter'
    print(f'name at work location is {work}')
    
