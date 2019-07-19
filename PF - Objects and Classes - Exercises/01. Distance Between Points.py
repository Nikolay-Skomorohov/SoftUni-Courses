import math


class Point:
    def __init__(self, point_x=None, point_y=None):
        self.point_x = point_x
        self.point_y = point_y

    def calculate_distance(self, point_1, point_2):
        side_a = point_1.point_x - point_2.point_x
        side_b = point_1.point_y - point_2.point_y
        distance = math.sqrt((side_a ** 2) + (side_b ** 2))
        return distance


point_1_input = list(map(int, input().split()))
point_2_input = list(map(int, input().split()))
obj_point_1 = Point(point_1_input[0], point_1_input[1])
obj_point_2 = Point(point_2_input[0], point_2_input[1])

result_obj = Point()

print(f"{result_obj.calculate_distance(obj_point_1, obj_point_2):.3f}")
