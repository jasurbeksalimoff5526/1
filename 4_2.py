import csv


# 1-masala
students = [
    ["Ali", 18, "Python"],
    ["Vali", 20, "Django"],
    ["Hasan", 19, "FastAPI"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append([row[0], int(row[1]), row[2]])

print(data)


# 2-masala
products = [
    {"name": "Laptop", "price": 1200, "qty": 5},
    {"name": "Phone", "price": 800, "qty": 10},
    {"name": "Mouse", "price": 20, "qty": 50}
]

with open("products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "price", "qty"])
    writer.writeheader()
    writer.writerows(products)

with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        data.append({
            "name": row["name"],
            "price": int(row["price"]),
            "qty": int(row["qty"])
        })

print(data)


# 3-masala
result = []
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        result.append({
            "username": row["username"],
            "email": row["email"]
        })

print(result)


# 4-masala
numbers = [
    [2, 5, 8],
    [10, 3, 7],
    [6, 6, 6]
]

with open("numbers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(numbers)

with open("numbers.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        nums = list(map(int, row))
        print(sum(nums))


# 5-masala
passed = []
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["score"]) >= 60:
            passed.append({
                "name": row["name"],
                "score": int(row["score"])
            })

print(passed)


# 6-masala
students2 = [
    {"name": "Ali", "age": 18, "score": 75},
    {"name": "Vali", "age": 19, "score": 90},
    {"name": "Hasan", "age": 18, "score": 60},
    {"name": "Olim", "age": 20, "score": 85}
]

with open("students2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerows(students2)

with open("students2.csv", "r") as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        data.append({
            "name": row["name"],
            "age": int(row["age"]),
            "score": int(row["score"])
        })

data.sort(key=lambda x: x["score"], reverse=True)
print(data)


# 7-masala
updated = []
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        salary = float(row["salary"])
        if salary < 1000:
            salary = salary * 1.2
        updated.append({
            "id": row["id"],
            "name": row["name"],
            "salary": salary
        })

with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "salary"])
    writer.writeheader()
    writer.writerows(updated)

print(updated)


# 8-masala
combined = []
for file in ["group1.csv", "group2.csv"]:
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            combined.append({
                "name": row["name"],
                "score": int(row["score"])
            })

with open("final.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(combined)

print(combined)


# 9-masala
totals = {}
with open("orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row["user"]
        amount = int(row["amount"])
        if user in totals:
            totals[user] += amount
        else:
            totals[user] = amount

print(totals)


# 10-masala
clean = []
errors = []

with open("students_validation.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row["age"])
        score = int(row["score"])

        if age < 0 or score > 100:
            errors.append(row)
        else:
            clean.append(row)

with open("clean_students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerows(clean)

with open("errors.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerows(errors)

print("Clean:", clean)
print("Errors:", errors)