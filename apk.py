import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fungsi untuk menghitung jumlah kata dalam teks
def hitung_kata():
    teks = teks_input.get("1.0", tk.END).strip()
    if teks:
        jumlah_kata = len(teks.split())
        hasil_label.config(text=f"Jumlah kata: {jumlah_kata}")
    else:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu!")

# Fungsi untuk menghapus teks di kotak input
def hapus_teks():
    teks_input.delete("1.0", tk.END)
    hasil_label.config(text="")
    messagebox.showinfo("Info", "Teks telah dihapus!")

# Membuat antarmuka pengguna dengan Tkinter
app = tk.Tk()
app.title("Penghitung Kata")
app.geometry("600x500")  # Menentukan ukuran jendela
app.configure(bg="#ffd1dc")  # Mengatur warna latar belakang pink pastel

# Label judul
judul_label = tk.Label(app, text="💖 Aplikasi Penghitung Kata 💖", font=("Comic Sans MS", 20, "bold"), bg="#ff69b4", fg="white", pady=10, padx=20, relief=tk.GROOVE, bd=3)
judul_label.pack(pady=10, fill=tk.X)

# Kotak input untuk teks
teks_label = tk.Label(app, text="📝 Masukkan teks di bawah ini:", font=("Comic Sans MS", 12, "bold"), bg="#ffd1dc", fg="#333")
teks_label.pack(pady=5)

frame_teks = tk.Frame(app, bg="#ffd1dc", padx=10, pady=5)
teks_input = tk.Text(frame_teks, height=10, width=55, font=("Comic Sans MS", 12), bg="#ffffff", fg="#000", relief=tk.GROOVE, bd=3, wrap=tk.WORD)
teks_input.pack()
frame_teks.pack()

# Frame untuk tombol
tombol_frame = tk.Frame(app, bg="#ffd1dc")

hitung_button = ttk.Button(tombol_frame, text="✨ Hitung Kata ✨", command=hitung_kata, style="TButton")
hitung_button.grid(row=0, column=0, padx=10, pady=10)

hapus_button = ttk.Button(tombol_frame, text="❌ Hapus Teks ❌", command=hapus_teks, style="TButton")
hapus_button.grid(row=0, column=1, padx=10, pady=10)

tombol_frame.pack()

# Label untuk menampilkan hasil
hasil_label = tk.Label(app, text="", font=("Comic Sans MS", 14, "bold"), fg="#d81b60", bg="#ffd1dc")
hasil_label.pack(pady=10)

# Gaya tombol
style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 12, "bold"), padding=6, background="#ff69b4", foreground="black")
style.map("TButton", background=[("active", "#ff1493")])

# Menjalankan aplikasi
app.mainloop()
