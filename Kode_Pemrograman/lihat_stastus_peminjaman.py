import csv
import pandas as pd
from datetime import datetime
import os
from tabulate import tabulate
def clear_screen():
    os.system('cls')
    
def read_csv(nama_file):
    data = []
    with open(nama_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            data.append(row)
    return data

def selection_sort(data, index):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j][index] < data[min_idx][index]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def binary_search(data, target, index):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][index] < target:
            low = mid + 1
        elif data[mid][index] > target:
            high = mid - 1
        else:
            return mid
    return -1

def menghitung_denda(peminjaman, pengembalian):
    hari_ini = datetime.now().date()
    tanggal_peminjaman = pd.to_datetime(peminjaman).date()
    
    if pengembalian and pengembalian != 'NUll':
        tanggal_pengembalian = pd.to_datetime(pengembalian).date()
        waktu = (tanggal_pengembalian - tanggal_peminjaman).days
    else:
        waktu = (hari_ini - tanggal_peminjaman).days
        tanggal_pengembalian = None
    
    if waktu > 7:
        hari_denda = waktu - 7
        akumulasi = hari_denda * 500
        status = f"Denda {akumulasi} rupiah"
        if not tanggal_pengembalian:
            status += " dan masih berjalan"
    else:
        akumulasi = 0
        status = "Denda 0 rupiah"
    return akumulasi, status

def tampilkan_data(data, nim, nama):
    selection_sort(data, 0)  
    index = binary_search(data, nim, 0)
    if index != -1:
        df = pd.DataFrame(columns=[
            "NIM", "Nama Peminjam", "NISBN", "Judul Buku", 
            "Jumlah Buku Dipinjam", "Tanggal Peminjaman", 
            "Tanggal Pengembalian", "Status", "Denda"
        ])
        for i in range(len(data)):
            if data[i][0] == nim and data[i][1].lower() == nama.lower():
                pengembalian = data[i][6] if data[i][6] != 'NUll' else None
                status = menghitung_denda(data[i][5], pengembalian)
                row_data = data[i] + [status]
                df.loc[len(df)] = row_data
        if not df.empty:
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
        else:
            print("Data tidak ditemukan.")
    else:
        print("Data tidak ditemukan.")

def sub_fitur():
    nama_file = 'histori_peminjaman.csv'
    data = read_csv(nama_file)
    while True:
        clear_screen()
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        tampilkan_data(data, nim, nama)
        ulang = input("\nApakah Anda ingin melihat status peminjaman lagi? (y/n): ")
        if ulang.lower() != 'y':
            break
