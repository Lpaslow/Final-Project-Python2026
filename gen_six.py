import tkinter as tk
import random
import requests
import threading


# ---------------- GEN 6 ONLY (KALOS) ---------------- #
BASE_URL = "https://pokeapi.co/api/v2/generation/6"

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
        self.root.title("Kalos Pokémon Generator")
        self.root.geometry("520x450")

        # ❄️ Kalos dark-blue background
        self.root.configure(bg="#0b1b2b")

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Kalos Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#0b1b2b",
            fg="#ffffff"
        )
        title.pack(pady=15)

        # ---------- MAIN CARD ----------
        self.card = tk.Frame(
            root,
            bg="#132a3a",  # deep Kalos blue
            bd=2,
            highlightbackground="#d4af37",  # gold accent
            highlightthickness=2
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Gen 6 Pokémon...",
            font=("Segoe UI", 10),
            bg="#132a3a",
            fg="#ffffff"
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#d4af37",   # gold
            fg="black",
            activebackground="#e6c55a",
            activeforeground="black",
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
            bg="#0b1b2b",
            bd=1,
            highlightbackground="#7ec8ff",  # light Kalos blue
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # ---------- OUTPUT TEXT ----------
        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#0b1b2b",
            fg="#ffffff",
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Kalos Ready!", fg="#d4af37")
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" KALOS HYBRID \n\n"
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