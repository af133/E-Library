# import pandas as pd
# # 
# def profil_user(nim):
#     try:
#         all_data = pd.read_csv('data_peminjam.csv', delimiter=",", dtype={'NIM': str})
#     except FileNotFoundError:
#         return "File 'data_peminjam.csv' tidak ditemukan."

#     profil_user = all_data.loc[all_data['NIM'] == nim]
#     if profil_user.empty:
#         return f"Pengguna dengan NIM {nim} tidak ditemukan."

#     print(profil_user)
    
#     kolom_pilihan = {
#         '1': 'Nama Mahasiswa',
#         '2': 'Tanggal Lahir',
#         '3': 'Nomor Telepon',
#         '4': 'Fakultas',
#         '5': 'Jurusan'
#     }

#     while True:
#         print('''
#     Mau Ngedit Apa:
#     1. Nama Mahasiswa
#     2. Tanggal Lahir
#     3. Nomor Telepon
#     4. Fakultas
#     5. Jurusan
#     ''')
#         pilihan_edit = input('Pilih nomor: ')
#         if pilihan_edit in kolom_pilihan:
#             data_baru = input('Masukkan data barunya: ')
#             kolom = kolom_pilihan[pilihan_edit]
#             all_data.loc[all_data['NIM'] == nim, kolom] = data_baru
#             all_data.to_csv('data_peminjam.csv', index=False)
#             print("Data berhasil diperbarui.")
            
#             updated_data = all_data.loc[all_data['NIM'] == nim]
#             print(updated_data)
#         else:
#             print('Pilihan tidak valid, ulangi lagi.')

#         selesai_edit = input("\nApakah Anda selesai mengedit data? (y/t): ")
#         if selesai_edit.lower() == 'y':
#             break

import flask as f
import tabulate as tb
