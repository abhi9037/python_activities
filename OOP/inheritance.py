

class Decimal():
    def __init__(self, number, position):
        self.number = number
        self.position = position

    def __repr__(self):
        return "%.{}f".format(self.position) % self.number

class Currency(Decimal):
    def __init__(self, symbel, number, position):
        super().__init__(number,position)
        self.symbel = symbel

    def __repr__(self):
        return "{}{}".format(self.symbel,super().__repr__())


print (Currency('$',25.5672,2))