import os
import time
from logo_launch_page import loading
loading()
os.system("cls")
selesai=False
while not selesai:  # melakukam looping
    print('[1] Login\n[2] Sign Up')
    pilih=input("Pilih: ")
    if pilih=='1': # melakukan login
        from login import login_peminjam # pemanggilan login funstion peminjam
        from login import login_perpustakawan # pemanggilan funstion login perpustakaan
        username=input("Username: ") # input user
        passwors=input("Password: ") # input pw
        perpustakaan=login_perpustakawan(username,passwors)
        peminjam=login_peminjam(username,passwors)
        if bool(perpustakaan) is not False:
                if perpustakaan[0]=='1': # menentukan apakah perpus
                            print("Ditemukan")
                            time.sleep(1)
                            os.system('cls')
                            from halaman_utama_pustakawan import halaman_utama_pustakawan
                            halaman_utama_pustakawan(0,(perpustakaan[1]),0)
                            break
        if bool(peminjam) is not False:
                    if peminjam[0]=='2': # menentukan apakah peminjam
                            print("Ditemukan")
                            time.sleep(1)
                            os.system('cls')
                            from halaman_peminjam_atau_siswa import halaman_peminjam
                            halaman_peminjam(1,(peminjam[1]),0)
                            
        if bool(perpustakaan)==bool(peminjam):
               print("Tidak ditemukan")
               time.sleep(1)
               os.system("cls")
    elif pilih=='2': # sign up hanya bis dilakukan oleh perpustakawan
        from sign_up import sign_up
        sign_up(0) # 0 ===> memnunjukkan ini hanya untuk perpustakawan
        
    else:
        print("Maaf Anda salah ketik")
        time.sleep(0.9)
        os.system("cls")