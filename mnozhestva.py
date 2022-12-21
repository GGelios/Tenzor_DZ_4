"""Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
       1. входят одновременно в оба;
       2. входят только в первое, но не входят во второе;
       3. входят только во второе, но не входят в первое;
       4. входят в первое или во второе, но не в оба из них одновременно."""

import random
a=[]
b=[]
for i in range(0,10):
    a.append(random.randint(-10,10))
    b.append(random.randint(-10,10))
a=set(a)
b=set(b)
print('First set', a, 'Second set', b)
print('Include a and b', a&b)
print('Include in a, not include in b', a-b)
print('Include in b, not include in a', b-a)
print('Include in a or b, but not in both', a^b)
