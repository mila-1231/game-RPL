import tkinter as tk
import random

# Daftar kata dan deskripsi/gambar (kita akan gunakan deskripsi teks sederhana)
word_data = {
    "BOLA": "Untuk bermain sepak.",
    "KUCING": "Hewan peliharaan yang suka mengeong.",
    "BUKU": "Tempat untuk membaca cerita.",
    "PENA": "Untuk menulis di kertas.",
    "PIRING": "Tempat meletakkan makanan.",
    "SEPEDA": "Kendaraan roda dua yang dikayuh.",
    "BUNGA": "Cantik dan berwarna-warni.",
    "AYAM": "Hewan yang berkokok di pagi hari."
}
words = list(word_data.keys())

# Palet Warna Cerah untuk Anak-anak
BG_COLOR = "#e0f7fa"  # Light Cyan
FG_COLOR = "#2e7d32"  # Green
ACCENT_COLOR = "#ffb300"  # Amber
ERROR_COLOR = "#f44336"   # Red

class GuessReadingGame:
    def __init__(self, master):
        self.master = master
        master.title("Tebak Baca!")
        master.config(bg=BG_COLOR)

        self.current_word = random.choice(words)
        self.description = word_data[self.current_word]
        self.attempts_left = 3
        self.score = 0

        self.label_title = tk.Label(master, text="Ayo Tebak!", font=("Arial", 28, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
        self.label_title.pack(pady=20)

        self.label_description = tk.Label(master, text=self.description, font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify='center')
        self.label_description.pack(pady=30)

        self.entry_guess = tk.Entry(master, font=("Arial", 24), bg="white", fg=FG_COLOR, insertbackground=ACCENT_COLOR, justify='center')
        self.entry_guess.pack(pady=15, padx=50, fill=tk.X)
        self.entry_guess.focus_set()

        self.frame_info = tk.Frame(master, bg=BG_COLOR)
        self.frame_info.pack()

        self.label_attempts = tk.Label(self.frame_info, text=f"Kesempatan: {self.attempts_left}", font=("Arial", 16), bg=BG_COLOR, fg=FG_COLOR)
        self.label_attempts.pack(side=tk.LEFT, padx=15)

        self.label_score = tk.Label(self.frame_info, text=f"Skor: {self.score}", font=("Arial", 16), bg=BG_COLOR, fg=FG_COLOR)
        self.label_score.pack(side=tk.LEFT, padx=15)

        self.button_guess = tk.Button(master, text="Tebak!", font=("Arial", 20, "bold"), bg=ACCENT_COLOR, fg="white", command=self.check_guess, relief=tk.RAISED, bd=5, padx=20, pady=10)
        self.button_guess.pack(pady=20)

        self.label_result = tk.Label(master, text="", font=("Arial", 24, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        self.label_result.pack(pady=20)

    def check_guess(self):
        guess = self.entry_guess.get().upper()
        self.entry_guess.delete(0, tk.END)

        if guess == self.current_word:
            self.score += self.attempts_left * 100
            self.label_score.config(text=f"Skor: {self.score}")
            self.label_result.config(text="Benar sekali!", fg="green")
            self.master.config(bg="#81c784") # Light Green
            self.after_next_word(1500)
        else:
            self.attempts_left -= 1
            self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
            self.label_result.config(text="Coba lagi!", fg=ERROR_COLOR)
            self.master.config(bg="#e57373") # Light Red
            self.master.after(500, lambda: self.master.config(bg=BG_COLOR))
            if self.attempts_left == 0:
                self.label_result.config(text=f"Maaf, jawabannya adalah {self.current_word}", fg=ERROR_COLOR)
                self.after_next_word(2000)

    def after_next_word(self, delay):
        self.master.after(delay, self.next_word)
        self.entry_guess.config(state=tk.DISABLED)
        self.button_guess.config(state=tk.DISABLED)

    def next_word(self):
        global words
        if words:
            self.current_word = random.choice(words)
            self.description = word_data[self.current_word]
            words.remove(self.current_word)
            self.attempts_left = 3
            self.label_description.config(text=self.description)
            self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
            self.label_result.config(text="")
            self.entry_guess.config(state=tk.NORMAL)
            self.button_guess.config(state=tk.NORMAL)
            self.entry_guess.focus_set()
            self.master.config(bg=BG_COLOR)
        else:
            self.label_title.config(text="Permainan Selesai!", font=("Arial", 36, "bold"), fg=ACCENT_COLOR)
            self.label_description.config(text=f"Skor Akhir: {self.score}", font=("Arial", 24), fg=FG_COLOR)
            self.label_attempts.pack_forget()
            self.label_score.pack_forget()
            self.entry_guess.pack_forget()
            self.button_guess.pack_forget()
            self.label_result.pack_forget()

root = tk.Tk()
game = GuessReadingGame(root)
root.mainloop()