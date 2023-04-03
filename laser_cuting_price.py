# А если здесь соответствия между этими переменными? ->
# Есть. Словарь может отразить эти соответствия. ->
# Создаем словарь соответсвия толщины к вариантам стоимости.
# надо как-то текст помещать в поле, полное имя 'constant'
MN_0 = 0.000001
MN_1 = 0.0000078
MN_2 = 350
min_cut_length = 100
min_cut_price = 5000

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


def input_data_research():
    info_list = {
        'cutting_length': int(input('Длинна резки (м/п) = ')),
        'thickness': int(input('Толщина (мм) = ')),
        'length': int(input('Длинна (мм) = ')),
        'width': int(input('Ширина (мм) = ')),
        'amount_of_inserts': int(input('Кол-во вставок шт = ')),
        'number_of_pieces': int(input('Кол-во деталей (шт.) = ')),
        'bending_count': int(input('Кол-во гибов шт = '))
    }
    return info_list


# необходимость в этой функции по вопросом тоже


def insert_price(amount_of_inserts) -> int:
    magic_multiplyaer = 10
    return amount_of_inserts * magic_multiplyaer

# это зрябыло вынесено в функцию, т.к. это лишь произведение вводимых данных и
# выполняется оно один раз. Это произведение массы на цену 350 р./кг.


def metal_price(metal_V, number_of_pieces):
    return metal_V * number_of_pieces * MN_1 * MN_2


def cutting_price(
    thickness: int,
    cutting_length: int,
    min_cut_price: int,
    min_cut_length: int
) -> int:
    price_list = thicknesses[thickness]
    if cutting_length <= min_cut_length:
        cutting_price = price_list['cost_more']
    else:
        cutting_price = price_list['cost_less']
    cutting_money = cutting_length * cutting_price
    return cutting_money if cutting_money > min_cut_price else min_cut_price


def bending_price(bending_count: int):
    if bending_count < 20:
        bending_price = 200
    else:
        bending_price = 100
    bending_money = bending_count * bending_price
    return bending_money


def generate_customer_invoice(input_data):
    metal_V = (
        input_data['length'] * input_data['width'] * input_data['thickness']
    )
    metal_S = input_data['length'] * input_data['width']
    metal_square = metal_S * MN_0
    metal_mass = metal_V * input_data['number_of_pieces'] * MN_1
    metal_final_price = metal_mass * MN_2
    cuting_final_price = cutting_price(
        input_data['thickness'],
        input_data['cutting_length'],
        min_cut_price,
        min_cut_length
    )
    insert_final_price = insert_price(input_data['amount_of_inserts'])
    bending_final_price = bending_price(input_data['bending_count'])
    not_our_metal = (
        cuting_final_price + insert_final_price + bending_final_price
    )
    our_metal = metal_final_price + not_our_metal

    invoice = {
        'metal_space': metal_square,
        'metal_mass': metal_mass,
        'metal_final_price': metal_final_price,
        'cuting_final_price': cuting_final_price,
        'insert_final_price': insert_final_price,
        'bending_final_price': bending_final_price,
        'not_our_metal': not_our_metal,
        'our_metal': our_metal
    }
    # счёт фактуры
    return invoice


def invoice_visual(customer_invoice):
    print('X' * 10)
    print(f"Площадь металла: {customer_invoice['metal_space']}")
    print(f"Масса металла: {customer_invoice['metal_mass']}")
    print(f"Стоимость металла: {customer_invoice['metal_final_price']}")
    print(
        f"Стоимость лазерной резки: {customer_invoice['cuting_final_price']}")
    print(f"Стоимость вставок: {customer_invoice['insert_final_price']}")
    print(f"Стоимость гибки: {customer_invoice['bending_final_price']}")
    print(f"Если мтеалл наш: {customer_invoice['our_metal']}")
    print(f"Если мтеалл НЕ наш: {customer_invoice['not_our_metal']}")


def main():
    invoice_visual(generate_customer_invoice(input_data_research()))


main()
