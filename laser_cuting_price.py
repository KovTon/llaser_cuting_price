# А если здесь соответствия между этими переменными? ->
# Есть. Словарь может отразить эти соответствия. ->
# Создаем словарь соответсвия толщины к вариантам стоимости.
С = 0.0000078  # надо как-то текст помещать в поле, полное имя 'constant'
C2 = 350
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
        'cutting length': int(input('Длинна резки (м/п) = ')),
                 'amount_of_inserts': int(input('Кол-во вставок шт = ')),
                 'thickness': int(input('Толщина (мм) = ')),
                 'length': int(input('Длинна (мм) = ')),
                 'width': int(input('Ширина (мм) = ')),
                 'number_of_pieces': int(input('Кол-во деталей (шт.) = ')),
                 'bending_count': int(input('Кол-во гибов шт = '))
    }
    return info_list


#     info_list.append(f'Площадь металла:{(info_list[length] * info_list[width] *0.000001) * info_list[number_of_pieces]} (м^2)')
#     info_list.append(f'Масса маталла:{info_list[3] * info_list[4] * info_list[4] * info_list[5] * С}(кг)')
#     info_list.append(f'Стоимость металла: {metal_cost} (руб)')
#     return info_list


def insert_price_calculate(amount_of_inserts):
    magic_multiplyaer = 10
    return amount_of_inserts * magic_multiplyaer


def metal_price_calculate(length, width, thickness, number_of_pieces):
    return length * width * thickness * number_of_pieces * С * C2


def cutting_cost(
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


def bending_cost(bending_count: int):
    if bending_count < 20:
        bending_price = 200
    else:
        bending_price = 100
    bending_money = bending_count * bending_price
    return bending_money


def counting_cost_out():
    insert_price_calculate(amount_of_inserts)
    metal = metal_params()
    cutting = cutting_cost(thickness, cutting_length)
    bendin = bending_cost()
    not_our_metal = cutting + insert_money + bending_money
    our_metal = metal_cost + not_our_metal
  
# def final_report():
# print(
#         f'{metal}\n'
#         f'Стоимость реза: {cutting_cost(thickness, cutting_length)}руб.\n'
#         f'Стоимость вставок: {insert_money} рублей\n'
#         f'Стоимость гибки: {bending_money} рублей''
#     )
#     print(f'Если металл наш:{our_metal} \nЕсли метал НЕ наш:{not_our_metal}')


def main():
    spisok = input_data_research()
    print(spisok)
    print(spisok)


main()
