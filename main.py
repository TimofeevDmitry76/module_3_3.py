def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()                                 #  без аргументов
print_params(2.2, 'столбец', False)   #  с тремя аргументами
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = ['овал', 69, 6.7 ]
values_dict = {'a':69, 'b':'клетка', 'c':True}
print_params(**values_dict)
print_params(*values_list)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


