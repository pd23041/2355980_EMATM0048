import Barista as Br
import Materials as Mat
import Cash
import InputJudgment as IJ
import SupplierCost as SC


# Simulation of a six-month run of a coffee shop
def simulate_shop(months):
    # cash = 10000
    demand = {
            'Espresso': 500,
            'Americano': 200,
            'Filter': 300,
            'Macchiato': 400,
            'Flat White': 600,
            'Latte': 1000
        }
    barista_manager = Br.BaristaManager()
    materials_manager = Mat.MaterialsManager()
    expend_manager = SC.ExpenditureManager(materials_manager)
    cash = Cash.Cash()

    # Simulation of a six-month run of a coffee shop
    for month in range(1, months+1):
        print(f"====================================")
        print(f"======== SIMULATING MONTH {month} ========")
        print(f"====================================")

        # Funds at the beginning of the month
        cash_begin = cash.cash_begin()
        print(cash_begin)

        # Inventory at the beginning of each month
        current_materials = materials_manager.show_storage()

        # Fill the raw materials and calculate the cost
        materials_cost = expend_manager.supplier_cost(current_materials)

        # Determining the adequacy of funds
        if materials_cost > cash_begin:
            print('Not enough money, bankrupt.')
            break

        # Add a barista and determine if you have a specialty
        barista_number = IJ.get_poistives(input('>>> Enter the number of recruitment baristas: \n'))
        for i in range(int(barista_number)):
            barista_manager.hire_barista(month)

        # terminate the baristas and how many to terminate.
        fire_barista_option = input('Do you want to fire a barista? (y/n): ')
        if fire_barista_option.lower() == 'y':
            number = IJ.get_poistives(input('>>> Enter number of barists: \n'))
            for i in range(number):
                barista_manager.fire_barista()

        # Exporting barista parameters and importing them into the material management class
        baristas = barista_manager.show_barista()

        # Calculate the labor force for each month and bring the labor force into the judgment
        labour = barista_manager.get_barista_labour()

        # Updating Demand
        for name, number in demand.items():
            materials_manager.update_demand(name, number)

        # Import barista parameters Judge whether to halve the production time based on the barista
        materials_manager.materials_demand(labour, baristas)

        # Calculation of income and expenditure
        revenue = materials_manager.income()
        barista_cost = barista_manager.barista_cost()
        storages_cost = materials_manager.storage_cost()

        # Renewal of cash
        cash_end = cash.cash_end(revenue, barista_cost, storages_cost, materials_cost)

        # Print store business information
        print(f"=== FINAL STATE month {month} ===")
        print(f"Shop Name: Boost, Cash: {cash_end:.2f}")
        print("     Pantry")
        for material, info in current_materials.items():
            print(f"        {material}, {info['volume']:.2f} (capacity={info['max_volume']})")
        print("     Baristas")
        barista_names= barista_manager.show_barista()
        print(barista_names)
        for name in barista_names:
            print(f"        Barista {name}, hourly rate=15\n")

        # Updated inventory for the beginning of the next month
        current_materials =materials_manager.update_storage()
        return current_materials
