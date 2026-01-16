#1
'''
def katta_kichik():
    lst = [34, 27, 8 ,17, 97, 104]
    a = min(lst)
    b = max(lst)
    lst2 = [a, b]
    t = tuple(lst2)
    return t
print(katta_kichik())
'''


#2
'''
def son(a):
    l = []
    for i in range(1, a + 1):
        if i % 2 == 0 :
            l.append(i)
    return l


print(son(27))
'''


#3
'''
def toq_func(list):
    result = [i for i in list if i % 2 == 1]
    return result
print(toq_func([1, 2, 3, 8, 44, 78, 99, 45]))
'''


#4
'''
a = input("tekst kiriting: ")
def str_num():
    result = [i for i in a if i.isdigit() == True]
    return result
print(str_num())
'''


#5
'''
a = 87
def glob_change():
    global a
    a = 47
    return a
print(glob_change())
print(a)
'''


#6
'''
def sum_kv(*args):
    summ = sum(list(args))
    result = summ ** 2
    return result
print(sum_kv(1, 2, 4, 77))
'''


#7
'''
name = input("ismingiz: ")
age = input("yoshingiz: ")
country = input("qayerdansiz: ")

def malumot(**kwargs):
    for i,k in kwargs.items():
        print(f"{i}: {k}")

malumot(ismi = name, yoshi = age, manzili = country)
'''


#9

def claer_repeat(list):
    result = [i for i in list if type(i) == str ]