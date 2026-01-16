#1

'''
a = int(input("son kiriting: "))
b = int(input("son kiriting: "))

try:
    c = a / b
except ZeroDivisionError:
    print('0 ga bolish mumkin emas')
else:
    print(c)
finally:
    print("Hisoblash tugadi")
'''


#2

'''
try:
    a = int(input("son kiriting: "))
except ValueError:
    print('son kiriting matn emas!!!')
else:
    print(a**2)
'''


#3

'''
numbers = [10, 20, 30, 40, 50]
a = int(input("index kiriting: "))
try:
    print(numbers[a])
except IndexError:
    print("index noto'gri kiritildi!!!")
finally:
    print("Dastur yakunlandi")
'''


#4

'''
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

a = input("kalitni kiriting: ")

try:
    b = student[a]
except KeyError:
    print("kalit noto'gri kiritildi!!!")
else:
    print(student[a])
finally:
    print("Dastur yakunlandi")
'''

#5

'''
try:
    password = input("Parol kiriting: ")
    if len(password) < 8:
        print("Error")
    else:
        print("Parol qabul qilindi")
finally:
    print("Tekshiruv tugadi")
'''


#6

'''
data = [5, 10, 15]

try:
    a = int(input("index kiriting: "))
    b = data[a]
except ValueError:
    print("son kiriting")
except IndexError:
    print("index noto'gri kiritildi!!!")
else:
    print(data[a])
finally:
    print("Dastur yakunlandi")
'''


#7

'''
for i in range(1,31):
    if i % 3 == 0:
        continue
    print(i)
'''


#8

'''
lst =[]
for i in range(10):
    a = int(input(f"{i+1}-sonni kiriting: "))
    if a < 0:
        continue
    lst.append(a)
print(sum(lst))
'''


