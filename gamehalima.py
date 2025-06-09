import tkinter as tk
import random

# Fungsi untuk menentukan hasil pertandingan
def hasil_permainan(pemilihan_pahlawan):
    pilihan_monster = random.choice(["Batu", "Kertas", "Gunting"])
    if pemilihan_pahlawan == pilihan_monster:
        hasil = "Seri!"
    elif (pemilihan_pahlawan == "Batu" and pilihan_monster == "Gunting") or \
         (pemilihan_pahlawan == "Gunting" and pilihan_monster == "Kertas") or \
         (pemilihan_pahlawan == "Kertas" and pilihan_monster == "Batu"):
        hasil = "Pahlawan menang!"
    else:
        hasil = "Monster menang!"
    
    return pilihan_monster, hasil

# Fungsi untuk menangani klik tombol pilihan pahlawan
def pilih_pahlawan(pemilihan_pahlawan):
    pilihan_monster, hasil = hasil_permainan(pemilihan_pahlawan)
    label_hasil.config(text=f"Monster memilih: {pilihan_monster}\n{hasil}")

# Fungsi untuk menantang monster
def tantang_monster():
    label_hasil.config(text="Pahlawan siap menantang monster!\nPilih Batu, Kertas, atau Gunting untuk bertarung!")

# Setup window tkinter
root = tk.Tk()
root.title("Pahlawan vs Monster - Rock, Paper, Scissors")

# Label utama
label = tk.Label(root, text="Pilih Pahlawan: Batu, Kertas, atau Gunting", font=("Arial", 14))
label.pack(pady=10)

# Tombol untuk menantang monster
button_tantang = tk.Button(root, text="Menantang Monster", width=20, command=tantang_monster)
button_tantang.pack(pady=10)

# Tombol pilihan
button_batu = tk.Button(root, text="Batu", width=20, command=lambda: pilih_pahlawan("Batu"))
button_batu.pack(pady=5)

button_kertas = tk.Button(root, text="Kertas", width=20, command=lambda: pilih_pahlawan("Kertas"))
button_kertas.pack(pady=5)

button_gunting = tk.Button(root, text="Gunting", width=20, command=lambda: pilih_pahlawan("Gunting"))
button_gunting.pack(pady=5)

# Label untuk hasil pertandingan
label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=20)

# Jalankan aplikasi
root.mainloop()