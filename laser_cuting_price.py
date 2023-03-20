# А если здесь соответствия между этими переменными? ->
# Есть. Словарь может отразить эти соответствия. ->
# Создаем словарь соответсвия толщины к вариантам стоимости.
c = 0.0000078  # надо как-то текст помещать в поле, полное имя 'constant'
thicknesses = {
    1: {'cost_less': 27, 'cost_more': 20},
    2: {'cost_less': 36, 'cost_more': 28},
    3: {'cost_less': 57, 'cost_more': 43},
    4: {'cost_less': 64, 'cost_more': 50},
    5: {'cost_less': 76, 'cost_more': 58},
    6: {'cost_less': 87, 'cost_more': 68},
    8: {'cost_less': 111, 'cost_more': 84},
    10: {'cost_less': 154, 'cost_more': 125},
    12: {'cost_less': 191, 'cost_more': 144},
    14: {'cost_less': 224, 'cost_more': 186},
    16: {'cost_less': 360, 'cost_more': 298},
    20: {'cost_less': 519, 'cost_more': 432},
}


def info_research():
    info_list = []
    # global cutting_length
    cutting_length = info_list.append(int(input('Длинна резки (м/п) = ')))
    inserts_money = info_list.append(int(input('Кол-во вставок шт = ')))
    # global thickness
    thickness = info_list.append(int(input('Толщина (мм) = ')))
    # global metal_cost
    length = info_list.append(int(input('Длинна (мм) = ')))
    width = info_list.append(int(input('Ширина (мм) = ')))
    number_of_pieces = info_list.append(int(input('Кол-во деталей (шт.) = ')))
    info_list.append(f'Площадь металла:{(info_list[3] * info_list[4] *0.000001) * info_list[5]} (м^2)')
    info_list.append(f'Масса маталла:{info_list[3] * info_list[4] * info_list[4] * info_list[5] * c}(кг)')
    info_list.append(f'Стоимость металла: {metal_cost} (руб)')
    return info_list


def metal_cost(length, width, thikness, number_of_pieces):
    thickness = info_list.append(int(input('Толщина (мм) = ')))
    # global metal_cost
    meatal_price = 0
    length = info_list[3]
    width = info_list[4]
    number_of_pieces = int(input('Кол-во деталей (шт.) = '))
    metal_price = length * width * thickness * number_of_pieces * c * 350
    return metal_price


def cutting_cost(thickness: int, cutting_length: int) -> int:
    price_list = thicknesses[thickness]
    if cutting_length <= 100:
        cutting_price = price_list['cost_more']
    else:
        cutting_price = price_list['cost_less']
    cutting_money = cutting_length * cutting_price
    return cutting_money if cutting_money > 5000 else 5000


def insert_cost():
    global insert_money
    insert_money = int(input('Кол-во вставок шт = ')) * 10
    return insert_money


def bending_cost():
    bending_count = int(input('Кол-во гибов шт = '))
    if bending_count < 20:
        bending_price = 200
    else:
        bending_price = 100
    global bending_money
    bending_money = bending_count * bending_price
    return f'Стоимость гибки: {bending_money} рублей'


def cost_out():
    insert_cost()
    metal = metal_params()
    cutting = cutting_cost(thickness, cutting_length)
    bending = bending_cost()
    not_our_metal = cutting + insert_money + bending_money
    our_metal = metal_cost + not_our_metal
    print(
        f'{metal}\n'
        f'Стоимость реза: {cutting_cost(thickness, cutting_length)}руб.\n'
        f'Стоимость вставок: {insert_money} рублей\n'
        f'{bending}'
    )
    print(f'Если металл наш:{our_metal} \nЕсли метал НЕ наш: {not_our_metal}')


# cost_out()
# print(cutting_cost(20, 48))
# print(cutting_cost(12, 1450))
info_research()
metal_cost()