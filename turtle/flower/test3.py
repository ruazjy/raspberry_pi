import turtle
# create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()

# draw stem and centre
babbage.color('green', 'black')
babbage.left(90)
babbage.forward(100)
babbage.right(90)
babbage.color('orange', 'yellow')
babbage.begin_fill()
babbage.circle(10)
babbage.end_fill()

for i in range(23):
    babbage.color('red', 'black')
    babbage.left(15)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
window.exitonclick()


