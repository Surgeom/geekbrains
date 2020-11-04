of1 = []
of2 = []
of3 = []


class WarehouseOfEquip:
    def __init__(self, *args):
        self.dict_of_equip = {'printer': [], 'scanner': [], 'xerox': []}
        self.company_parts = {'Office1': of1, 'Office2': of2, 'Office3': of3}
        self.equip = [*args]

    def get_new_eq(self):
        for x in self.equip:
            if x.__class__.__name__ == "Printer":
                self.dict_of_equip['printer'].append(x)
            elif x.__class__.__name__ == "Scanner":
                self.dict_of_equip['scanner'].append(x)
            elif x.__class__.__name__ == "Xerox":
                self.dict_of_equip['xerox'].append(x)

    def go_to_of(self, of, pr_name, num):
        for i in range(num):
            self.company_parts[f"{of}"].append(self.dict_of_equip[f'{pr_name}'])


class OfficeEquipment:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}"


class Printer(OfficeEquipment):
    def __init__(self, model, price, speed):
        super().__init__(model, price)
        self.speed = speed


class Scanner(OfficeEquipment):
    def __init__(self, model, price, time_scan):
        super().__init__(model, price)
        self.time_scan = time_scan


class Xerox(OfficeEquipment):
    def __init__(self, model, price, num_paper):
        super().__init__(model, price)
        self.num_paper = num_paper


pr = Printer(1, 2, 3)
scl = WarehouseOfEquip(pr)
scl.get_new_eq()
print(scl.dict_of_equip)
scl.go_to_of('Office1', 'printer', 1)
print(of1)
