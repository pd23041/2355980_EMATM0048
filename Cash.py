class Cash:
    def __init__(self):
        self.cash = 10000
        self.rent = 1500

    # Return of initial funds for each month
    def cash_begin(self):
        return self.cash

    # Return of funds at the end of each month
    def cash_end(self, revenue, barista_cost, storages_cost, materials_cost):
        self.cash = self.cash + revenue - barista_cost - storages_cost - self.rent - materials_cost
        return self.cash

