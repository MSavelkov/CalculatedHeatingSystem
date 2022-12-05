import tkinter as tk
from tkinter.ttk import Combobox

class FirstWindow(tk.Toplevel):
    """ Создание рабочего окна """
    def __init__(
            self, resizable=(False, False), title='Система отопления'
    ):
        """ Параметры рабочего окна """
        self.win = tk.Toplevel()
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='#FFA07A')
        self.win.title(title)

        # Вывод обозначения аргументов
        # Узел отопления
        tk.Label(self.win, text='Система отопления', font=('Arial', 15), bg='#FFA07A').grid(row=0, column=1)
        tk.Label(self.win, text='Первичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=1, column=1)
        # Маркеровка кода блока
        tk.Label(self.win, text='Код блока', font=('Arial', 15), bg='#FFA07A').grid(row=2, column=0, stick='w')
        self.cod_load = tk.Entry(self.win)
        self.cod_load.grid(row=2, column=1)

        tk.Label(self.win, text='Отопительная нагрузка', font=('Arial', 14), bg='#FFA07A').grid(row=3, column=0,
                                                                                                stick='w')
        tk.Label(self.win, text='Расход воды на отопление', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=0,
                                                                                                   stick='w')
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=2, stick='w')
        tk.Label(self.win, text='Выбор диаметра трубы', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=0,
                                                                                               stick='w')
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=2, stick='w')
        tk.Label(self.win, text='Скорость воды на отопление', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=0,
                                                                                                     stick='w')
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=2, stick='w')
        # Вторичный контур отопления
        tk.Label(self.win, text='Вторичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=7, column=1)
        tk.Label(self.win, text='Температура подачи', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=0,
                                                                                             stick='w')
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=2,
                                                                                             stick='w')
        tk.Label(self.win, text='Температура обратной', font=('Arial', 14), bg='#FFA07A').grid(row=9, column=0,
                                                                                               stick='w')
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=9, column=2,
                                                                                             stick='w')
        tk.Label(self.win, text='Расход воды на отопление', font=('Arial', 14), bg='#FFA07A').grid(row=10, column=0,
                                                                                                   stick='w')
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=10, column=2, stick='w')
        tk.Label(self.win, text='Выбор диаметра трубы', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=0,
                                                                                               stick='w')
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=2, stick='w')
        tk.Label(self.win, text='Скорость воды на отопление', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=0,
                                                                                                     stick='w')
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=2, stick='w')

        # Создание окн ввода информации
        self.warm_load = tk.Entry(self.win)
        self.warm_consumption = tk.Entry(self.win, bg='#D3D3D3')
        self.warm_speed = tk.Entry(self.win, bg='#D3D3D3')
        self.temp_in_t1 = tk.Entry(self.win)
        self.temp_from_t2 = tk.Entry(self.win)
        self.warm_consumption1 = tk.Entry(self.win, bg='#D3D3D3')
        self.warm_speed1 = tk.Entry(self.win, bg='#D3D3D3')

        self.warm_load.grid(row=3, column=1)
        self.warm_consumption.grid(row=4, column=1)
        self.warm_speed.grid(row=6, column=1)
        self.temp_in_t1.grid(row=8, column=1)
        self.temp_from_t2.grid(row=9, column=1)
        self.warm_consumption1.grid(row=10, column=1)
        self.warm_speed1.grid(row=12, column=1)

        # Вспомогательное окно выбора диаметра и размерности
        self.warm_load_return = Combobox(self.win)
        self.warm_load_return['values'] = ('Гкал/ч', 'Мкал/ч', 'Ккал/ч', 'кВт')
        self.warm_load_return.current(1)
        self.warm_load_return.grid(row=3, column=2)

        self.diametr1 = Combobox(self.win)
        self.diametr1['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr1.current()
        self.diametr1.grid(row=5, column=1)

        self.diametr2 = Combobox(self.win)
        self.diametr2['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr2.current()
        self.diametr2.grid(row=11, column=1)

        # Кнопки добавить и закрыть
        self.btn_cancel = tk.Button(self.win, text='Закрыть', bd=5, command=self.destroy_window)
        self.btn_cancel.grid(row=13, column=2, stick='wens', padx=5, pady=5)
        # btn_ok = tk.Button(self.win, text='Добавить', bd=5)
        # btn_ok.grid(row=12, column=1, stick='wens', padx=5, pady=5)

        # Проверка на окрытие окна
        self.is_open = True

    def destroy_window(self):
       self.win.destroy()
       self.is_open = False