import InputJudgment as IJ

class MaterialsManager:
    def __init__(self):
        # 定义咖啡种类 价格 时间 配料
        self.coffee_types = {
            'Espresso': {'time': 3, 'beans': 8, 'milk': 0, 'spices': 0, 'price': 1.5},
            'Americano': {'time': 2, 'beans': 6, 'milk': 0, 'spices': 0, 'price': 2.5},
            'Filter': {'time': 1, 'beans': 4, 'milk': 0, 'spices': 0, 'price': 1.5},
            'Macchiato': {'time': 4, 'beans': 8, 'milk': 0.1, 'spices': 2.0, 'price': 3.0},
            'Flat White': {'time': 5, 'beans': 8, 'milk': 0.2, 'spices': 1.0, 'price': 3.5},
            'Latte': {'time': 6, 'beans': 8, 'milk': 0.3, 'spices': 3.0, 'price': 4.0}
        }

        self.storages = {
            'milk': {'volume': 300, 'pantry': 0.1, 'depre': 0.4, 'max_volume': 300},
            'beans': {'volume': 20000, 'pantry': 0.001, 'depre': 0.1, 'max_volume': 20000},
            'spices': {'volume': 4000, 'pantry': 0.001, 'depre': 0, 'max_volume': 4000},
        }
        # 计算需求
        self.demand = {name: 0 for name in self.coffee_types}

        self.pantry = {
            'milk': 0,
            'beans': 0,
            'spices': 0
        }

    # 计算在劳动力内能卖多少咖啡 以及所需要的原料
    def update_demand(self, coffee_name, amount):
        if coffee_name in self.coffee_types:
            self.demand[coffee_name] = amount
        else:
            print(f'{coffee_name} is a invalid input, re-enter the coffee name')

    # 判断材料需求  劳动力是否足够
    def materials_demand(self, labour, baristas):
        beans_need = 0
        milk_need = 0
        spices_need = 0
        rate = 1
        for name, amount in self.demand.items():
            coffee = self.coffee_types[name]
            # 检查劳动力不足 且原料不足的情况
            amount = IJ.change_demand_poistives(amount, input(f'{name}, demand {amount}, how much to sell: '))

            # 遍历咖啡师 判断是否有该咖啡的专业咖啡师 若有则时间减半 无则维持不变
            for _, detail in baristas.items():
                if name == detail['special_type']:  # 这里有个问题，如果
                    rate = 0.5
                    break
                else:
                    rate = 1.0

            # 打印参数 以便判断
            # print(baristas)
            # print(rate)

            if labour < coffee['time'] * amount * rate:
                capacity = labour // coffee['time']
                print(f'Insufficient labour: quantity requested {amount}, capacity {capacity}')
                amount = IJ.change_demand_poistives(capacity, input(f'{name}, demand {amount}, how much to sell: '))
                # self.demand[name] = amount

            # 满足劳动力的同时  计算每种咖啡所需要的原料 判断原料是否充足
            milk_needed = coffee.get('milk', 0) * amount
            beans_needed = coffee.get('beans', 0) * amount
            spices_needed = coffee.get('spices', 0) * amount
            if self.storages['beans']['volume'] < beans_needed or \
                    self.storages['milk']['volume'] < milk_needed or \
                    self.storages['spices']['volume'] < spices_needed:
                print(f"Insufficient ingredients:")
                print(f" milk need {coffee['milk'] * amount} pantry {self.storages['milk']['volume']}")
                print(f" beans need {coffee['beans'] * amount} pantry {self.storages['beans']['volume']}")
                print(f" spices need {coffee['spices'] * amount} pantry {self.storages['spices']['volume']}")
                milks_loss = self.storages['milk']['volume'] // coffee['milk']
                beans_loss = self.storages['beans']['volume'] // coffee['beans']
                spices_loss = self.storages['spices']['volume'] // coffee['spices']
                amount = IJ.change_demand_poistives(min(milks_loss,beans_loss,spices_loss), input(f'{name}, demand {amount}, how much to sell: '))
                milk_needed = coffee.get('milk', 0) * amount
                beans_needed = coffee.get('beans', 0) * amount
                spices_needed = coffee.get('spices', 0) * amount

            # 更新demand
            self.update_demand(name, amount)

            # 实时更新库存
            self.storages['milk']['volume'] -= milk_needed
            self.storages['beans']['volume'] -= beans_needed
            self.storages['spices']['volume'] -= spices_needed

            # 更新劳动力
            labour -= coffee['time'] * amount * rate

            # 更新总需求
            beans_need += beans_needed
            milk_need += milk_needed
            spices_need += spices_needed

        return milk_need, beans_need, spices_need

    # 打印月尾时的库存存量
    def show_storage(self):
        return self.storages

    # 计算仓储支出
    def storage_cost(self):
        cost = 0
        for name in self.pantry:
            cost += self.storages[name]['volume'] * self.storages[name]['pantry']
        return cost

    # 计算所有咖啡销售的总收入
    def income(self):
        revenue = 0
        for name, amount in self.demand.items():
            revenue += self.coffee_types[name]['price'] * amount
        return revenue

    # 每个月月初根据折损率更新库存 根据此数据跟供应商进货
    def update_storage(self):
        for name, depre in self.storages.items():
            if depre['volume'] >= 0:
                upload_volume = depre['volume'] * (1 - depre['depre'])
                depre['volume'] = upload_volume
        return self.storages