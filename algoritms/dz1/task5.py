class PlatesStack:
    def __init__(self):
        self.plates = [[]]
        self.maxsize = 2

    def __str__(self):
        return str(self.plates)

    def push_in(self, el):
        if len(self.plates[len(self.plates) - 1]) < self.maxsize:
            self.plates[len(self.plates) - 1].append(el)
        elif len(self.plates[len(self.plates) - 1]) >= self.maxsize:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(el)

    def pop_out(self):
        if [] in self.plates and len(self.plates)>1:
            self.plates.remove([])
        return self.plates[-1:][0].pop()


a = PlatesStack()
a.push_in(1)
a.push_in(2)
a.push_in(3)
a.push_in(4)
a.pop_out()
a.pop_out()
a.pop_out()


print(a.plates)
