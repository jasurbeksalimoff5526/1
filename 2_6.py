#59

'''
a = r"C:\Program Files\JetBrains\PyCharm 2025.3.1\bin\pycharm64.exe"
b = a.rfind(".")

print(f"fayl kengaytmasi: {a[b+1:]}")
'''


#60

'''
a = r"C:\Program Files\JetBrains\PyCharm 2025.3.1\bin\pycharm64.exe"
b = a.split("\\")

if len(b) < 3:
    print("\ ")
else :
    print(b[1])
'''


#61

'''
a = r"C:\Program Files\JetBrains\PyCharm 2025.3.1\bin\pycharm64.exe"
b = a.split("\\")

if len(b) < 3:
    print("\ ")
else :
    print(b[2])
'''


#62

'''
a = input("tekst kiriting: ")
kichik = 'abcdefghijklmnopqrstuvwxyz'
katta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ""

for i in a:
    if i in kichik:
        b = kichik.find(i)
        c = kichik[(b + 1) % 26]
        result += c
    elif i in katta:
        b = katta.find(i)
        c = katta[(b + 1) % 26]
        result += c
print(result)
'''


#63

'''
a = input("tekst kiriting: ")
k = int(input("son kiriting: "))
kichik = 'abcdefghijklmnopqrstuvwxyz'
katta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ""
for i in a:
    if i in kichik:
        b = kichik.find(i)
        c = kichik[(b + k) % 26]
        result += c
    elif i in katta:
        b = katta.find(i)
        c = katta[(b + k) % 26]
        result += c
print(result)
'''


#64

'''
a = input("tekst kiriting: ")
k = int(input("son kiriting: "))
kichik = 'abcdefghijklmnopqrstuvwxyz'
katta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ""
for i in a:
    if i in kichik:
        b = kichik.find(i)
        c = kichik[(b - k) % 26]
        result += c
    elif i in katta:
        b = katta.find(i)
        c = katta[(b - k) % 26]
        result += c

print(result)
'''


#65

'''
a = input("tekst kiriting: ")
b = input("harf kiriting: ")
alifbo = 'abcdefghijklmnopqrstuvwxyz'

x = alifbo.find(a[0])
y = alifbo.find(b)
k = abs((x - y) % 26)

print(k)
'''


#66

'''
a = input("tekst kiriting: ")
result = ""
result2 = ""
for i in range(0, len(a)):
    if i % 2 == 0 :
        result += a[i]
    else :
        result2 += a[i]

print(result+result2[::-1])
'''


#67

'''
a = input("tekst kiriting: ")
result = ""
b = int(len(a)/2)

for i in range(b):
    result += a[i] + a[-(i + 1)]

if len(a) % 2 != 0:
    result += a[b]

print(result)
'''


#68

'''
a = input("tekst kiriting: ").lower()
alifbo = 'abcdefghijklmnopqrstuvwxyz'
t = ""
lst = []
for k in a:
    if not k.isdigit():
        t += k

for i in range(len(t) - 1):
    if t[i] in alifbo and t[i+1] in alifbo:
        if alifbo.index(t[i+1]) - alifbo.index(t[i]) != 1:
            print(a[0])
            break
else:
    print("0")
'''