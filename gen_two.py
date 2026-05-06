import tkinter as tk
from tkinter import ttk
import random
import requests
import threading


# Gen 2 endpoint (Johto)
BASE_URL = "https://pokeapi.co/api/v2/generation/2"

every_pokemon = []


def load_pokemon():
    global every_pokemon

    response = requests.get(BASE_URL)
    data = response.json()

    every_pokemon = [p["name"].capitalize() for p in data["pokemon_species"]]


def generate_creature():
    return {
        "head": random.choice(every_pokemon),
        "body": random.choice(every_pokemon),
        "arms": random.choice(every_pokemon),
        "legs": random.choice(every_pokemon),
        "tail": random.choice(every_pokemon),
        "wings": random.choice(every_pokemon),
        "eyes": random.choice(every_pokemon)
    }


# GUI
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Generator (Johto Edition)")
        self.root.geometry("520x450")
        self.root.configure(bg="#2c2c2c")  # dark silver background

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#2c2c2c",
            fg="#ffd700"  # gold
        )
        title.pack(pady=15)

        # ---------- CARD FRAME ----------
        self.card = tk.Frame(
            root,
            bg="#3a3a3a",  # silver panel
            bd=2,
            highlightbackground="#c0c0c0",  # silver border
            highlightthickness=1
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Pokémon...",
            font=("Segoe UI", 10),
            bg="#3a3a3a",
            fg="#87cefa"  # light blue
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#ffd700",   # gold button
            fg="black",
            activebackground="#ffcc00",
            activeforeground="black",
            padx=10,
            pady=6,
            command=self.show_result,
            state="disabled",
            relief="flat"
        )
        self.btn.pack(pady=10)

        # ---------- OUTPUT BOX ----------
        self.output_frame = tk.Frame(
            self.card,
            bg="#1e1e1e",  # darker silver
            bd=1,
            highlightbackground="#87cefa",  # light blue border
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#87cefa",  # light blue text
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Ready!", fg="#ffd700")  # gold
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" GEN TWO HYBRID \n\n"
            f"Head: {c['head']}\n"
            f"Body: {c['body']}\n"
            f"Arms: {c['arms']}\n"
            f"Legs: {c['legs']}\n"
            f"Tail: {c['tail']}\n"
            f"Wings: {c['wings']}\n"
            f"Eyes: {c['eyes']}"
        )

        self.output.config(text=text)


# RUN
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()