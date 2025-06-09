import tkinter as tk
from tkinter import messagebox
import random

QUESTIONS = [
    {"letters": list("ASIP"), "valid_words": {"API", "SAPI", "PISA", "SIAP", "PAS", "ISA", "ASIA"}},
    {"letters": list("KOTA"), "valid_words": {"KOTA", "TOKA", "AKT", "TAKO", "AKO", "TOK"}},
    {"letters": list("BUDA"), "valid_words": {"BUDA", "DUBA", "BADU", "UBA", "DUA"}},
    {"letters": list("RINA"), "valid_words": {"RINA", "IRAN", "AIR", "NIRA", "ARIN", "RIA", "NAI"}},
    {"letters": list("TANI"), "valid_words": {"TANI", "ANTI", "NITA", "NIA", "TAN", "TIN"}},
    {"letters": list("LIMA"), "valid_words": {"LIMA", "MILA", "AMI", "ILA", "LIA"}},
    {"letters": list("DONA"), "valid_words": {"DONA", "ADON", "ANDA", "NODA", "ADO"}},
    {"letters": list("SARI"), "valid_words": {"SARI", "ARIS", "RISA", "ISA", "SIR"}},
    {"letters": list("TARA"), "valid_words": {"TARA", "ARTA", "RATA", "TAR", "ARA"}},
    {"letters": list("MIRA"), "valid_words": {"MIRA", "IRMA", "RIMA", "RIA", "RAM"}},
    {"letters": list("KILA"), "valid_words": {"KILA", "KALI", "ILKA", "LAKI", "ALI"}},
    {"letters": list("BUDI"), "valid_words": {"BUDI", "IDU", "DUI", "DIB", "UBI"}},
    {"letters": list("RAMA"), "valid_words": {"RAMA", "AMAR", "MARA", "ARA", "AMA"}},
    {"letters": list("DINA"), "valid_words": {"DINA", "NADI", "ADIN", "ANDI", "DIN"}},
    {"letters": list("RINA"), "valid_words": {"RINA", "NIRA", "IRAN", "AIR", "RIA"}},
    {"letters": list("SUKA"), "valid_words": {"SUKA", "KUSA", "KAS", "USA", "AKU"}},
    {"letters": list("TINA"), "valid_words": {"TINA", "ANTI", "NITA", "INA", "TIN"}},
    {"letters": list("NIKO"), "valid_words": {"NIKO", "KOIN", "KONI", "KIO", "INO"}},
    {"letters": list("LINA"), "valid_words": {"LINA", "NILA", "ALIN", "NIA", "ILA"}},
    {"letters": list("JOKI"), "valid_words": {"JOKI", "KOJI", "IJO", "JOK", "OKI"}},
    {"letters": list("SITA"), "valid_words": {"SITA", "TISA", "ASTI", "SAI", "TIS"}},
    {"letters": list("FIRA"), "valid_words": {"FIRA", "RIFA", "ARIF", "RIA", "FAI"}},
    {"letters": list("RENA"), "valid_words": {"RENA", "ENAR", "ERAN", "NARE", "ENA"}},
    {"letters": list("ASIP"), "valid_words": {"API", "SAP", "PISA", "SIAP", "PAS", "ISA", "ASIA"}},
    {"letters": list("KOTA"), "valid_words": {"KOTA", "TOKA", "AKT", "TAKO", "AKO", "TOK"}},
    {"letters": list("BUDA"), "valid_words": {"BUDA", "DUBA", "BADU", "UBA", "DUA"}},
    {"letters": list("RINA"), "valid_words": {"RINA", "IRAN", "AIR", "NIRA", "ARIN", "RIA", "NAI"}}
]

class WordConnectGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Teka-Teki Kata - Word Connect")
        self.master.configure(bg="#eaf2f8")

        self.question_index = 0
        self.selected_letters = ""
        self.found_words = set()
        self.letter_buttons = []

        self.build_interface()
        self.load_question()

    def build_interface(self):
        tk.Label(self.master, text="TEKA-TEKI KATA", font=("Helvetica", 24, "bold"), bg="#eaf2f8", fg="#34495e").pack(pady=10)

        self.display_label = tk.Label(self.master, text="", font=("Helvetica", 22), bg="white", fg="#2c3e50",
                                      width=20, height=2, relief=tk.SUNKEN)
        self.display_label.pack(pady=5)

        self.letter_frame = tk.Frame(self.master, bg="#eaf2f8")
        self.letter_frame.pack(pady=10)

        action_frame = tk.Frame(self.master, bg="#eaf2f8")
        action_frame.pack()

        btn_style = {
            "font": ("Helvetica", 12),
            "width": 12,
            "fg": "black",
            "relief": tk.RAISED
        }

        tk.Button(action_frame, text="CEK KATA", command=self.check_word, bg="#a9dfbf", activebackground="#82e0aa", **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="HAPUS", command=self.reset_word, bg="#f5b7b1", activebackground="#f1948a", **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="ACAK ULANG", command=self.shuffle_letters, bg="#aed6f1", activebackground="#85c1e9", **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="BERIKUTNYA", command=self.next_question, bg="#d2b4de", activebackground="#bb8fce", **btn_style).pack(side=tk.LEFT, padx=5)

        tk.Label(self.master, text="Kata Ditemukan:", font=("Helvetica", 14, "bold"), bg="#eaf2f8", fg="#34495e").pack(pady=(15, 5))
        self.result_listbox = tk.Listbox(self.master, width=30, height=6, font=("Helvetica", 14), bg="white", fg="#2c3e50")
        self.result_listbox.pack()

        self.status_label = tk.Label(self.master, text="0 kata ditemukan", font=("Helvetica", 12), bg="#eaf2f8", fg="#2c3e50")
        self.status_label.pack(pady=5)

    def load_question(self):
        question = QUESTIONS[self.question_index]
        self.current_letters = question["letters"]
        self.valid_words = question["valid_words"]

        self.found_words.clear()
        self.result_listbox.delete(0, tk.END)
        self.status_label.config(text="0 kata ditemukan")
        self.reset_word()
        self.generate_letters()

    def generate_letters(self):
        for btn in self.letter_buttons:
            btn.destroy()
        self.letter_buttons.clear()

        shuffled = random.sample(self.current_letters, len(self.current_letters))
        for letter in shuffled:
            btn = tk.Button(self.letter_frame, text=letter, font=("Helvetica", 20, "bold"), width=4, height=2,
                            bg="#ffffff", fg="#2c3e50", activebackground="#d5dbdb",
                            command=lambda l=letter: self.add_letter(l))
            btn.pack(side=tk.LEFT, padx=5)
            self.letter_buttons.append(btn)

    def shuffle_letters(self):
        self.reset_word()
        self.generate_letters()

    def add_letter(self, letter):
        self.selected_letters += letter
        self.display_label.config(text=self.selected_letters)

    def check_word(self):
        word = self.selected_letters.upper()
        if word in self.valid_words and word not in self.found_words:
            self.found_words.add(word)
            self.result_listbox.insert(tk.END, word)
            self.status_label.config(text=f"{len(self.found_words)} kata ditemukan")
            messagebox.showinfo("Benar!", f"'{word}' adalah kata yang valid!")
        elif word in self.found_words:
            messagebox.showwarning("Sudah Ditemukan", f"Kata '{word}' sudah ditemukan.")
        else:
            messagebox.showerror("Salah", f"'{word}' bukan kata yang valid.")
        self.reset_word()

    def reset_word(self):
        self.selected_letters = ""
        self.display_label.config(text="")

    def next_question(self):
        self.question_index = (self.question_index + 1) % len(QUESTIONS)
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordConnectGame(root)
    root.mainloop()
