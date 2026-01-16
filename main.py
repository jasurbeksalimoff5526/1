'''
def test_func():
    n = int(input('son kiriting: '))
    if n % 2 == 0 and n % 7 == 0:
        print('Sirli son')
    else:
        print('oddiy son')
test_func()
'''
'''
def qoshish(a, b, c=0):
    print(a+b+c)
qoshish(7, 8, 8)
'''
'''
def per(a,b):
    p = 2*(a+b)
    s = a*b
    print(p,s)
eni = int(input('son kiriting: '))
boyi = int(input('son kiriting: '))
per(eni , boyi)
'''
'''
def maks(list):
    print(max(list))

maks([1, 2, 3, 5])
'''


txt = "Hello, welcome to my world."
belgi = 'o'
a = -1
for i in txt:
    if i != belgi:
        a += 1



