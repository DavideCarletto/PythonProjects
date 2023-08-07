from proglog import ProgressLogger
import customtkinter as tk
from tkinter import ttk
from AutoScrollLabel import AutoScrollLabel
class ProgressBar(ProgressLogger):
    def __init__(self, root):
        super(ProgressBar, self).__init__(init_state=None)
        self.root = root

        self.progress_label = AutoScrollLabel(self.root, text="", text_color="#565B5E", justify = "left")
        self.percentage_label = tk.CTkLabel(self.root, text="")

        self.pb = tk.CTkProgressBar(
            root,
            orientation='horizontal',
            mode='determinate',
            progress_color="green",
            determinate_speed=3
        )

        self.pb.set(0)

        self.download_status_lable = tk.CTkLabel(self.root, text_color="#2aaa45")
        self.audio_converting_lable = tk.CTkLabel(self.root, text = "Converting audio to mp3...", text_color="#565B5E")
        self.merging_video_audio_lable = tk.CTkLabel(self.root, text="Merging video and audio...", text_color="#565B5E")

    def callback(self, **kw):
        super(ProgressBar, self).callback(**kw)

        if (kw["merge"] == True):
            print("merging video and audio file:", end=" ")

        print(f"{kw['total']}/100")

    def update_progress(self, percentage, offset, factor = 1):
        while(self.pb.get() * 100 < percentage/factor+ offset):
            self.pb.set(self.pb.get()+(0.005/factor))
            self.pb.update()
            self.percentage_label.configure(text=f"{int(self.pb.get()*100)}%")
            print(percentage/factor+offset)

        if self.pb.get()*100 >= 100:
            self.progress_label.after(1000, self.progress_label.stop_scrolling())
            self.progress_label.lable.grid_forget()
            self.progress_label.frame.grid_forget()
            self.download_status_lable.grid(row = 1, column = 1, sticky ="we")

    def show(self, row, column):
        self.progress_label.grid(row=1, column=1, sticky="we", columnspan = 3)
        self.progress_label.show(row = 1, column=1)
        self.progress_label.grid_configure(sticky="s")
        self.progress_label.grid_propagate(False)
        self.progress_label.set_text("")
        self.percentage_label.grid(row=0, column=2, sticky="w", padx=10)
        self.pb.grid(column=column, row=row, sticky = "we")


    def show_text(self, lable):
        self.progress_label.lable.grid_forget()
        self.progress_label.frame.grid_forget()
        lable.grid(row=1, column=1, sticky="we")

    def clear(self):
        self.progress_label.grid_forget()
        self.percentage_label.grid_forget()
        self.download_status_lable.grid_forget()
        self.audio_converting_lable.grid_forget()
        self.merging_video_audio_lable.grid_forget()

