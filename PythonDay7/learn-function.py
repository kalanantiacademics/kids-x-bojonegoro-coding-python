def kondisi_tanah_kering():
    print("\nKONDISI TANAH KERING")
    print("====================")
    print("Tanah terlihat pecah-pecah.")
    print("Tanaman membutuhkan tambahan air.")
    print("Petani perlu memeriksa saluran irigasi.")


def kondisi_tanah_lembap():
    print("\nKONDISI TANAH LEMBAP")
    print("====================")
    print("Tanah mengandung cukup air.")
    print("Kondisi tanah baik untuk pertumbuhan tanaman.")
    print("Petani tetap perlu memantau kondisi sawah.")


def kondisi_tanah_basah():
    print("\nKONDISI TANAH TERLALU BASAH")
    print("===========================")
    print("Air terlalu banyak di area sawah.")
    print("Akar tanaman dapat kekurangan udara.")
    print("Petani perlu mengalirkan kelebihan air.")


while True:
    print("\nPILIH INFORMASI KONDISI TANAH")
    print("=============================")
    print("1. Tanah kering")
    print("2. Tanah lembap")
    print("3. Tanah terlalu basah")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan (1-4): "))

    if pilihan == 1:
        kondisi_tanah_kering()
    elif pilihan == 2:
        kondisi_tanah_lembap()
    elif pilihan == 3:
        kondisi_tanah_basah()
    elif pilihan == 4:
        print("\nProgram selesai.")
        break
    else:
        print("\nPilihan tidak tersedia.")
        print("Silakan masukkan angka 1 sampai 4.")