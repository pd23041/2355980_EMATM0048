# Barista management system
# Barista add subtract function
# Labor force calculation
# Employee payroll calculation


class BaristaManager:
    def __init__(self):
        self.barista = {}
        self.hourly_rate = 15

    def is_exist(self, name):
        if self.barista and name in self.barista:  # Determine if it already exists
            print('barista already exists')
            name = self.is_exist(input('Type again\n'))  # If the entry is incorrect, prompt to re-enter.
            return name
        else:
            return name

    # Updated Specialty Barista
    def add_barista(self, name, month, is_special=False, special_type=None):
        if len(self.barista) >= 4: # 咖啡师人数必须[1,4]
            print('At full capacity')
        # elif self.barista and name in self.barista: # 判断是否已经存在
        #     print('barista already exists')
        #     self.barista[name] = self.add_barista(input('Type again\n'), month) # 若输入错误，提示重新输入。
        else:
            self.barista[name] = {'hourly rate': self.hourly_rate, 'is_special': is_special, 'special_type': special_type}
            print(f'Added {name}, hourly rate=15 in month {month}')  # 这里的month要for

    # Function: determine whether there is a coffee Judge whether the input is correct Calculate the number of baristas
    def remove_barista(self, name):
        if len(self.barista) <= 1:
            print('There are not enough baristas to reduce them.')  # 判断是否不存在 不存在则不能remove
        elif name not in self.barista:
            print('Baristas do not exist, please re-enter\n')  # 判断输入是否正确
            self.remove_barista(input())
        else:
            del self.barista[name]
            print(f'barista {name} is been removed')

    # Recruitment of barista
    def hire_barista(self,month):
        name = input('Enter barista name:\n')
        name = self.is_exist(name)
        special = input('Does the barista have a special? (y/n):')
        if special == 'y':
            special_type = input('Enter the special coffee type: ')
            self.add_barista(name, month, is_special=True, special_type=special_type)
        else:
            self.add_barista(name, month, is_special=False, special_type=None)

    # Terminate the barista
    def fire_barista(self):
        name = input('Enter the name of the barista to be fired:\n')
        self.remove_barista(name)

    # Calculate labor force
    def get_barista_labour(self):
        return 80 * 60 * len(self.barista)

    # Barista expenses
    def barista_cost(self):
        return 15 * 120 * len(self.barista)

    # Show baristas
    def show_barista(self):
        return self.barista
