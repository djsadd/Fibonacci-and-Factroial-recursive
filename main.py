# Recursive python 3.10


def get_fibonacci(a, f=[1, 1]):
    #Возвращает список/массив чисел Фибоначчи
    if a == len(f):
        return f # Возвращает список если когда а будет равна своей длине введенего числа 'fibonacci'
    z = f[-1] + f[-2]
    f.append(z)
    return get_fibonacci(a) # Рекурсия будет вызываться до тех пока числа список 'f' не будет равняться числу 'a' из перменной 'fibonacci'


fibonacci = int(input('Введите длину числа Фибоначчи: '))
print(f'Список числа Фибоначчи равен: {get_fibonacci(fibonacci)}')


def get_factorial(num):
    # Возвращает факториал введенного числа
    if num == 1:
        return num
    return num * get_factorial(num - 1)


fact = int(input('Введте число для поиска факториала: '))
print(f'Факториар равен: {get_factorial(fact)}')
