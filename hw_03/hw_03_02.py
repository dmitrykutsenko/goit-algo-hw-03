import turtle


def koch_curve(t, order, size):
  """

  Функція для малювання рекурсивної сніжинки Коха.

  Args:
    t: Об'єкт Turtle, який використовується для малювання.
    order: Рівень рекурсії.
    size: Довжина сторони базового трикутника.
  """

  if order == 0:
    t.forward(size)
  else:
    for angle in [60, -120, 60, 0]:
      koch_curve(t, order - 1, size / 3)
      t.left(angle)


# Функція для створення сніжинки Коха
def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Початкова позиція для рівностороннього трикутника
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Створення трьох сторін сніжинки Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Запит рівня рекурсії у користувача
recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха (0-10): "))
draw_koch_snowflake(recursion_level)

# Малювання сніжинки Коха
# koch_snowflake(t, recursion_level, 300)

# Завершення
#screen.mainloop()
