import pandas as pd
import os
import time
data_peminjam=pd.read_csv('data_peminjam.csv')
data_pustakawan=pd.read_csv('data_pustakawan.csv')
data_login_perpustakawan =pd.read_csv('data_login_dan_signup_pustakawan.csv') 
data_login_peminjam=pd.read_csv('data_login_dan_signup_peminjam.csv')
simpan=data_peminjam,data_pustakawan
def sign_up(siapa_yang_sign_up):
    data=data_pustakawan["NIP"],data_peminjam["NIM"]
    berdasarkan=["NIP","NIM"]
    nip=int(input(f'Masukkan {berdasarkan[siapa_yang_sign_up]}: '))
    try:
        for NIP in data[siapa_yang_sign_up]: 
            if nip == int(NIP):
                ada_nip=True
                break
            else:
                ada_nip=False
        if  ada_nip is False:
            print(f"{berdasarkan[siapa_yang_sign_up]} tidak ditemukan")
            time.sleep(1)
            os.system("cls")
        else:
            print(f"{berdasarkan[siapa_yang_sign_up]} ditemukan")
            time.sleep(1)
            os.system("cls")
            username=input("Masukkan username: ")
            for username_perpustaaan in data_login_perpustakawan["username"]:
                if username ==username_perpustaaan:
                    pencarian=False
                    break
                pencarian=True
                continue
            for usenam_peminjam in data_login_peminjam["username"]:
                if  username ==usenam_peminjam:
                    pencarian1=False
                    break
                pencarian1=True
                continue
            if pencarian1 == True and pencarian == True:
                username=username
            else:
                username=False
            if username is False:
                print("Username telah ada")
            else:
                def password_akun(password):              
                    data=password
                    if len(data)>=8:
                        data1=data
                        hasil=True
                    else:
                        hasil=False
                        print("Minimal 8 karakter")
                    if hasil==True:
                        simpan=[]
                        for i in range(len(data1)):
                            if 'Z'>=data1[i] >='A' or 'z'>=data1[i]>='a':
                                simpan.append(i)
                        if bool(simpan) is not False:
                            data2=data1
                            hasil=True
                        else:
                            hasil=False
                            print('Harus ada karakter huruf')
                        if hasil ==True:
                            simpan2=[]
                            for i in range(len(data2)):
                                if '0'<= data2[i]<='9':
                                    simpan2.append(data2[i])
                            if bool(simpan2) is not False:
                                if berdasarkan[siapa_yang_sign_up]=="NIP":
                                        print('berhasil')
                                        with open('data_login_dan_signup_pustakawan.csv','a') as signup:
                                            signup_simpan=username,","+password,","+str(nip),'\n'
                                            signup.writelines(signup_simpan) 
                                else:
                                        with open('data_login_dan_signup_peminjam.csv','a') as signup:
                                            signup_simpan=username,","+password,","+str(nip),'\n'
                                            signup.writelines(signup_simpan) 
                            else:
                                print("Harus ada karakter angka")
                password_akun(input("Ketik password: "))
            time.sleep(1)
            os.system("CLS")
    except:
        print("Anda salah ketik")