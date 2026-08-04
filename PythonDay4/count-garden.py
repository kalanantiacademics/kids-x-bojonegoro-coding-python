print("KALKULATOR KEBUN")
print("====================")

length = float(input("Panjang kebun (meter): "))
width = float(input("Lebar kebun (meter): "))

area = length * width

seeds = int(input("Jumlah bibit: "))
seeds_price = int(input("Harga satu bibit: Rp"))

total_price = seeds * seeds_price

water_per_meter = 2
water_needs = area * water_per_meter

print("HASIL PERHITUNGAN")
print("====================")
print("Luas kebun       :", area, "m²")
print("Total biaya bibit: Rp", total_price)
print("Kebutuhan air    :", water_needs, "liter")