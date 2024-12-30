import pandas as pd
import time
from datetime import datetime
from tabulate import tabulate

import datetime as tanggal
import os
baca_buku= pd.read_csv('data_buku_perpustakaan.csv')
data_peminjam=pd.read_csv('data_peminjam.csv')
histori_peminjaman=pd.read_csv('histori_peminjaman.csv')
header=["NO","NISBN","Judul Buku","Nama Pengarang","Jumlah Buku","Penerbit","Genre"]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Function sorting

def pengurutan__data_peminjam(berdasarkan,nilai):
    simpan=data_peminjam,baca_buku,histori_peminjaman
    simpan1=simpan[nilai]
    simpan_data_sementara=simpan1[berdasarkan] # menyimpan data 
    # berdasarkan kategorinya [NIM/Nama Mahasiswa/ dll]
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
        if nilai==0:
            data_peminjam.loc[indeks_awal],data_peminjam.loc[indeks_baru]=data_peminjam.loc[indeks_baru],data_peminjam.loc[indeks_awal]
        # pertukaran nilai atau pembenahan nilai
        elif nilai==1:
            baca_buku.loc[indeks_awal],baca_buku.loc[indeks_baru]=baca_buku.loc[indeks_baru],baca_buku.loc[indeks_awal]

        else:
            
            histori_peminjaman.loc[indeks_awal],histori_peminjaman.loc[indeks_baru]=histori_peminjaman.loc[indeks_baru],histori_peminjaman.loc[indeks_awal]
    if nilai==0:
        data_peminjam.to_csv('data_peminjam.csv',index=False)
    elif nilai==1:
        baca_buku.to_csv('data_buku_perpustakaan.csv',index=False)
    else:
        histori_peminjaman.to_csv('histori_peminjaman.csv',index=False)
    # simpan secara permanen ke csv
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Pencarian

def pencarian_data_peminjam(berdasarkan,target,nilai): # digunakan untuk membantu fungsi lain yang membutuhkan indeksnya
    # misal drop, edit, search book
    pengurutan__data_peminjam(berdasarkan,nilai) # pertama-pertama akan dieksekusi oleh ini untuk mengurutkan dulu
    # karena binary search butuh diurutkan
    simpan=data_peminjam,baca_buku,histori_peminjaman
    simpan1=simpan[nilai]
    kiri=0
    kanan=len(simpan1[berdasarkan])-1
    simpan_indeks=[]
    try:
        while kiri <= kanan:
            tengah = (kiri + kanan) // 2
            if simpan1[berdasarkan][tengah] == target:
                simpan_indeks.append(tengah)
                # Mengecek nilai yang sama pada sebelah kiri dari tengah
                kiri1 = tengah - 1
                while kiri1 >= 0 and simpan1[berdasarkan][kiri1] == target:
                    simpan_indeks.append(kiri1)
                    kiri1 -= 1
                # Mengecek nilai yang sama pada sebelah kanan dari tengah
                kanan1 = tengah + 1
                while kanan1 < len(simpan1[berdasarkan]) and simpan1[berdasarkan][kanan1] == target:
                    simpan_indeks.append(kanan1)
                    kanan1 += 1
                return simpan_indeks
            elif simpan1[berdasarkan][tengah] < (target):
                kiri = tengah + 1
            else:
                kanan = tengah - 1
    except:
            return -1

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Peminjaman
def peminjaman_buku():
    print(tabulate(baca_buku,headers=header,tablefmt='fancy_grid'))
    nim=int(input("Ketik NIM: "))
    indeks_mahasiswa=pencarian_data_peminjam("NIM",(nim),0)
    if bool(indeks_mahasiswa)==False:
        print("Nim tidak ditemukan")
    else:   
        nisbn1=int(input("Ketik nomor buku: "))
        nisbn=baca_buku.loc[nisbn1,"NISBN"]
        indeks_judul=pencarian_data_peminjam("NISBN",(nisbn),1)
        indeks_histori=pencarian_data_peminjam("NIM",(nim),2)
        jumlah=0
        pinjam_buku=int(input("Jumlah Buku: "))
        if pinjam_buku==1:
            kondisi=False 
            if bool(indeks_histori)==True:           
                for judul_dipinjam in indeks_histori:
                    if (baca_buku.loc[indeks_judul[0],'Judul Buku']==histori_peminjaman.loc[judul_dipinjam,'Judul Buku']) and histori_peminjaman.loc[judul_dipinjam,'Status']=='Masih Pinjam' :
                        kondisi=True
            if kondisi is not True:
                tanggal_peminjaman=str(tanggal.date.today())
                def peminjaman_lebih_lanjut(nim_mahasiswa, nama_mahasiswa, nisbn, judul_buku, jumlah_buku, tgl_peminjaman, tgl_pengembalian, status):
                    data_peminjam=f"{nim_mahasiswa},{nama_mahasiswa},{nisbn},{judul_buku},{jumlah_buku},{tgl_peminjaman},{tgl_pengembalian},{status}\n"
                    def pengurangan_buku(): 
                        baca_buku.loc[indeks_judul,'Jumlah Buku']-=int(pinjam_buku)
                        baca_buku.to_csv('data_buku_perpustakaan.csv',index=False)
                        print("Berhasil")
                    with open ('histori_peminjaman.csv','a') as simpan_peminjaman:
                        pengurangan_buku()
                        simpan_peminjaman.writelines(str(data_peminjam))
                if baca_buku.loc[indeks_judul[0],'Jumlah Buku']==0:
                    print("Buku masih dipinjam")
                else:

                    try:
                        for i in indeks_histori:
                            if histori_peminjaman.loc[i,"Status"]=="Masih Pinjam":
                                jumlah+=histori_peminjaman["Jumlah Buku Dipinjam"][i]
                        if jumlah+pinjam_buku<=3:
                            nama_mahasiswa = data_peminjam.loc[indeks_mahasiswa[0],'Nama Mahasiswa']
                            judul_buku = baca_buku.loc[indeks_judul[0],'Judul Buku']
                            
                            peminjaman_lebih_lanjut(str(nim), nama_mahasiswa, str(nisbn), judul_buku, str(pinjam_buku), tanggal_peminjaman, "NUll", "Masih Pinjam")
                        else:
                            print("Maaf hanya bisa minjam 3 buku")
                    except:
                            nama_mahasiswa = data_peminjam.loc[indeks_mahasiswa[0],'Nama Mahasiswa']
                            judul_buku = baca_buku.loc[indeks_judul[0],'Judul Buku']
                            peminjaman_lebih_lanjut(str(nim),nama_mahasiswa, str(nisbn), judul_buku, str(pinjam_buku), tanggal_peminjaman, "NUll", "Masih Pinjam")
            else:
        
                print("Tiap judul hanya bisa pinjam 1 buku")
        else:
            print("Tiap judul hanya bisa pinjam 1 buku tidak dapat lebih")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Pengembalian

def pengembalian():
    nim=int(input("Ketik NIM: "))
    indeks_histori=pencarian_data_peminjam("NIM",(nim),2)
    nisbn=int(input("Ketik NISBN: "))
    indeks_judul=pencarian_data_peminjam("NISBN",(nisbn),1)
    try:
        for i in indeks_histori:
            if histori_peminjaman.loc[i,'Status']=="Masih Pinjam":
                if int(histori_peminjaman.loc[i,'NISBN'])==(nisbn):
                    print(tabulate(pd.DataFrame(histori_peminjaman.iloc[i])))
                    pilih=input('Apakah ini yang dikembalikan (y/t)? ')
                    if pilih.lower()=='y':
                        jumlah=input("Jumlah buku yang dikembalikan: ")
                        def pengembalian_lebih_lanjut():
                            baca_buku.loc[indeks_judul,'Jumlah Buku']+=int(jumlah)
                            histori_peminjaman.loc[i,"Status"]="Telah dikembalikan"
                            histori_peminjaman.loc[i,'Tanggal Pengembalian']=str(tanggal.date.today())
                            baca_buku.to_csv('data_buku_perpustakaan.csv',index=False)
                            histori_peminjaman.to_csv('histori_peminjaman.csv',index= False)
                        tanggal_pengembalian=(datetime.today())
                        tanggal_pinjam=histori_peminjaman.loc[i,'Tanggal Peminjaman']
                        tanggal_peminjaman = datetime.strptime(tanggal_pinjam,'%Y-%m-%d')
                        hari = ((tanggal_pengembalian)-(tanggal_peminjaman)).days
                        if hari>7:
                            print(f"Anda mendapatkan denda Rp {(hari-7)*500}")
                            pengembalian_lebih_lanjut()
                        else:
                            print("Anda tidak mendapatkan denda")
                            pengembalian_lebih_lanjut()
    except:
            print("Tidak ditemukan")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5 Tambah Data Peminjam

def tambah_data_peminjam():
    pengurutan__data_peminjam("NIM",0)
    with open ('data_peminjam.csv', 'a') as buku:
        # membuka csv dnegan a (append) sehingga bisa menambah data baru tanpa menghilangkan data 
        # sebelumnya. Jika W maka tambah dara baru+hapus data sebelumnya
        NIM=int(input('NIM: '))
        nama_peminjam= input('Nama Mahasiswa: ')
        tanggal_lahir= input('Tanggal lahir: ')
        no_tlpn=input('No telepon: ')
        fakultas=input('Fakultas: ')
        jurusan=input("Jurusan: ")
        # NIM,Nama Mahasiswa,Tanggal Lahir,Nomor Telepon,Fakultas,Jurusan
        simpan_data_baru=f"{NIM},{nama_peminjam},{tanggal_lahir},{no_tlpn},{fakultas},{jurusan}\n"
        buku.writelines(simpan_data_baru)
        print('Berhasil')
    time.sleep(1)
    os.system("CLS")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6 Perpanjangan Peminjaman Buku

def perpanjangan_pinjam_buku():
    nim=int(input("Ketik NIM: "))
    indeks_histori=pencarian_data_peminjam("NIM",(nim),2)
    data=[]
    indeks_=[]
    if bool(indeks_histori)==True:
        no=1
        slice=0
        for i in indeks_histori:
                if histori_peminjaman.loc[i,'Status']=='Masih Pinjam':
                    Judul_Buku=histori_peminjaman.loc[i,'Judul Buku']
                    Jumlah_Buku=histori_peminjaman.loc[i,'Jumlah Buku Dipinjam']
                    Tanggal_Peminjaman=histori_peminjaman.loc[i,'Tanggal Peminjaman']
                    buku=[no,Judul_Buku,Jumlah_Buku,Tanggal_Peminjaman]
                    data.append(buku)
                    indeks_.append(indeks_histori[slice])
                    no+=1
                    slice+=1
                slice+=1
        if bool(data)==True:
            print(tabulate(data,headers=['NO','Judul Buku','Jumlah Dipinjam','Tanggal Peminjaman'],tablefmt='fancy_grid'))
            perpanjang=input("Ketik no buku yang akan diperpanjang: ")
            try:
                indeks=indeks_[int(perpanjang)-1]
                histori_peminjaman.loc[indeks,'Tanggal Peminjaman']=str(tanggal.date.today())
                histori_peminjaman.to_csv('histori_peminjaman.csv',index= False)
                print("Berhasil")
                time.sleep(1)
                os.system("CLS")
            except:
                 print("Data tidak ditemukan")
    else:
        print("Data tidak ditemukan")
        
