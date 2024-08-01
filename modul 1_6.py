my_dict = {'Kate': 1990, 'Andrew': 1987, 'Sofia': 2014, 'Seva': 2015}
print(my_dict)
print(my_dict['Kate'])
print(my_dict.get('Lena'))
my_dict.update({'Sasha': 1966,
                'Kolya': 1993})
a = my_dict.pop('Andrew')
print(a)
print(my_dict)

my_set = {2, 4, 'хлеб', 2, 23.34, 'хлеб', 4, 23.34}
print(my_set)
my_set.update([5,8,])
my_set.discard(23.34)
print(my_set)