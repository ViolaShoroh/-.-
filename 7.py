import tkinter as tk
from random import randint

class MatrixApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x350")
        self.matrix_frame = None
        self.texts = []
        self.labels = []
        self.matrix_model = []
        self.matrix_width = tk.IntVar(self)
        self.matrix_height = tk.IntVar(self)
        self.matrix_width.set(0)
        self.matrix_height.set(0)
        self.init_ui()
        self.draw_matrix()
        
    def init_ui(self):
        self.matrix_height_listbox = tk.Listbox(self, width=10, height=20,
                                                font="Arial 11",
                                                exportselection=False)
        self.matrix_width_listbox = tk.Listbox(self, width=10, height=20,
                                               font="Arial 11",
                                               exportselection=False)
        lb1 = tk.Label(self, text="Высота")
        lb2 = tk.Label(self, text="Ширина")
        lb1.place(x=15, y=300)
        lb2.place(x=95, y=300)
        for i in range(9, 12):
            self.matrix_height_listbox.insert(tk.END, i)
            self.matrix_width_listbox.insert(tk.END, i)
        self.matrix_height_listbox.grid(row=0, column=0, sticky='w')
        self.matrix_width_listbox.grid(row=0, column=1, sticky='w')
        self.matrix_height_listbox.bind('<<ListboxSelect>>',
                                        self.on_listbox_select)
        self.matrix_width_listbox.bind('<<ListboxSelect>>',
                                       self.on_listbox_select)
        self.bind('<Return>', self.highlight_row)
        
    def on_listbox_select(self, _):
        if self.matrix_height_listbox.curselection():
            self.matrix_height.set(int(self.matrix_height_listbox.get(self.matrix_height_listbox.curselection())))
        if self.matrix_width_listbox.curselection():
            self.matrix_width.set(int(self.matrix_width_listbox.get(self.matrix_width_listbox.curselection())))
        self.draw_matrix()
        
    def draw_matrix(self):
        width = self.matrix_width.get()
        height = self.matrix_height.get()
        self.matrix_model = []
        if self.matrix_frame:
            self.matrix_frame.destroy()
        self.matrix_frame = tk.Frame(self)
        self.matrix_frame.grid(row=0, column=2)
        self.texts = []
        self.labels = []
        for current_row in range(height):
            self.matrix_model.append([])
            self.texts.append(tk.Text(self.matrix_frame, height=1,width=40, borderwidth=2))
            self.texts[current_row].grid(row=current_row, column=0, sticky="we")
            count = 0
            for cell in range(width):
                value = randint(-100, 100)
                self.matrix_model[current_row].append(value)
                if 10 <= abs(value) <= 99 and str(abs(value))[0] <= str(abs(value))[-1]:
                    count += sum(int(digit) for digit in str(abs(value)))
                self.texts[current_row].insert(tk.END, str(value) + " ")
            self.labels.append(tk.Label(self.matrix_frame, text=str(count), borderwidth=2, relief="groove"))
            self.labels[-1].grid(row=current_row, column=1)

    def highlight_row(self, _):
        height = self.matrix_height.get()
        width = self.matrix_width.get()
        max_row_index = -1
        max_count = 0
        for row in range(height):
            count = 0
            for j in range(width):
                if 10 <= abs(self.matrix_model[row][j]) <= 99:
                    first_digit = int(str(abs(self.matrix_model[row][j]))[0])
                    second_digit = int(str(abs(self.matrix_model[row][j]))[-1])
                    if first_digit <= second_digit:
                        count += sum(int(digit) for digit in str(abs(self.matrix_model[row][j])))
            if count > max_count:
                max_count = count
                max_row_index = row
        for i in range(height):
            if i == max_row_index:
                self.texts[i].config(bg='green', state='disabled')
                self.labels[i].config(bg='green')
            else:
                self.texts[i].config(bg='white', state='disabled')
                self.labels[i].config(bg='white')
            

if __name__ == "__main__":
    app = MatrixApp()
    app.mainloop()
