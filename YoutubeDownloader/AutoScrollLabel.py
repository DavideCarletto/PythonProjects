import customtkinter as tk

class AutoScrollLabel(tk.CTkLabel):
    def __init__(self, master, text, text_color, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.text = text
        self.scroll_delay = 75  # Millisecondi tra uno spostamento e l'altro
        self.scroll_speed = 2    # Numero di pixel di spostamento ad ogni passo
        self.current_offset = 0  # Offset corrente del testo
        self.text_color = text_color

        self.scrolling = False
        # Crea un frame contenente la label con il testo
        self.frame = tk.CTkFrame(self.master, height=20)
        self.frame.grid_propagate(False)
        # self.frame.grid(row=1, column=1, sticky="ewsn")
        # Imposta il layout del frame utilizzando il grid layout
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Crea la label all'interno del frame
        self.lable = tk.CTkLabel(self.frame, text=self.text, justify="center", anchor="w", text_color=text_color)
        self.lable.grid_configure(row=0, column=0, sticky="ew")

        # Inizia il loop per lo scorrimento automatico


    def show(self, row, column):
        # Crea la label all'interno del frame
        self.frame.grid(row=row, column=column, sticky = "n")


    def auto_scroll(self):
        if self.scrolling:
            # Sposta la label orizzontalmente
            self.current_offset += self.scroll_speed
            self.lable.place(x=-self.current_offset, y=0)

            # Se il testo ha superato il limite sinistro, riportalo all'inizio
            if self.current_offset >= self.frame.winfo_reqwidth():
                self.current_offset = -self.frame.winfo_reqwidth()

            # Richiama la funzione dopo un ritardo
            self.after(self.scroll_delay, self.auto_scroll)

    def set_text(self, text):
        self.lable.configure(text = text)

    def start_scrolling(self):
        self.scrolling = True
        self.auto_scroll()

    def stop_scrolling(self):
        self.scrolling = False

    def set_fg_color(self, color):
        self.frame.configure(fg_color=color)

    def set_text_color(self, color):
        self.lable.configure(text_color= color)