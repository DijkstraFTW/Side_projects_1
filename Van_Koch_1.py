from turtle import *


k = eval(input("Enter the lenght of the snowflake"))
j = input("Enter the color of the snowflake")
n = 6

color(j)
def koch():
    speed(0)
    forward(k/3)
    left(60)
    forward(k/3)
    right(120)
    forward(k/3)
    left(60)
    forward(k/3)

def snowflake():
    koch()
    left(60)
    koch()
    right(120)
    koch()
    left(60)
    koch()

def total():
    p = 0
    while p < n:
        snowflake()
        right(60)
        snowflake()
        left(120)
        p = p + 1
    
total()
input('Press ENTER to exit')