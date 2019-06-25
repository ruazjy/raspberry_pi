import turtle
import time

# Python程序由一系列命令组成并从上到下执行
# 可以通过循环和if语句控制程序
# 不必事必躬亲，通过导入模块
# 函数可以帮助重用代码，也可以使程序变得易于理解和维护
# 变量可以存储信息以便后面使用


boxsize = 200
caught = False
score = 0


# functions that are called on keypresses
def up():
    mouse.forward(10)
    checkbound()


def left():
    mouse.left(45)


def right():
    mouse.right(45)


def back():
    mouse.backward(10)
    checkbound()


def quitTurtles():
    window.bye()


# stop the mouse from leaving the square set by box size
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto((boxsize, mouse.ycor()))
    if mouse.xcor() < -boxsize:
        mouse.goto((-boxsize, mouse.ycor()))
    if mouse.ycor() > boxsize:
        mouse.goto((mouse.xcor(), boxsize))
    if mouse.ycor() < -boxsize:
        mouse.goto((mouse.xcor(), -boxsize))


# set up screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()

mouse.penup()
mouse.goto(100, 100)

# add key listeners
# 当键盘上产生某些输入时，执行对应的函数
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(back, "Down")
window.onkeypress(quitTurtles, "Escape")

difficulty = window.numinput("Difficulty",
                             "Enter a difficulty from easy (1), for hard (5) ",
                             minval=1, maxval=5)
window.listen()
# main loop
# note how it changes with difficulty
# 当老鼠没有被猫抓住的时候，一直执行循环
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8 + difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))
window.textinput("Game Over", "Well done.You scored:" + str(score * difficulty))
window.bye()

