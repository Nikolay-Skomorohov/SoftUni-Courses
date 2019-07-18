class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def is_inside(self, r2):
        if self.left >= r2.left\
            and self.right <= r2.right\
            and self.right <= r2.right\
            and self.top >= r2.top\
            and self.bottom <= r2.bottom:
            return "Inside"
        else:
            return "Not inside"


def read_rectangle():
    input_list = [int(num) for num in input().split()]
    rect = Rectangle(*input_list)
    return rect


def main():
    rect_obj_1 = read_rectangle()
    rect_obj_2 = read_rectangle()
    print(rect_obj_1.is_inside(rect_obj_2))


if __name__ == '__main__':
    main()
