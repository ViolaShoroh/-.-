import tkinter as tk
import winsound
transfer_conditions = {
    0:['L', 1, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя_', 8],
    1:['i', 2, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    2:['s', 3, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    3:['t', 4, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    4:['b', 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    5:['o', 6, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    6:['x', 7, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    7:['(', 17, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕ-ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 8],
    8:['=', 9],
    9:['L', 10],
    10:['i', 11],
    11:['s', 12],
    12:['t', 13],
    13:['b', 14],
    14:['o', 15],
    15:['x', 16],
    16:['(', 17],
    17:['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя_', 18, ')', 'КОНЕЦ'],
   18:['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуф-хцчшщъыьэюя1234567890_', 18, ')', 'КОНЕЦ'],
}
class App(tk.Tk):
    current_state: tk.StringVar
    entry: tk.Entry
    def __init__(self): 
        super().__init__()
        self.geometry('200x200')
        self.init_ui()
        self.mainloop()
    def init_ui(self):
        self.current_state = tk.StringVar(value='0')
        self.check = (self.register(self.validate), "%P")
        self.entry = tk.Entry(self,validate='key', validatecommand=self.check)
        self.entry.pack()
        tk.Label(self, text='Текущее состояние:').pack()
        tk.Label(self, textvariable=self.current_state).pack()
        tk.Button(self, text='Перезагрузить', command=self.restart).pack()
    def validate(self, entry_string):
        current_state = -1
        if self.current_state.get().isdigit():
            current_state = int(self.current_state.get())
        if len(entry_string) == 0:
            return False
        last_symbol = entry_string[-1]
        if current_state in transfer_conditions.keys():
            transfer_condition = transfer_conditions[current_state]
            if len(transfer_condition) % 2 != 0:
                raise ValueError('transfer conditions has incorrect value')
            condition_count = len(transfer_condition) // 2
            for i in range(condition_count):
                if last_symbol in transfer_condition[0 + i * 2]:
                    self.current_state.set(value=str(transfer_condition[1 + i * 2]))
                    return True
        winsound.Beep(100, 100)
        return False
    def restart(self):
        self.current_state.set(0)
        self.entry.config(validate='none')
        self.entry.delete(0, tk.END)
        self.entry.config(validate='key')
App()
