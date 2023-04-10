def xlen(elmt): #fungsi len general
    count = 0
    for i in elmt:
        count += 1
    return count


def xappend(list, element):
    list += [element]
    return list

def xsplit(string):
    temp = []
    dummy = ""
    for char in string:
        if char == ";":
            temp = xappend(temp, dummy)
            dummy = ""
        else:
            dummy += char

    temp = xappend(temp,dummy)
    return temp
    
user = []
password = []
role = []

with open("user.csv") as file:
    rows = file.readlines()

for i in range(xlen(rows)):
    if i < xlen(rows) - 1:
        multi = xsplit(rows[i+1])
        for j in range(2):
            if j == 0:
                user = xappend(user, multi[j])
            elif j == 1:
                password = xappend(password, multi[j])
            elif j == 2:
                role = xappend(role, multi[j])

def login(user, password):
    num  = xlen(user)
    username = input("Username: ")
    passw = input("Password: ")
    
    for i in range(num):
        if (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            Status = True
            main()
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
            main()
        else:
            print("Username tidak terdaftar!")

    return Status #dicek untuk saat logout

def logout():
    quit

def help():
    print("Submenu....")
    
def main():
    opsi = input()
    if opsi == "login":
        login(user, password)
    elif opsi == "help":
        help()
    elif opsi == "logout":
        logout()

main()