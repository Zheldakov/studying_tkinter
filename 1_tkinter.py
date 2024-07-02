# Изучение библиотеки tkinter
from tkinter import *

root = Tk()                                 # Объект библиотеки
root.title("Тестовое приложенине")          # Название окна
root.iconbitmap("serpmolot.ico")            # ico в заголовке окна
root.geometry("600x600")                    # Установка размеров окна
# прещает или разрешает изменять ширину и высоту
root.resizable(width=False, height=True)
# root.config(bg ='yellow')                  # Цвет фона окна (1-й способ)
root['bg'] = "green"                        # Цвет фона окна (2-й способ)

# Работа с кнопкой
def click():
    # функция для кнопки
    print("Привет")


btn = Button(root, text='Кнопка', command=click,   # Описание кнопки (если вызывать функцию со скобками click(), функция вызовится 1 раз
             #font='Arial 20',                          # Шрифт (1-й вариант)
             font=('Comic Sans MS', 20, 'bold'),                # Шрифт задается картежем, если он не в одно слово (2-й вариант)
             #  width = 10,                             # Ширена кнопки
             #  height= 10,                             # Высота кнопки
             bg='lime',                                 # фон кнопки
             fg='yellow',                                 # цвет текста
             activebackground="red",                    # фон нажатой кнопки
             activeforeground="white",                   # цвет фона при нажатии
            #  state=['disabled']                          # прописываем для отключения кнопки(нельзяя с ней взаимодействовать)
 
            )


btn.pack()                                                 # Отображение кнопки


root.mainloop()                             # Вызов окна