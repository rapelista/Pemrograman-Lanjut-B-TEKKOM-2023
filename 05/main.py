with open('users.csv', 'r+') as file:
    print(file.read())
    file.write("halo")
    print(file.read())


# with open("a.txt", 'r') as file:
#     print(file.read())

# with open("a.txt", 'w') as file:
#     file.write("ubah file a")

# import os
# if os.path.exists("a.txt"):
#     os.remove("a.txt")

# with open("a.txt", 'x') as file:
#     file.write("buat file a")

# import csv, os

# with open("users.csv", "w", newline='') as file:
#     fieldnames = ["no", "username", "password"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()

#     writer.writerow({ 
#         'no': 1,
#         'username': 'admin',
#         'password': 'admin'
#      })
#     writer.writerow({ 
#         'no': 2,
#         'username': 'guest',
#         'password': 'guest'
#      })
    
# new_file = open('new_users.csv', 'w')
# _file = csv.DictWriter(new_file, fieldnames=['no','username','password'])
# _file.writeheader()

# with open("users.csv", "r") as file:
#     users = csv.DictReader(file)
#     for user in users:
#         print("no", user['no'])
#         print("username", user['username'])
#         print("password", user['password'])

#         _file.writerow(user)
#     else:
#         os.remove('users.csv')

# with open("users.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)


# import os


# os.rename('users.csv', 'new_users.csv')













# import csv

# while True:
#     print()
#     print("=" * 5 ,"| Menu |", "=" * 5)
#     print("type -1 in Name for cancel")
#     print("1. Register")
#     print("2. Login")

#     menu = input("Select: ")
    
#     if menu == '-1':
#         break

#     elif menu == '1':
#         while True:
#             print()
#             print("=" * 5 ,"| Register |", "=" * 5)
#             print("type -1 in Name for cancel")

#             name = input("Name\t : ")

#             if name == '-1':
#                 break

#             password = input("Password : ")

#             is_registered = None

#             with open('users.csv', 'r') as file:
#                 users = csv.DictReader(file)
#                 for _user in users:
#                     if _user['name'] == name:
#                         is_registered = True
#                         break

#             print()

#             if is_registered:
#                 print("User is already registered!")

#             else:
#                 with open("users.csv", "a") as file:
#                     writer = csv.DictWriter(file, fieldnames=['name', 'password', 'permission'])
#                     writer.writerow({'name': name, 'password': password, 'permission': 0})

#                 print("Register success, please login!")
#                 break

#     elif menu == '2':
#         while True:
#             print()
#             print("=" * 5 ,"| Login |", "=" * 5)
#             print("type -1 in Name for cancel")

#             name = input("Name\t : ")

#             if name == '-1':
#                 break

#             password = input("Password : ")
            
#             user = None

#             with open('users.csv', 'r') as file:
#                 users = csv.DictReader(file)
#                 for _user in users:
#                     if _user['name'] == name and _user['password'] == password:
#                         user = _user
#                         break
            
#             print()

#             if user != None:
#                 while True:
#                     print("Hi,", user['name'])
#                     with open("hello.txt", "r") as file:
#                         print(file.read())
                        
#                     print("Menu: ")

#                     if user['permission'] == '1':
#                         print("1. Edit kata sambutan")
                    
#                     print("0. Logout")

#                     user_menu = input("Select: ")

#                     if user_menu == '0':
#                         print()
#                         print("Logout...")
#                         break

#                     elif user_menu == '1' and user['permission'] == '1':
#                         sambutan = input("Masukkan sambutan baru: ")
#                         with open("hello.txt", 'w') as file:
#                             file.write(sambutan)

#                         print()
                    
#             else:
#                 print("Authentication failed")