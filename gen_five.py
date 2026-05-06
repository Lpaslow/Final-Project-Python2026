import tkinter as tk
import random
import requests
import threading


# ---------------- GEN 5 ONLY ---------------- #
BASE_URL = "https://pokeapi.co/api/v2/generation/5"

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
        self.root.title("Unova Pokémon Generator")
        self.root.geometry("520x450")

        # Dark Unova background
        self.root.configure(bg="#0a0a0a")

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Unova Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#0a0a0a",
            fg="white"
        )
        title.pack(pady=15)

        # ---------- MAIN CARD ----------
        self.card = tk.Frame(
            root,
            bg="#141414",
            bd=2,
            highlightbackground="#00e5ff",
            highlightthickness=2
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Gen 5 Pokémon...",
            font=("Segoe UI", 10),
            bg="#141414",
            fg="white"
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#f5f5f5",
            fg="black",
            activebackground="#cccccc",
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
            bg="#0a0a0a",
            bd=1,
            highlightbackground="#00e5ff",
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # ---------- OUTPUT TEXT ----------
        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#0a0a0a",
            fg="white",
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        # Load Pokémon in background thread
        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Gen 5 Ready!", fg="white")
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" UNOVA HYBRID \n\n"
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