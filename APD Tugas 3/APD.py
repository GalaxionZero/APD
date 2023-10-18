# for i in range(9):
#     if i == 0:
#         continue
#     elif i == 6:
#         print(4, end='')
#         continue
#     elif i == 7:
#         print(3, end='')
#         continue
#     elif i == 8:
#         print(2, end='')
#         continue
#     print(i, end='')


# for i in range(1, 9, 1):
#     if i == 6:
#         print(4, end='')
#         continue
#     elif i == 7:
#         print(3, end='')
#         continue
#     elif i == 8:
#         print(2, end='')
#         continue
#     print(i, end='')


x = int(input('Masukkan berapa banyak pengulangan: '))
y = int(input('Masukkan berapa batasan angka: '))
output = ''
for i in range(1, x + 1):
    if i <= y:
        output += str(i)
    else:
        output += str(y - (i - y))

print(output)