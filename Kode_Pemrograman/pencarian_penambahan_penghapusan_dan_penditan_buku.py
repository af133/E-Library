import tabulate
import pandas as pd
import os
import csv
import time
baca_buku= pd.read_csv('data_buku_perpustakaan.csv')
isi_buku=['NISBN','Judul Buku','Nama Pengarang','Jumlah Buku','Penerbit','Genre'] #penampungan header buku
with open ('data_buku_perpustakaan.csv',mode='r',newline='') as baca:
    hasil=csv.reader(baca)
    ditampung=[]
    for row in  hasil:
        ditampung.append(row)
tabel=baca_buku

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# 1. Function sorting

def pengurutan(berdasarkan): # nama fungsi
        simpan_data_sementara=baca_buku[berdasarkan] # menyimpan data 
            # berdasarkan kategorinya [judul/nama pnegarang/nisbn dll]
        jumlah_data=len(simpan_data_sementara) 
        for i in range(jumlah_data): # ini memulai sorting menggunakn selection sort
            indeks_awal=i # meyimpan indeksnya 
            indeks_pembanding=indeks_awal # sebagai pembanding ketika run
            nilai_terbesar=simpan_data_sementara[indeks_awal]
            while indeks_pembanding<jumlah_data:
                if nilai_terbesar>=simpan_data_sementara[indeks_pembanding]: # perkondisiannya 
                    nilai_terbesar=simpan_data_sementara[indeks_pembanding]
                    indeks_baru=indeks_pembanding # indeks yang diperlukan nanti saat soting
                indeks_pembanding+=1
            baca_buku.loc[indeks_awal],baca_buku.loc[indeks_baru]=baca_buku.loc[indeks_baru],baca_buku.loc[indeks_awal]
                # pertukaran nilai 
        baca_buku.to_csv('data_buku_perpustakaan.csv',index=False)
        # simpan secara permanen ke csv
        return False
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# 2. Function penambahan

def tambah_buku():
    pengurutan("NISBN")
    with open ('data_buku_perpustakaan.csv', 'a') as buku:
        nisbn=(input('NISBN: '))
        judul_buku= input('Judul Buku: ')
        nama_pengarang= input('Nama Pengarangr: ')
        jumlah_buku= input('Jumlah Buku: ')
        penerbit=input('Penerbit: ')
        genre=input('Genre: ')
        simpan_data_baru_buku=f"{nisbn},{judul_buku},{nama_pengarang},{jumlah_buku},{penerbit},{genre}\n"
        buku.writelines(simpan_data_baru_buku)
        print('Berhasil')
    time.sleep(1)
    os.system("CLS")
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# 3. Function Pencarian

def pencarian(berdasarkan,target): # digunakan untuk membantu fungsi lain yang membutuhkan indeksnya
    # misal drop, edit, search book
    pengurutan(berdasarkan) # pertama-pertama akan dieksekusi oleh ini untuk mengurutkan dulu

    # karena binary search butuh diurutkan
    kiri=0
    kanan=len(baca_buku[berdasarkan])-1
    simpan_indeks=[]
    while kiri <= kanan:

        tengah = (kiri + kanan) // 2
        if baca_buku[berdasarkan][tengah] == target:
            simpan_indeks.append(tengah)
            # Mengecek nilai yang sama pada sebelah kiri dari tengah
            kiri1 = tengah - 1
            while kiri1 >= 0 and baca_buku[berdasarkan][kiri1] == target:
                simpan_indeks.append(kiri1)
                kiri1 -= 1
            # Mengecek nilai yang sama pada sebelah kanan dari tengah
            kanan1 = tengah + 1
            while kanan1 < len(baca_buku[berdasarkan]) and baca_buku[berdasarkan][kanan1] == target:
                simpan_indeks.append(kanan1)
                kanan1 += 1
            return simpan_indeks
        elif baca_buku[berdasarkan][tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# 4. Function Edit

def edit_buku(intput_kategori_untuk_pencarian): 
    print(tabulate.tabulate(ditampung, tablefmt="heavy_grid"))
    data=["NISBN","Judul Buku","Nama Pengarang","Penerbit","Genre"]
    dicari=input(f'Ketik {data[intput_kategori_untuk_pencarian-1]}: ')
    berdasarkan=data[(intput_kategori_untuk_pencarian)-1]
    if intput_kategori_untuk_pencarian-1==0: 
        dicari=int(dicari)
    indeks=pencarian(berdasarkan,dicari)
    try:
            def pengeditan_lebih_lanjut(indeks):
                for i in range(len(isi_buku)):
                    yes=input(f"Apakah {isi_buku[i]} salah (y/t)? ") 
                    if yes=='y':
                        perbaiki=input("Perbaiki: ")
                        if isi_buku[i]=='NISBN' or isi_buku[i]=="Jumlah Buku":
                            perbaiki=int(perbaiki)
                        baca_buku.loc[indeks,isi_buku[i]]=perbaiki
            header=["NO","NISBN","Judul Buku","Nama Pengarang","Jumlah Buku","Penerbit","Genre"]
            menampung_indeks_pencarian=[]
            indeks_ditampung=[]
            no=0         
            for j in indeks:
                    no+=1
                    row =[no]+baca_buku.iloc[j].tolist()
                    menampung_indeks_pencarian.append(row)
                    indeks_ditampung.append(j)
            print(tabulate.tabulate(menampung_indeks_pencarian,headers=header,tablefmt='fancy_grid'))
            nilai=(input("Ketik No buku yang akan diedit ")) 
            try:
                    j=indeks_ditampung[int(nilai)-1]
                    pengeditan_lebih_lanjut(j) 
                    time.sleep(1)
                    os.system("CLS")
            except:
                        print("Anda salah ketik")
                        time.sleep(1)
                        os.system("CLS")
            baca_buku.to_csv('data_buku_perpustakaan.csv',index=False)
            pengurutan(berdasarkan)
            os.system("CLS")
    except:
        if indeks==-1 :
            print("Buku tidak ditemukan")

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# 5. Function Hapus
def hapus_buku():
    data_baru_buku = pd.read_csv('data_buku_perpustakaan.csv')
    print(data_baru_buku.to_string(index=False))
    nisbn_dicari = input("Ketik NISBN : ")
    try:
        nisbn_dicari = int(nisbn_dicari)
        index = data_baru_buku[data_baru_buku['NISBN'] == nisbn_dicari].index[0]
        data_baru_buku = data_baru_buku.drop(index)
        data_baru_buku.to_csv('data_buku_perpustakaan.csv', index=False)
        print("Data berhasil dihapus")
    except IndexError:
        print("Data tidak ditemukan")
    except ValueError:
        print("Masukkan NISBN dalam bentuk angka")
