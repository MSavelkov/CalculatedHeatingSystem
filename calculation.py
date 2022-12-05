def number_size(translate_num, heat_load):
    """ Функция распознование размерности тепловой нагрузки """
    if translate_num == 'Гкал/ч':
        heat_load = heat_load / 1000
    elif translate_num == 'Мкал/ч':
        heat_load = heat_load
    elif translate_num == 'Ккал/ч':
        heat_load = heat_load / 1000000
    elif translate_num == 'кВт':
        heat_load = heat_load / 1.163
    return heat_load

def get_water_consumption(heat_load, temprature_1, temprature_2):
    """ Функия расчета расхода сетевой воды """
    water_consumption = heat_load / (temprature_1 - temprature_2)
    return round(water_consumption, 3)

def get_speed_in_the_pipe(water_consumption, diametr):
    """ Фунцкия расчета скорости сетевой воды в трубопроводе """
    water_speed = ((18.8 / diametr) ** 2) * water_consumption
    return round(water_speed, 3)

def get_consumption_circulation(consumption, circulation):
    """ Фунцкия расчета циркуляции воды """
    consumption_cir = consumption * (circulation / 100)
    return round(consumption_cir, 3)


