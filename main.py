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


