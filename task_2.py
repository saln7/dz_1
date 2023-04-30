#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

gur_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(gur_list)

get_dia_min = int(input("Введите минимум диапозона: "))
get_dia_max = int(input("Введите максимум диапозона: "))
result_list = list()

for i in range(len(gur_list)):
    
    if gur_list[i] >= get_dia_min and gur_list[i] <= get_dia_max:
        result_list.append(i)
        

print(result_list)