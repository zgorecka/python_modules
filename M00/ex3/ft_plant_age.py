def ft_plant_age():
    print("Enter plant age in days: ", end='')
    a = int(input())
    if a > 60:
        print("Plant is ready to harvest!", end='')
    else:
        print("Plant needs more time to grow.", end='')
