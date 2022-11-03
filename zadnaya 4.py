i_numb = int(input("Введите число:"))
i_numb0 = 0

while i_numb > 0:
    digit = i_numb % 10
    i_numb = i_numb // 10
    i_numb0 = i_numb0 * 10
    i_numb0 = i_numb0 + digit

print('Обратное число:', i_numb0)