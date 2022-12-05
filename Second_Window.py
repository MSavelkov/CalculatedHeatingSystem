import tkinter as tk
from tkinter.ttk import Combobox

class SecondWindow(tk.Toplevel):
    """ Создание рабочего окна """
    def __init__(
            self, resizable=(False, False), title='Система горячего водоснабжения'
    ):
        """ Параметры рабочего окна """
        self.win = tk.Toplevel()
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='#FFA07A')
        self.win.title(title)

        # ГВС 1 ступени
        tk.Label(self.win, text='ГВС одноступенчатая', font=('Arial', 15), bg='#FFA07A').grid(row=0, column=1)
        tk.Label(self.win, text='Первичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=1, column=1)
        # Маркеровка кода блока
        tk.Label(self.win, text='Код блока', font=('Arial', 15), bg='#FFA07A').grid(row=2, column=0, stick='w')
        self.cod_load = tk.Entry(self.win)
        self.cod_load.grid(row=2, column=1)
        # Ввод прямой сетевой воды
        tk.Label(self.win, text='Температура прямой (лето)', font=('Arial', 14), bg='#FFA07A').grid(row=3, column=0,
                                                                                               stick='w')
        self.temp_t1_gfs = tk.Entry(self.win)
        self.temp_t1_gfs.grid(row=3, column=1)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=3, column=2, stick='w')

        # Ввод обратной сетевой воды
        tk.Label(self.win, text='Температура обратной (лето)', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=0,
                                                                                                 stick='w')
        self.temp_t2_gfs = tk.Entry(self.win)
        self.temp_t2_gfs.grid(row=4, column=1)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=2, stick='w')

        # Ввод нагрузки ГВС
        tk.Label(self.win, text='Нагрузка ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=0, stick='w')
        self.gfs_load = tk.Entry(self.win)
        self.gfs_load.grid(row=5, column=1)
        self.translate_gfs = Combobox(self.win)
        self.translate_gfs['values'] = ('Гкал/ч', 'Мкал/ч', 'Ккал/ч', 'кВт')
        self.translate_gfs.current(1)
        self. translate_gfs.grid(row=5, column=2)

        # Результат расход воды на гвс
        tk.Label(self.win, text='Расход воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=0, stick='w')
        self.gfs_consumption = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs_consumption.grid(row=6, column=1)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=2, stick='w')

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра трубы', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=0, stick='w')
        self.diametr_gfs = Combobox(self.win)
        self.diametr_gfs['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr_gfs.current()
        self.diametr_gfs.grid(row=7, column=1)
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=2, stick='w')

        # Результат расчета скорости воды на ГВС
        tk.Label(self.win, text='Скорость воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=0, stick='w')
        self.gfs_speed = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs_speed.grid(row=8, column=1)
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=2, stick='w')

        tk.Label(self.win, text='Вторичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=9, column=1)

        # Ввод температуры гвс
        tk.Label(self.win, text='Температура ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=10, column=0, stick='w')
        self.temp_gfs = tk.Entry(self.win)
        self.temp_gfs.grid(row=10, column=1)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=10, column=2, stick='w')

        # Ввод температуры хвс
        tk.Label(self.win, text='Температура ХВС', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=0, stick='w')
        self.temp_hfs = tk.Entry(self.win)
        self.temp_hfs.grid(row=11, column=1)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=2, stick='w')

        # Результат расход воды на ГВС
        tk.Label(self.win, text='Расход воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=0, stick='w')
        self.gfs_consumption1 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs_consumption1.grid(row=12, column=1)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=2, stick='w')

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=13, column=0, stick='w')
        self.diametr_gfs1 = Combobox(self.win)
        self.diametr_gfs1['values'] = (15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr_gfs1.current()
        self.diametr_gfs1.grid(row=13, column=1)
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=13, column=2, stick='w')

        # Результат расчета скорости воды на ГВС
        tk.Label(self.win, text='Скорость воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=14, column=0, stick='w')
        self.gfs_speed1 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs_speed1.grid(row=14, column=1)
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=14, column=2, stick='w')

        # Циркуляция
        tk.Label(self.win, text='Процент циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=15, column=0, stick='w')
        self.circulation = tk.Entry(self.win)
        self.circulation.grid(row=15, column=1)
        tk.Label(self.win, text='%', font=('Arial', 14), bg='#FFA07A').grid(row=15, column=2, stick='w')

        # Расход циркуляции
        tk.Label(self.win, text='Расход циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=16, column=0, stick='w')
        self.consumption_cir = tk.Entry(self.win, bg='#D3D3D3')
        self.consumption_cir.grid(row=16, column=1)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=16, column=2, stick='w')

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=17, column=0,
                                                                                               stick='w')
        self.diametr_cir = Combobox(self.win)
        self.diametr_cir['values'] = (15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr_cir.current()
        self.diametr_cir.grid(row=17, column=1)
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=17, column=2, stick='w')

        # Результат расчета скорости воды на циркуляции
        tk.Label(self.win, text='Скорость циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=18, column=0, stick='w')
        self.cir_speed = tk.Entry(self.win, bg='#D3D3D3')
        self.cir_speed.grid(row=18, column=1)
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=18, column=2, stick='w')

        # Кнопки добавить и закрыть
        self.btn_cancel = tk.Button(self.win, text='Закрыть', bd=5, command=self.destroy_window)
        self.btn_cancel.grid(row=19, column=2, stick='wens', padx=5, pady=5)

        # Проверка на окрытие окна
        self.is_open = True

    def destroy_window(self):
        self.win.destroy()
        self.is_open = False