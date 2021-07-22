from turtle import Turtle, Screen
import random
bubbles = Turtle()
screen = Screen()

bubbles.shape("classic")

# def shapes(num_of_side):
#     for _ in range(num_of_side):
#         angle = 360 / num_of_side
#         bubbles.forward(100)
#         bubbles.left(angle)

#
# for i in range(3, 11):
#     bubbles.color(random.choice(colours))
#     shapes(i)


# q = True
# while q:
#     coin = random.randrange(0, 2)
#     angle = random.randrange(0,360,90)
#     bubbles.color(random.choice(colours))
#     bubbles.pensize(10)
#     bubbles.speed(10)
#     if coin == 0:
#         bubbles.left(angle)
#         print(coin)
#     else:
#         bubbles.right(angle)
#         print(coin)
#     bubbles.forward(15)

bubbles = Turtle()
screen = Screen()


def move_forward():
    bubbles.forward(10)


def move_backward():
    bubbles.backward(10)

def clockwise():
    bubbles.right(10)

def counter_clockwise():
    bubbles.left(10)

def clear():
    bubbles.clear()
screen.onkey (move_forward, "w")
screen.onkey (move_backward, "s")
screen.onkey (clockwise, "d")
screen.onkey (counter_clockwise, "a")
screen.onkey (clear, "c")
screen.listen()
screen.exitonclick()