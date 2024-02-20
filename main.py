import inspect
import telebot


class Test:
    def __init__(self, num_l, num_t):
        self.num_l = num_l
        self.num_t = num_t

    def func(self):
        if len(self.num_l) == len(self.num_t):
            for i in range(len(self.num_l)):
                yield self.num_l[i] * self.num_t[i]


def introspection_info(obj):
    # help(obj)
    #
    # print(type(obj))
    #
    # print(f'Тип объекта:{type(obj)} атрибут:', hasattr(obj, 'num_l'))
    # if hasattr(obj, 'num_l'):
    #     print('сам атрибут', getattr(obj, 'num_l'))
    # # или
    # atr = 'num_l'
    # print(getattr(obj, atr, f"атрибута '{atr}' нет"))

    # print(dir(obj))

    # print(callable(obj))
    # print(isinstance(obj, list))
    print(inspect.getmodule(obj))
    print(f'Тип объекта:{type(obj)},\n'
          f'Атрибуты объекта: {dir(obj)}\n'
          f'Методы объекта: {dir(obj)}\n'
          f' ')
    pass


my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
test = Test(my_list, my_tuple)
result = test.func()

# for j in result:
#     print(j)

introspection_info(telebot)
introspection_info(my_list)
introspection_info(my_tuple)
introspection_info(test)
introspection_info(result)
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}