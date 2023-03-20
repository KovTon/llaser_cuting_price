
# def insert_meatla_info():
#     cutting_length = int(input('Длинна резки (м/п) = '))
#     thickness = int(input('Толщина (мм) = '))
#     length = int(input('Длинна (мм) = '))
#     width = int(input('Ширина (мм) = '))
#     number_of_pieces = int(input('Кол-во деталей (шт.) = '))
#     insert_money = int(input('Кол-во вставок шт = ')) * 10
#     bending_count = int(input('Кол-во гибов шт = '))

#     metal_cost = length * width * thickness * number_of_pieces * 0.0000078 * 350

# info = {'толщина': "0"}
# print(info)
# info['толщина'] = "uheif"
# print(info)
# print(info.values())
# print(info.items())
# print(info.keys())

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")


# Попытка составить словарь из КЛЮЧА- фразы и
# ЗНАЧЕНИЯ- введенное число, параметр

# info = {'толщина': 0}
# thikness = input(f'Длинна резки(м/п)={info["толщина"]}')
# print(info)
