for i in range(2, 20):
    for j in range(2, 20):
        print('{:2d} X {:2d} = {:3d}\t'.format(j, i, i*j), end='')
    print()