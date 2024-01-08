#  Determine whether the input is correct


# Determine if the input is legal Contains a range of values
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


# Determine if the input is legal Contains a range of values
def change_demand_poistives(number, change_demand):
    while True:
        try:
            change_demand = int(change_demand)
            if 0<= change_demand <= number:
                return change_demand
            else:
                print('Please enter an integer value')
                return change_demand_poistives(number, input())

        except (TypeError, ValueError):
            print('Please enter an integer value')
            return change_demand_poistives(number, input())
