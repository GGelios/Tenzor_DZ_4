# Реализовать сортировку списка методом пузырька.

import random
a=[]
for i in range(0,10):
    a.append(random.randint(-10,10))
print('Unsorted list:', a)
for i in range((len(a)-1)):
    for j in range((len(a)-1)):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print('Sorted list:', a)
