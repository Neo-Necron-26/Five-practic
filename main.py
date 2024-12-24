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

# Меню выбора функции
def main():
    print("Меню выбора функции:")
    print("1. sin(x) с использованием ряда Маклорена")
    print("2. sinh(x) с использованием ряда Маклорена")

    
    choice = int(input("Выберите функцию (1, 2 или 3): "))
    
    if choice in [1, 2, 3]:
        x = float(input("Введите значение x: "))
        if choice == 1:
            result = maclaurin_sin(x)
            print(f"sin({x}) = {result}")
        elif choice == 2:
            result = maclaurin_sinh(x)
            print(f"sinh({x}) = {result}")
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
