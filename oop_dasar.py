#Class Pegawai
class pegawai :
    jml_pegawai = 0
    def __init__(self, nama, jabatan, gaji=0):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        pegawai.jml_pegawai += 1

    def display_jumlah_pegawai(self):
        print("Jumlah pegawai :", pegawai.jml_pegawai)
    
    def display_pegawai(self):
        print("Nama :", self.nama, "jabatan :", self.jabatan, "gaji :", self.gaji)

    def gaji_tahun(self):
        gaji_tahun = self.gaji * 12
        print("Nama :", self.nama, "gaji(tahun) :", gaji_tahun)

from pegawai import pegawai

pegawai1 = pegawai("Angga", "CEO", 15000000)
pegawai2 = pegawai("Nafisa", "Manager", 10000000)

pegawai1.display_pegawai()
pegawai2.display_pegawai()

pegawai1.gaji_tahun()
pegawai2.gaji_tahun()

print("Total pegawai :", pegawai.jml_pegawai)