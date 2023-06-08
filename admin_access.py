# Impor library eksternal
import os
from cryptography.fernet import Fernet
import mysql.connector as mysql

# Menghubungkan ke database server
os.system('cls')
try:
    print('Menghubungkan ke database...')
    dbconn = mysql.connect(host='localhost', user='root', passwd='', database='to_do_list')
except:
    print('Database Tidak Terhubung')
    quit()
else:
    print('Database Terhubung')
    dbcursor = dbconn.cursor()
# Sub Program Enkripsi (Encryption)
def enkripsi(string):
    string = bytes(string, 'utf-8')
    key  = Fernet.generate_key()
    return [str(Fernet(key).encrypt(string))[2:-1], key]
def dekripsi(encstring, key):
    encstring = bytes(encstring, 'utf-8')
    return str(Fernet(key).decrypt(encstring))[2:-1]
# Sub Program Validasi Akun berdasarkan email
def cekAkun(email):
    dbcursor.execute(f"""
    SELECT email FROM db_user WHERE email="{email}"
    """)
    return len(dbcursor.fetchall())
# Sub Program Autentikasi Akun
def authAkun(email, password):
    dbcursor.execute(f"""
    SELECT * FROM db_user WHERE email="{email}"
    """)
    getData = dbcursor.fetchone()
    decryptedPass = dekripsi(getData[2], getData[3])
    if decryptedPass == password:
        return (True, getData[4])
    else:
        return (False,)
# Sub Program Buat Akun (Create)
def buatAkun(email, password, jenisAkses, namaAkun):
    if cekAkun(email) == 0:
        passEnkripsi = enkripsi(password)
        dbcursor.execute("""
        INSERT INTO db_user(email, password, pass_key, jenis_akses, nama) VALUES (%s, %s, %s, %s, %s)
        """, (email, passEnkripsi[0], passEnkripsi[1], jenisAkses, namaAkun))
        dbconn.commit()
        print('Akun berhasil dibuat')
    else:
        print('Akun tidak bisa dibuat')
# Sub Program Lihat Semua Akun (Read)
def lihatAkun():
    dbcursor.execute("""
    SELECT * FROM db_user
    """)
    for i,v in enumerate(dbcursor.fetchall()):
        print(f'({i + 1}) {v[0]} | {v[1]} | {v[4]}')
# Sub Program mendapatkan info seluruh kolom
def getInfoAkun(email):
    dbcursor.execute(f"""
    SELECT * FROM db_user WHERE email="{email}"
    """)
    return dbcursor.fetchone()
# Sub Program mendapatkan email berdasarkan index
def getInfoRow(index=0):
    dbcursor.execute("""
    SELECT email FROM db_user
    """)
    return dbcursor.fetchall()[index][0]
# Sub Program mendapatkan info jumlah baris
def getInfoAllRow():
    dbcursor.execute("""
    SELECT email FROM db_user
    """)
    return len(dbcursor.fetchall())
# Sub Program Edit Password Akun (Update)
def editPass(email, password):
    passEnkripsi = enkripsi(password)
    dbcursor.execute("""
    UPDATE db_user SET password=%s, pass_key=%s WHERE email=%s
    """, (passEnkripsi[0], passEnkripsi[1], email))
    dbconn.commit()
    print('Ubah Password Berhasil')
# Sub Program Hapus Akun (Delete)
def hapusAkun(email):
    dbcursor.execute(f"""
    DELETE FROM db_user WHERE email="{email}"
    """)
    dbconn.commit()
    print('Menghapus akun Berhasil')
# Tampilan menu masing-masing akses
listMenuUser = ('Keluar', 'Ubah Password')
listMenuAdmin = ('Keluar', 'Lihat semua akun', 'Buat akun baru', 'Ubah password', 'Hapus akun')
# Tampilan menu user
def menuUser(email):
    dataAkun = getInfoAkun(email)
    while True:
        os.system('cls')
        for i in range(1, len(listMenuUser)):
            print(f'({i}) {listMenuUser[i]}')
        print('(0)', listMenuUser[0])
        pilihanMenu = 0
        try:
            pilihanMenu = int(input('Pilih Menu -> '))
        except:
            pass
        else:
            if pilihanMenu == 0:
                os.system('cls')
                dbconn.close()
                print('Terima Kasih')
                break
            elif pilihanMenu == 1:
                os.system('cls')
                ubahPass = input('Masukkan password baru -> ')
                editPass(dataAkun[0], ubahPass)
                os.system('pause')
            else:
                pass
# Tampilan menu admin
def menuAdmin(email):
    dataAkun = getInfoAkun(email)
    while True:
        os.system('cls')
        for i in range(1, len(listMenuAdmin)):
            print(f'({i}) {listMenuAdmin[i]}')
        print('(0)', listMenuAdmin[0])
        try:
            pilihanMenu = int(input('Pilih Menu -> '))
        except:
            pass
        else:
            if pilihanMenu == 0:
                os.system('cls')
                dbconn.close()
                print('Terima Kasih')
                break
            elif pilihanMenu == 1:
                os.system('cls')
                print('=== Lihat semua akun ===')
                lihatAkun()
                os.system('pause')
            elif pilihanMenu == 2:
                os.system('cls')
                print('=== Buat Akun Baru ===')
                usnm = input('Buat email -> ')
                if cekAkun(usnm) == 0:
                    nama = input('Nama Lengkap -> ')
                    pasw = input('Buat password -> ')
                    print('(1) User\x0A(2) Admin')
                    akses = 0
                    try:
                        akses = int(input('Buat Akses -> '))
                    except:
                        print('Akun tidak bisa dibuat')
                    else:
                        if akses == 1:
                            buatAkun(usnm, pasw, 'user', nama)
                        elif akses == 2:
                            buatAkun(usnm, pasw, 'admin', nama)
                        else:
                            print('Akun tidak bisa dibuat')
                else:
                    print('Akun tidak bisa dibuat')
                os.system('pause')
            elif pilihanMenu == 3:
                os.system('cls')
                print('=== Ubah Password ===')
                lihatAkun()
                target = 0
                try:
                    target = int(input('Pilih akun yang ingin diubah -> '))
                except:
                    print('Tidak dapat mengedit akun')
                else:
                    if target <= getInfoAllRow():
                        pasw = input('Edit password menjadi -> ')
                        editPass(getInfoRow(target - 1), pasw)
                    else:
                        print('Tidak dapat mengedit akun')
                os.system('pause')
            elif pilihanMenu == 4:
                os.system('cls')
                print('=== Hapus Akun ===')
                lihatAkun()
                target = 0
                try:
                    target = int(input('Pilih akun yang ingin dihapus -> '))
                except:
                    print('Tidak dapat menghapus akun')
                else:
                    if target <= getInfoAllRow():
                        hapusAkun(getInfoRow(target - 1))
                    else:
                        print('Tidak dapat menghapus akun')
                os.system('pause')
            else:
                pass
# Menu utama login
def mainMenu():
    while True:
        os.system('cls')
        print('Selamat Datang\x0ASilahkan masuk aplikasi')
        email = input('Masukkan email -> ')
        if cekAkun(email) == 0:
            print('Akun ini tidak tersedia')
            os.system('pause')
        else:
            password = input('Masukkan password -> ')
            auth = authAkun(email, password)
            if auth[0] == True:
                if auth[1] == 'admin':
                    menuAdmin(email)
                else:
                    menuUser(email)
                break
            else:
                print('Password anda salah')
                os.system('pause')
mainMenu()