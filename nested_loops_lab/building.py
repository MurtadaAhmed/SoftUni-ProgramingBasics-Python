floors = int(input())
rooms = int(input())
for floor in range(floors, 0 , -1):  # -1 because we are starting from top down
    for room in range(0, rooms):
        if floor == floors:  # it means that if we are in the last floor, we need to use L
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 != 0 and floor != floors:
            print(f"A{floor}{room}",end=" ")
        if floor % 2 == 0 and floor != floors:
            print(f"O{floor}{room}", end=" ")
    print()  # this one is to make new line between the floors

