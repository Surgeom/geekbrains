class Road:
    def __init__(self, road_length, road_width):
        self._lenght = int(road_length)
        self._width = int(road_width)

    def road_m(self, kg, sm):
        return f"{self._width * self._lenght * int(kg) * int(sm)}T"


a = Road(20, 5000)
print(a.road_m(25, 5))
