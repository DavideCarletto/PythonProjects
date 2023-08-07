import customtkinter as ctk
import threading
import time

class AnimatedFrame(ctk.CTkFrame):
    def __init__(self, parent,**kwargs):
        super().__init__(parent, **kwargs)
        self.grid(row=0, column=0, sticky="ewsn")

    def start_animation(self, duration):
        print(self.winfo_height())
        t = threading.Thread(target=self.animate_frame(self.winfo_height(), 0, duration))
        t.start()

    def animate_frame(self, start_y, end_y, duration=0.01):
        # Calcola il numero di frame da generare durante l'animazione
        frames = int(duration * 120)  # Supponiamo 60 FPS (frame per secondo)

        # Calcola il cambiamento di posizione y per ogni frame
        y_step = (end_y - start_y) / frames

        # Esegui l'animazione
        for i in range(frames + 1):
            y_pos = start_y + i * y_step
            self.place_configure(y=int(y_pos))
            self.update()
            time.sleep(1 / 60)  # Attendi per simulare i 60 FPS
