from math import*
def minus(a, b):
    res = a-b
    print("Ответ:",res)
def plus(a, b):
    res = a+b
    print("Ответ:",res)
def delenie(a, b):
    res = a/b
    print("Ответ:",res)
def zarb(a, b):
    res = a*b
    print("Ответ:",res)
def ispodkoren(a):
    res = sqrt(a)
    print(int(res))
def foiz(a):
    res = a/100
    print("Ответ:",res)
def stepen(a, b):
    res = a**b
    print("Ответ:",res)
def dvichnakod(a):
    if a == 0:
        return "0"
    res = ""
    while a > 0:
        res = str(a % 2) + res
        a //= 2
    print("Ответ:",res)
def factoriali(a):
    cnt = 1
    for i in range(1,a+1):
        cnt*=i
    print("Ответ:",cnt)
while True:
    n = int(input("1.Сложение\n2.Уменьшение\n3.Умножение\n4.Деление\n5.Корень\n6.Степень\n7.Двоичный кодирование числа\n8.Факториал\n9.Выход\nПожайлуста выбирите функцую: "))
    if n == 1:
        plus(int(input("Первое число: ")),int(input("Второе число: ")))
    elif n == 2:
        minus(int(input("Первое число: ")),int(input("Второе число: ")))
    elif n == 3:
        zarb(int(input("Первое число: ")),int(input("Второе число: ")))
    elif n == 4:
        delenie(int(input("Первое число: ")),int(input("Второе число: ")))
    elif n == 5:
        ispodkoren(int(input("Вводите число: ")))
    elif n == 6:
        stepen(int(input("Первое число: ")),int(input("Второе число: ")))
    elif n == 7:
        dvichnakod(int(input("Вводите число: ")))
    elif n == 8:
        factoriali(int(input("Вводите число: ")))
    elif n == 9:
        print("Пока")
        break
    else:
        print("Выбирете функциию из списка!!")
        

    