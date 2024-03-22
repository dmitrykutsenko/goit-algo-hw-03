import turtle


def koch_snowflake(t, order, size):
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
      koch_snowflake(t, order - 1, size / 3)
      t.left(angle)


def draw_koch_snowflake(order, size=300):
  """

  Функція для налаштування середовища та малювання сніжинки Коха.

  Args:
    order: Рівень рекурсії.
    size: Довжина сторони базового трикутника.
  """

  window = turtle.Screen()
  window.bgcolor("white")

  t = turtle.Turtle()
  t.speed(0)
  t.penup()
  t.goto(-size / 2, 0)
  t.pendown()

  koch_snowflake(t, order, size)

  window.mainloop()


# Запит рівня рекурсії у користувача
order = int(input("Введіть рівень рекурсії (0-10): "))

# Малювання сніжинки
draw_koch_snowflake(order)
