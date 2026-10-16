"""Meet 20 - AI Fruit Classifier (Python SMP)

Program Machine Learning sederhana berdasarkan materi Meet 20.
Instal library: python -m pip install scikit-learn
Jalankan:       python main.py

Dataset di bawah adalah CONTOH BUATAN untuk belajar,
bukan pengukuran buah asli.
"""

from sklearn.tree import DecisionTreeClassifier


# =========================================================
# STEP 1 - DATASET (X)
# =========================================================
# Kita MEMBUAT SENDIRI contoh data untuk melatih AI.
# Setiap baris: [berat dalam gram, panjang dalam cm, tekstur]
# Kode tekstur: 0 = halus, 1 = kasar
X = [
    [150, 7.5, 0],   # Apel
    [180, 8.2, 0],   # Apel
    [210, 9.0, 0],   # Apel

    [110, 6.5, 1],   # Jeruk
    [150, 7.6, 1],   # Jeruk
    [190, 8.7, 1],   # Jeruk

    [90, 15.0, 0],   # Pisang
    [120, 19.0, 0],  # Pisang
    [160, 22.0, 0]   # Pisang
]


# =========================================================
# STEP 2 - LABEL / JAWABAN BENAR (y)
# =========================================================
# Urutan label harus sama dengan urutan contoh di X.
y = [
    "Apel", "Apel", "Apel",
    "Jeruk", "Jeruk", "Jeruk",
    "Pisang", "Pisang", "Pisang"
]


# =========================================================
# STEP 3 - MEMBUAT DAN MELATIH MODEL
# =========================================================
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
print("AI berhasil dilatih!")


# =========================================================
# STEP 4 - INPUT BUAH BARU DARI PENGGUNA
# =========================================================
# Bagian ini BUKAN dataset training.
# Angka yang dimasukkan adalah ciri buah BARU untuk ditebak.
try:
    berat = float(input("Berat buah (gram): "))
    panjang = float(input("Panjang buah (cm): "))
    tekstur = int(input("Tekstur (0=halus, 1=kasar): "))

    if berat <= 0 or panjang <= 0 or tekstur not in (0, 1):
        print("Input tidak valid. Gunakan angka positif dan tekstur 0/1.")
    else:
        # =================================================
        # STEP 5 - PREDICTION / MENAMPILKAN HASIL
        # =================================================
        buah_baru = [[berat, panjang, tekstur]]
        hasil = model.predict(buah_baru)
        print("Prediksi AI:", hasil[0])

except ValueError:
    print("Input harus angka. Jalankan program dan coba lagi.")
