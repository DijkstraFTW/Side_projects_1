from turtle import *


k = eval(input("Enter the lenght of the snowflake"))
j = input("Enter the color of the snowflake")
l = eval(input("Enter the nombre of iterations"))
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

def snowflake(l):
    if l == 0 :
        koch()
    else :
        snowflake(l-1)
        left(60)
        snowflake(l-1)
        right(120)
        snowflake(l-1)
        left(60)
        snowflake(l-1)

snowflake(l)