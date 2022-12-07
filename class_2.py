class Bottle:
    color = 'white'
    contains = float(0.0)

    def get_content(self):
        return self.contains

    def fill(self, add):
        self.contains += add

bottle_1 = Bottle()
bottle_1.color = 'Красная'
bottle_1.get_content()
print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())
# Красная 0
# Красная 100
bottle_2 = Bottle()
bottle_2.color = 'Синяя'
bottle_2.get_content()
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
#
#
#
#     print(bottle_1.color, bottle_1.get_content())
#     bottle_1.fill(100)
#     print(bottle_1.color, bottle_1.get_content())
#
#     print(bottle_2.color, bottle_2.get_content())
#     bottle_2.fill(500)
#
#
#     Красная 0
#     Красная 100
#     Синяя 0
#     Синяя 500