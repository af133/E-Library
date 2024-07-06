import pandas as pd
from tabulate import tabulate
isi_buku=['NISBN','Judul Buku','Nama Pengarang','Jumlah Buku','Penerbit','Genre']
import os
# from logo_launch_page import logo1
import time
baca_buku= pd.read_csv('data_buku_perpustakaan.csv')
# Bagian yang menampung fitur-fitur pustakawan
# from penghapusan_pengeditan_pencarian_dan_penambahan_buku import mengurutkan_buku_untuk_fitur_pengurutan_pengeditan_dan_penghapusan_buku
# Bagian pemanggilan function di file py penghapusan_pengeditan_pencarian_dan_penambahan_buku
selesai=False
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
# pengelolaan buku

def peminjaman_buku1():
    from peminjaman_dan_pengembalian import peminjaman_buku
    peminjaman_buku()
def pengembalian1():
    from peminjaman_dan_pengembalian import pengembalian
    pengembalian()
def tambah_buku1():
    from pencarian_penambahan_penghapusan_dan_penditan_buku import tambah_buku
    tambah_buku()
def hapus_buku1():
    from pencarian_penambahan_penghapusan_dan_penditan_buku import hapus_buku
    hapus_buku()
def edit_buku1():
    from pencarian_penambahan_penghapusan_dan_penditan_buku import edit_buku
    edit_buku(int(input('Plih pencarian kategori untuk pengeditan: ')))
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
def perpanjagan_pinjam_buku1():
    from  peminjaman_dan_pengembalian import perpanjangan_pinjam_buku
    perpanjangan_pinjam_buku()
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

# pengelolaan pustakawan

def tambah_data_pustakawan1():
    from lihat_tambah_hapus_dan_edit_pustakwan import tambah_data_pustakawan
    tambah_data_pustakawan() # penambahan data pustakawan
def hapus_data_pustakawan1():
        from lihat_tambah_hapus_dan_edit_pustakwan import hapus_data_perpustakaan
        hapus_data_perpustakaan()
def edit_data_pustakawan1():
    from lihat_tambah_hapus_dan_edit_pustakwan import edit_profil_perpustakawan
    edit_profil_perpustakawan()
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

# pengelolaan peminjam
def tambah_data_peminjam1():
    from peminjaman_dan_pengembalian import tambah_data_peminjam
    tambah_data_peminjam()
def sign_up1(berdasarkan):
    from sign_up import sign_up
    sign_up(berdasarkan)
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

# penampungan segala pengelolaan

def halaman_utama_pustakawan(sebagai,nip,indeks):
    while not selesai:
            from logo_launch_page import logo1
            logo1(sebagai,nip,indeks)
            print('[1] Pengelolaan Buku')
            print('[2] Pengelolaan Data Pustakawan')
            print('[3] Pengelolaan Data Peminjam')
            print('Tekan [ENTER] untuk keluar')
            pilih=input("Pilih: ")
            if pilih=="1": # Pusat pengololaan buku
                    print('[1] Peminjaman Buku')
                    print('[2] Pengembalian Buku')
                    print('[3] Tambah Data Buku')
                    print('[4] Hapus Data Buku')
                    print('[5] Pengeditan Data Buku')
                    print('[6] Pencarian Data Buku')
                    print('[7] Perpanjangan Pinjam Buku')
                    print('Tekan [ENTER] untuk keluar')
                    pilih_lagi=input('Pilih: ')
                    if pilih_lagi=="1": # done peminjaman buku
                        peminjaman_buku1()
                        time.sleep(1)
                        os.system('CLS')
                    elif pilih_lagi=="2": # proses data pengembalian (dalam proses)
                        pengembalian1()
                        time.sleep(1)
                        os.system('CLS')
                    elif pilih_lagi=='3': # done tambah buku 
                        tambah_buku1()
                        time.sleep(1)
                        os.system('CLS')
                    elif pilih_lagi=='4': # done hapus buku 
                        hapus_buku1()
                        time.sleep(1)
                        os.system('CLS')
                    elif pilih_lagi =='5': # done pengeditan buku 
                        print("[1] NISBN\n[2] Judul Buku\n[3] Nama Pengarang\n[4] Penerbit\n[5] Genre")
                        edit_buku1()
                        time.sleep(1)
                        os.system('CLS')
                    elif pilih_lagi =='6': # done proses pencarian buku 
                        pencarian_buku1()
                        time.sleep(1)
                        os.system("CLS")
                    elif pilih_lagi=='7': # done perpanjangan peminjaman buku 
                        perpanjagan_pinjam_buku1()
                        time.sleep(1)
                        os.system("CLS")
            elif pilih =="2" : # berhubungan dengan profil pustakawan 
                # edit, tambah, dan hapus data pustakawan
                    # fungsi yang berada di file lihat_tambah_hapus_dan_edit_pustakwan
                        from lihat_tambah_hapus_dan_edit_pustakwan import lihat_data_pustakawan
                        lihat_data_pustakawan() # pemanggilan fungsi yang menampilkan 
                    # data profil pustakawan
                        print('[1] Tambah Data Pustakawan\n[2] Hapus Data Pustakawan\n[3] Edit Profil Pustakawan') 
                        pililah=input('Pilih: ')
                        if pililah =="1": # tambah data pustakawan
                            tambah_data_pustakawan1() # penambahan data pustakawan
                            time.sleep(1)
                            os.system('CLS')
                        elif pililah =="2":  # hapus data pustakawan
                            hapus_data_pustakawan1()
                            time.sleep(1)
                            os.system('CLS')
                        elif pililah =='3': # edit data pustakawan
                            edit_data_pustakawan1()
                            time.sleep(1)
                            os.system('CLS')
                        else:
                             os.system("CLS")
                             print("Kembali di halaman utama")
                             time.sleep(1)
                             os.system("CLS")
                    
            elif pilih=='3':
                print("[1] Pengisian biodata peminjam\n[2] Pembuatan aku peminjam\nTekan [Entter] untuk keluar")
                pilih_lagi=(input('Pilih: '))
                if pilih_lagi=='1':
                    tambah_data_peminjam1()
                    time.sleep(1)
                    os.system('CLS')
                elif pilih_lagi=='2':
                    sign_up1(1)
                    time.sleep(1)
                    os.system('CLS')
            
            else: # keluar dari sistem
                selesai is True
                break
            os.system("cls")
