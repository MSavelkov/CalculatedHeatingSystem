import tkinter as tk
from tkinter import filedialog as fd
from First_Window import FirstWindow
from Second_Window import SecondWindow
from Third_Window import ThirdWindow
from tkinter.ttk import Combobox
from calculation import number_size, get_water_consumption, get_speed_in_the_pipe, get_consumption_circulation
import json

class Window:
    """ Создание рабочего окна """
    def __init__(
            self, title='Программа расчета блочного теплового пункта', resizable=(False, False)
    ):
        """ Параметры рабочего окна """
        self.win = tk.Tk()
        self.win.title(title)
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='#FFA07A')
        self.win.iconbitmap('windy_forecast_pressure_air_weather_icon_228440.ico')
        self.result = {
            'Узел ввода': {},
        }

        # Вспомогательное окно выбора диаметра и размерности
        self.heat_load_return = Combobox(self.win)
        self.heat_load_return['values'] = ('Гкал/ч', 'Мкал/ч', 'Ккал/ч', 'кВт')
        self.heat_load_return.current(1)
        self.heat_load_return.grid(row=3, column=2)

        self.diametr = Combobox(self.win)
        self.diametr['values'] = (25, 32, 40, 50, 65, 80, 100, 125, 150, 200)
        self.diametr.current(0)
        self.diametr.grid(row=7, column=1)

        # Создание окн ввода информации
        self.heat_load = tk.Entry(self.win)
        self.temp_in = tk.Entry(self.win)
        self.temp_from = tk.Entry(self.win)
        self.water_consumption = tk.Entry(self.win, bg='#D3D3D3')
        self.water_speed = tk.Entry(self.win, bg='#D3D3D3')

        self.heat_load.grid(row=3, column=1)
        self.temp_in.grid(row=4, column=1)
        self.temp_from.grid(row=5, column=1)
        self.water_consumption.grid(row=6, column=1)
        self.water_speed.grid(row=8, column=1)

        # Вывод обозначения аргументов
        tk.Label(self.win, text='Программа расчета блочного теплового пункта',
                 font=('Arial', 20), bg='#FFA07A').grid(row=0, column=0, columnspan=3)
        # Узел ввода
        tk.Label(self.win, text='Узел ввода', font=('Arial', 15), bg='#FFA07A').grid(row=1, column=1)
        # Маркеровка кода блока
        tk.Label(self.win, text='Код блока', font=('Arial', 15), bg='#FFA07A').grid(row=2, column=0, stick='w')
        self.cod_load = tk.Entry(self.win)
        self.cod_load.grid(row=2, column=1)

        tk.Label(self.win, text='Тепловая нагрузка', font=('Arial', 14), bg='#FFA07A').grid(row=3, column=0, stick='w')
        tk.Label(self.win, text='Температура прямой', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=0, stick='w')
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=4, column=2, stick='w')
        tk.Label(self.win, text='Температура обратной', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=0,
                                                                                               stick='w')
        tk.Label(self.win, text=u'\N{DEGREE SIGN} C', font=('Arial', 14), bg='#FFA07A').grid(row=5, column=2, stick='w')
        tk.Label(self.win, text='Расход сетевой воды', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=0,
                                                                                              stick='w')
        tk.Label(self.win, text='м\u00B3/ч', font=('Arial', 14), bg='#FFA07A').grid(row=6, column=2, stick='w')
        tk.Label(self.win, text='Выбор диаметра циркуляции', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=0,
                                                                                                    stick='w')
        tk.Label(self.win, text='мм', font=('Arial', 14), bg='#FFA07A').grid(row=7, column=2, stick='w')
        tk.Label(self.win, text='Скорость сетевой воды', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=0,
                                                                                                stick='w')
        tk.Label(self.win, text='м/c', font=('Arial', 14), bg='#FFA07A').grid(row=8, column=2, stick='w')

        btn_creat_win1 = tk.Button(text='Добавить систему отопления', bd=5, command=self.creat_win1)
        btn_creat_win1.grid(row=9, column=0, columnspan=7, stick='wens', padx=5, pady=5)
        btn_creat_win2 = tk.Button(text='Добавить систему ГВС - 1', bd=5, command=self.creat_win2)
        btn_creat_win2.grid(row=10, column=0, columnspan=7, stick='wens', padx=5, pady=5)
        btn_creat_win3 = tk.Button(text='Добавить систему ГВС - 2', bd=5, command=self.creat_win3)
        btn_creat_win3.grid(row=11, column=0, columnspan=7, stick='wens', padx=5, pady=5)
        btn_calculate = tk.Button(text='Результат', bd=5, command=self.get_calculate)
        btn_calculate.grid(row=12, column=1, columnspan=2, stick='wens', padx=5, pady=5)
        save_ = tk.Button(text='Сохранить результат', bd=5, command=self.save_file)
        save_.grid(row=12, column=0, columnspan=1, stick='wens', padx=5, pady=5)

        self.wins: list[FirstWindow] = []
        self.win2: list[SecondWindow] = []
        self.win3: list[ThirdWindow] = []

    def run_win(self):
        """ Запуск рабочего окна """
        self.win.mainloop()

    def creat_win1(self):
        """ Создание дополниетльного окна """
        self.wins.append(FirstWindow())

    def creat_win2(self):
        """ Создание дополниетльного окна """
        self.win2.append(SecondWindow())

    def creat_win3(self):
        """ Создание дополниетльного окна """
        self.win3.append(ThirdWindow())

    def get_calculate(self):
        """ Калькурятор """
        cod_load = self.cod_load.get()
        heat = float(self.heat_load.get())
        heat_load_return = self.heat_load_return.get()
        temp_in = int(self.temp_in.get())
        temp_from = int(self.temp_from.get())
        diametr = int(self.diametr.get())

        converted_heat_load = number_size(translate_num=heat_load_return, heat_load=heat)
        consumption = get_water_consumption(heat_load=converted_heat_load, temprature_1=temp_in, temprature_2=temp_from)
        speed = get_speed_in_the_pipe(water_consumption=consumption, diametr=diametr)

        self.water_consumption.delete(0, 'end')
        self.water_speed.delete(0, 'end')
        self.water_speed.insert(0, speed)
        self.water_consumption.insert(0, consumption)

        result = self.result['Узел ввода']
        result['Код блока'] = cod_load
        result['Тепловая нагрузка'] = heat
        result['Температура прямой'] = temp_in
        result['Температура обратной'] = temp_from
        result['Диаметр трубы'] = diametr
        result['Скорость'] = speed
        result['Расход сетевой воды'] = consumption

        # Калькулятор для первого окна
        for index, window in enumerate(self.wins, start=1):
            cod_load1 = window.cod_load.get()
            warm = float(window.warm_load.get())
            warm_load_return = window.warm_load_return.get()
            diametr1 = int(window.diametr1.get())
            diametr2 = int(window.diametr1.get())
            temp_t1 = int(window.temp_in_t1.get())
            temp_t2 = int(window.temp_from_t2.get())

            converted_heat_load = number_size(translate_num=warm_load_return, heat_load=warm)
            consumption1 = get_water_consumption(heat_load=converted_heat_load, temprature_1=temp_in, temprature_2=temp_from)
            speed1 = get_speed_in_the_pipe(water_consumption=consumption, diametr=diametr1)
            consumption2 = get_water_consumption(heat_load=converted_heat_load, temprature_1=temp_t1, temprature_2=temp_t2)
            speed2 = get_speed_in_the_pipe(water_consumption=consumption2, diametr=diametr2)

            window.warm_consumption.delete(0, 'end')
            window.warm_consumption1.delete(0, 'end')
            window.warm_speed.delete(0, 'end')
            window.warm_speed1.delete(0, 'end')
            window.warm_speed.insert(0, speed1)
            window.warm_speed1.insert(0, speed2)
            window.warm_consumption.insert(0, consumption1)
            window.warm_consumption1.insert(0, consumption2)

            key = f'Узел отопления - {index}'
            self.result[key] = {}
            result = self.result[key]
            result['Код блока'] = cod_load1
            result['Тепловая нагрузка'] = warm
            result['Температура прямой'] = temp_t1
            result['Температура обратной'] = temp_t2
            result['Диаметр трубы'] = diametr1
            result['Диаметр трубы'] = diametr2
            result['Скорость'] = speed1
            result['Расход сетевой воды'] =consumption1
            result['Скорость'] = speed2
            result['Расход сетевой воды'] = consumption2

        # Калькулятор для второго окна
        for index1, window1 in enumerate(self.win2, start=1):
            if window1 and window1.is_open:
                # Первичный контур
                cod_load2 = window1.cod_load.get()
                warm_gfs = float(window1.gfs_load.get())
                t1_gfs = int(window1.temp_t1_gfs.get())
                t2_gfs = int(window1.temp_t2_gfs.get())
                warm_load_gfs = window1.translate_gfs.get()
                diametr_gfs = int(window1.diametr_gfs.get())
                converted_heat_load = number_size(translate_num=warm_load_gfs, heat_load=warm_gfs)
                consumption3 = get_water_consumption(heat_load=converted_heat_load, temprature_1=t1_gfs,
                                                     temprature_2=t2_gfs)
                speed3 = get_speed_in_the_pipe(water_consumption=consumption3, diametr=diametr_gfs)
                window1.gfs_consumption.delete(0, 'end')
                window1.gfs_speed.delete(0, 'end')
                window1.gfs_speed.insert(0, speed3)
                window1.gfs_consumption.insert(0, consumption3)
                # Вторичный контур
                temp_gfs = int(window1.temp_gfs.get())
                temp_hfs = int(window1.temp_hfs.get())
                diametr_gfs1 = int(window1.diametr_gfs1.get())
                consumption4 = get_water_consumption(heat_load=converted_heat_load, temprature_1=temp_gfs,
                                                     temprature_2=temp_hfs)
                speed4 = get_speed_in_the_pipe(water_consumption=consumption4, diametr=diametr_gfs1)
                window1.gfs_consumption1.delete(0, 'end')
                window1.gfs_speed1.delete(0, 'end')
                window1.gfs_speed1.insert(0, speed4)
                window1.gfs_consumption1.insert(0, consumption4)
                # Расход циркуляции
                cir = int(window1.circulation.get())
                diametr_cir = int(window1.diametr_cir.get())
                cir_load = get_consumption_circulation(consumption=consumption4, circulation=cir)
                speed_circulation = get_speed_in_the_pipe(water_consumption=cir_load, diametr=diametr_cir)
                window1.consumption_cir.delete(0, 'end')
                window1.cir_speed.delete(0, 'end')
                window1.cir_speed.insert(0, speed_circulation)
                window1.consumption_cir.insert(0, cir_load)

                key1 = f'ГВС одноступенчатая - {index1}'
                self.result[key1] = {}
                result = self.result[key1]
                result['Код блока'] = cod_load2
                result['Температура прямой'] = t1_gfs
                result['Температура обратной'] = t2_gfs
                result['Тепловая нагрузка'] = warm_gfs
                result['Расход воды на ГВС'] = consumption3
                result['Диаметр трубы'] = diametr_gfs
                result['Скорость'] = speed3
                result['Температура ГВС'] = temp_gfs
                result['Температура ХВС'] = temp_hfs
                result['Расход воды на ГВС'] = consumption4
                result['Диаметр трубы'] = diametr_gfs1
                result['Скорость'] = speed4
                result['Процент циркуляции'] = cir
                result['Расход циркуляции'] = cir_load
                result['Диаметр циркуляции'] = diametr_cir
                result['Скорость циркуляции'] = speed_circulation

        # Калькулятор для третьего окна
        for index2, window2 in enumerate(self.win3, start=1):
            if window2 and window2.is_open:
                # Первичный контур
                cod_load3 = window2.cod_load.get()
                warm_gfs2 = float(window2.gfs2_load.get())
                t1_gfs2 = int(window2.temp_tn1.get())
                t2_gfs2 = int(window2.temp_tn2.get())
                warm_load_gfs2 = window2.translate_gfs2.get()
                diametr1_gfs2 = int(window2.diametr1_gfs2.get())
                diametr2_gfs2 = int(window2.diametr2_gfs2.get())
                consumption5 = int(window2.gfs2_consumption1.get())
                consumption6 = int(window2.gfs2_consumption2.get())

                # converted_heat_load = number_size(translate_num=warm_load_gfs2, heat_load=warm_gfs2)

                speed4 = get_speed_in_the_pipe(water_consumption=consumption5, diametr=diametr1_gfs2)
                speed5 = get_speed_in_the_pipe(water_consumption=consumption6, diametr=diametr2_gfs2)

                #self.win2.gfs_consumption.delete(0, 'end')
                window2.gfs2_speed1.delete(0, 'end')
                window2.gfs2_speed2.delete(0, 'end')

                window2.gfs2_speed1.insert(0, speed4)
                window2.gfs2_speed2.insert(0, speed5)
                #self.win2.gfs_consumption.insert(0, consumption3)

                # Вторичный контур
                temp_gfs_t1 = int(window2.temp_gfs_t1.get())
                temp_hfs_t2 = int(window2.temp_hfs_t2.get())
                diametr2_gfs3 = int(window2.diametr2_gfs3.get())
                diametr2_gfs4 = int(window2.diametr2_gfs4.get())
                consumption7 = int(window2.gfs2_consumption3.get())
                consumption8 = int(window2.gfs2_consumption4.get())

                speed6 = get_speed_in_the_pipe(water_consumption=consumption7, diametr=diametr2_gfs3)
                speed7 = get_speed_in_the_pipe(water_consumption=consumption8, diametr=diametr2_gfs4)

                #self.win2.gfs_consumption1.delete(0, 'end')
                window2.gfs2_speed3.delete(0, 'end')
                window2.gfs2_speed4.delete(0, 'end')

                window2.gfs2_speed3.insert(0, speed6)
                window2.gfs2_speed4.insert(0, speed7)
                #self.win2.gfs_consumption1.insert(0, consumption4)

                # Расход циркуляции
                cir2 = int(window2.circulation2.get())
                diametr_cir2 = int(window2.diametr2_cir.get())
                cir_load2 = get_consumption_circulation(consumption=consumption7, circulation=cir2)
                speed_circulation2 = get_speed_in_the_pipe(water_consumption=cir_load2, diametr=diametr_cir2)

                window2.consumption2_cir2.delete(0, 'end')
                window2.cir2_speed.delete(0, 'end')

                window2.cir2_speed.insert(0, speed_circulation2)
                window2.consumption2_cir2.insert(0, cir_load2)

                key2 = f'ГВС одноступенчатая - {index2}'
                self.result[key2] = {}
                result = self.result[key2]
                result['Код блока'] = cod_load3
                result['Температура прямой'] = t1_gfs2
                result['Температура обратной'] = t2_gfs2
                result['Тепловая нагрузка'] = warm_gfs2
                result['Расход воды на ГВС 1ст'] = consumption5
                result['Расход воды на ГВС 2ст'] = consumption6
                result['Диаметр трубы 1ст'] = diametr1_gfs2
                result['Диаметр трубы 2ст'] = diametr2_gfs2
                result['Скорость воды в 1ст'] = speed4
                result['Скорость воды во 2ст'] = speed5
                result['Температура ГВС'] = temp_gfs_t1
                result['Температура ХВС'] = temp_hfs_t2
                result['Расход воды на ГВС 1ст'] = consumption7
                result['Расход воды на ГВС 2ст'] = consumption8
                result['Диаметр трубы 1ст'] = diametr2_gfs3
                result['Диаметр трубы 2ст'] = diametr2_gfs4
                result['Скорость в 1ст'] = speed6
                result['Скорость во 2ст'] = speed7
                result['Процент циркуляции'] = cir2
                result['Расход циркуляции'] = cir_load2
                result['Диаметр циркуляции'] = diametr_cir2
                result['Скорость циркуляции'] = speed_circulation2

    def save_file(self):
        """ Сохранение данных в файл """
        name = fd.asksaveasfilename(
        defaultextension='json',
        filetypes=[("Текстовые файлы", "*.json"), ("Все файлы", "*.*")],
    )
        if name:
            with open(name, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    win = Window()
    win.run_win()