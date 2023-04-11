from construct import *

            

def main2():
    stat = 1
    opsi = input()
    if opsi == "login":
        if stat == 0:
            print("Anda sudah login!")
        else:
            cek = login(user, password)
            stat = status(cek)
            main2()

    elif opsi == "logout":
        logout()
    elif opsi  == "help":
        print("aaa")

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
            return(username, role[i]) 
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")


def main():
    username = "pass"
    status = False
    while status == False:
        opsi = input(">>> \n")
        if opsi == "login":
            if username != "pass":
                print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan logout sebelum melakukan login kembali")
            else:
                (username, role) = login(user, password)

        elif opsi == "logout":
            logout()

def logout():
     quit()

def status(cek):
    for i in range(length(user)):
        if user[i] == cek:
            return 0
        else:
            return 1

