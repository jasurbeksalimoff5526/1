
#1
with open("hello.txt", "w") as f:
    f.write("Salom Python")

#2
with open("hello.txt", "r") as f:
    print(f.read())

#3
with open("names.txt", "r") as f:
    count = 0
    for line in f:
        count += 1
print(count)

#4
with open("log.txt", "a") as f:
    f.write("Dastur ishga tushdi\n")

#5
try:
    with open("data.txt", "r"):
        print("Mavjud")
except FileNotFoundError:
    print("Mavjud emas")

#6
with open("text.txt", "r") as f:
    words = f.read().split()
print(len(words))

#7
with open("lines.txt", "r") as f:
    longest = ""
    for line in f:
        if len(line) > len(longest):
            longest = line
print(longest)

#8
with open("numbers.txt", "r") as f:
    total = 0
    for line in f:
        total += int(line.strip())
print(total)

#9
with open("input.txt", "r") as f:
    content = f.read()

with open("output.txt", "w") as f:
    f.write(content.upper())

#10
with open("data.txt", "r") as f:
    lines = f.readlines()

with open("clean.txt", "w") as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)

#11
with open("story.txt", "r") as f:
    text = f.read().lower()

clean_text = ""
for ch in text:
    if ch.isalnum() or ch.isspace():
        clean_text += ch

words = clean_text.split()

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

most_word = ""
most_count = 0

for w in counts:
    if counts[w] > most_count:
        most_count = counts[w]
        most_word = w

print(most_word, most_count)

#12
with open("mixed.txt", "r") as f:
    text = f.read()

current = ""
numbers = []

for ch in text:
    if ch.isdigit():
        current += ch
    else:
        if current != "":
            numbers.append(current)
            current = ""

if current != "":
    numbers.append(current)

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(num + "\n")

#13
with open("source.txt", "r") as s:
    data = s.read()

with open("backup.txt", "w") as d:
    d.write(data)

#14
with open("words.txt", "r") as f:
    text = f.read()

clean_text = ""
for ch in text:
    if ch.isalnum() or ch.isspace():
        clean_text += ch

words = clean_text.split()

longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w

print(longest_word)

#15
with open("numbers.txt", "r") as f:
    nums = []
    for line in f:
        nums.append(int(line.strip()))

print(max(nums))
print(min(nums))
print(sum(nums) / len(nums))