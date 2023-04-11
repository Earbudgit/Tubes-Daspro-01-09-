from construct import *
from command import *

def main():
    username = "pass"
    role = "none"
    status = False
    while status == False:
        opsi = input(">>> \n")
        if opsi == "help":
            help(role)

        elif opsi == "login":
            if username != "pass":
                print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali')
            else:
                (username, role) = login(user, password)
                
        elif opsi == "logout":
            if username == "pass":
                print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
            else:
                (username, role) = logout()
    
main()
