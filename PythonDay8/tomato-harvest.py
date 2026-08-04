print("SMART TOMATO HARVEST")
print("====================")

tomato_colors = ["hijau", "kuning kemerahan", "merah"]
check_history = []


def tampilkan_warna():
    print("\nPILIHAN WARNA TOMAT")
    print("--------------------")

    for color in tomato_colors:
        print("-", color)


def cek_panen():
    print("\nCEK KESIAPAN PANEN")
    print("-------------------")

    tampilkan_warna()

    color = input("Masukkan warna tomat: ").lower()
    texture = input("Masukkan tekstur tomat (keras/lunak): ").lower()

    if color == "hijau":
        result = "Tomat masih muda dan belum siap dipanen."

    elif color == "kuning kemerahan" and texture == "keras":
        result = "Tomat siap dipanen untuk dikirim."

    elif color == "merah" and texture == "keras":
        result = "Tomat siap dipanen untuk pasar dekat."

    elif color == "merah" and texture == "lunak":
        result = "Tomat terlalu matang dan harus segera digunakan."

    else:
        result = "Kondisi tomat tidak dikenali."

    print("\nHASIL PEMERIKSAAN")
    print("-------------------")
    print(result)

    check_history.append(result)


def tampilkan_riwayat():
    print("\nRIWAYAT PEMERIKSAAN")
    print("-------------------")

    if len(check_history) == 0:
        print("Belum ada pemeriksaan.")

    else:
        for result in check_history:
            print("-", result)


while True:
    print("\nMENU UTAMA")
    print("==========")
    print("1. Cek kesiapan panen")
    print("2. Tampilkan warna tomat")
    print("3. Tampilkan riwayat")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        cek_panen()

    elif pilihan == "2":
        tampilkan_warna()

    elif pilihan == "3":
        tampilkan_riwayat()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")