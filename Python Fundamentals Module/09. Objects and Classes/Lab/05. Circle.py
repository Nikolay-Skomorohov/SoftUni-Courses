class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        return ((self.diameter / 2) ** 2) * self.__pi

    def calculate_area_of_sector(self, angle):
        radius_power = ((self.diameter / 2) ** 2)
        angle_calc = ((angle * self.__pi) / 360)
        return radius_power * angle_calc


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
