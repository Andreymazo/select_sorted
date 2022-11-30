# Razmer polinoma
def f(a):
    count = 0
    index = 0
    for i in a:
        if i in a[index + 1:]:
            x = a.find(i, index + 1)  # Est index sovpaednia
            a = a.replace(a[x], '')
            print(a)
            count += 2
            index = 0
        elif i not in a[index + 1:]:
            # a = a.replace(a[index], '')
            print(a)
            index += 1

    if len(a) > 1:
        count = count+1
        return count, print(count)

f('hgjjafg')