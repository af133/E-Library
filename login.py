import pandas as pd
import os
import time
selesai=False
data_login_perpustakawan =pd.read_csv('data_login_dan_signup_pustakawan.csv') 
data_login_peminjam=pd.read_csv('data_login_dan_signup_peminjam.csv')
def login_peminjam(username,password):
        for i,peminjam in enumerate(data_login_peminjam['username']):
            if username==peminjam:
                indeks=i
                hasil=True
                break
            hasil=False
        if hasil==True:
            if password==data_login_peminjam['password'][indeks]:
                return '2',data_login_peminjam.loc[indeks,'NIM']
        return False
    
def login_perpustakawan(username,password):
        for i,perpustakaan in enumerate (data_login_perpustakawan['username']):
                if username==perpustakaan:
                    indeks=i
                    hasil1=True
                    break
                hasil1=False
        if hasil1==True: 
                if password==data_login_perpustakawan['password'][indeks]:
                    return '1',data_login_perpustakawan.loc[indeks,'NIP']
        return False