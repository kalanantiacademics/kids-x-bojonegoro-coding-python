print("PENGECEK PERTUMBUHAN BAYAM")
print("===========================")

height = int(input("Masukkan tinggi bayam (cm): "))

if height >= 20:
    print("Bayam sudah siap dipanen.")
elif height >= 10:
    print("Bayam masih dalam tahap pertumbuhan.")
    print("Tunggu hingga tingginya mencapai 20 cm.")
else:
    print("Bayam masih berupa bibit kecil.")
    print("Bayam masih membutuhkan waktu untuk tumbuh.")