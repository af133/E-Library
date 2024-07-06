import tabulate
import pandas as pd
# Membuka data csv yang menyimpan data pustawakan, ganti pathnya agar bisa membuka 
# datanya. path yang dimaksud = C:/ ... 
data_pustakawan=pd.read_csv('data_pustakawan.csv')
headers=['NIP','Nama Pustakawan','Tanggal Lahir','Nomor Telepon','Jabatan']


#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# MELIHAT PROFIL

def lihat_data_pustakawan(): # ==> melihat profil perpustakawan
   for i in range(1): # menampilkan data perpustakawan 1 kali
        data_pustakawan=pd.read_csv('data_pustakawan.csv')
        tabel=tabulate.tabulate(data_pustakawan,headers=headers,tablefmt="double_grid") # type: ignore [masih mengalami gangguan], tapi bisa
        print(tabel)
#------------------------------------------------------------------------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------------------------------------------------------------------------

# EDIT PROFIL PERPUSTAKAAN

def edit_profil_perpustakawan(): # edit profil perpustakawan
        data_pustakawan = pd.read_csv('data_pustakawan.csv')
        nip_yang_dicari = int(input("Ketik NIP: "))  # melakukan pencarian berdasarkan NIP lalu diedit
        Nip = data_pustakawan['NIP']
        berhasil = False
        for indeks in range(len(Nip)):  # menggunakan linear search
            if nip_yang_dicari == Nip[indeks]:
                berhasil = indeks  # jika ditemukan maka akan menghasilkan indeksnya di perpustakawan
                break
        if berhasil is not False:
            for i in range(5):
                # Proses perbaikan data perpustakawan
                edit = input(f"Apakah {headers[i]} salah? (y/t) ")
                if edit.lower() == 'y':  # Menentukan salah atau tidak (y/t)
                    perbaikan_data = input('Perbarui data: ')
                    if headers[i] == "NIP":  # khusus nip akan menggunakan integer selain itu menggunakan string
                        perbaikan_data = int(perbaikan_data)
                    data_pustakawan.loc[berhasil, headers[i]] = perbaikan_data
                    # penyimpaan ke csv
                    data_pustakawan.to_csv('data_pustakawan.csv', index=False)
        else:
            print('Data tidak ditemukan')
        
#------------------------------------------------------------------------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Hapus data perpustakawan 

def hapus_data_perpustakaan():
        data_pustakawan = pd.read_csv('data_pustakawan.csv')
        nip_yang_dicari = input("Ketik NIP untuk hapus data perpustakawan: ")
        try:
            nip_yang_dicari = int(nip_yang_dicari)
            index = data_pustakawan[data_pustakawan['NIP'] == nip_yang_dicari].index[0]
            data_pustakawan = data_pustakawan.drop(index)
            data_pustakawan.to_csv('data_pustakawan.csv', index=False)
        except IndexError:
            print("Data tidak ditemukan")
        except ValueError:
            print("Masukkan NIP dalam bentuk angka")

#------------------------------------------------------------------------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Tambah data perpustakawan 

def tambah_data_pustakawan():
        nip = input('Nip: ')
        nama_pustakawan = input('Nama pustakawan: ')
        tanggal_lahir = input('Tanggal lahir: ')
        nomor_telepon = input('No telepon: ')
        jabatan = input('Jabatan: ')
        simpan_data_baru_pustakawan = f'{nip},{nama_pustakawan},{tanggal_lahir},{nomor_telepon},{jabatan}\n'
        with open('data_pustakawan.csv', 'a') as pustakawan:
            pustakawan.write(simpan_data_baru_pustakawan)
        pustakawan.close()
        print('Data pustakawan berhasil ditambahkan')
        