from __future__ import division

class MyInt:
    def __init__(self, val):
        # if not isinstance(val, int or str):
        #     raise TypeError('Vvod dolzhen bit celim chislom ili strokoi')
        self.__val = val

    def __str__(self):#Pereopredelili vivod na polzovatelia, chtobi ne ssilku pokazivalo
        return str(self.__val)
    def __repr__(self):# Vivod dliya spesialista
        return f'{self.__class__}, {self.__val}'

    @classmethod
    def verify_val(cls, other):
        if not isinstance(other, int or str):
            raise TypeError('Vvod dolzhen bit celim chislom ili strokoi')
        other = int(other)
        return other

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (str, MyInt)):
            raise TypeError("Operand d bit tipa str ili Myint")
        return int(other) if isinstance(other,str) else other.__val

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.__val == sc  # Zdes piton sravnivaet i vidaet True ili False

    def __ne__(self, other):
        print('Nequal')
        sc = self.__verify_data(other)
        return self.__val != sc

    def __lt__(self, other):
        sc = other if isinstance(other,int) else other.seconds  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.__val < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.__val > sc

    def __le__(self, other):
        sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.__val <= sc

    def __ge__(self, other):
        sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.__val >= sc

    def __add__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int
        return MyInt(self.__val + other)  # Obespechivaet slozhenie slagaemix bez potery type class, t.e. ostaetsia eksemliyar

    def __sub__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int
        return MyInt(self.__val - other)

    def __rsub__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int
        return MyInt(self.__val - other)

    def __truediv__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int
        return MyInt(self.__val / other)

    def __rtruediv__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int

        return MyInt(other / self.__val)
    def __mul__(self, other):
        if isinstance(other, str):
            other = int(other)  # Perevodim str v int
        return MyInt(self.__val * other)

    def __len__(self):
        return len(self.__val)

a = MyInt(5)
# print(a < 3)
# False
print(a >= '3')
# True
# print(a == '5')
# True
# # x = MyInt(3)
# # x = x + 3
# # print(x)
# a = MyInt(5)
# a = a + '5'
# print(a)
# # 10
# a = a - 2 - 3
# a
# print(a)
# # <class '__main__.MyInt'>: 5
# a = a * '5'
# print(a)
# # 25
# a = a/ 10
# print(a)
# # 2.5

