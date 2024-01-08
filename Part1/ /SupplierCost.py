class ExpenditureManager:
    def __init__(self, materials_manager):
        self.materials_manager = materials_manager
        self.supplier = {
            'milk': 0.3,
            'beans': 0.1,
            'spices': 0.05
        }

    def supplier_cost(self, current_materials):
        cost = 0
        storages = current_materials
        print(storages)
        for name, volume in storages.items():
            need_volume = volume['max_volume'] - volume['volume']
            cost += need_volume * self.supplier[name]
            volume['volume'] = volume['max_volume']
        return cost