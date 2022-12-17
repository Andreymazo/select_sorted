class Meta(type):
   def __new__(cls, name, base, attrs):
        uppercase_attrs = {
                attr.upper(): v ##Ne ochen mne tut ponyatno kak upper prisvaivaetsia znacheniyam slovarya, no rabotaet
               for attr, v in attrs.items()
           }
        return super(Meta, cls).__new__(cls, name, base, uppercase_attrs)

class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586

m = Math()
print(m.PI)
# 3.141592653589793
print(m.E)
# 2.718281828459045
print(m.pi)
# AttributeError: 'Math' object has no attribute 'pi'