import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

def draw():
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

if __name__ == "__main__":
    sc.setup(600, 600)
    pen.speed(0)

    for i in range(8):  # Rows
        for j in range(8):  # Columns
            x = j * 30
            y = i * 30
            pen.up()
            pen.goto(x, y)
            pen.down()

            if (i + j) % 2 == 0:
                col = 'black'
            else:
                col = 'white'
            pen.fillcolor(col)
            pen.begin_fill()
            for _ in range(4):
                pen.forward(30)
                pen.left(90)
            pen.end_fill()

    pen.hideturtle()
    turtle.done()
