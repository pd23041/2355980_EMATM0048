import Barista as Br
import Materials as Mat
import Cash
import InputJudgment as IJ
import SupplierCost as SC


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

    for month in range(1, months+1):
        print(f"====================================")
        print(f"======== SIMULATING MONTH {month} ========")
        print(f"====================================")

        # 月初资金
        cash_begin = cash.cash_begin()
        print(cash_begin)

        # 每个月最初的存量
        current_materials = materials_manager.show_storage()

        # 填充原料并计算成本
        materials_cost = expend_manager.supplier_cost(current_materials)

        if materials_cost > cash_begin:
            print('Not enough money, bankrupt.')
            break

        # 添加咖啡师 并判断是否有专长
        barista_number = IJ.get_poistives(input('>>> Enter number of barists: \n'))
        for i in range(int(barista_number)):
            name = input('Enter barista name.\n')
            name = barista_manager.is_exist(name)
            special = input('Does the barista have a special? (y/n):')
            if special == 'y':
                special_type = input('Enter the special coffee type: ')
                barista_manager.add_barista(name, month, is_special=True, special_type=special_type)
            else:
                barista_manager.add_barista(name, month, is_special=False, special_type=None)

        # 导出咖啡师的参数 并将参数导入到材料管理类中
        baristas = barista_manager.show_barista()

        # 计算每个月的劳动力  并将劳动力带入判断
        labour = barista_manager.get_barista_labour()

        # 更新demand需求
        for name, number in demand.items():
            materials_manager.update_demand(name, number)

        # 导入咖啡师参数 根据咖啡师判断制作时间是否减半
        materials_manager.materials_demand(labour, baristas)

        # 计算收支
        revenue = materials_manager.income()
        barista_cost = barista_manager.barista_cost()
        storages_cost = materials_manager.storage_cost()

        # 更新现金流
        cash_end = cash.cash_end(revenue, barista_cost, storages_cost, materials_cost)

        # 打印最终信息
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

        # 更新下一个月月初库存
        current_materials =materials_manager.update_storage()
