import turtle

def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.speed(15)

    col = ("white","pink","cyan")
    for i in range (300):
        t.pencolor(col[i%3])
        t.forward(i*4)
        t.right(121)

    s.exitonclick()

if __name__ == "__main__":
    main()