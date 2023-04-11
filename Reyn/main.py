def length(lst): #len final 
    elmt = xappend(lst, "&")
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count


def dumstring(list):
    if len(list) == 0:
        return ""
    dumstr = str(list[0])
    index = 1
    while index < len(list):
        dumstr += "" + str(list[index])
        index += 1

    return dumstr


def xappend(lst1,lst2):
    lst = [*lst1,*lst2]
    return lst

def xlen(elmt):
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count

with open("user.csv") as file:
    rows = file.readlines()

user = [0 for i in range(3)]
password = [0 for i in range(3)]
role = [0 for i in range(3)]

char = ""
k = 0
parameter = 0

for i in range(length(rows)): #rows = list
    dumarray = rows[i]
    dumstr = dumstring(dumarray)
    for j in range(length(dumstr)):
        if dumstr[j] == ";":
            parameter += 1
            if parameter == 1:
                user[k] = char
                char = ""
            elif parameter == 2:
                password[k] = char
                char = ""

        elif j == (length(dumstr)-1):
                role[k] = char + dumstr[length(dumstr)-1]
                char = ""

        elif dumstr[j] != ";":
            char += dumstr[j]

    char =""
    k += 1
    parameter = 0


def login(user, password):
    num  = length(user)
    username = input("Username: ")
    passw = input("Password: ")
    count = 0
    for i in range(num):
        if username != user[i]:
            count += 1
            if count == length(user):
                print("Username tidak terdaftar!")
        elif (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
    main()


def logout():
    quit
    main()

def main():
    opsi = input()
    if opsi == "login":
        login(user, password)
    elif opsi == "logout":
        logout()
    elif opsi  == "help":
        print("aaa")

main()
