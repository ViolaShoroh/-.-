import tkinter as tk
import math


class Triangle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.angle = 0
        self.id = None
    
    def draw(self):
        x0, y0 = 400, 350
        x1, y1 = x0 + 300, y0
        x2, y2 = x0, y0 - 300
        self.id = self.canvas.create_polygon(x0, y0, x1, y1, x2, y2)
    
    def rotate(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0
        x0, y0 = 400, 350
        x1, y1 = x0 + 300 * math.cos(math.radians(-self.angle)), y0 - 300 * math.sin(math.radians(-self.angle))
        x2, y2 = x0 - 300 * math.sin(math.radians(-self.angle)), y0 - 300 * math.cos(math.radians(-self.angle))
        self.canvas.coords(self.id, x0, y0, x1, y1, x2, y2)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.triangle = Triangle(self.canvas)
        self.triangle.draw()
        self.is_running = False
        self.timer_id = None
        self.create_widgets()
    
    def create_widgets(self):
        start_button = tk.Button(self.root, text='Пуск', command=self.start, width=10,
                           height=10)
        start_button.place(x=20, y=40)
        pause_button = tk.Button(self.root, text='Пауза', command=self.pause, width=10,
                           height=10)
        pause_button.place(x=20, y=220)
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.rotate()
    
    def pause(self):
        if self.is_running:
            self.is_running = False
            self.canvas.after_cancel(self.timer_id)
    
    def rotate(self):
        self.triangle.rotate()
        if self.is_running:
            self.timer_id = self.canvas.after(100, self.rotate)

app = App()
app.root.mainloop()
