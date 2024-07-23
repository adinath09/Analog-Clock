from turtle import Turtle, Screen
import datetime

window = Screen()
window.title("Analog DigitalClock")
window.bgcolor("black")
window.setup(width=1000, height=800)

circle = Turtle()
circle.penup()
circle.pencolor("#118893")
circle.speed(0)
circle.pensize(25)
circle.hideturtle()
circle.goto(0, -390)
circle.pendown()
circle.fillcolor("#17202A")
circle.begin_fill()
circle.circle(400)
circle.end_fill()

hHand = Turtle()
hHand.shape("arrow")
hHand.color("white")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)

mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

sHand = Turtle()
sHand.shape("arrow")
sHand.color("dark red")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=36)

centerCircle = Turtle()
centerCircle.shape("circle")
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# Position and write the numbers on the clock face
positions = [
    (170, 260, "1"), (300, 140, "2"), (340, -30, "3"), 
    (300, -200, "4"), (170, -325, "5"), (0, -370, "6"), 
    (-170, -325, "7"), (-300, -200, "8"), (-340, -30, "9"), 
    (-280, 140, "10"), (-160, 260, "11"), (0, 300, "12")
]

for x, y, num in positions:
    pen.goto(x, y)
    pen.write(num, align="center", font=("Algerian", 50, "bold"))

def movehHand():
    currentHourInternal = datetime.datetime.now().hour % 12
    degree = (currentHourInternal - 3) * -30
    currentMinuteInternal = datetime.datetime.now().minute
    degree -= 0.5 * currentMinuteInternal
    hHand.setheading(degree)
    window.ontimer(movehHand, 60000)

def movemHand():
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree -= currentSecondInternal * 0.1
    mHand.setheading(degree)
    window.ontimer(movemHand, 1000)

def movesHand():
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

movehHand()
movemHand()
movesHand()

window.mainloop()
