from typing import final


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            ph_listaya = list()

            for negma in range(int(self.height)):
                hmm_ = f"{'*' * int(self.width)}"
                ph_listaya.append(hmm_)
            final_picture = "\n".join(ph_listaya)

            return final_picture

    def get_amount_inside(self, polygon):
        return int(polygon.get_area() / self.get_area())

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(width=side, height=side)

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)


##INITIAL TESTING##
##FOR Rectangle CLASS##
# mwah = Rectangle(2, 2)
# moo = Rectangle(4, 4)
# print(mwah.get_amount_inside(moo))
# print(mwah)
# print(mwah.get_picture())

##FOR Square CLASS##
# wah = Square(side=5)
# wah.set_side(side_length=7)
# wah.set_height(2)
# wah.set_width(9)
# print(wah)
