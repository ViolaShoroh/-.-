from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.diameter = 100
        self.color = 'red'
        self.text = 'x'
        self.shadow_thickness = 3
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self.master, width=500, height=500)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.circle = self.draw_circle()
        self.text_ids = self.draw_text()
        self.canvas.bind('<Alt-Button-1>',
                         lambda event: self.do_change_sign(event.x, event.y))
        self.canvas.bind('<Control-Button-1>',
                         lambda event: self.do_change(event.x, event.y))
        self.master.bind("<Down>", self.down_arrow)
        self.master.bind("<Up>", self.up_arrow)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        options_menu = Menu(menu, tearoff=0)
        options_menu.add_command(label="100", command=lambda: self.set_diameter(100))
        options_menu.add_command(label="150", command=lambda: self.set_diameter(150))
        options_menu.add_command(label="200", command=lambda: self.set_diameter(200))
        options_menu.add_command(label="250", command=lambda: self.set_diameter(250))
        options_menu.add_command(label="300", command=lambda: self.set_diameter(300))
        options_menu.add_command(label="350", command=lambda: self.set_diameter(350))
        options_menu.add_command(label="400", command=lambda: self.set_diameter(400))
        menu.add_cascade(label="Диаметр", menu=options_menu)

        self.color_scale = Scale(self.master, from_=1200, to=24000,
                                 orient="vertical", command=self.set_color,
                                 length=450)
        self.color_scale.place(x=480, y=10)

    def draw_circle(self):
        self.canvas.delete(ALL)
        x = y = 250
        r = self.diameter // 2
        return self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                       outline=self.color)

    def draw_text(self):
        x = y = 250
        ids = []
        for i in range(-self.shadow_thickness, self.shadow_thickness + 1):
            for j in range(-self.shadow_thickness, self.shadow_thickness + 1):
                id = self.canvas.create_text(x + i, y + j, text=self.text,
                                             font=("Arial", 30))
                ids.append(id)
        return ids

    def do_change_sign(self, x, y):
        if self.is_inside_circle(x, y):
            self.text = '+'
            for id in self.text_ids:
                self.canvas.delete(id)
            self.text_ids = self.draw_text()

    def do_change(self, x, y):
        if self.is_inside_circle(x, y):
            self.text = 'x'
            for id in self.text_ids:
                self.canvas.delete(id)
            self.text_ids = self.draw_text()

    def up_arrow(self, event):
        self.set_thickness(min(5, self.shadow_thickness + 1))

    def down_arrow(self, event):
        self.set_thickness(max(1, self.shadow_thickness - 1))

    def set_thickness(self, thickness):
        self.shadow_thickness = thickness
        for id in self.text_ids:
            self.canvas.delete(id)
        self.text_ids = self.draw_text()

    def set_diameter(self, diameter):
        if diameter in (100, 150, 200, 250, 300, 350, 400):
            self.diameter = diameter
            self.circle = self.draw_circle()
            self.text_ids = self.draw_text()

    def set_color(self, value):
        if 1200 <= self.color_scale.get() < 5000:
            self.color = 'red'
        elif 5000 <= self.color_scale.get() < 8800:
            self.color = 'orange'
        elif 8800 <= self.color_scale.get() < 12600:
            self.color = 'purple'
        elif 12600 <= self.color_scale.get() < 16400:
            self.color = 'green'
        elif 16400 <= self.color_scale.get() < 20200:
            self.color = 'blue'
        elif 20200 <= self.color_scale.get() <= 24000:
            self.color = 'black'
        self.master.title(self.color)
        self.circle = self.draw_circle()
        self.text_ids = self.draw_text()
        
    def is_inside_circle(self, x, y):
        x0, y0, x1, y1 = self.canvas.coords(self.circle)
        r = (x1 - x0) / 2
        x_center, y_center = x0 + r, y0 + r
        if ((x - x_center)**2 + (y - y_center)**2) <= (r**2):
            return True
        else:
            return False
        
root = Tk()
root.title("red")
root.geometry('550x500')
root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()
