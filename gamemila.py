import tkinter as tk
import random

# Data untuk Game Tebak Kata Biologi (Sendi) - Part 1
part1_data = {
    "ENGSEL": "Sendi seperti pada pintu, memungkinkan gerakan satu arah.",
    "PELURU": "Sendi yang memungkinkan gerakan ke segala arah, seperti bahu.",
    "PUTAR": "Sendi yang memungkinkan gerakan rotasi, seperti leher.",
    "GESER": "Sendi yang memungkinkan gerakan meluncur atau sedikit bergeser, seperti pergelangan tangan.",
     "JANTUNG": "Organ yang memompa darah ke seluruh tubuh.",
    "PARU-PARU": "Organ tempat pertukaran oksigen dan karbon dioksida.",
    "MATA": "Indera untuk melihat.",
    "TELINGA": "Indera untuk mendengar.",
    "KULIT": "Indera peraba pada tubuh manusia.",
    "HIDUNG": "Indera untuk mencium bau.",
    "LIDAH": "Indera untuk mengecap rasa.",
    "TULANG": "Kerangka yang menyokong tubuh manusia.",
    "OTOT": "Bagian tubuh yang membantu kita bergerak.",
    "LAMBUNG": "Tempat makanan dicerna setelah dari mulut.",
}
part1_words = list(part1_data.keys())
PART1_TITLE = "Tebak Kata Biologi"
PART1_BG = "#c8e6c9"  # Soft Light Green
PART1_FG = "#388e3c"  # Soft Dark Green

# Data untuk Game Tebak Kata Matematika Dasar - Part 2
part2_data = {
    "TAMBAH": "Proses menghitung jumlah total.",
    "KURANG": "Proses mengambil sebagian.",
    "KALI": "Penjumlahan berulang.",
    "BAGI": "Membagi menjadi bagian yang sama.",
    "ANGKA": "Simbol yang digunakan untuk menghitung disebut.",
    "JUMLAH": "Hasil dari penjumlahan disebut disebut.",
    "SELISIH": "Hasil dari pengurangan disebut.",
    "PERKALIAN": "Operasi untuk menghitung hasil kali disebut.",
    "PEMBAGIAN": "Operasi untuk membagi sesuatu secara adil disebut.",
    "SATUAN": "Nilai terkecil dalam sistem bilangan disebut.",
    "LIMA": "Angka setelah empat adalah.",
    "DUA": "Angka sebelum tiga adalah.",
    "NOL": "Angka yang menunjukkan tidak ada adalah.",
    "HASIL": "Jawaban dari sebuah operasi hitung adalah.",
}
part2_words = list(part2_data.keys())
PART2_TITLE = "Tebak Kata Matematika"
PART2_BG = "#bbdefb"  # Soft Light Blue
PART2_FG = "#1e88e5"  # Soft Dark Blue

# Data untuk Game Tebak Kata Kimia Dasar - Part 3
part3_data = {
    "ATOM": "Unit dasar materi.",
    "MOLEKUL": "Dua atau lebih atom yang terikat bersama.",
    "UNSUR": "Zat murni yang terdiri dari satu jenis atom.",
    "SENYAWA": "Zat yang terbentuk dari dua atau lebih unsur yang berbeda.",
    "GAS": "Bentuk zat yang mengalir dan tidak punya bentuk tetap, seperti udara.",
    "CAIR": "Bentuk zat yang mengalir dan mengambil bentuk wadahnya, seperti air.",
    "PADAT": "Bentuk zat yang memiliki bentuk dan volume tetap, seperti batu.",
    "REAKSI": "Perubahan kimia saat dua zat bercampur.",
    "AIR": "Cairan penting untuk kehidupan, rumus kimianya H2O.",
    "OKSIGEN": "Gas yang kita hirup untuk bernapas.",
    "KARBON": "Unsur penting yang ada dalam semua makhluk hidup.",
    "ASAM": "Zat dengan rasa asam, seperti cuka atau lemon.",
    "BASA": "Zat yang terasa licin dan bisa menetralkan asam.",
    "CAMPURAN": "Gabungan dua atau lebih zat yang tidak bereaksi kimia.",

}
part3_words = list(part3_data.keys())
PART3_TITLE = "Tebak Kata Kimia"
PART3_BG = "#f48fb1"  # Soft Pink
PART3_FG = "#c2185b"  # Soft Dark Pink

# Palet Warna Umum untuk Jendela Utama
MAIN_BG = "#e0f2f1"  # Soft Light Teal
MAIN_FG = "#263238"  # Soft Dark Grey

class GuessingGame:
    def __init__(self, master, title, word_data, words, bg_color, fg_color):
        self.master = master
        master.title(title)
        master.config(bg=bg_color)
        self.word_data = word_data
        self.words = list(words)
        self.current_word = random.choice(self.words)
        self.hint = self.word_data[self.current_word]
        self.attempts_left = 10
        self.score = 0
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.accent_color = self.fg_color # Gunakan warna teks sebagai aksen sederhana

        self.label_title = tk.Label(master, text=title, font=("Arial", 32, "bold"), bg=bg_color, fg=self.fg_color)
        self.label_title.pack(pady=30)

        self.label_hint_text = tk.Label(master, text="Petunjuk:", font=("Arial", 18, "italic"), bg=bg_color, fg=self.fg_color)
        self.label_hint_text.pack()

        self.label_hint = tk.Label(master, text=self.hint, font=("Arial", 20), bg=bg_color, fg=self.fg_color, wraplength=350, justify='center')
        self.label_hint.pack(pady=20)

        self.entry_guess = tk.Entry(master, font=("Arial", 24), bg="white", fg=self.fg_color, insertbackground=self.fg_color, justify='center')
        self.entry_guess.pack(pady=15, padx=50, fill=tk.X)
        self.entry_guess.focus_set()

        self.frame_info = tk.Frame(master, bg=bg_color)
        self.frame_info.pack()

        self.label_attempts = tk.Label(self.frame_info, text=f"Kesempatan: {self.attempts_left}", font=("Arial", 16), bg=bg_color, fg=self.fg_color)
        self.label_attempts.pack(side=tk.LEFT, padx=15)

        self.label_score = tk.Label(self.frame_info, text=f"Skor: {self.score}", font=("Arial", 16), bg=bg_color, fg=self.fg_color)
        self.label_score.pack(side=tk.LEFT, padx=15)

        self.button_guess = tk.Button(master, text="Tebak!", font=("Arial", 20, "bold"), bg=self.fg_color, fg="white", command=self.check_guess, relief=tk.RAISED, bd=5, padx=20, pady=10)
        self.button_guess.pack(pady=10)

        self.button_hint = tk.Button(master, text="Bantuan 2 Huruf", font=("Arial", 14), bg="lightyellow", fg="black", command=self.show_hint, relief=tk.RAISED, bd=3, padx=10, pady=5)
        self.button_hint.pack(pady=5)

        self.label_result = tk.Label(master, text="", font=("Arial", 24, "bold"), bg=bg_color, fg=self.fg_color)
        self.label_result.pack(pady=20)

        self.revealed_letters = [] # Menyimpan indeks huruf yang sudah diungkap

    def show_hint(self):
        if self.attempts_left > 0:
            available_indices = [i for i, char in enumerate(self.current_word) if i not in self.revealed_letters]
            if len(available_indices) >= 2:
                hint_indices = random.sample(available_indices, 2)
                hint_letters = [self.current_word[i] for i in hint_indices]
                hint_text = "Bantuan: " + ", ".join(hint_letters)
                self.label_result.config(text=hint_text, fg="blue")
                self.attempts_left -= 1 # Mengurangi kesempatan saat meminta bantuan
                self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
                self.revealed_letters.extend(hint_indices)
            elif len(available_indices) == 1:
                hint_index = available_indices[0]
                hint_letter = self.current_word[hint_index]
                self.label_result.config(text=f"Bantuan: {hint_letter}", fg="blue")
                self.attempts_left -= 1
                self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
                self.revealed_letters.append(hint_index)
            else:
                self.label_result.config(text="Tidak ada huruf lagi untuk diungkap.", fg="gray")
        else:
            self.label_result.config(text="Kesempatan habis!", fg="red")

    def check_guess(self):
        guess = self.entry_guess.get().upper()
        self.entry_guess.delete(0, tk.END)

        if guess == self.current_word:
            self.score += self.attempts_left * 100
            self.label_score.config(text=f"Skor: {self.score}")
            self.label_result.config(text="Benar!", fg="green")
            if self.bg_color == PART1_BG:
                self.master.config(bg="#e6ee9c") # Soft Light Lime
            elif self.bg_color == PART2_BG:
                self.master.config(bg="#b3e5fc") # Soft Lighter Blue
            elif self.bg_color == PART3_BG:
                self.master.config(bg="#f06292") # Soft Pink
            self.after_next_word(1500)
        else:
            self.attempts_left -= 1
            self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
            self.label_result.config(text="Coba lagi!", fg="red")
            self.master.config(bg="#ffcdd2") # Soft Light Red
            self.master.after(500, lambda: self.master.config(bg=self.bg_color))
            if self.attempts_left == 0:
                self.label_result.config(text=f"Jawabannya adalah {self.current_word}", fg="red")
                self.after_next_word(2000)

    def after_next_word(self, delay):
        self.master.after(delay, self.next_word)
        self.entry_guess.config(state=tk.DISABLED)
        self.button_guess.config(state=tk.DISABLED)
        self.button_hint.config(state=tk.DISABLED)

    def next_word(self):
        if self.words:
            self.current_word = random.choice(self.words)
            self.hint = self.word_data[self.current_word]
            self.words.remove(self.current_word)
            self.label_hint.config(text=self.hint)
            self.label_attempts.config(text=f"Kesempatan: {self.attempts_left}")
            self.label_result.config(text="")
            self.entry_guess.config(state=tk.NORMAL)
            self.button_guess.config(state=tk.NORMAL)
            self.button_hint.config(state=tk.NORMAL)
            self.entry_guess.focus_set()
            self.master.config(bg=self.bg_color)
            self.revealed_letters = [] # Reset huruf yang diungkap untuk kata baru
        else:
            self.label_title.config(text="Permainan Selesai!", font=("Arial", 36, "bold"), fg=self.fg_color)
            self.label_hint_text.pack_forget()
            self.label_hint.config(text=f"Skor Akhir: {self.score}", font=("Arial", 24), fg=self.fg_color)
            self.label_attempts.pack_forget()
            self.label_score.pack_forget()
            self.entry_guess.pack_forget()
            self.button_guess.pack_forget()
            self.button_hint.pack_forget()
            self.label_result.pack_forget()

def start_game(part):
    game_window = tk.Toplevel(root)
    if part == 1:
        GuessingGame(game_window, PART1_TITLE, part1_data, part1_words, PART1_BG, PART1_FG)
    elif part == 2:
        GuessingGame(game_window, PART2_TITLE, part2_data, part2_words, PART2_BG, PART2_FG)
    elif part == 3:
        GuessingGame(game_window, PART3_TITLE, part3_data, part3_words, PART3_BG, PART3_FG)

root = tk.Tk()
root.title("AYO BELAJAR")
root.config(bg=MAIN_BG)

label_pilih = tk.Label(root, text="Let's play", font=("Arial", 28, "bold"), bg=MAIN_BG, fg=MAIN_FG)
label_pilih.pack(pady=30)

button_part1 = tk.Button(root, text="BIOLOGI", font=("Arial", 20, "bold"), bg=PART1_BG, fg=PART1_FG, command=lambda: start_game(1), relief=tk.RAISED, bd=5, padx=30, pady=15)
button_part1.pack(pady=15)

button_part2 = tk.Button(root, text="MATEMATIKA", font=("Arial", 20, "bold"), bg=PART2_BG, fg=PART2_FG, command=lambda: start_game(2), relief=tk.RAISED, bd=5, padx=30, pady=15)
button_part2.pack(pady=15)

button_part3 = tk.Button(root, text="KIMIA", font=("Arial", 20, "bold"), bg=PART3_BG, fg=PART3_FG, command=lambda: start_game(3), relief=tk.RAISED, bd=5, padx=30, pady=15)
button_part3.pack(pady=15)

root.mainloop()