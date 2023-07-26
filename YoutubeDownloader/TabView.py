import customtkinter as tk
import Slider


class TabView(tk.CTkTabview):
    def __init__(self, master, **kwargs):
        try:
            self.video_res_list = kwargs.pop("video_res_list")
            self.audio_res_list = kwargs.pop("audio_res_list")
        except:
            self.video_res_list = None
            self.audio_res_list = None

        super().__init__(master, **kwargs)

        self.add("Video and audio")
        self.add("Only video")
        self.add("Only audio")
        self.set("Video and audio")

        self.show_tab_elements()
        self.configure(command = self.show_tab_elements)

    def show_tab_elements(self):

        rowcount= 0

        self.tab(self.get()).grid_rowconfigure(0, weight=1)
        self.tab(self.get()).grid_rowconfigure(1, weight=1)

        self.tab(self.get()).grid_columnconfigure(0, weight=2)
        self.tab(self.get()).grid_columnconfigure(1, weight=3)

        if "video" in self.get().lower() and self.video_res_list is not None:
            video_res_slider = Slider.Slider(self.tab(self.get()), value_list=self.video_res_list, from_=min(self.video_res_list), to=max(self.video_res_list))
            video_res_slider.grid(row=rowcount, column=0, sticky="we", pady=30)
            rowcount+=1

        if "audio" in self.get().lower() and self.audio_res_list is not None:
            audio_res_slider = Slider.Slider(self.tab(self.get()), value_list=self.audio_res_list, from_=min(self.audio_res_list), to=max(self.audio_res_list))
            audio_res_slider.grid(row=rowcount, column=0, sticky="we", pady = 30)
