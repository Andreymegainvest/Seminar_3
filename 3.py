# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# lst = []
# sum = 0
# for i in my_list:
#     lst = my_list[1::2]
# print(lst)
# for i in lst:
#     sum += i
# # print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 5, 6]
# lst = []
# for i in my_list:
    #   lst = [my_list[0] * my_list[3], my_list[1] * my_list[2]]
# print(lst)    
 
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in lst:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#             max = i - int(i)
# result = max - min
# print(float(round(result, 3)))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите десятичное число: '))
# numberb = " "
# while number > 0:
#     numberb = str(number % 2) + numberb
#     number = number // 2
# print(str(numberb))    


