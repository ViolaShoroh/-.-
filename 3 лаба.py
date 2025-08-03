import tkinter as tk
from PIL import ImageTk, Image
 
root = tk.Tk()
root.geometry("500x500")
root.title("Учебные дисциплины")
root.configure(bg='papaya whip')
root.resizable(width=False, height=False)

class Table:
    #кнопка выхода
    exit_button = tk.Button(root, text="Закрыть", font="Arial 15",
                     bg="red", fg="white", command=root.destroy)
    exit_button.place(x=380, y=450)


    def __init__(self, master):
        self.master = master
        self.names = [("Математический анализ", "Петров В.В."),
                      ("Программирование", "Попов А.С."),
                      ("Русский язык", "Приходько Т.В."),
                      ("Физика", "Иванов А.А."),
                      ("Алгебра", "Маск И.С."),
                      ("Химия", "Нечаев С.А."),
                      ("Вычислительная техника", "Захаров Х.Р."),
                      ("Дискретная математика", "Руденко А.И."),
                      ("Электроника", "Сеченов Д.С."),
                      ("Операционные системы", "Филатова Л.А.")]
        self.check_vars = []
        self.show_labels = []

        self.photo_dict = {"Петров В.В.": ImageTk.PhotoImage(Image.open("Петров В.В..png")),
              "Попов А.С.": ImageTk.PhotoImage(Image.open("Попов А.С..png")),
              "Приходько Т.В.": ImageTk.PhotoImage(Image.open("Приходько Т.В..png")),
              "Иванов А.А.": ImageTk.PhotoImage(Image.open("Иванов А.А..png")),
              "Маск И.С.": ImageTk.PhotoImage(Image.open("Маск И.С..png")),
              "Нечаев С.А.": ImageTk.PhotoImage(Image.open("Нечаев С.А..png")),
              "Захаров Х.Р.": ImageTk.PhotoImage(Image.open("Захаров Х.Р..png")),
              "Руденко А.И.": ImageTk.PhotoImage(Image.open("Руденко А.И..png")),
              "Сеченов Д.С.": ImageTk.PhotoImage(Image.open("Сеченов Д.С..png")),
              "Филатова Л.А.": ImageTk.PhotoImage(Image.open("Филатова Л.А..png"))}

        self.canvas = tk.Canvas(root, width=180, height=150, bg="white")
        self.canvas.place(x=300, y=10)

        self.create_widgets()

    def create_widgets(self):
        for i, name in enumerate(self.names):
            name_label = tk.Label(self.master, text=name[0], bg='papaya whip')
            name_label.grid(row=i, column=0, padx=10, pady=10)

            show_var = tk.BooleanVar()
            show_check = tk.Checkbutton(self.master, variable=show_var, bg='papaya whip')
            show_check.grid(row=i, column=1)
            self.check_vars.append(show_var)

            surname_label = tk.Label(self.master, text=name[1], bg='papaya whip')
            surname_label.grid(row=i, column=2, padx=10, pady=10)
            surname_label.config(fg="papaya whip")
            self.show_labels.append(surname_label)

            name_label.bind("<Button-1>", lambda event, index=i: self.show_surname(index))
            name_label.bind("<Button-2>", lambda event, index=i: self.show_surname(index))
            name_label.bind("<Button-3>", lambda event, index=i: self.show_surname(index))
    def show_surname(self, index):
        if self.check_vars[index].get():
            surname = self.names[index][1]
            self.show_labels[index].config(fg="black")
            self.canvas.delete("all")
            self.canvas.create_image(100, 100, image=self.photo_dict[surname])
        else:
            self.show_labels[index].config(fg='papaya whip')

            
            
table = Table(root)
root.mainloop()
