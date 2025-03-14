from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("tk root title")
        self.__root.geometry(f"{width}x{height}")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running_status = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running_status = True
        while self.__running_status:
            self.redraw()

    def close(self):
        self.__running_status = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)