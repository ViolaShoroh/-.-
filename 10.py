import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import base64
import keyboard

class PasswordManager:
    def __init__(self):
        self.password_file = "passwords.txt"
        self.font_size = 12
        self.run_attempts = 0
        self.counter = 0
        self.attempts_counter = 0


        self.create_password_window()

    def create_password_window(self):
        self.create_password_root = tk.Tk()
        self.create_password_root.title("Создать пароли")
        self.create_password_root.geometry('280x210')

        self.password1_label = tk.Label(self.create_password_root,
                                        text="Пароль для изменения размера шрифта:")
        self.password1_label.pack(pady=5)
        self.password1_entry = tk.Entry(self.create_password_root, show="*")
        self.password1_entry.pack(pady=5)

        self.password2_label = tk.Label(self.create_password_root,
                                        text="Пароль для запуска программы:")
        self.password2_label.pack(pady=5)
        self.password2_entry = tk.Entry(self.create_password_root, show="*")
        self.password2_entry.pack(pady=5)

        self.save_button = tk.Button(self.create_password_root, text="Сохранить",
                                     command=self.save_passwords)
        self.save_button.pack(pady=10)

    def save_passwords(self):
        password1 = self.password1_entry.get()
        password2 = self.password2_entry.get()

        if len(password1) < 8 or len(password2) < 8 or not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1) or not any(char.isdigit() for char in password2) or not any(char.isalpha() for char in password2):
            messagebox.showerror("Ошибка",
                                 "Оба пароля должны быть не меньше 8 символов и содержать в себе цифры и буквы.")
        else:
            encoded_password1 = base64.b64encode(password1.encode()).decode()
            encoded_password2 = base64.b64encode(password2.encode()).decode()

            with open(self.password_file, 'w') as file:
                json.dump({'password1': encoded_password1, 'password2': encoded_password2}, file)

            self.create_password_root.destroy()
            self.show_menu()

    def show_menu(self):
        self.menu_root = tk.Tk()
        self.menu_root.title("Меню")
        self.menu_root.geometry('280x130')

        self.font_button = tk.Button(self.menu_root, text="Изменить размер шрифта",
                                     command=self.change_font_size)
        self.font_button.pack(pady=10)

        self.run_button = tk.Button(self.menu_root, text="Запустить программу",
                                    command=self.run_program)
        self.run_button.pack(pady=10)

    def change_font_size(self):
        entered_password = simpledialog.askstring("Изменить размер шрифта",
                                                  "Введите пароль:", show='*')

        passwords = self.load_passwords()

        if entered_password == passwords['password1']:
            font_size_entry = simpledialog.askinteger("Размер шрифта",
                                                      "Введите размер(12-24):", minvalue=12, maxvalue=24)
            if font_size_entry:
                self.font_size = font_size_entry

    def run_program(self):
        if self.counter == 6:
            messagebox.showwarning("Предупреждение", "Смените пароль")
            self.create_password_window()
            return
        entered_password = simpledialog.askstring("Запустить программу",
                                                  "Введите пароль:",
                                                  show='*')
        passwords = self.load_passwords()
        if entered_password == passwords['password2']:
            self.counter += 1
            self.menu_root.destroy()
            self.program_root = tk.Tk()
            self.program_root.title("Программа")
            self.program_label = tk.Label(self.program_root, text="Шморгай", font=("Arial", self.font_size))
            self.program_label.pack(expand=True)
            self.program_root.mainloop()
        else:
            self.attempts_counter += 1
            messagebox.showerror("Ошибка",
                                 "Неверный пароль. Осталось попыток: ".format(3 - self.attempts_counter))
            if self.attempts_counter == 3:
                self.menu_root.after(0, lambda: self.menu_root.focus_force())

    def change_label_text(self):
        if self.program_label.cget("text") == "Шморгай":
            self.program_label.config(text="21-ВТ-2")
        elif self.program_label.cget("text") == "21-ВТ-2":
            self.program_label.config(text="46 вариант")
        elif self.program_label.cget("text") == "46 вариант":
            self.program_label.config(text="Шморгай")
        self.program_label.after(5000, self.change_label_text)


    def load_passwords(self):
        try:
            with open(self.password_file, 'r') as file:
                passwords = json.load(file)
                passwords['password1'] = base64.b64decode(passwords['password1']).decode()
                passwords['password2'] = base64.b64decode(passwords['password2']).decode()
            return passwords
        except (FileNotFoundError, json.JSONDecodeError):
            return {'password1': '', 'password2': ''}

if __name__ == "__main__":
    password_manager = PasswordManager()
    tk.mainloop()
