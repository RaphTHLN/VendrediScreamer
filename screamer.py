import time
import pygame
import random
import threading
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys


def launch_screamer():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.attributes('-topmost', True)

    img = Image.open("screamer.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img = img.resize((screen_width, screen_height), resample=Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=tk_img)
    panel.pack()

    def close(event=None):
        root.destroy()

    root.bind("<Escape>", close)
    root.mainloop()

def play_screamer_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("screamer.mp3")  # ou .wav
    pygame.mixer.music.play()


while True: 
    delay = random.randint(1, 3600)
    print(f"Attente de {delay} secondes avant le screamer... 😈")
    time.sleep(delay)
    threading.Thread(target=play_screamer_sound).start()
    launch_screamer()