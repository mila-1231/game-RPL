import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import threading
import time
from datetime import datetime

# Membuat koneksi dengan database SQLite
def create_db():
    conn = sqlite3.connect('tugas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tugas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        deskripsi TEXT,
                        waktu TEXT)''')
    conn.commit()
    conn.close()

# Menambahkan tugas ke database
def tambah_tugas():
    deskripsi = entry_tugas.get()
    waktu = entry_waktu.get()
    
    if not deskripsi or not waktu:
        messagebox.showwarning("Input Error", "Mohon isi semua kolom.")
        return
    
    conn = sqlite3.connect('tugas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tugas (deskripsi, waktu) VALUES (?, ?)", (deskripsi, waktu))
    conn.commit()
    conn.close()
    
    list_tugas.insert('', 'end', values=(deskripsi, waktu))
    entry_tugas.delete(0, tk.END)
    entry_waktu.delete(0, tk.END)
    messagebox.showinfo("Tugas Ditambahkan", "Tugas berhasil ditambahkan!")

# Menghapus tugas yang dipilih
def hapus_tugas():
    selected_item = list_tugas.selection()
    if not selected_item:
        messagebox.showwarning("Pilih Tugas", "Pilih tugas yang ingin dihapus.")
        return
    
    for item in selected_item:
        deskripsi = list_tugas.item(item, "values")[0]
        
        conn = sqlite3.connect('tugas.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tugas WHERE deskripsi=?", (deskripsi,))
        conn.commit()
        conn.close()
        
        list_tugas.delete(item)
    
    messagebox.showinfo("Tugas Dihapus", "Tugas berhasil dihapus!")

# Fungsi pengingat
def pengingat():
    while True:
        conn = sqlite3.connect('tugas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT deskripsi, waktu FROM tugas")
        tasks = cursor.fetchall()
        conn.close()
        
        current_time = datetime.now().strftime("%H:%M")
        for deskripsi, waktu in tasks:
            if waktu == current_time:
                messagebox.showinfo("Pengingat", f"Waktunya: {deskripsi} - {waktu}")
        time.sleep(60)

# Menjalankan pengingat dalam thread terpisah
def start_pengingat_thread():
    thread = threading.Thread(target=pengingat, daemon=True)
    thread.start()

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("TIMEDATE Reminder")
root.geometry("450x450")
root.configure(bg="#D4E6F1")  # Warna latar belakang biru muda

style = ttk.Style()
style.configure("TFrame", background="#D4E6F1")
style.configure("TLabel", background="#D4E6F1", font=("Arial", 10, "bold"))
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("Treeview", background="white", fieldbackground="white", font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

frame = ttk.Frame(root, padding=10)
frame.pack(fill='both', expand=True)

# Form input tugas
ttk.Label(frame, text="Tugas:").grid(row=0, column=0, sticky='w', pady=5)
entry_tugas = ttk.Entry(frame, width=50)
entry_tugas.grid(row=0, column=1, pady=5)

# Form input waktu
ttk.Label(frame, text="Waktu (HH:MM):").grid(row=1, column=0, sticky='w', pady=5)
entry_waktu = ttk.Entry(frame, width=50)
entry_waktu.grid(row=1, column=1, pady=5)

# Tombol tambah
ttk.Button(frame, text="Tambah Tugas", command=tambah_tugas, style="TButton").grid(row=2, column=0, columnspan=2, pady=10)

# Tabel tugas
columns = ("Tugas", "Waktu")
list_tugas = ttk.Treeview(frame, columns=columns, show="headings", height=8)
list_tugas.heading("Tugas", text="Tugas")
list_tugas.heading("Waktu", text="Waktu")
list_tugas.column("Tugas", width=200)
list_tugas.column("Waktu", width=230)
list_tugas.grid(row=3, column=0, columnspan=2, pady=5)

# Tombol hapus
ttk.Button(frame, text="Hapus Tugas", command=hapus_tugas, style="TButton").grid(row=4, column=0, columnspan=2, pady=10)

# Memulai aplikasi dan pengingat
create_db()
start_pengingat_thread()
root.mainloop()
