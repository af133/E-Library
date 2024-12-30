import pandas as pd
isi_buku=['NISBN','Judul Buku','Nama Pengarang','Jumlah Buku','Penerbit','Genre']
import os
import time
from tabulate import tabulate
from logo_launch_page import logo1
def pencarian_buku1():
    print("[1] NISBN\n[2] Judul Buku\n[3] Nama Pengarang\n[5] jumlah Stok\n[5] Penerbit\n[6] Genre")
    berdasarkan=isi_buku[int(input("Pilih pencarian berdasarkan [Ketik Nomor]: "))-1]
    target=(input(f'Ketik {berdasarkan}: '))
    if berdasarkan=='NISBN':
        target=int(target)
    from pencarian_penambahan_penghapusan_dan_penditan_buku import pencarian
    indeks= pencarian(berdasarkan,target)
    simpan=[]
    for i in indeks:
        simpan.append(baca_buku.iloc[i])
    tabel=tabulate(pd.DataFrame(simpan),headers='keys',showindex=False,tablefmt='fancy_gridy') 
    print(tabel)   
    input()

baca_buku= pd.read_csv('data_buku_perpustakaan.csv')
def halaman_peminjam(nilai,nim,indeks):
            while True:
                logo1(nilai,nim,indeks)
                print('[1] Pecarian Buku\n[2] Edit Profil\n[3] Status Peminjaman\nTekan [a] untuk berhenti')
                pilih=(input("Pilih: "))
                if pilih=="1": # Pencarian buku
                    pencarian_buku1()
                elif  pilih =='2': # Edit profil
                    from edit_profil_peminjam import profil_user
                    profil_user(str(nim))
                    os.system(input())
                    os.system("CLS")
                elif pilih =="3": # Status Pinjam & Pengembalian buku
                    from lihat_stastus_peminjaman import sub_fitur
                    sub_fitur(str(nim))
                    os.system("CLS")
                elif pilih=='a':
                     break
                else:
                     print("Maaf anda salah ketik")
                     time.sleep(1)
                     os.system("cls")
                       
                
