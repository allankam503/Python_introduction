"""Name and age."""


Name = input("Enter your name: ")
Age = input("Enter your age: ")

if Name == "":
    print("Name not found")

if Age == "":
    print("Age not found")

print("Hello " + Name + " you are " + Age + " years old!")

"""Time."""

sec_amount = input("Enter number of sec: ")
amount = int(sec_amount)
amount_hour = amount // 3600
print(amount_hour)
amount = amount % 3600

amount_min = amount // 60
print(amount_min)
amount = amount & 60

amount_sec = amount // 1
print(amount_sec)
amount = amount % 1

print(str(amount_hour) + ":" + str(amount_min) + ":" + str(amount_sec))

"""N."""

n = input("Enter your n number: ")
print(int(str(n)) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

"""Max num."""
n = int(input("Enter sum: "))
num_len = len(str(n))
max_digit = 0
while True:
    for i in range(num_len):
        if n % 10 > max_digit:
            max_digit = n % 10
            n = n // 10
        else:
            n = n // 10
    print(max_digit)
    break

"""Income"""

income = float(input("Доход фирмы: "))
loss = float(input("Убыток фипмы: "))
if income > loss:
    print("Все не так плохо!")
    profit = income - loss
    print("Рентабельнрсть состовляет " + str(profit))
    num_workers = int(input("Кол-во сотрудников: "))
    quality = income / num_workers
    print("Прибыль в соотношении одного работника " + str(quality))
elif loss > income:
    print("Все печально!")
else:
    print("Работаем в 0.")

"""Sportsmen."""

a = float(input("Введите первый результат в км: "))
b = float(input("Введите второй результат в км: "))
day_counter = 1

while b - a > 0:
    a = a + (a * 0.1)
    day_counter += 1
print("На " + str(day_counter) + " день спортсмен достиг результата — не менее 3 км.")







