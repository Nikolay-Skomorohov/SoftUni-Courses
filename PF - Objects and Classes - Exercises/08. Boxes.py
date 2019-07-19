import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(point1, point2):
        arg1 = (point1.x - point2.x)
        arg2 = (point1.y - point2.y)
        return math.sqrt(arg1 ** 2 + arg2 ** 2)


class Box:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def calculate_perimeter(self, width, height):
        return (width * 2) + (height * 2)

    def calculate_area(self, width, height):
        return width * height


def input_data():
    box_obj_list = []
    num_list = [pair for pair in input().split(" | ")]
    while num_list[0] != "end":
        points_obj_list = []
        for i in num_list:
            new_point = list(map(int, i.split(":")))
            points_obj_list.append(Point(*new_point))
        box_obj_list.append(Box(*points_obj_list))
        num_list = [pair for pair in input().split(" | ")]
    return box_obj_list


def main():
    for box in input_data():
        width = Point.calculate_distance(box.top_left, box.top_right)
        height = Point.calculate_distance(box.top_left, box.bottom_left)
        print(f"Box: {width:.0f}, {height:.0f}")
        print(f"Perimeter: {box.calculate_perimeter(width, height):.0f}")
        print(f"Area: {box.calculate_area(width, height):.0f}")


if __name__ == "__main__":
    main()
