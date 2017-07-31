
import turtle

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction= UP

def up():
    global direction
    direction=UP
    print ('you pressed UP')


def down():
    global direction
    direction=DOWN
    print('you pressed DOWN')


def left():
    global direction
    direction=LEFT
    print ('you pressed LEFT')

def right():
    global direction
    direction =RIGHT
    print('RIGHT')


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()




