from ast import Str
from database import Database as db
from prettytable import PrettyTable

class Barang:
    def __init__(self):
        self.__kode_barang = None
        self.__nama_barang_barang = None
        self.__jenis_barang = None
        self.__harga = None
        self.__info = None
        self.db = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info == None):
            return f'Kode barang: {self.__kode_barang}\nnama_barang barang: {self.__nama_barang_barang}\nJenis barang: {self.__jenis_barang}\nHarga: {self.__harga}'
        else:
            return self.__info
    
    @property
    def kode_barang(self):
        return self.__kode_barang

    @kode_barang.setter
    def kode_barang(self, value):
        self.__kode_barang = value
    
    @property
    def nama_barang(self):
        return self.__nama_barang

    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value
    
    @property
    def jenis_barang(self):
        return self.__jenis_barang

    @jenis_barang.setter
    def jenis_barang(self, value):
        self.__jenis_barang = value
    
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
        
    def save(self):
        self.db = db()
        sql = F'INSERT INTO barang (kode_barang,nama_barang,jenis_barang,harga) VALUES (\'{self.__kode_barang}\',\'{self.__nama_barang}\',\'{self.__jenis_barang}\',\'{self.__harga}\')'
        self.affected = self.db.insert(sql)
        self.db.disconnect
        return self.affected
        
    def update(self, kode_barang):
        self.db = db()
        val = (kode_barang,self.__nama_barang,self.__jenis_barang,self.__harga, kode_barang)
        sql = 'UPDATE barang SET kode_barang = %s, nama_barang = %s, jenis_barang = %s, harga = %s WHERE kode_barang = %s;'
        self.affected = self.db.update(sql, val)
        self.db.disconnect
        return self.affected
        
    def delete(self, kode_barang):
        self.db = db()
        sql="DELETE FROM barang WHERE kode_barang='" + str(kode_barang) + "';"
        self.affected = self.db.delete(sql)
        self.db.disconnect
        return self.affected
        
    def getByKodeBarang(self, kode_barang):
        self.db = db()
        sql="SELECT * FROM barang WHERE kode_barang='" + kode_barang + "';"
        self.result = self.db.findOne(sql)
        if(self.result != None):
            self.__kode_barang = self.result[1]
            self.__nama_barang = self.result[2]
            self.__jenis_barang = self.result[3]
            self.__harga = self.result[4]
            self.affected = self.db.cursor.rowcount
        else:
            self.__kode_barang = ''
            self.__nama_barang = ''
            self.__jenis_barang = ''
            self.__harga = ''
            self.affected = 0
            self.affected = 0
            self.db.disconnect
            return self.result

    def getAllData(self):
        self.db = db()
        sql = 'SELECT * FROM barang;'
        self.result = self.db.findAll(sql)
        if(self.result == 0):
            return self.result
        else:
            tabelBarang = PrettyTable(["ID Barang", "Kode Barang", "Nama Barang", "Jenis Barang", "Harga"])
            for res in self.result:
                tabelBarang.add_row([str(res[0]),res[1],res[2],res[3],str(res[4])])
            print(tabelBarang)
