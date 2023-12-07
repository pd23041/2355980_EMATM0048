
# 精简代码块
class MaterialsDemand:
    def __init__(self):
        self.milk = 0
        self.beans = 0
        self.spices = 0
        self.pantry = 0
        self.labour = 0
        self.temp = 0

    def materials_demand(self, name, coffee_demand, labour):
        # 定义咖啡类型及其对应的需求
        coffee_types = {
            'Espresso': {'labour_per_cup': 3, 'beans_per_cup': 8},
            'Americano': {'labour_per_cup': 2, 'beans_per_cup': 6},
            # ... 其他咖啡类型及其需求 ...
        }

        if name in coffee_types:
            demand_info = coffee_types[name]
            self.temp += demand_info['labour_per_cup'] * coffee_demand[name]
            if self.temp > labour:
                max_demand = (labour - self.labour) // demand_info['labour_per_cup']
                print('Insufficient labour: quantity requested %d, capacity %d' % (coffee_demand[name], max_demand))
                coffee_demand[name] = change_demand_poistives(max_demand, input('please change how much to sell\n'))
            self.labour += demand_info['labour_per_cup'] * int(coffee_demand[name])
            self.beans += demand_info['beans_per_cup'] * coffee_demand[name]
            # ... 根据需要更新其他原料 ...
        else:
            print("Invalid coffee name.")

# 示例使用
demand = MaterialsDemand()
coffee_demand = {'Espresso': 10}  # 假设 Espresso 的需求量是 10
demand.materials_demand('Espresso', coffee_demand, 15)  # 示例输入
