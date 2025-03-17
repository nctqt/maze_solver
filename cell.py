from line import Line
from point import Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "red"
        else:
            line_color = "white"
        x_mid_source = (self._x1 + self._x2) / 2
        y_mid_source = (self._y1 + self._y2) / 2
        x_mid_dest = (to_cell._x1 + to_cell._x2) / 2
        y_mid_dest = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(x_mid_source, y_mid_source), Point(x_mid_dest, y_mid_dest))
        self._win.draw_line(line, line_color)
