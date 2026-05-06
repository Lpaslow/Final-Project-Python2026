import tkinter as tk
import random
import requests
import threading


# Gen 4 ONLY (Sinnoh)
BASE_URL = "https://pokeapi.co/api/v2/generation/4"

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
        self.root.title("Pokémon Generator")
        self.root.geometry("520x450")

        # -------- BACKGROUND (Platinum dark) --------
        self.root.configure(bg="#1c1c24")

        # ---------- TITLE ----------
        title = tk.Label(
            root,
            text=" Pokémon Generator ",
            font=("Segoe UI", 18, "bold"),
            bg="#1c1c24",
            fg="#6ec1ff"  # diamond blue
        )
        title.pack(pady=15)

        # ---------- CARD ----------
        self.card = tk.Frame(
            root,
            bg="#2a2a35",  # platinum gray
            bd=2,
            highlightbackground="#ffb6d9",  # pearl pink
            highlightthickness=2
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------- STATUS ----------
        self.status = tk.Label(
            self.card,
            text="Loading Pokémon...",
            font=("Segoe UI", 10),
            bg="#2a2a35",
            fg="#9ad4ff"  # lighter blue
        )
        self.status.pack(pady=5)

        # ---------- BUTTON ----------
        self.btn = tk.Button(
            self.card,
            text=" Generate Pokémon ",
            font=("Segoe UI", 11, "bold"),
            bg="#ffb6d9",  # pearl pink
            fg="black",
            activebackground="#ffcce6",
            padx=10,
            pady=6,
            command=self.show_result,
            state="disabled",
            relief="flat"
        )
        self.btn.pack(pady=10)

        # ---------- OUTPUT ----------
        self.output_frame = tk.Frame(
            self.card,
            bg="#16161d",
            bd=1,
            highlightbackground="#6ec1ff",  # diamond border
            highlightthickness=1
        )
        self.output_frame.pack(padx=15, pady=10, fill="both", expand=True)

        self.output = tk.Label(
            self.output_frame,
            text="",
            justify="left",
            font=("Consolas", 11),
            bg="#16161d",
            fg="#e0f4ff",  # soft icy blue text
            anchor="nw"
        )
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        threading.Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        load_pokemon()
        self.status.config(text="Ready!", fg="#ffb6d9")  # pink highlight
        self.btn.config(state="normal")

    def show_result(self):
        if not every_pokemon:
            return

        c = generate_creature()

        text = (
            f" GEN FOUR HYBRID \n\n"
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