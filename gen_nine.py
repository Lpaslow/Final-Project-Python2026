import tkinter as tk
import random
import requests
import threading


# ---------------- GEN 9 ONLY (PALDEA) ---------------- #
BASE_URL = "https://pokeapi.co/api/v2/generation/9"

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


# ---------------- GUI ---------------- #
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Generator")
        self.root.geometry("520x450")

        # 🌄 open-world background
        self.root.configure(bg="#1a1026")  # deep violet night sky

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text="Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#1a1026",
            fg="#ffffff"
        )
        title.pack(pady=15)

        # ---------- MAIN CARD ----------
        self.card = tk.Frame(
            root,
            bg="#2a1b3d",  # dark violet (Scarlet/Violet mix)
            bd=2,
            highlightbackground="#ff4d6d",  # scarlet pink accent
            highlightthickness=2
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Gen 9 Pokémon...",
            font=("Segoe UI", 10),
            bg="#2a1b3d",
            fg="#a7ffeb"  # mint/green accent (open world feel)
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#ff4d6d",   # Scarlet accent
            fg="white",
            activebackground="#ff7a8f",
            activeforeground="white",
            padx=10,
            pady=6,
            command=self.show_result,
            state="disabled",
            relief="flat"
        )
        self.btn.pack(pady=10)

        # ---------- OUTPUT FRAME ----------
        self.output_frame = tk.Frame(
            self.card,
            bg="#1a1026",
            bd=1,
            highlightbackground="#8be9ff",  # Violet futuristic blue
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # ---------- OUTPUT TEXT ----------
        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#1a1026",
            fg="#ffffff",
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Ready!", fg="#ff4d6d")
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" GEN NINE HYBRID \n\n"
            f"Head: {c['head']}\n"
            f"Body: {c['body']}\n"
            f"Arms: {c['arms']}\n"
            f"Legs: {c['legs']}\n"
            f"Tail: {c['tail']}\n"
            f"Wings: {c['wings']}\n"
            f"Eyes: {c['eyes']}"
        )

        self.output.config(text=text)


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()