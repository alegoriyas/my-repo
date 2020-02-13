from turtle import *           # Подключаем модуль turtle
from tkinter import *

reset()          # Приводим черепашку в начальное положение
down()           # Опускаем перо перо (начало рисования)
shape("turtle")  # Стандартный треугольник заменили на "черепашку"
forward(20)      # Проползти 20 пикселей вперед
left(90)         # Поворот влево на 90 градусов
forward(20)      # Рисуем вторую сторону квадрата
left(90)
forward(20)      # Рисуем третью сторону квадрата
left(90)
forward(20)      # Рисуем четвертую сторону квадрата
up()             # Поднять перо (закончить рисовать
down()

def square(lenght):
	for i in range(4):
		forward(lenght)
		left(90)

def tilted_square(grads):
	left(grads)     # now we can change the angle only here
	length = 100
	square(length)

gradus = 20
tilted_square(gradus)
tilted_square(gradus)
tilted_square(gradus)
tilted_square(gradus)
tilted_square(gradus)

fd(100)

def polygon(n, lenght):
	angle = 360.0 / n
	for i in range(n):
		fd(lenght)
		lt(angle)
polygon(n=7, lenght=70)

exitonclick()	 # Задержать окно на экране