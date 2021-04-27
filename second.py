"""Задание 2
Написать программу на языке python версии 3, отсеивающую автомобильные
номера неправильного формата, т.е. проверка ГРЗ типа 1А из проверочного списка.
Пример списка: ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"].
Для данного примера правильным ответом будет  ["A123AA11", "А222АА123"].
"""

import re

# Список номеров
vehicle_sign_list = ['А123АА11', 'А222АА123', 'р923См16', 'Е100Ее02',
                     '', 'А', 'a12%!df12',
                     'A12AA123', 'A123CC1234', 'AA123A12',
                     'В703АЯ59', 'К404ВЕ112', 'Н217ОР160']
# Первые четыре варианта - верные (регистр не учитывается)
# Не подходят потому что: присутствует недопустимая буква (разрешенные: АВЕКМНОРСТУХ),
# последние два - потому что такого кода региона не существует

# Список уникальных кодов регионов, используемых в знаках
valid_region_codes = [102, 113, 116, 121, 122, 123, 124,
                      125, 126, 134, 136, 138, 142, 147,
                      150, 152, 154, 156, 159, 161, 164,
                      173, 174, 177, 178, 186, 190, 193,
                      196, 197, 198, 199, 702, 716, 750,
                      761, 763, 774, 777, 790, 797, 799]


# Первый вариант решения
def first_solution() -> None:
    for sign in vehicle_sign_list:
        # Попадает ли очередной знак под шаблон:
        is_match = re.match(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', sign.upper())

        region_code = re.search(r'\d{2,}$', sign)

        if is_match and region_code is not None:
            region_code = region_code.group()

            # Отбрасываем лишний ноль, имеющийся у регионов со значением < 10
            # чтобы иметь возможность сделать cast to int
            if region_code[0] == '0':
                region_code = region_code[1:]

            region_code = int(region_code)
            if region_code in valid_region_codes or 1 <= region_code <= 99:
                valid.append(sign)


# Второй вариант решения
def is_digit(possible_num: str) -> bool:
    if re.match(r'\d', possible_num):
        return True
    return False


def is_right_char(possible_char: str) -> bool:
    if re.match(r'[АВЕКМНОРСТУХ]', possible_char.upper()):
        return True
    return False


def second_solution() -> None:
    for sign in vehicle_sign_list:
        i = 0
        sign_is_valid = True

        # Отбрасываем сразу, если маленькая длина строки
        if len(sign) < 8:
            sign_is_valid = False
        else:
            # Проверям каждый символ строки на корректность
            for char in sign:
                i += 1
                if (2 <= i <= 4 or 7 <= i <= 9) and not is_digit(char):
                    sign_is_valid = False
                    break
                elif (i == 1 or 5 <= i <= 6) and not is_right_char(char):
                    sign_is_valid = False
                    break
            # Проверяем код региона
            region_code = re.search(r'\d{2,}$', sign).group()
            if region_code[0] == '0':
                region_code = region_code[1:]
            region_code = int(region_code)
            if region_code not in valid_region_codes and not (1 <= region_code <= 99):
                sign_is_valid = False
        if sign_is_valid:
            valid.append(sign)


if __name__ == '__main__':
    valid = []

    first_solution()
    # second_solution()

    print('Valid:', valid)
