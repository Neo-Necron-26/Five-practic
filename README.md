Программа содержит несколько *функций* - [рядов Маклорена](https://ru.wikipedia.org/wiki/%D0%A0%D1%8F%D0%B4_%D0%A2%D0%B5%D0%B9%D0%BB%D0%BE%D1%80%D0%B0#%D0%A0%D1%8F%D0%B4%D1%8B_%D0%9C%D0%B0%D0%BA%D0%BB%D0%BE%D1%80%D0%B5%D0%BD%D0%B0_%D0%BD%D0%B5%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D1%85_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9), и *меню* для управления работой программы. Взаимодействие с пользователем осуществляется через **консоль**.

Опции меню:
- Выполнить функцию 3
- Выполнить функцию 9
- Выполнить функцию 10 *(добавлено [Никита Ильиных](https://github.com/NGribojuy))*
- Выход

Реализовано разложение формул:
- [X] $cos(x)$
- [X] $(1+x)^m$
- [X] $(1-x)^m$

Пример кода:
```
def f3(x, n):
    """Ряд Маклорена функции cos(x)"""
    answer = 1
    for i in range(1, n+1):
        answer += ((-1)**i) * (x**(2 * i) / factorial(2 * i))
    return answer
```
![Bin]([https://github.com/user-attachments/assets/676a7e45-1bb5-407c-982e-4721a1ee3394](https://static.kinoafisha.info/k/articles/1200/upload/articles/762839970828.jpg))
***Bin***

