# print(list(range(10)))
# print(list(range(10, 20)))
# print(list(range(10, 20, 3)))

# for i in range(1, 11):
#     print('ini angka ke-', i, sep='')

# for i in range(1, 11):
#     # continue -> skip ke looping berikutnya
#     # if i == 5:
#     #     continue
#     # print('ini angka ke-', i, sep='')

#     if i == 5:
#         break
#     print('ini angka ke-', i, sep='')

# print('looping selesai')

# i = 0
# # (10 < 10 == FALSE)
# while True:
#     print('nilai i:', i)
#     i += 1
# print('selesai')

# x = 10
# print(x, type(x))

# x = "kelas b"
# print(x, type(x))

# x = 10.1
# print(x, type(x))

# x = None
# print(x, type(x))

# x = int(input("masukin apapun: "))
# print(x, type(x))

# int() -> integer
# float () -> float
# str () ->  str















# Pseudocode:
# --------------------------------
# if year modulo 4 is 0
# then
#     if year modulo 100 is 0
#     then
#        if year modulo 400 is 0
#        then
#            is_leap_year
#        else
#            not_leap_year
#     else is_leap_year
# else not_leap_year


# ------------------------------------------------

# PROSEDUR PRAKTIKUM 01

# while True:
#     year = int(input("masukan angka: "))

#     if year < 0:
#         break

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print('Tahun kabisat')
#             else:
#                 print('Bukan tahun kabisat')
#         else:
#             print('Tahun kabisat')
#     else:
#         print('Bukan tahun kabisat')

# ------------------------------------------------

# PROSEDUR PRAKTIKUM 02

# _input = input("Masukkan input: ")

# print(_input, type(_input))

# m = int(_input[0])
# n = int(_input[2])
# l = int(_input[4])

# print('m =', m, type(m))
# print('n =', n, type(n))
# print('l =', l, type(l))

# print('-' * 20)

# for tinggi in range(m):
#     for lebar in range(n):
#         if tinggi < l or tinggi >= m - l or lebar < l:
#             print('*', end='')
#         else:
#             print('.', end='')
    
#     print('')


# ------------------------------------------------

# PROSEDUR PRAKTIKUM 03

# _input = int(input("Jumlah angka genap yang ingin disimpan:"))

# n_input = 0

# while n_input < _input:

#     angka = int(input("Masukkan angka: "))

#     if angka % 2 == 0:
#         n_input += 1
#         print(angka)
#         continue
#     else:
#         print("bukan angka genap!")
