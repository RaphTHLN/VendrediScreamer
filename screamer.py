import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random
import threading
import time

# =============================================

# Chemins des fichiers pour les images et les sons.
SCREAMER_IMAGE_PATH = "screamer.png"
SCREAMER_SOUND_PATH = "screamer.mp3"
SHINY_IMAGE_PATH = "shiny.png"
SHINY_SOUND_PATH = "shiny.mp3"

# Probabilité de l'événement "shiny".
SHINY_PROBABILITY_RANGE = 100

def play_selected_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(SELECTED_SOUND_PATH)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def launch_screamer():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    root.bind("<Escape>", lambda e: root.destroy())

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    img = Image.open(SELECTED_IMAGE_PATH)
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.pack()

    sound_thread = threading.Thread(target=play_selected_sound)
    sound_thread.start()

    root.mainloop()

if __name__ == "__main__":
    while True:
        RANDOM_DELAY_SECONDS = random.randint(1, 3600)  # Délai aléatoire entre 1 et 3600 secondes
        IS_SHINY_EVENT = random.randint(1, SHINY_PROBABILITY_RANGE) == 1
        SELECTED_IMAGE_PATH = SHINY_IMAGE_PATH if IS_SHINY_EVENT else SCREAMER_IMAGE_PATH
        SELECTED_SOUND_PATH = SHINY_SOUND_PATH if IS_SHINY_EVENT else SCREAMER_SOUND_PATH

        print("Lancement du screamer dans", RANDOM_DELAY_SECONDS, "secondes")
        time.sleep(RANDOM_DELAY_SECONDS)
        launch_screamer()
