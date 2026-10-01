import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "phonebook.txt"


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        pass

def load_contacts():
    listbox.delete(0, tk.END)
    with open(FILE_NAME, "r") as file:
        for line in file:
            if "," in line:
                nama, nomor = line.strip().split(",", 1)
                listbox.insert(tk.END, f"{nama} - {nomor}")

def add_contact():
    nama = entry_nama.get().strip()
    nomor = entry_nomor.get().strip()

    if not nama or not nomor:
        messagebox.showwarning("Error", "Nama dan Nomor harus diisi!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{nama},{nomor}\n")

    entry_nama.delete(0, tk.END)
    entry_nomor.delete(0, tk.END)
    load_contacts()

def delete_contact():
    dipilih = listbox.curselection()
    if not dipilih:
        messagebox.showwarning("Error", "Klik kontak yang mau dihapus dulu!")
        return

    teks_dipilih = listbox.get(dipilih[0])

    nama_dihapus = teks_dipilih.split(" - ")[0]

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if not line.startswith(nama_dihapus + ","):
                file.write(line)

    load_contacts()

root = tk.Tk()
root.title("Phone Book")
root.geometry("300x450")


tk.Label(root, text="Name:").pack(pady=(10, 0))
entry_nama = tk.Entry(root, width=30)
entry_nama.pack()

tk.Label(root, text="Number:").pack(pady=(5, 0))
entry_nomor = tk.Entry(root, width=30)
entry_nomor.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)

listbox = tk.Listbox(root, width=35, height=12)
listbox.pack(pady=10)

tk.Button(root, text="Delete Selected Contact", command=delete_contact).pack()

load_contacts()

root.mainloop()