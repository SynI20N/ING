try:
    N = int(input("Введите высоту пирамиды: "))
except ValueError:
    print("Невозможно привести к целочисленному значению")
    exit(1)
if N <= 0:
    print("Высота должна быть больше нуля")
    exit(2)
spaces = N
symbols = 1
for i in range(N):
    string = " " * spaces
    if i < 5:
        string += "*" * symbols
    elif i < 10:
        string += "O" * symbols
    else:
        string += "+" * symbols
    spaces -= 1
    symbols += 2
    print(string)
