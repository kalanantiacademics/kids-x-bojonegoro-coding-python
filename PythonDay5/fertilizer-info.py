print("INFORMASI JENIS PUPUK")
print("==========================")
print("1. Pupuk Kompos")
print("2. Pupuk Kandang")
print("3. Pupuk NPK")
print("4. Pupuk Urea")

pilihan = int(input("Pilih jenis pupuk (1-4): "))

if pilihan == 1:
    print("PUPUK KOMPOS")
    print("Pupuk kompos dibuat dari bahan organik yang telah membusuk.")
    print("Contoh: daun kering, sisa sayuran, dan rumput.")
    print("Manfaat: memperbaiki kondisi tanah dan menambah bahan organik.")
elif pilihan == 2:
    print("PUPUK KANDANG")
    print("Pupuk kandang dibuat dari kotoran hewan yang telah diolah.")
    print("Contoh: kotoran sapi, kambing, atau ayam.")
    print("Manfaat: menambah unsur hara dan membuat tanah lebih subur.")
elif pilihan == 3:
    print("PUPUK NPK")
    print("Pupuk NPK mengandung nitrogen, fosfor, dan kalium.")
    print("Nitrogen membantu pertumbuhan daun.")
    print("Fosfor membantu pertumbuhan akar dan bunga.")
    print("Kalium membantu memperkuat tanaman.")
elif pilihan == 4:
    print("PUPUK UREA")
    print("Pupuk urea mengandung nitrogen dalam jumlah tinggi.")
    print("Manfaat: membantu pertumbuhan batang dan membuat daun lebih hijau.")
    print("Pupuk urea harus digunakan sesuai takaran agar tanaman tidak rusak.")
else:
    print("Pilihan tidak tersedia.")
    print("Masukkan angka dari 1 sampai 4.")