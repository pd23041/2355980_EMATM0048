class BaristaManager:
    def __init__(self):
        self.barista = {}
        self.hourly_rate = 15

    def is_exist(self, name):
        if self.barista and name in self.barista:  # 判断是否已经存在
            print('barista already exists')
            name = self.is_exist(input('Type again\n'))  # 若输入错误，提示重新输入。
            return name
        else:
            return name

    # 招聘咖啡师 更新专业咖啡师
    def add_barista(self, name, month, is_special=False, special_type=None):
        if len(self.barista) >= 4: # 咖啡师人数必须[1,4]
            print('At full capacity')
        # elif self.barista and name in self.barista: # 判断是否已经存在
        #     print('barista already exists')
        #     self.barista[name] = self.add_barista(input('Type again\n'), month) # 若输入错误，提示重新输入。
        else:
            self.barista[name] = {'hourly rate': self.hourly_rate, 'is_special': is_special, 'special_type': special_type}
            print(f'Added {name}, hourly rate=15 in month {month}')  # 这里的month要for

    # 解聘咖啡师
    #   实现功能：判断是否存在咖啡师
    #           判断输入是否正确
    #           计算咖啡师人数
    def remove_barista(self, name):
        if len(self.barista) <= 1:
            print('There are not enough baristas to reduce them.')  # 判断是否不存在 不存在则不能remove
        elif name not in self.barista:
            print('Baristas do not exist, please re-enter\n')  # 判断输入是否正确
            self.remove_barista(input())
        else:
            del self.barista[name]
            print(f'barista {name} is been removed')

    def hire_barista(self,month):
        name = input('Enter barista name:\n')
        name = self.is_exist(name)
        special = input('Does the barista have a special? (y/n):')
        if special == 'y':
            special_type = input('Enter the special coffee type: ')
            self.add_barista(name, month, is_special=True, special_type=special_type)
        else:
            self.add_barista(name, month, is_special=False, special_type=None)

    def fire_barista(self):
        name = input('Enter the name of the barista to be fired:\n')
        self.remove_barista(name)

    # 计算劳动力
    def get_barista_labour(self):
        return 80 * 60 * len(self.barista)

    # 咖啡师花费
    def barista_cost(self):
        return 15 * 120 * len(self.barista)

    # 展示咖啡师 以及 人数
    def show_barista(self):
        return self.barista