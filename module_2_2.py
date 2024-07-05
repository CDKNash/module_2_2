num_1 = int(input('Введите число_1: '))
num_2 = int(input('Введите число_2: '))
num_3 = int(input('Введите число_3: '))
if num_1 == num_2 == num_3:
    print(3)
elif num_1 == num_2 or num_1 == num_3:
    print(2)
else:
    print(0)
