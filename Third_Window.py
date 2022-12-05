import tkinter as tk
from tkinter.ttk import Combobox

class ThirdWindow(tk.Toplevel):
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
        tk.Label(self.win, text='ГВС двухступенчатая', font=('Arial', 15), bg='#FFA07A').grid(row=0, column=1, columnspan=2)
        tk.Label(self.win, text='Первичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=1, column=1, columnspan=2)
        # Маркеровка кода блока
        tk.Label(self.win, text='Код блока', font=('Arial', 15), bg='#FFA07A').grid(row=2, column=0, stick='w')
        tk.Label(self.win, text='1 ст', font=('Arial', 15), bg='#FFA07A').grid(row=3, column=1, stick='n')
        tk.Label(self.win, text='2 ст', font=('Arial', 15), bg='#FFA07A').grid(row=3, column=2, stick='n')
        self.cod_load = tk.Entry(self.win)
        self.cod_load.grid(row=2, column=1, columnspan=2)

        # Ввод прямой сетевой воды
        tk.Label(self.win, text='Температура прямой (лето)', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=0,
                                                                                                    stick='w')
        self.temp_tn1 = tk.Entry(self.win)
        self.temp_tn1.grid(row=4, column=1, columnspan=2)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=4)

        # Ввод обратной сетевой воды
        tk.Label(self.win, text='Температура обратной (лето)', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=0,
                                                                                                      stick='w')
        self.temp_tn2 = tk.Entry(self.win)
        self.temp_tn2.grid(row=5, column=1, columnspan=2)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=4)

        # Ввод нагрузки ГВС
        tk.Label(self.win, text='Нагрузка ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=0, stick='w')
        self.gfs2_load = tk.Entry(self.win)
        self.gfs2_load.grid(row=6, column=1, columnspan=2)
        self.translate_gfs2 = Combobox(self.win)
        self.translate_gfs2['values'] = ('Гкал/ч', 'Мкал/ч', 'Ккал/ч', 'кВт')
        self.translate_gfs2.current(1)
        self.translate_gfs2.grid(row=6, column=4)

        # Расход воды на гвс
        tk.Label(self.win, text='Расход воды', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=0, stick='w')
        self.gfs2_consumption1 = tk.Entry(self.win)
        self.gfs2_consumption1.grid(row=7, column=1)
        self.gfs2_consumption2 = tk.Entry(self.win)
        self.gfs2_consumption2.grid(row=7, column=2)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=4)

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра трубы', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=0,
                                                                                               stick='w')
        self.diametr1_gfs2 = Combobox(self.win)
        self.diametr1_gfs2['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr1_gfs2.current()
        self.diametr1_gfs2.grid(row=8, column=1)
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=4)

        self.diametr2_gfs2 = Combobox(self.win)
        self.diametr2_gfs2['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr2_gfs2.current()
        self.diametr2_gfs2.grid(row=8, column=2)

        # Результат расчета скорости воды
        tk.Label(self.win, text='Скорость воды', font=('Arial', 14), bg='#FFA07A').grid(row=9, column=0,
                                                                                               stick='w')
        self.gfs2_speed1 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs2_speed1.grid(row=9, column=1)
        self.gfs2_speed2 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs2_speed2.grid(row=9, column=2)
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=9, column=4)

        tk.Label(self.win, text='Вторичный контур', font=('Arial', 15), bg='#FFA07A').grid(row=10, column=1, columnspan=2)

        # Ввод температуры гвс
        tk.Label(self.win, text='Температура ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=0, stick='w')
        self.temp_gfs_t1 = tk.Entry(self.win)
        self.temp_gfs_t1.grid(row=11, column=1, columnspan=2)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=11, column=4)
        # Ввод температуры хвс
        tk.Label(self.win, text='Температура ХВС', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=0, stick='w')
        self.temp_hfs_t2 = tk.Entry(self.win)
        self.temp_hfs_t2.grid(row=12, column=1, columnspan=2)
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=12, column=4)

        # Результат расход воды на ГВС
        tk.Label(self.win, text='Расход воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=13, column=0,
                                                                                             stick='w')
        self.gfs2_consumption3 = tk.Entry(self.win)
        self.gfs2_consumption3.grid(row=13, column=1)
        self.gfs2_consumption4 = tk.Entry(self.win)
        self.gfs2_consumption4.grid(row=13, column=2)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=13, column=4)

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=14, column=0,
                                                                                             stick='w')
        self.diametr2_gfs3 = Combobox(self.win)
        self.diametr2_gfs3['values'] = (15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr2_gfs3.current()
        self.diametr2_gfs3.grid(row=14, column=1)

        self.diametr2_gfs4 = Combobox(self.win)
        self.diametr2_gfs4['values'] = (15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr2_gfs4.current()
        self.diametr2_gfs4.grid(row=14, column=2)

        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=14, column=4)

        # Результат расчета скорости воды на ГВС
        tk.Label(self.win, text='Скорость воды на ГВС', font=('Arial', 14), bg='#FFA07A').grid(row=15, column=0,
                                                                                               stick='w')
        self.gfs2_speed3 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs2_speed3.grid(row=15, column=1)
        self.gfs2_speed4 = tk.Entry(self.win, bg='#D3D3D3')
        self.gfs2_speed4.grid(row=15, column=2)

        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=15, column=4)

        # Циркуляция
        tk.Label(self.win, text='Процент циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=16, column=0,
                                                                                             stick='w')
        self.circulation2 = tk.Entry(self.win)
        self.circulation2.grid(row=16, column=1, columnspan=2)
        tk.Label(self.win, text='%', font=('Arial', 14), bg='#FFA07A').grid(row=16, column=4)

        # Расход циркуляции
        tk.Label(self.win, text='Расход циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=17, column=0, stick='w')
        self.consumption2_cir2 = tk.Entry(self.win, bg='#D3D3D3')
        self.consumption2_cir2.grid(row=17, column=1, columnspan=2)
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=17, column=4)

        # Выбор деаметра трубы
        tk.Label(self.win, text='Выбор диаметра циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=18, column=0,
                                                                                                    stick='w')
        self.diametr2_cir = Combobox(self.win)
        self.diametr2_cir['values'] = (15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr2_cir.current()
        self.diametr2_cir.grid(row=18, column=1, columnspan=2)
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=18, column=4)

        # Результат расчета скорости воды на циркуляции
        tk.Label(self.win, text='Скорость циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=19, column=0,
                                                                                              stick='w')
        self.cir2_speed = tk.Entry(self.win, bg='#D3D3D3')
        self.cir2_speed.grid(row=19, column=1, columnspan=2)
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=19, column=4)

        # Кнопки добавить и закрыть
        self.btn2_cancel = tk.Button(self.win, text='Закрыть', bd=5, command=self.destroy_window)
        self.btn2_cancel.grid(row=20, column=4, stick='wens', padx=5, pady=5)

        self.is_open = True

    def destroy_window(self):
        self.win.destroy()
        self.is_open = False

