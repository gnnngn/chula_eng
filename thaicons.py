import tkinter as tk
import random

# List of Thai consonants with their Romanized names
thai_consonants = [
    ("ก", "gor kai"),
    ("ข", "kho khai"),
    ("ค", "kho khwai"),
    ("ง", "ngo ngu"),
    ("จ", "jor jaan"),
    ("ฉ", "cho ching"),
    ("ช", "cho chang"),
    ("ซ", "so so"),
    ("ญ", "yo ying"),
    ("ฎ", "do cha-da"),
    ("ฏ", "to pa-tak"),
    ("ฐ", "tho than"),
    ("ณ", "no nen"),
    ("บ", "bo baimai"),
    ("ป", "po pla"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.card_frame = tk.Frame(self.root, bd=2, relief="ridge", width=300, height=200)
        self.card_frame.pack(pady=30)
        
        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 48), width=5, height=2)
        self.card_label.pack()
        
        self.flip_button = tk.Button(self.root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next", command=self.next_card)
        self.next_button.pack()
        
        self.current_card = None
        self.show_new_card()
    
    def show_new_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        self.flipped = False
    
    def flip_card(self):
        if self.flipped:
            self.card_label.config(text=self.current_card[0])
        else:
            self.card_label.config(text=self.current_card[1])
        self.flipped = not self.flipped
    
    def next_card(self):
        self.show_new_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

# Filename: thaicons.py
