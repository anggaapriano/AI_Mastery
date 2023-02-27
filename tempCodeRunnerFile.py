from pegawai import pegawai

pegawai1 = pegawai("Angga", "CEO", 15000000)
pegawai2 = pegawai("Nafisa", "Manager", 10000000)

pegawai1.display_pegawai()
pegawai2.display_pegawai()

pegawai1.gaji_tahun()
pegawai2.gaji_tahun()

print("Total pegawai :", pegawai.jml_pegawai)