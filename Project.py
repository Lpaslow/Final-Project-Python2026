import tkinter as tk
from tkinter import ttk
import random


# SIMPLE FAKE DATA
every_pokemon = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Eevee", "Gengar", "Snorlax", "Mew", "Lucario"
]

def generate_creature():
    return {
        "head": random.choice(every_pokemon),
        "body": random.choice(every_pokemon),
        "arms": random.choice(every_pokemon),
        "legs": random.choice(every_pokemon),
        "tail": random.choice(every_pokemon),
        "wings": random.choice(every_pokemon),
        "eyes": random.choice(every_pokemon),
    }



# GUI
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Parts Generator")
        self.root.geometry("450x350")

        tk.Label(root, text="Pokémon Parts Generator", font=("Arial", 14)).pack(pady=10)

        self.btn = tk.Button(root, text="Generate Pokémon", command=self.show_result)
        self.btn.pack(pady=10)

        self.output = tk.Label(root, text="", justify="left", font=("Arial", 11))
        self.output.pack(pady=20)

    def show_result(self):
        c = generate_creature()

        text = (
            f"👾 Generated Pokémon:\n\n"
            f"Head: {c['head']}\n"
            f"Body: {c['body']}\n"
            f"Arms: {c['arms']}\n"
            f"Legs: {c['legs']}\n"
            f"Tail: {c['tail']}\n"
            f"Wings: {c['wings']}\n"
            f"Eyes: {c['eyes']}"
        )

        self.output.config(text=text)



# RUN APP
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()