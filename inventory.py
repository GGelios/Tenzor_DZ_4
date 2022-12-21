"""Создать игровой инвентарь. Должна быть возможность добавлять в него предметы и удалять предметы из него. Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. Вывод предметов должен быть с названием предмета и его весом."""

weight = 0
inventory = {'DragonLore':(6), 'Bread':(0.5), 'Dorogoi Dnevnik...':(0.3),
             'Koshka':(1), 'Butterfly':(0.0)} 

while True:
    choose = input('''What you want to do?
    1. Add item
    2. Delete item
    3. View inventory
    4. Exit
    ''')
    weight = sum(inventory.values())
    print(weight, '/100', sep='')
    
    if weight > 100:
        print('You are overloaded')
    elif choose == '1' and weight < 100:
        dweight = int(input('Input weight: '))
        weight = weight + dweight
        if weight < 100:
            inventory[input('Enter a name ')] = dweight
        else:
            print('Error')
    elif choose == '2':
        inventory.pop(input('What do you want to delete '))
    elif choose == '3':
        print(inventory)
    elif choose == '4':
        break
    else:
        print("Error")
