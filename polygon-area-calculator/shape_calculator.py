class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width, self.height = width, height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            poly = ['*' * self.width for i in range(self.height)]
            poly_string = ''
            for i in poly:
                poly_string += i
                poly_string += '\n'
            return poly_string

    def get_amount_inside(self, poly):
        poly_height = poly.height
        poly_width = poly.width
        a = self.height // poly_height
        b = self.width // poly_width
        return a * b


class Square(Rectangle):
    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, height):
        self.height = height
        self.width = height

    def __init__(self, side):
        self.width, self.height = side, side
