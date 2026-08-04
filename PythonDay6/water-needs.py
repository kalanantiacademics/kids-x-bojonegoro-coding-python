print("KALKULATOR KEBUTUHAN AIR")
print("========================")

while True:
    area = int(input("Masukkan luas kebun (m²): "))
    water_per_meter = float(input("Air untuk setiap m² (liter): "))

    water_needs = area * water_per_meter

    print("Kebutuhan air:", water_needs, "liter")

    ulang = input("Hitung kebun lain? (ya/tidak): ").lower()
    if ulang == "tidak":
        print("Program selesai.")
        break
