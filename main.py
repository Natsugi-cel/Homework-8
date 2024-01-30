print("Hello world")

################# 1 ###############

def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введіть число: "))
exp = int(input("Введіть його ступінь: "))
print("Результат зведення в ступінь дорівнює:", power(base, exp))

############## 2 ##############

input sumCount(int value)
{
    if (value <= 0)
        return 0; // базовий випадок (умова завершення)
    else if (value == 1)
        return 1; // базовий випадок (умова завершення)
    else
        return sumCount(value - 1) + value; // рекурсивний виклик функції

}

################ 3 ################

def sum_range(a, b):
    if a > b:
        return 0
    return a + sum_range(a+1, b)
print(sum_range(1, 5))




