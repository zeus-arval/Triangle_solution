# Добро пожаловать в программу по помощи в математике! Тут будут расписываться решения для прямоугольного треугольника
import math
from math import sin, cos, tan
from colorama import Fore, Style


def c_sin(x, y):
    """Формула по вычислению синуса угла"""
    si = math.degrees(x / y)
    return si


def c_cos(x, y):
    """Формула по вычислению косинуса угла"""
    co = math.degrees(x / y)
    return co


def c_tan(x, y):
    """Формула по вычислению тангенса угла"""
    ta = math.degrees(x / y)
    return ta


def c_x_s(y, z):
    """Формула по вычислению катета через синус угла"""
    cxs = y * sin(z)
    return cxs


def c_x_c(y, z):
    """Формула по вычислению катета через косинус угла"""
    cxc = y * cos(z)
    return cxc


def c_x_t(y, z):
    """Формула по вычислению катета через тангенс угла"""
    cxt = y * tan(z)
    return cxt


def c_y_s(x, z):
    """Формула по вычислению гипотенузы через синус угла"""
    cys = x / sin(z)
    return cys


def c_y_c(x, z):
    """Формула по вычислению гипотенузы через косинус угла"""
    cyc = x / cos(z)
    return cyc


def c_y_t(x, z):
    """Формула по вычислению гипотенузы через тангенс угла"""
    cyt = x / tan(z)
    return cyt


def t_p_c(x, y):
    """Введение теоремы Пифагора для нахождения гипотенузы"""
    tpc = math.sqrt(x ** 2 + y ** 2)
    return tpc


def t_p_a(y, z):
    """Введение теоремы Пифагора для нахождения катета"""
    tpa = math.sqrt(z ** 2 - y ** 2)
    return tpa


def square(x, y):
    """Введение формулы нахождения площади треугольника"""
    s = x * y / 2
    print(f'Зная все стороны треугольника найдем его площадь: \nS = a * b / 2\nS = {s}')
    return s


def perimeter(x, y, z):
    """Введение формулы для нахождения периметра треугольника"""
    per = x + y + z
    print(f'Зная все стороны треугольника найдем его периметр: \nP = a + b + c\nP = {per}')
    return per


def conditions(a, b, c, alpha, betta):
    if c > a > 0 == betta == alpha == b or alpha != c > a > 0 == betta == b or betta != c > a > 0 == alpha == b \
            or alpha != betta != c > a == 0 == b:
        print(f'Найдем катет b \nПо теореме Пифагора:\nb² = c² - a² \nb = √(c² - a²) \nb = {t_p_a(a, c)} см')
        """1. Находим b"""
        if alpha == 0:
            print(f'Найдем угол α:\nsin α = a / c\nα = {str(c_sin(a, c))}°')
            """2. Находим угол α"""
            if betta == 0:
                print(f'Найдем угол β:\nsin β = b / c\nβ = {str(c_sin(t_p_a(a, c), c))}°')
                """3. Находим угол β"""
                square(a, t_p_a(a, c))
                perimeter(a, t_p_a(a, c), c)
                """4. Находим площадь и периметр"""
            else:
                square(a, t_p_a(a, c))
                perimeter(a, t_p_a(a, c), c)
                """4. Находим площадь и периметр"""
        else:
            if betta == 0:
                print(f'Найдем угол β:\nsin β = b / c\nβ = {c_sin(t_p_a(a, c), c)}°')
                """3. Находим угол β"""
                square(a, t_p_a(a, c))
                perimeter(a, t_p_a(a, c), c)
                """4. Находим площадь и периметр"""
            else:
                square(a, t_p_a(a, c))
                perimeter(a, t_p_a(a, c), c)
                """4. Находим площадь и периметр"""

    elif c > b > 0 == a == alpha == betta or alpha != c > b > 0 == a == betta or betta != c > b > 0 == a == alpha \
            or betta != alpha != c > b > 0 == a:
        print(f'Найдем катет a \nПо теореме Пифагора:\n a² = c² - b² \na = √(c² - b²) \na = {t_p_a(b, c)} см')
        """1. Находим a"""
        if alpha == 0:
            print(f'Зная катет b и гипотенузу с найдем угол α:\n sin α = a / c:\nα = {c_sin(t_p_a(b, c), c )} °')
            """2. Находим угол α"""
            if betta == 0:
                print(f'Зная катет а и гипотенузу с найдем угол β:\n sin β = b / c:\nβ = {c_sin(b, c)} °')
                """3. Находим угол β"""
                square(a, b)
                perimeter(a, b, c)
                """4.Находим площадь и периметр"""
            else:
                square(a, b)
                perimeter(a, b, c)
                """4.Находим площадь и периметр"""
        else:
            if betta == 0:
                print(f'Зная катет а и гипотенузу с найдем угол β:\n sin β = b / c:\nβ = {c_sin(b, c)} °')
                """3. Находим угол β"""
                square(a, b)
                perimeter(a, b, c)
                """4.Находим площадь и периметр"""
            else:
                square(a, b)
                perimeter(a, b, c)
                """4.Находим площадь и периметр"""

    elif a != b > 0 == c == alpha == betta or c > a != b > 0 == betta == alpha or alpha != a != b > 0 == betta == c \
            or betta != a != b > 0 == c == alpha or alpha != betta != a != b > 0 == c or alpha != c > a != b > 0 == \
            betta or betta != c > a != b > 0 == alpha or alpha != betta != c > a != b:
        if c == 0:
            print(f'Найдем гипотенузу с \nПо теореме Пифагора:\nc² = a² + b² \nc = √(a² + b²) \nc = {t_p_c(a, b)} см')
            """1. Находим c"""
            if alpha == 0:
                print(f'Зная катет а и гипотенузу с найдем угол α:\n sin α = a / c:\nα = {c_sin(a, (t_p_c(a, b)))}')
                """2. Находим угол α"""
                if betta == 0:
                    print(f'Зная катет b и гипотенузу с найдем угол β:\nsin β = b / c\nβ = {c_sin(b, (t_p_c(a, b)))}')
                    """3. Находим угол β"""
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
                else:
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
            else:
                if betta == 0:
                    print(f'Зная катет b и гипотенузу с найдем угол β:\nsin β = b / c\nβ = {c_sin(b, (t_p_c(a, b)))}')
                    """3. Находим угол β"""
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
                else:
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
        else:
            if alpha == 0:
                print(f'Зная катет а и гипотенузу с найдем угол α:\n sin α = a / c:\nα = {c_sin(a, c)}')
                """2. Находим угол α"""
                if betta == 0:
                    print(f'Зная катет b и гипотенузу с найдем угол β:\n sin β = a / c:\nβ = {c_sin(b, c)}')
                    """3. Находим угол β"""
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
                else:
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
            else:
                if betta == 0:
                    print(f'Зная катет b и гипотенузу с найдем угол β:\n sin β = a / c:\nβ = {c_sin(b, c)}')
                    """3. Находим угол β"""
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""
                else:
                    square(a, b)
                    perimeter(a, b, c)
                    """4. Находим площадь и периметр"""

    elif a != alpha > 0 == b == c == betta:
        print(f'Найдем гипотенузу через формулу по нахождению синуса угла:\n c = a / sin α \n c = {c_y_s(a, alpha)} см')
        """1. Находим c"""
        print(f'Найдем катет b \nПо теореме Пифагора:\n b² = c² - a² \nb = √(c² - a²) \nb = {t_p_a(a, c)} см')
        """2. Находим b"""
        print(f'Зная катет b и гипотенузу с найдем угол β:\n sin β = a / c:\nβ = {c_sin(t_p_a(a, c), c_y_s(a, alpha))}')
        """3. Находим угол β"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""

    elif b != alpha > 0 == a == c == betta:
        print(f'Найдем гипотенузу через формулу по нахождению косинуса угла:\n c = b / cos α \n c = '
              f'{c_y_c(a, alpha)} см')
        """1. Находим c"""
        print(f'Найдем катет a \nПо теореме Пифагора:\n a² = c² - b² \na = √(c² - b²) \na = '
              f'{t_p_a(b, c_y_c(a, alpha))} см')
        """2. Находим a"""
        print(f'Зная катет b и гипотенузу с найдем угол β:\n sin β = a / c:\nβ ='
              f' {c_sin(t_p_a(b, c_y_c(a, alpha)), c_y_c(a, alpha))}')
        """3. Находим угол β"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""

    elif a != betta > 0 == b == c == alpha:
        print(f'Найдем гипотенузу через формулу по нахождению косинуса угла:\n c = b / cos α \n c ='
              f' {c_y_c(a, betta)} см')
        """1. Находим c"""
        print(f'Найдем катет b \nПо теореме Пифагора:\n b² = c² - a² \nb = √(c² - a²) \nb ='
              f' {t_p_a(a, c_y_c(a, betta))} см')
        """2. Находим b"""
        print(f'Зная катет b и гипотенузу с найдем угол α:\n sin α = a / c:\nα ='
              f' {c_sin(a, c_y_c(a, betta))}')
        """3. Находим угол α"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""

    elif b != betta > 0 == a == c == alpha:
        print(f'Найдем гипотенузу через формулу по нахождению косинуса угла:\n c = b / cos α \n c ='
              f' {c_y_s(b, betta)} см')
        """1. Находим c"""
        print(f'Найдем катет a \nПо теореме Пифагора:\n a² = c² - b² \na = √(c² - b²) \na = '
              f'{t_p_a(b, c_y_s(b, betta))} см')
        """2. Находим a"""
        print(f'Зная катет a и гипотенузу с найдем угол α:\n sin α = a / c:\nβ ='
              f' {c_sin(t_p_a(b, c_y_s(b, betta)) ,c_y_s(b, betta))} см')
        """3. Находим угол α"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""

    elif c != alpha > 0 == a == b == betta:
        print(f'Найдем катет b через формулу по нахождению косинуса угла:\n b = c * cos α \n b ='
              f' {c_x_c(c, alpha)} см')
        """1. Находим b"""
        print(f'Найдем катет a \nПо теореме Пифагора:\n a² = c² - b² \na = √(c² - b²) \na ='
              f' {t_p_a(c_x_c(c, alpha), c)} см')
        """2. Находим a"""
        print(f'Зная катет b и гипотенузу с найдем угол β:\n sin β = a / c:\nβ ='
              f' {c_sin(t_p_a(b, c_y_c(a, alpha)), c_y_c(a, alpha))}')
        """3. Находим угол β"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""

    elif c != betta > 0 == a == alpha == b:
        print(f'Найдем гипотенузу через формулу по нахождению косинуса угла:\n c = b / cos α \n c ='
              f' {c_y_c(a, alpha)} см')
        """1. Находим b"""
        print(f'Найдем катет a \nПо теореме Пифагора:\n a² = c² - b² \na = √(c² - b²) \na = {t_p_a(b, c)} см')
        """2. Находим a"""
        print(c_sin(b, c))
        """3. Находим угол α"""
        square(a, b)
        perimeter(a, b, c)
        """4. Находим площадь и периметр"""


def main():
    values = list(map(float, input("Введите все известные данные в виде (a, b, c, угол alpha,угол betta): ").split()))
    a = values[0]
    b = values[1]
    c = values[2]
    alpha = values[3]
    betta = values[4]
    conditions(a, b, c, alpha, betta)


if __name__ == '__main__':
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print("Приветствую вас в пробной приложении по решению задач по тригонометрии!")
    main()
