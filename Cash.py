class Cash:
    def __init__(self):
        self.cash = 10000
        self.rent = 1500

    def cash_begin(self):
        return self.cash

    def cash_end(self, revenue, barista_cost, storages_cost, materials_cost):
        self.cash = self.cash + revenue - barista_cost - storages_cost - self.rent - materials_cost
        return self.cash

