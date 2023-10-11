### <font color="ffr567"> Общее описание решений

1. <font color="majenta"> Скопировал репозиторий с помощью команды git clone>
2. Открыл папку geometric_lib с помощью команды cd
3. Создали ветку new_412870 и перешли на неё с помощmю команды git branch -b
4. Создал файл rectangle.py  помощью команды echo >
5. Добавил код в файл
6. Сохранили добавление файла с помощью команды git add
7. Добавил коммит  с помощью команды git commit -m
8. Создал файл triangle.py с помощью команды echo >
9. Добавил код в файл
10. Сохранили добавление файла с помощью команды git add
11. Исправили ошибку в файле rectangle.py
12. Сохранили изменения в файле с помощью команды git add
13. Добавил коммит  с помощью команды git commit -m
14. Построили граф истории всего репозитория с однострочным выводом коммитов с помощью команды git log --oneline --graph --all
15. Построили граф истории текущей ветки с однострочным выводом коммитов с помощью команды git log --oneline --graph 
16. Взяли хэши двух последних коммитов из истории и посмотрели внесенные изменения с помощью команды git show
17. перешли в main  с помощью команды git checkout
18. сделали merge в ветку main с помощью команды git merge
19. изменили origin с помощью команды git remote set-url origin
20. отправили репозитерий на локальный репозиторий(GitHub) с помощью команды git push -u origin
21. удалили ветку <new_412780> с помощью команды git branch -d
### <font color="ffr567">Описание каждой функции с примерами вызова
#### <font color="leakds">rectangle
    def area(a, b):
    return a * b
<font color="majenta">Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b

 example:

 input: 2 3

 output:6

    def perimeter(a, b):
    return (a + b)*2
Принимает числа a и b (стороны прямоугольник), возвращает периметр прямоугольника со сторонами a и b'''

example:

input: 2 3

output: 10

 #### <font color="leakds">square
    def area(a):
    return a * a
<font color="majenta">Принимает число a (сторона квадрата), возвращает площадь квадрата со стороной a

example:

input: 2

output: 4

    def perimeter(a):
    return 4 * a

Принимает число a (сторона квадрата), возвращает периметр квадрата со стороной a

example:

input: 2

output: 8

#### <font color="leakds">triangle
    def area(a, h):
    return a * h / 2

<font color="majenta">Принимает числа a и h (основавние и высота треугольника), возвращает площадь треугольника с основанием a и высотой h

example:

input: 2 3

output: 3

    def perimeter(a, b, c):
    return a + b + c

Принимает числа a, b, c (стороны треугольника), возвращает периметр треугольника со сторонами a, b, c

example:

input: 2 3 4

output: 9

#### <font color="leakds">circle

    import math
<font color="majenta">Подключил библиотеку math

    def area(r):
    return math.pi * r * r

Принимает число r(радиус),Возвращает площадь круга с радиусом r

example:

input: 5

output: 78.540

    def perimeter(r):
    return 2 * math.pi * r

Принимает число r(радиус), Возвращает периметр круга с радиусом r

example:

input: 5

output: 31.416

## <font color="leakds">Коммиты

### commit c528801bb9ccb012377e83d5ebf483df5913f2f0
      Author: Ramzes <ramzes.abulashvili.asus@gmail.com>
      Date:   Wed Sep 27 01:02:50 2023 +0300

      new file was added

### commit 1455e03e8eb7b9742b8e063464b8d76e6b41e3fc (origin/main, origin/HEAD)
      Author: Ramzes <ramzes.abulashvili.asus@gmail.com>
      Date:   Wed Sep 27 01:04:57 2023 +0300

      error was fixed in rectangle.py




