from tkinter import *
import time

# Создание окна
root = Tk()
root.title('Ноябрь 2023')
root.geometry("600x420")
root.resizable(width=False, height=False)


# Функция для получения дней месяца
def days_in_month(year, month):
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return 29
    else:
        return [31,28,31,30,31,30,31,31,30,31,30,31][month-1]

# Задание размеров окна
canvas_width = 600
canvas_height = 410

# Создание холста
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Определение размеров ячейки и шрифта
cell_width = 80
cell_height = 50
font_size = 14

# Определение начальной позиции для метки
marker_x = cell_width*3 + 12
marker_y = cell_height*5 + 10

# Создание функции для рисования календаря
def draw_calendar(year, month):

    # Дни недели
    days_of_week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    for i in range(7):
        canvas.create_text(i * cell_width + cell_width // 2,
                           cell_height * 2 - cell_height,
                           text=days_of_week[i],
                           font=('Arial', font_size), fill='black')

    # Дни месяца
    num_days = days_in_month(year, month)
    start_day = time.strptime(f'{year}-{month}-01', '%Y-%m-%d').tm_wday
    for i in range(1, num_days+1):
        x = (start_day + i - 1) % 7
        y = (start_day + i - 1) // 7 + 2
        canvas.create_text(x * cell_width + cell_width // 2,
                           y * cell_height - cell_height // 4,
                           text=str(i), font=('Arial', font_size), fill='black')
    # Метка на последнем дне месяца
    canvas.create_polygon(marker_x+10, marker_y+10, marker_x+40, marker_y+10,
                          marker_x+50,marker_y+25, marker_x+40, marker_y+40,
                          marker_x+10, marker_y+40, marker_x, marker_y+25,
                          fill='', outline='red', width=3, tag='c')
    
# Функция для движения метки
def animate():
    global marker_x, marker_y
    while True:
        marker_x -= cell_width
        if marker_x < 10:
            marker_x = canvas_width - cell_width - 24
            marker_y -= cell_height
        if marker_y == 60 and marker_x == 96:
            marker_y = cell_height*5 + 10
            marker_x = cell_width*3 + 12
        canvas.delete('c')
        draw_calendar(2023,11)
        canvas.update()
        time.sleep(0.6)
        # Проверяем, была ли нажата кнопка "Стоп"
        if stop_flag:
            break
    # Возвращаем метку на начальное положение
    canvas.delete('c')
    marker_x = cell_width*3 + 12
    marker_y = cell_height*5 + 10
    draw_calendar(2023,11)
    


def start():
    global stop_flag
    stop_flag = False
    # Запускаем анимацию
    animate()

def stop():
    global stop_flag
    stop_flag = True
    

# Создание кнопок
start_button = Button(root, text='Пуск', command=start, width=10,
                           height=5)
start_button.place(x=220, y=310)


main_menu = Menu()
main_menu.add_cascade(label="Стоп", command=stop)



draw_calendar(2023,11)

root.config(menu=main_menu)
# Запуск главного цикла
root.mainloop()
