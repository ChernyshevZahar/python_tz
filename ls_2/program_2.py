numbers = [255, 16, 0, -42]

hex_digits = '0123456789ABCDEF'
for number in numbers:
# Если число равно 0, то возвращаем '0'
    if number == 0:
        hex_string = '0'
    else:
    # Обрабатываем отрицательные числа
        is_negative = number < 0
        if is_negative:
            number = -number
        # Преобразование числа в шестнадцатеричное представление
        hex_string = ''
        while number > 0:
            remainder = number % 16
            hex_string = hex_digits[remainder] + hex_string
            number //= 16
        # Добавляем префикс '-' для отрицательных чисел
        if is_negative:
            hex_string = '-' + hex_string
        print(hex_string)
