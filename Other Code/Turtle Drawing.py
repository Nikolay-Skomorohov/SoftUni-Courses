from turtle import Turtle
import random


def circle(t, length):
    """Draws a circle with the given length"""
    for count in range(360):
        t.forward(length / 100)
        t.left(1)


def square(t, length):
    """Draws a square with the given length"""
    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t, length):
    """Draws a hexagon with the given length"""
    for count in range(6):
        t.forward(length)
        t.left(60)


def radial_hexagons(t, length, n=25):
    """Draws a radial pattern of n hexas with the given length"""
    for count in range(n):
        for count2 in range(n):
            t.screen.colormode(255)
            t.pencolor(random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
            t.begin_fill()
            t.fillcolor(random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255))
            hexagon(t, length)
            t.left(360 / n)
            t.end_fill()


def random_walk(t, distance, turns=20):
    """Turns a random number of degrees
    and moves a given distance for a fixed number of turns."""
    for x in range(turns):
        t.screen.colormode(255)
        t.pencolor(random.randint(0, 255),
                   random.randint(0, 255),
                   random.randint(0, 255))
        if x % 2 == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
        t.forward(distance)
    t.end_fill()


def main():
    t = Turtle()
    t.shape("turtle")

    while True:
        command = input("Square, Hexagon, Radial, Circle, Random: ")
        length = int(input("Enter length: "))
        if command == "Square":
            square(t, length)
            break
        elif command == "Hexagon":
            hexagon(t, length)
            break
        elif command == "Circle":
            circle(t, length)
            break
        elif command == "Random":
            random_walk(t, length)
            break
        elif command == "Radial":
            radial_hexagons(t, length)
            break
        else:
            print("Please enter a valid shape or length.")
            continue


if __name__ == "__main__":
    main()
