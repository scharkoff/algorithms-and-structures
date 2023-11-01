from sympy import symbols, Eq, solve

# Создаем символьные переменные
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Создаем уравнение
equation = Eq(x1 + x2 + x3 + x4, 30)

# Дополнительные ограничения
constraints = [x1 >= 1, x2 >= -5, x3 >= 0, x4 >= 8]

# Решаем систему уравнений с учетом ограничений
solutions = solve([equation] + constraints, (x1, x2, x3, x4), domain=symbols('Z'))

# Выводим количество решений
print("Количество решений:", len(solutions))
