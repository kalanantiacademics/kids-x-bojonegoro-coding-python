colors = ["merah", "hijau", "kuning", "biru"]

while True:
    print("COLOR LIST MANAGER")
    print("===================")
    print("1. Tambahkan warna")
    print("2. Hapus warna")
    print("3. Tampilkan semua warna")
    print("4. Keluar")

    choice = int(input("Pilih menu (1-4): "))

    if choice == 1:
        new_color = input("Masukkan warna baru: ")
        colors.append(new_color)

        print(new_color, "berhasil ditambahkan.")
    elif choice == 2:
        removed_color = input("Masukkan warna yang ingin dihapus: ")

        if removed_color in colors:
            colors.remove(removed_color)
            print(removed_color, "berhasil dihapus.")
        else:
            print("Warna tidak ditemukan.")
    elif choice == 3:
        print("Daftar warna:", colors)
    elif choice == 4:
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")
        input("Press enter to continue...")