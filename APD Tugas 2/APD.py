print('\nOutput 1:')
o1 = 1
while o1 <= 10:
    print(o1)
    o1 += 1

print('\nOutput 2:')
o2 = 1
while o2 <= 10:
    print(o2, end=' ')
    o2 += 1

print('\n\nOutput 3:')
o3 = 10
while o3 >= 1:
    print(o3, end=' ')
    o3 -= 1

print('\n\nOutput 4:')
o4 = 1
while o4 <= 10:
    print(o4 * 2, end=' ')
    o4 += 1

print('\n\nOutput 4a:')
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()

print('\nOutput 4b:')
for i in range(1, 6):
    for j in range(1, 6):
        if j == 3:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()

print('\nOutput 4c:')
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:
            print(j, end=' ')
        else:
            print(0, end=' ')
    print()

print('\nOutput 4d')
for i in range(1, 6):
    for j in range(1, 6):
        if i == 2:
            print('0', end=' ')
        elif i == 4:
            print('0', end=' ')
        else:
            print(j, end=' ')
    print()

print('\nOutput 4e')
for i in range(1, 6):
    for j in range(1, 6):
        if j == i:
            print('a', end=' ')
        else:
            print(j, end=' ')
    print()

print('\nOutput 4f')
start = 1
for i in range(5):
    for j in range(start, start + 5):
        print(j, end=' ')
    print()
    start += 5

ganjil = len([x for x in range(1, 26) if x % 2 != 0])
genap = len([x for x in range(1, 26) if x % 2 == 0])
print(f"\nAda {ganjil} angka bilangan ganjil")
print(f"Ada {genap} angka bilangan genap")

print('\nOutput 5')
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()

print('\nOutput 6')
for i in range(1, 6):
    for j in range(i):
        print(4, end=' ')
    print()

print('''\nOutput 7:
      \n''')
