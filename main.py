from database import Database
from barang import Barang


class Main:
    def __init__(self):
        try:
            while True:
                print('\n======= Aplikasi CRUD Barang =======')
                print('0. Keluar Program')
                print('1. Tampil Semua Data Barang')
                print('2. Tambah Data Barang')
                print('3. Cari Data Barang')
                print('4. Update Data Barang')
                print('5. Hapus Data Barang')
                menu = int(input('Masukkan Menu: '))
                if(menu == 0):
                    break
                elif(menu == 1):
                    print('\n')
                    self.allData()
                elif(menu == 2):
                    print('\n')
                    self.insert()
                elif(menu == 3):
                    print('\n')
                    self.search()
                elif(menu == 4):
                    print('\n')
                    self.update()
                elif(menu == 5):
                    print('\n')
                    self.delete()
                else:
                    print('Keyowrd salah!')
        except:
            print('Keyowrd salah!')
            Main()

    def search(self):
        try:
            print('===== CARI DATA BARANG =====')
            kode = input('Masukkan Kode Barang: ')
            print(kode)
            brg = Barang()
            result = brg.getByKodeBarang(kode)
            value = brg.affected
            if(value != 0):
                print('- DATA BARANG -')
                print(f'Kode Barang     : {brg.kode_barang}')
                print(f'Nama Barang     : {brg.nama_barang}')
                print(f'Jenis Barang    : {brg.jenis_barang}')
                print(f'Harga           : {brg.harga}')
            else:
                print('Data Barang Tidak Ditemukan!')
        except:
            pass

    def insert(self):
        try:
            print('===== TAMBAH DATA BARANG =====')
            brg = Barang()
            kode = input('Masukkan Kode Barang: ')
            nama = input('Masukkan Nama Barang: ')
            jenis = input('Masukkan Jenis Barang: ')
            harga = input('Masukkan Harga: ')
            brg.kode_barang = kode
            brg.nama_barang = nama.capitalize()
            brg.jenis_barang = jenis.capitalize()
            brg.harga = harga
            simpan = brg.save()
            if(simpan > 0):
                print('Data Barang Disimpan!')
            else:
                print('Data Barang Gagal Disimpan!')
            brg.getAllData()
        except:
            pass

    def update(self):
        try:
            print('===== UBAH DATA BARANG =====')
            kode = input('Masukkan Kode Barang: ')
            brg = Barang()
            result = brg.getByKodeBarang(kode)
            value = brg.affected
            if(value != 0):
                print('- DATA BARANG -')
                print(f'Kode Barang     : {brg.kode_barang}')
                print(f'Nama Barang     : {brg.nama_barang}')
                print(f'Jenis Barang    : {brg.jenis_barang}')
                print(f'Harga           : {brg.harga}')
            else:
                print('Maaf data tidak ditemukan!')
            print('\n')
            ubah = input('Apakah anda ingin merubah data (y/n)? ')
            ubah = ubah.lower()
            namaBaru = input(f'Masukkan Nama Barang Baru ({brg.nama_barang}): ')
            jenisBaru = input(f'Masukkan Jenis Barang Baru ({brg.jenis_barang}): ')
            hargaBaru = input(f'Masukkan Harga Baru ({brg.harga}): ')
            
            if(namaBaru == ''):
                brg.nama_barang = brg.nama_barang
            else:
                brg.nama_barang = namaBaru.capitalize()
        
            if(jenisBaru == ''):
                brg.jenis_barang = brg.jenis_barang
            else:
                brg.jenis_barang = jenisBaru.capitalize()
                
            if(hargaBaru == ''):
                brg.harga = brg.harga
            else:
                brg.harga = hargaBaru
                
            simpan = brg.update(kode)
            if(simpan > 0):
                print('Data Barang Diperbarui')
            else:
                print('Data Barang Gagal Diperbarui')
            brg.getAllData()
        except:
            pass

    def delete(self):
        try:
            print('===== HAPUS DATA BARANG =====')
            kode = input('Masukkan Kode Barang: ')
            brg = Barang()
            simpan = brg.delete(kode)
            if(simpan > 0):
                print('Data Barang Dihapus')
            else:
                print('Data Barang Gagal Dihapus')
            brg.getAllData()
        except:
            pass
    
    def allData(self):
        brg = Barang()
        brg.getAllData()
     
if __name__ ==  '__main__':
    app = Main()