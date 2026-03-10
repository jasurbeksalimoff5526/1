# MultiThreading bo‘yicha 10 ta masala
#
# 1.  1 dan 100 gacha sonlarni chiqarish Ikki ta thread yarating: 1-thread
#     1 dan 50 gacha sonlarni chiqarsin. 2-thread 51 dan 100 gacha
#     sonlarni chiqarsin.
#
# 2.  Juft va toq sonlar Ikki thread yarating: Biri juft sonlarni
#     chiqarsin. Biri toq sonlarni chiqarsin. Range: 1 dan 100 gacha.
#
# 3.  Sonlar yig‘indisi List beriladi: nums = [1,2,3,4,5,6,7,8,9,10] 2
#     thread yarating: 1-thread listning birinchi yarmini yig‘indisini
#     hisoblasin. 2-thread listning ikkinchi yarmini yig‘indisini
#     hisoblasin. Oxirida umumiy yig‘indini toping.
#
# 4.  Faktorial hisoblash Ikki thread yarating: Biri 5 faktorialni
#     hisoblasin. Biri 7 faktorialni hisoblasin.
#
# 5.  Matndagi harflarni sanash Matn beriladi: text = “python
#     multithreading” 2 thread yarating: Biri unli harflar sonini
#     hisoblasin. Biri undosh harflar sonini hisoblasin.
#
# 6.  Listdagi eng katta son List: [23,54,12,76,89,33,45,90] 2 thread
#     yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
#     yarmini tekshiradi. Oxirida eng katta sonni toping.
#
# 7.  Kvadratlar hisoblash List: [1,2,3,4,5,6,7,8] 2 thread yarating: Biri
#     1 dan 4 gacha elementlarni kvadratga oshirsin. Biri 5 dan 8 gacha
#     elementlarni kvadratga oshirsin.
#
# 8.  Tub sonlarni topish 1 dan 100 gacha tub sonlarni toping. 1-thread 1
#     dan 50 gacha tekshiradi. 2-thread 51 dan 100 gacha tekshiradi.
#
# 9.  Stringlarni katta harfga o‘tkazish List:
#     [“python”,“django”,“fastapi”,“backend”] 2 thread yarating: Biri
#     birinchi 2 elementni upper qiladi. Biri qolgan elementlarni upper
#     qiladi.
#
# 10. Palindrom tekshirish List: [“level”,“python”,“radar”,“hello”] 2
#     thread yarating: Biri birinchi 2 so‘zni tekshiradi. Biri qolgan 2
#     so‘zni tekshiradi. Har bir so‘z palindrom yoki yo‘qligini aniqlang.
#
# MultiProcessing bo‘yicha 10 ta masala
#
# 1.  1 dan N gacha yig‘indi 2 ta process yarating: Biri 1 dan 500000
#     gacha sonlar yig‘indisini hisoblasin. Biri 500001 dan 1000000 gacha
#     sonlar yig‘indisini hisoblasin.
#
# 2.  Faktorial 2 ta process yarating: Biri 10 faktorialni hisoblasin.
#     Biri 12 faktorialni hisoblasin.
#
# 3.  Tub sonlarni topish 1 dan 10000 gacha tub sonlarni toping. 1-process
#     1 dan 5000 gacha tekshiradi. 2-process 5001 dan 10000 gacha
#     tekshiradi.
#
# 4.  Fibonacci 2 ta process yarating: Biri Fibonacci(30) ni hisoblasin.
#     Biri Fibonacci(35) ni hisoblasin.
#
# 5.  Eng katta sonni topish List: [12,45,67,23,89,90,34,22] 2 process
#     yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
#     yarmini tekshiradi. Oxirida eng katta sonni toping.
#
# 6.  Kvadratlar yig‘indisi 1 dan 100000 gacha sonlarning kvadratlari
#     yig‘indisini hisoblang. 2 process yarating: Biri 1 dan 50000 gacha
#     hisoblaydi. Biri 50001 dan 100000 gacha hisoblaydi.
#
# 7.  Listni sort qilish List: [34,12,76,23,89,11,90,45] 2 process
#     yarating: Har biri listning yarmini sort qiladi. Keyin natijalar
#     birlashtiriladi.
#
# 8.  Digit yig‘indisi Katta sonlar listi: [123456, 987654, 567890,
#     345678] 2 process yarating: Har biri listning yarmini ishlaydi. Har
#     sonning raqamlari yig‘indisini toping.
#
# 9.  Eng kichik sonni topish List: [45,23,67,12,89,34,10] 2 process
#     yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
#     yarmini tekshiradi. Oxirida eng kichik sonni toping.
#
# 10. Tub sonlar sonini hisoblash 1 dan 20000 gacha nechta tub son
#     borligini toping. 2 process yarating: 1-process 1 dan 10000 gacha
#     tekshiradi. 2-process 10001 dan 20000 gacha tekshiradi.



import threading
from concurrent.futures import ThreadPoolExecutor


#multithreading
#1


'''
def a():
    for i in range(1, 51):
        print(i)

def b():
    for i in range(51, 101):
        print(i)

t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)

t1.start()
t2.start()

t1.join()
t2.join()
'''

#2

'''
def a():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

def b():
    for i in range(1, 101):
        if i % 2 == 1 :
            print(i)

t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)

t1.start()
t2.start()

t1.join()
t2.join()
'''

#3

'''
nums = [1,2,3,4,5,6,7,8,9,10]
def a():
    summ = 0
    for i in nums[:int(len(nums)/2)]:
        summ += i
    return summ

def b():
    summ = 0
    for i in nums[int(len(nums)/2):]:
        summ += i
    return summ

with ThreadPoolExecutor() as executor:  #thread natijasini olish uchun

    thread1 = executor.submit(a)
    thread2 = executor.submit(b)

    natija1 = thread1.result()
    natija2 = thread2.result()

print(f"Thread_1: {natija1}")
print(f"Thread_2: {natija2}")
print(f"SUM: {natija1 + natija2}")
'''

#4

'''
def faktorial(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    print(f"{i} faktorial: {result}")


t1 = threading.Thread(target=faktorial(5))
t2 = threading.Thread(target=faktorial(7))

t1.start()
t2.start()

t1.join()
t2.join()
'''

#5

'''
text = "python multithreading"

def unli():
    count = 0
    for i in text:
        if i in "aeiou":
            count += 1
    print("unlilar", count)

def undosh():
    count = 0
    for i in text:
        if i not in "aeiou ":
            count += 1
    print("undoshlar", count)

t1 = threading.Thread(target=unli)
t2 = threading.Thread(target=undosh)

t1.start()
t2.start()

t1.join()
t2.join()
'''

#6

'''
lst = [23,54,12,76,89,33,45,90]
def a():
    summ = 0
    for i in lst[:int(len(lst)/2)]:
        if i > summ :
            summ = i
    return summ

def b():
    summ = 0
    for i in lst[int(len(lst)/2):]:
        if i > summ :
            summ = i
    return summ

with ThreadPoolExecutor() as executor:  #thread natijasini olish uchun 

    thread1 = executor.submit(a)
    thread2 = executor.submit(b)

    natija1 = thread1.result()
    natija2 = thread2.result()

print(f"Thread_1: {natija1}")
print(f"Thread_2: {natija2}")
print(f"MAX: {max(natija1, natija2)}")
'''

#7

