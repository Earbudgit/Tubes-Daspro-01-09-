def length(lst): #len final 
    elmt = xappend(lst, "&")
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count


def dumstring(list): #mengubah list[i] menjadi str
    if length(list) == 0:
        return ""
    dumstr = str(list[0])
    index = 1
    while index < length(list):
        dumstr += "" + str(list[index])
        index += 1

    return dumstr


def xappend(lst1,lst2): #append 2 list menjadi list baru, != append
    lst = [*lst1,*lst2]
    return lst

def xlen(elmt): #fungsi untuk length
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count

def newlist(lst): #untuk menghasilkan list tanpa & 
    elmt = xappend(lst, "&")
    final = []
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&" and (i != 0):
            final = xappend(final, [elmt[i]])

    return final 

def cekstr(dumstring): #cek jika str ada \n
    newstr = ["&" for i in range(length(dumstring))]
    for i in range(length(dumstring)):
        for j in range(length(dumstring[i])):
            if dumstring[i][j] == "\n":
                break
            else:
                if newstr[i] == "&":
                    newstr[i] = str(dumstring[i][j])
                else:
                    newstr[i] += str(dumstring[i][j])
    return newstr

#untuk user csv
with open("user.csv") as file:
    rows = file.readlines()
user = ["&" for i in range(100)]
password = ["&" for i in range(100)]
role = ["&" for i in range(100)]

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


#untuk bahan bangunan
with open("bahan_bangunan.csv") as file:
    rows = file.readlines()
nama = []
deskripsi = []
jumlah = []

#untuk candi
with open("candi.csv") as file:
    rows = file.readlines()
id = []
pembuat = []
pasir = []
batu = []
air = []