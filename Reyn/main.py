def xlen(elmt): #fungsi len general
    count = 0
    for i in elmt:
        count += 1
    return count

def dumstring(str):
    dumstr = ''
    for i in str:
        dumstr += i
    return dumstr

with open("user.csv") as file:
    rows = file.readlines()


user = [0 for i in range(3)]
password = [0 for i in range(3)]
role = [0 for i in range(3)]

char = ""
k = 0
parameter = 0


for i in range(xlen(rows)):
    dumarray = rows[i]
    dumstr = dumstring(dumarray)
    for j in range(xlen(dumstr)):
        if dumstr[j] == ";":
            parameter += 1
            if parameter == 1:
                user[k] = char
                char = ""
            elif parameter == 2:
                password[k] = char
                char = ""

        elif j == xlen(dumstr)-1:
                role[k] = char + dumstr[xlen(dumstr)-1]
                char = ""

        elif dumstr[j] != ";":
            char += dumstr[j]

    char =""
    k += 1
    parameter = 0


def login(user, password):
    num  = xlen(user)
    username = input("Username: ")
    passw = input("Password: ")
    count = 0
    for i in range(num):
        if username != user[i]:
            count += 1
            if count == xlen(user):
                print("Username tidak terdaftar!")
        elif (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
    main()


def logout():
    quit

def main():
    opsi = input()
    if opsi == "login":
        login(user, password)
    elif opsi == "logout":
        logout()

main()
