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

    print(f"Loaded {len(every_pokemon)} Pokémon!")

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
        self.root.configure(bg="#1e1e2f")  # dark background

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Pokémon Parts Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2f",
            fg="#f5f5f5"
        )
        title.pack(pady=15)

        # ---------- CARD FRAME ----------
        self.card = tk.Frame(root, bg="#2a2a40", bd=0)
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Pokémon...",
            font=("Segoe UI", 10),
            bg="#2a2a40",
            fg="#aaaaaa"
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text="Generate Pokémon",
            font=("Segoe UI", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            padx=10,
            pady=5,
            command=self.show_result,
            state="disabled",
            relief="flat"
        )
        self.btn.pack(pady=10)

        # ---------- OUTPUT BOX ----------
        self.output_frame = tk.Frame(self.card, bg="#1e1e2f")
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#1e1e2f",
            fg="#00ffcc",
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Ready!", fg="#66ff66")
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" GENERATED CREATURE \n\n"
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