import tkinter as tk
from tkinter import ttk
import random
import requests
import threading



BASE_URL = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Gen 1 only

every_pokemon = []


def load_pokemon():
    global every_pokemon


    response = requests.get(BASE_URL)
    data = response.json()

    every_pokemon = [p["name"].capitalize() for p in data["results"]]


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



#gui

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Generator")
        self.root.geometry("520x450")
        self.root.configure(bg="#0f0f1a")  # dark blue-ish background

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Pokémon Parts Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#0f0f1a",
            fg="#ff3333"  # red
        )
        title.pack(pady=15)

        # ---------- CARD FRAME ----------
        self.card = tk.Frame(
            root,
            bg="#1a1a2b",
            bd=2,
            highlightbackground="#3399ff",  # blue border
            highlightthickness=1
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Pokémon...",
            font=("Segoe UI", 10),
            bg="#1a1a2b",
            fg="#66ff66"  # green
        )
        self.status.pack(pady=5)

#run
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()