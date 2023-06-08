import eel
import os
import datetime as d
from cryptography.fernet import Fernet
from mysql.connector import Error
import mysql.connector as mysql

# sub program enkripsi
def enkripsi(string):
    string = bytes(string, 'utf-8')
    key  = Fernet.generate_key()
    return [str(Fernet(key).encrypt(string))[2:-1], key]
def dekripsi(encstring, key):
    encstring = bytes(encstring, 'utf-8')
    return str(Fernet(key).decrypt(encstring))[2:-1]
def token():
    return str(Fernet.generate_key())[2:-1]
currentPath = os.getcwd()
currentPath = currentPath.replace('\\', '/')
eel.init('web')

asyncEel = True
# try:
#     # konek = mysql.connect(host = 'localhost',
#     #                 database = 'to_do_list',
#     #                 user = 'jati',
#     #                 password = '12345678')
#     konek = mysql.connect(host = 'localhost',
#                     database = 'to_do_list',
#                     user = 'root',
#                     password = '')
# except Error as e:
#     print('Koneksi database gagal...', e)
#     quit()
# else:
#     print('Koneksi database berhasil...')

# cursor_akun = konek.cursor()

@eel.expose
def dateDisplay():
    now = d.datetime.now()
    day = now.day
    month = now.month
    year = now.year 
    return f"{day}-{month}-{year}"
#Session
class Session():
    global mysql
    def __init__(self):
        self.conn = ''
        self.cursor = ''
        self.email = ''
        self.tanggal = dateDisplay()
    def bukaKoneksi(self, host = 'localhost',database = 'to_do_list',user = 'root',password = ''):
        try:
            self.conn = mysql.connect(host = host,database = database,user = user,password = password)
        except Error as e:
            print('Koneksi database gagal...', e)
            quit()
        else:
            print('Koneksi database berhasil...')
            self.cursor = self.conn.cursor()
            
    def tutupKoneksi(self):
        self.conn.close()
        
sesi = Session()
sesi.bukaKoneksi('localhost', 'to_do_list', 'root', '')

@eel.expose
def ceksesi():
    eel.giveAlert(sesi.email)

@eel.expose
def auth(email, password):
    email, password = str(email), str(password)
    sesi.cursor.execute(
        f'''
        SELECT password, pass_key FROM db_user WHERE email="{email}"
        '''
    )
    passdb = sesi.cursor.fetchall()[0]
    try:
        passdb, keydb = passdb[0], passdb[1]
        validation_akun = bool(password == dekripsi(passdb, keydb))
    except:
        print('Validasi Akun Gagal')
        eel.giveMsg('Akun tidak ditemukan')
    else:
        print('Validasi Akun Berhasil')
        if passdb[0] == '()':
            print('Error tidak diketahui')
            eel.giveMsg('Akun tidak ditemukan')
        elif validation_akun == False:
            print('Autentikasi Akun Gagal')
            eel.giveMsg('Email atau Password Salah')
        elif validation_akun == True:
            print('Autentikasi Akun Berhasil')
            sesi.email = email
            eel.dashboard()

@eel.expose
def createAkun(email, nama, password):
    email, nama, password = str(email), str(nama), str(password)
    sesi.cursor.execute (
        f'''
        SELECT email FROM db_user WHERE email="{email}"
        '''    
    )
    emaildb = sesi.cursor.fetchone()
    if emaildb != None:
        eel.giveMsg('Email sudah dipakai')
    else:
        passEnc = enkripsi(password)
        sesi.cursor.execute(
            '''
            INSERT INTO db_user (email, nama, password, pass_key, jenis_akses) 
            VALUES (%s,%s,%s,%s,%s)
            '''
        , (email, nama, passEnc[0], passEnc[1], 'user'))
        sesi.conn.commit()
        print('Berhasil tambah data akun')
        eel.dashboard() 

@eel.expose
def everyReload():
    sesi.cursor.execute('''
    SELECT * FROM db_task WHERE date=%s AND email=%s
    '''
    , (sesi.tanggal, sesi.email))
    hasilData = sesi.cursor.fetchall()
    # Bubble Sort
    for passnum in range(len(hasilData)-1, 0, -1):
        for i in range(passnum):
            if ord(hasilData[i][1][0]) > ord(hasilData[i+1][1][0]):
                temp = hasilData[i]
                hasilData[i] = hasilData[i + 1]
                hasilData[i + 1] = temp
            elif ord(hasilData[i][1][0]) == ord(hasilData[i+1][1][0]):
                if ord(hasilData[i][1][1]) > ord(hasilData[i+1][1][1]):
                    temp = hasilData[i]
                    hasilData[i] = hasilData[i + 1]
                    hasilData[i + 1] = temp
    eel.sendNotif(hasilData)

@eel.expose
def addTask(taskName, date_d, date_m, date_y):
    taskName, date_d, date_m, date_y = str(taskName), int(date_d), int(date_m), int(date_y)
    date_all = f'{date_d}-{date_m}-{date_y}'
    sesi.cursor.execute(
        '''
        INSERT INTO db_task (token, task, date, email, status)
        VALUES (%s, %s, %s, %s, %s)
        '''
    , (token(), taskName, date_all, sesi.email, 'false'))
    sesi.conn.commit()
    print('Berhasil tambah data task')
    eel.reload()

@eel.expose
def changeStatusTask(token, boolean):
    sesi.cursor.execute(
        '''
        UPDATE db_task SET status=%s WHERE token=%s
        '''
    , (boolean, token))
    sesi.conn.commit()
    print('Berhasil ubah status task')
    eel.reload()

@eel.expose
def deleteTask(token):
    sesi.cursor.execute(
        '''
        DELETE FROM db_task WHERE token=%s
        '''
    , (token,))
    sesi.conn.commit()
    print('Berhasil hapus task')
    eel.reload()

@eel.expose
def updateTask(token, taskName, date_d, date_m, date_y):
    token, taskName, date_d, date_m, date_y = str(token), str(taskName), int(date_d), int(date_m), int(date_y)
    date_all = f'{date_d}-{date_m}-{date_y}'
    sesi.cursor.execute(
        '''
        UPDATE db_task SET task=%s, date=%s WHERE token=%s
        '''
    , (taskName, date_all, token))
    sesi.conn.commit()
    print('Berhasil update task')
    eel.reload()
    
eel.start('index.html', block=False, app_mode=True, size=(810,600), cmdline_args=['--incognito', f'--user-data-dir={currentPath}/profiles/web'])
while asyncEel == True:
    eel.sleep(1)
    if asyncEel == False:
        break

