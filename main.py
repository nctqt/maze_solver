from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)



    # A larger, more visible line
    a = Point(100, 100)
    b = Point(200, 200)
    c = Point(350, 350)
    d = Point(550, 550)
    #line = Line(a, b)
    #win.draw_line(line, "red")

    # Add a few more lines to make sure drawing works
    #win.draw_line(Line(Point(0, 0), Point(800, 600)), "blue")
    #win.draw_line(Line(Point(0, 600), Point(800, 0)), "green")
    
    c1 = Cell(win)
    c2 = Cell(win)

    c1.draw(a.x, a.y, b.x, b.y)
    c2.draw(c.x, c.y, d.x, d.y)

    c1.draw_move(c2, undo=True)

    win.wait_for_close()


if __name__ == "__main__":
    main()