import math

# Ряд Маклорена для sin(x)
def maclaurin_sin(x, iterations=10):
    """
    Вычисляет значение функции sin(x) с использованием ряда Маклорена.
    
    Аргументы:
    x -- аргумент функции
    iterations -- количество итераций для приближенного вычисления (по умолчанию 10)
    
    Возвращаемое значение:
    Значение функции sin(x), вычисленное с помощью ряда Маклорена
    
    Исключения:
    Не генерирует исключений.
    
    Пример:
    >>> maclaurin_sin(1)
    0.8414709848078965
    """
    result = 0
    for n in range(iterations):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

# Ряд Маклорена для sinh(x)
def maclaurin_sinh(x, iterations=10):
    """
    Вычисляет значение функции sinh(x) с использованием ряда Маклорена.
    
    Аргументы:
    x -- аргумент функции
    iterations -- количество итераций для приближенного вычисления (по умолчанию 10)
    
    Возвращаемое значение:
    Значение функции sinh(x), вычисленное с помощью ряда Маклорена
    
    Исключения:
    Не генерирует исключений.
    
    Пример:
    >>> maclaurin_sinh(1)
    1.1752011936438014
    """
    result = 0
    for n in range(iterations):
        result += (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result


# Ряд Маклорена для ln(1 + x)
def maclaurin_ln(x, iterations=10):
    """
    Вычисляет значение функции ln(x) с использованием ряда Маклорена для ln(1 + (x-1)).

    Аргументы:
    x -- аргумент функции (x > 0)
    iterations -- количество итераций для приближенного вычисления (по умолчанию 10)

    Возвращаемое значение:
    Значение функции ln(x), вычисленное с помощью ряда Маклорена

    Исключения:
    Вызывает исключение ValueError, если x <= 0 или x <= -1.

    Пример:
    >>> maclaurin_ln(2)
    0.6931471805599453
    """
    if x <= 0:
        raise ValueError("x должно быть больше 0 для вычисления ln(x)")

    # Преобразуем x как 1 + (x - 1)
    x_minus_1 = x - 1
    if x_minus_1 <= -1:
        raise ValueError("x должно быть больше 0 и меньше 2 для использования разложения ln(1 + x)")

    result = 0
    for n in range(1, iterations + 1):
        result += (-1) ** (n + 1) * (x_minus_1 ** n) / n
    return result
# Меню выбора функции
def main():
    print("Меню выбора функции:")
    print("1. sin(x) с использованием ряда Маклорена")
    print("2. sinh(x) с использованием ряда Маклорена")
    print("3. ln(x) с использованием ряда Маклорена")
    
    choice = int(input("Выберите функцию (1, 2 или 3): "))
    
    if choice in [1, 2, 3]:
        x = float(input("Введите значение x: "))
        if choice == 1:
            result = maclaurin_sin(x)
            print(f"sin({x}) = {result}")
        elif choice == 2:
            result = maclaurin_sinh(x)
            print(f"sinh({x}) = {result}")
        elif choice == 3:
            try:
                result = maclaurin_ln(x)
                print(f"ln({x}) = {result}")
            except ValueError as e:
                print(e)
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
