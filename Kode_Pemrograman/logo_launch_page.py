import time
import os
import pandas as pd

data_peminjam= pd.read_csv('data_peminjam.csv')
data_pustakawan=pd.read_csv('data_pustakawan.csv')
data=data_pustakawan,data_peminjam
dt=['Pustakawan','User']
def logo_launch_page():
    os.system('cls')
    head_a=(r"     ___             _    __    _    __         ")
    head_b=(r"    |___  __ |    | | )  |__)  /_\  |__)  \_/   ")
    head_c=(r"    |___     |___ | |_ ) |  \ /   \ |  \   |    ")
    head_d=(r"                                                ")
    head_e=(r"                Selamat Datang                  ")
    header= '+'+'='*48+'+'+'\n'+\
            '|'+head_a+'|'+'\n'+\
            '|'+head_b+'|'+'\n'+\
            '|'+head_c+'|'+'\n'+\
            '|'+head_d+'|'+'\n'+\
            '|'+head_e+'|'+'\n'+\
            '|'+'='*48+'|'+'\n'
    print(header)
    time.sleep(2)
    input("Tekan [ENTER] untuk melanjutkan")      
    

def loading():
    logo_launch_page()
    os.system("cls")
    nol =' ______________________'
    nol1='|                      |'
    satu=' ______________________'
    dua='|/////                 |'

    tiga= ' ______________________'
    empat='|////////              |'
    lima=' ______________________'
    enam='|//////////////        |'
    tujuh=' ______________________'
    delapan='|//////////////////////|'
    headernol=nol+'\n'+nol1
    header=satu+'\n'+dua
    header2=tiga+'\n'+empat
    header3=lima+'\n'+enam
    header4=tujuh+'\n'+delapan
    simpan=[headernol,header,header2,header3,header4]
    for i in range(5):
        simpan1=simpan[i]
        print((simpan1))
        print('loading'.center(24))
        time.sleep(1)
        os.system("cls")
def logo1(sebagai,target,indeks):
    data2=data[int(sebagai)]
    indeks_baru=0
    nim_or_nip=['NIP','NIM']
    for indeks in data2[nim_or_nip[sebagai]]:
        if indeks==target:
            ditemukan=indeks_baru
        indeks_baru+=1
    nama=["Nama Pustakawan","Nama Mahasiswa"]
    nama1=nama[sebagai]
    data1='+'+'='*48+'+'+'\n'+\
            'Selamat datang di perpustakaan'.center(50)+'\n'+\
                f'{dt[int(sebagai)]} {data2[nama1][ditemukan]}'.center(50)+'\n'+\
            '+'+'='*48+'+'+'\n'
    print(data1)
    time.sleep(2)

def logo_close():
    
    pass
