import InputJudgment as IJ

class MaterialsManager:
    def __init__(self):
        # Define Coffee Type Price Time Ingredients
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

    # Calculate how much coffee can be sold within the labor force and what ingredients are needed
    def update_demand(self, coffee_name, amount):
        if coffee_name in self.coffee_types:
            self.demand[coffee_name] = amount
        else:
            print(f'{coffee_name} is a invalid input, re-enter the coffee name')

    # Determine material requirements Labor adequacy
    def materials_demand(self, labour, baristas):
        beans_need = 0
        milk_need = 0
        spices_need = 0
        rate = 1
        for name, amount in self.demand.items():
            coffee = self.coffee_types[name]
            # Checking labor shortages and raw material shortages
            amount = IJ.change_demand_poistives(amount, input(f'{name}, demand {amount}, how much to sell: '))

            # Iterate over baristas Determine if there is a specialty barista for this coffee
            for _, detail in baristas.items():
                if name == detail['special_type']:
                    rate = 0.5
                    break
                else:
                    rate = 1.0

            # Print parameters for judgment
            # print(baristas)
            # print(rate)

            if labour < coffee['time'] * amount * rate:
                capacity = labour // coffee['time']
                print(f'Insufficient labour: quantity requested {amount}, capacity {capacity}')
                amount = IJ.change_demand_poistives(capacity, input(f'{name}, demand {amount}, how much to sell: '))
                # self.demand[name] = amount

            # Determining the adequacy of raw materials
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

            # Update Demand
            self.update_demand(name, amount)

            # 实时更新库存
            self.storages['milk']['volume'] -= milk_needed
            self.storages['beans']['volume'] -= beans_needed
            self.storages['spices']['volume'] -= spices_needed

            # Updating the labor force
            labour -= coffee['time'] * amount * rate

            # Renewal of total material requirements
            beans_need += beans_needed
            milk_need += milk_needed
            spices_need += spices_needed

        return milk_need, beans_need, spices_need

    # Print the inventory stock at the end of the month
    def show_storage(self):
        return self.storages

    # Calculation of warehousing expenditures
    def storage_cost(self):
        cost = 0
        for name in self.pantry:
            cost += self.storages[name]['volume'] * self.storages[name]['pantry']
        return cost

    # Calculate total revenue from all coffee sales
    def income(self):
        revenue = 0
        for name, amount in self.demand.items():
            revenue += self.coffee_types[name]['price'] * amount
        return revenue

    # Update inventory based on discount rate
    def update_storage(self):
        for name, depre in self.storages.items():
            if depre['volume'] >= 0:
                upload_volume = depre['volume'] * (1 - depre['depre'])
                depre['volume'] = upload_volume
        return self.storages