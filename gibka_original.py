t_list = [ 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 20]

price_list_100 = [27, 36, 57, 64, 76, 87, 111, 154, 191, 224, 360, 519]

price_list_101 = [20, 28, 43, 50, 58, 68, 84, 125, 144, 186, 298, 432]


def metal_params():
    global metal_cost
    length = int(input('Длинна мм = '))
    width = int(input('Ширина мм = '))
    global t
    t = int(input('Толщина мм = '))
    number_of_pieces = int(input('Кол-во деталей шт = '))
    global metal_cost
    metal_cost = length * width * t * number_of_pieces * 0.0000078 * 350
    return f'Площадь металла: {(length* width *0.000001)*number_of_pieces} м^2 \nМасса маталла:{length * width * t * number_of_pieces * 0.0000078} кг \nСтоимость металла:{metal_cost} рублей'


def cutting_cost():
    cutting_length = int(input('Длинна резки м/п = '))
    for i in range(len(t_list)):
        if t == t_list[i] and cutting_length <= 100:
            cutting_price = price_list_100[i]
        elif t == t_list[i] and cutting_length > 100:
            cutting_price = price_list_101[i]
    global cutting_money
    # работает даже с ошибкой '"cutting_price" is possibly unboundPylance'
    cutting_money = cutting_length * cutting_price 
    if cutting_money < 5000:
        cutting_money = 5000
    return f'Стоимость лазерной резки: {cutting_money} рублей'


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
    cutting = cutting_cost()
    insert = insert_cost()
    bending = bending_cost()
    print(f'{metal}\n{cutting}\n{insert}\n{bending}')
    print(f'Если металл наш:{metal_cost + cutting_money + insert_money + bending_money} \nЕсли метал НЕ наш: {cutting_money + insert_money + bending_money}')


while True:
    cost_out()