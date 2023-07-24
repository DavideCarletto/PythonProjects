import customtkinter as tk

class TabView(tk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Video and audio")
        self.add("Only video")
        self.add("Only audio")
        self.set("Video and audio")

        video_and_audio_btn = tk.CTkButton(self.tab("Video and audio"))
        only_video_btn = tk.CTkButton(self.tab("Only video"))
        only_audio_btn = tk.CTkButton(self.tab("Only audio"))

        video_and_audio_btn.grid(row = 0,column=0)
        only_video_btn.grid(row = 0,column=1)
        only_audio_btn.grid(row = 0, column=2)