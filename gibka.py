# А если здесь соответствия между этими переменными? ->
# Есть. Словарь может отразить эти соответствия. ->
# Создаем словарь соответсвия толщины к вариантам стоимости.
t_list = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 20]
price_list_100 = [27, 36, 57, 64, 76, 87, 111, 154, 191, 224, 360, 519]
price_list_101 = [20, 28, 43, 50, 58, 68, 84,  125, 144, 186, 298, 432]


thickneses = {
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


def metal_params():
    global cutting_length
    cutting_length = int(input('Длинна резки м/п = '))
    global metal_cost
    length = int(input('Длинна мм = '))
    width = int(input('Ширина мм = '))
    global t
    t = int(input('Толщина мм = '))
    number_of_pieces = int(input('Кол-во деталей шт = '))
    global metal_cost
    metal_cost = length * width * t * number_of_pieces * 0.0000078 * 350
    return (
     f'Площадь металла:{(length* width *0.000001)*number_of_pieces} м^2\n'
     f'Масса маталла:{length * width * t * number_of_pieces * 0.0000078}кг\n'
     f'Стоимость металла: {metal_cost} рублей'
    )


def cutting_cost(t: int, cutting_length: int) -> int:
    price_list = thickneses[t]
    if cutting_length <= 100:
        cutting_price = price_list['cost_more']
    else:
        cutting_price = price_list['cost_less']

    cutting_money = cutting_length * cutting_price
    if cutting_money < 5000:
        cutting_money = 5000
    return cutting_money  # а можно в одну строку вывести return из 51-53 стр.


def insert_cost():
    global insert_money
    insert_money = int(input('Кол-во вставок шт = ')) * 10
    return f'Стоимость вставок: {insert_money} рублей'


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
    metal = metal_params()
    cutting = cutting_cost(t, cutting_length)
    insert = insert_cost()
    bending = bending_cost()
    our_metal = metal_cost + cutting + insert_money + bending_money
    not_our_metal = cutting + insert_money + bending_money
    print(f'{metal}\n{cutting}\n{insert}\n{bending}')
    print(f'Если металл наш:{our_metal} \nЕсли метал НЕ наш: {not_our_metal}')


cost_out()
