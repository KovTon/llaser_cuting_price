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

def insert_meatla_info():
    cutting_length = int(input('Длинна резки (м/п) = '))
    thickness = int(input('Толщина (мм) = '))
    length = int(input('Длинна (мм) = '))
    width = int(input('Ширина (мм) = '))
    number_of_pieces = int(input('Кол-во деталей (шт.) = '))
    insert_money = int(input('Кол-во вставок шт = ')) * 10
    bending_count = int(input('Кол-во гибов шт = '))

    metal_cost = length * width * thickness * number_of_pieces * 0.0000078 * 350

    # стоимость резки
    not_our_metal = cutting + insert_money + bending_money

    # стоимость резки + стоимость металла с нашей базы
    our_metal = metal_cost + not_our_metal

