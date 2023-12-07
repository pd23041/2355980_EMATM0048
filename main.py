# 实现咖啡师数量统计 展示咖啡师姓名
class BaristaManager:

    def __init__(self):
        self.barista_number = 0
        self.barista = []
        self.hourly_rate = 15
        self.labour = 0

    # 招聘咖啡师
    def add_barista(self, name):
        if len(self.barista) >= 4: # 咖啡师人数必须[1,4]
            print('At full capacity')
        elif self.barista and name in self.barista[0]: # 判断是否已经存在
            print('barista already exists')
            self.barista.append(self.add_barista(input('Type again\n'))) # 若输入错误，提示重新输入。
        else:
            self.barista.append(name)
            print('Added %s, hourly rate=15 in month 1' %(name))  # 这里的month要for
            self.barista_number += 1

    # 解聘咖啡师
    #   实现功能：判断是否存在咖啡师
    #           判断输入是否正确
    #           计算咖啡师人数
    def remove_barista(self, name):
        if self.barista_number < 1:
            print('Shortage of baristas, please recruit baristas in time.') # 判断是否不存在 不存在则不能remove
        elif name not in self.barista:
            print('Baristas do not exist, please re-enter') # 判断输入是否正确
            self.remove_barista(input())
        else:
            self.barista.remove(name)
            print('barista %s is been remove' %(name))
            self.barista_number -= 1
    def get_barista_labour(self):
        self.labour= 80 * 60 * self.barista_number
        return self.labour

    # 展示咖啡师 以及 人数
    def show_barista(self):
        return self.barista, self.barista_number

#
class MaterialsDemand:
    def __init__(self):
        self.milk = 0
        self.beens = 0
        self.spices = 0
        self.pantry = 0
        self.labour = 0
        self.temp = 0

    def materials_demand(self, name, labour):
        if name == 'Expresso':
            self.temp = self.temp + 3 * coffee_demand[name] # 中间变量 判断是否超过劳动力
            if self.temp > labour: # 劳动力不足
                time = (labour - self.labour) / 3 # 计算剩余劳动力
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n')) # 重新规划卖多少
                change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 3 * int(coffee_demand[name])
            self.beens = self.beens + 8 * coffee_demand[name]# 计算原料

        if name == 'Americano':
            self.temp = self.temp + 2 * coffee_demand[name]
            if self.temp > labour:
                time = (labour - self.labour) / 2
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n')) # 重新规划卖多少
                change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 2 * int(coffee_demand[name])
            self.beens = self.beens + 6 * coffee_demand[name]

        if name == 'Filter':
            self.temp = self.temp + 1 * coffee_demand[name]
            if self.temp > labour:
                time = (labour - self.labour)
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n')) # 重新规划卖多少
                change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 1 * int(coffee_demand[name])
            self.beens = self.beens + 4 * coffee_demand[name]

        if name == 'Macchiatto':
            self.temp = self.temp + 4 * coffee_demand[name]
            if self.temp > labour:
                time = (labour - self.labour) / 4
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n')) # 重新规划卖多少
                change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 4 * int(coffee_demand[name])
            self.milk = self.milk + 0.1 * coffee_demand[name] # 原料计算
            self.beens = self.beens + 8 * coffee_demand[name]
            self.spices = self.spices + 2 * coffee_demand[name]

        if name == 'Flat White':
            self.temp = self.temp + 5 * coffee_demand[name]
            if self.temp > labour:
                time = (labour - self.labour) / 5
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n'))
                change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 5 * int(coffee_demand[name])
            self.milk = self.milk + 0.2 * coffee_demand[name]
            self.beens = self.beens + 8 * coffee_demand[name]
            self.spices = self.spices + 1 * coffee_demand[name]

        if name == 'Latte':
            self.temp = self.temp + 6 * coffee_demand[name]
            if self.temp > labour:
                time = (labour - self.labour) / 6
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], time))
                coffee_demand[name] = change_demand_poistives(time, input('please change how much to sell\n')) # 重新规划卖多少
                # change_demand_poistives(time, coffee_demand[name])
            self.labour = self.labour + 6 * int(coffee_demand[name])
            self.milk = self.milk + 0.3 * coffee_demand[name]
            self.beens = self.beens + 8 * coffee_demand[name]
            self.spices = self.spices + 3 * coffee_demand[name]
        return self.milk, self.beens, self.spices

    # def calculate_labour(self, temp, labour, coffee_time):
    #     temp = temp + coffee_time * demand
    #     if temp > labour:
    #         time = (labour - labour) / coffee_time
    #         print('Insufficient labour: quantity requested %d, capacity %d' % (demand, time))
    #     labour = labour + 6 * demand
    #     return temp, labour






# 计算材料库存 所需材料
# class MaterialsManager:
#     def __init__(self):
#         self.milk = 0
#         self.beens = 0
#         self.Spices = 0
#
#     def need_coffee(self, ):
#
#     def add_materials(self, milk_liter, beens_g, Spices_g):
#         self.milk += milk_liter
#         self.beens += beens_g
#         self.spices += Spices_g
# 判断输入是否有效 必须为正整数


def get_poistives(number):
    while True:
        try:
            number = int(number)
            if 0<= number <= 4:
                return number
            else:
                print('Please enter an integer value')
                return get_poistives(input())

        except (TypeError, ValueError):
            print('Please enter an integer value')
            return get_poistives(input())

def change_demand_poistives(number, change_demand):
    while True:
        try:
            change_demand = int(change_demand)
            if 0<= change_demand <= number:
                return change_demand
            else:
                print('Please enter an integer value')
                return get_poistives(input())

        except (TypeError, ValueError):
            print('Please enter an integer value')
            return get_poistives(input())


coffee = BaristaManager()
barista_number = get_poistives(input('Enter number of barists\n'))
for i in range(int(barista_number)):
    name = input('Enter barista name.\n')
    coffee.add_barista(name)
labour = coffee.get_barista_labour()
# coffee.remove_barista(input())


material = MaterialsDemand()
coffee_demand = {
    'Expresso': 500,
    'Americano': 200,
    'Filter': 300,
    'Macchiatto': 400,
    'Flat White': 600,
    'Latte': 1000
}

coffee_time = {
    'Expresso': 2,
    'Americano': 3,
    'Filter': 1,
    'Macchiatto': 4,
    'Flat White': 5,
    'Latte': 6
}

for name, _ in coffee_demand.items():
    ingredients = material.materials_demand(name, labour)
print(ingredients)
print(coffee.show_barista())
print(coffee_demand)



