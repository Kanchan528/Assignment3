def tower_of_hanoi(disk, source, dest, aux):
    if disk == 1:
        print('Move disk from ',source,"to destination ",dest)
    
    else:
        tower_of_hanoi(disk-1, source, aux, dest)
        print('Move disk ',disk,'from source',source,'to destination', dest)
        tower_of_hanoi(disk-1, aux, dest, source)

disk = 4
tower_of_hanoi(disk, 'A', 'C', 'B')