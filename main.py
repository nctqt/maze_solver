from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    # A larger, more visible line
    a = Point(100, 100)
    b = Point(700, 500)
    line = Line(a, b)
    win.draw_line(line, "red")

    # Add a few more lines to make sure drawing works
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "blue")
    win.draw_line(Line(Point(0, 600), Point(800, 0)), "green")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()