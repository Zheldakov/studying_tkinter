# Изучение библиотеки tkinter
from tkinter import *

root = Tk()                                 # Объект библиотеки
root.title("Тестовое приложенине")          # Название окна
root.iconbitmap("serpmolot.ico")            # ico в заголовке окна
root.geometry("800x800")                    # Установка размеров окна
# прещает или разрешает изменять ширину и высоту
root.resizable(width=False, height=True)
# root.config(bg ='yellow')                  # Цвет фона окна (1-й способ)
root['bg'] = "green"                        # Цвет фона окна (2-й способ)

# Виджет кнопка___________________________________________________


def click():
    # функция для кнопки
    print("Привет")


btn = Button(root, text='Кнопка', command=click,   # Описание кнопки (если вызывать функцию со скобками click(), функция вызовится 1 раз
             # font='Arial 20',                         # Шрифт (1-й вариант)
            
             font=('Comic Sans MS', 20, 'bold'),        # Шрифт задается картежем, если он не в одно слово (2-й вариант)
             #  width = 10,                             # Ширена кнопки
             #  height= 10,                             # Высота кнопки
             bg='lime',                                 # фон кнопки
             fg='yellow',                               # цвет текста
             activebackground="red",                    # фон нажатой кнопки
             activeforeground="white",                  # цвет фона при нажатии
             #  state=['disabled']                      # прописываем для отключения кнопки(нельзяя с ней взаимодействовать)
             )

btn.pack()                                              # Отображение кнопки
#btn.place(x=10,y=10)                                   # Если нет pac() - определяет координаты прорисовки

# Виджет Lable______________________________________________________

label = Label(root,
              text='Какойто текст',
              font=('Comic Sans MS', 20, 'bold'),
              bg='lime',
              fg='brown'

              )

label.pack()  # Отображение Lable

# Картинка через Lable

img=PhotoImage(file='pic.png')                      # Объект картинка
logo = Label(root,image=img)                        # Lable с картинкой
logo.pack()

# Виджет Текстовое Поле_____________________________

text_form=Entry(root,               # Создание объекта текстового поля 
                #show='x'           #(ПАРАМЕТР show = "*" заменит все символы в строке на *)
                )              
text_form.pack()                    # Отображение текстового поля

text_form.insert(0, "Hello")        # Добавление надписи по умолчаеию (начинается текст с индекса 0)
text_form.insert(END, " World")     # (начинается текст с индекса END)


text_form.insert(END,"AAAA")        # Метод добавление текста в поле
print(text_form.get())              # Метод получает данные из поля
text_form.delete(0, END)            # Метод удоляет от нулевого индекса до конца в поле





root.mainloop()                                     # Вызов окна!!!