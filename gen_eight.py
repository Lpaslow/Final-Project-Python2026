import tkinter as tk
import random
import requests
import threading


# ---------------- GEN 8 ONLY (GALAR) ---------------- #
BASE_URL = "https://pokeapi.co/api/v2/generation/8"

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
        self.root.title("Galar Pokémon Generator")
        self.root.geometry("520x450")

        # ⚫ steel stadium background
        self.root.configure(bg="#111216")

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Galar Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#111216",
            fg="#ffffff"
        )
        title.pack(pady=15)

        # ---------- MAIN CARD ----------
        self.card = tk.Frame(
            root,
            bg="#1c1f26",  # steel gray
            bd=2,
            highlightbackground="#ff2e2e",  # bold red accent
            highlightthickness=2
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Gen 8 Pokémon...",
            font=("Segoe UI", 10),
            bg="#1c1f26",
            fg="#4da3ff"  # electric blue
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#ff2e2e",   # Galar red
            fg="white",
            activebackground="#ff6666",
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
            bg="#111216",
            bd=1,
            highlightbackground="#4da3ff",  # blue accent
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # ---------- OUTPUT TEXT ----------
        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#111216",
            fg="#ffffff",
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Galar Ready!", fg="#ff2e2e")
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" GALAR HYBRID \n\n"
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