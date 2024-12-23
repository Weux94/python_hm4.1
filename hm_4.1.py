list = [0, 1, 2, 0, 0, 0, 0, 6]

for x in list:
    if x == 0:
        list.append(x)
        list.remove(x)

        print(list)
