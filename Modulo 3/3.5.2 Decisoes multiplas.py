l1 = input('lado 1: ')
l2 = input('lado 2: ')
l3 = input('lado 3: ')
if l1 == l2 and l2== l3:
    print ('Equilatero')
if l1 == l2 or l2 == l3 or l1 == l3:
    print ('Isoceles')
if l1 != l2 and l2 != l3 and l1 != l3:
    print ('Escaleno') 