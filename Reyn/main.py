from construct import *

#gunakan fungsi newlist untuk memanggil suatu array
#cekstr digunakan untuk array yang berisikan \n

#User.csv
user = newlist(user)
password = newlist(password)
role = cekstr(newlist(role))  

#Bahan_Bangunan.csv
nama = newlist(nama)
deskripsi = newlist(deskripsi)
jumlah = newlist_int(jumlah)

#candi.csv
id = newlist_int(id)
pembuat = newlist(pembuat)
pasir = newlist_int(pasir)
batu = newlist_int(batu)
air = newlist_int(air)

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
                return("pass", "none")
        elif (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return(username, role[i]) 
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
            return("pass", "none")

def logout():
     username = "pass"
     role = "none"
     return(username, role)

def help(role):
    if role == "bandung_bondowoso":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. haousjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengumpulkan jin bangun")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja jin")
        print("8. laporancandi")
        print("   Untuk mengetahui proses pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data")

    elif role== "roro_jonggrang":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan data")
    
    elif role== "jin_pengumpul":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif role== "jin_pembangun":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    elif role == "none":
        print("====================== HELP ======================")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    else:
        return None

def summon_jin():
    return 0
