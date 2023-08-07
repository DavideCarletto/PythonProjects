import customtkinter as tk
import Slider
from collections import OrderedDict

class TabView(tk.CTkTabview):
    def __init__(self, master, main_frame, **kwargs):
        try:
            self.info_dict = kwargs.pop("info_dict")
            self.set_res_list_in_dict()
        except:
            print("Errore Nella creazione del TabView")

        super().__init__(master, **kwargs)

        self.add("Video and audio")
        self.add("Only video")
        self.add("Only audio")
        self.set("Video and audio")

        self.main_frame = main_frame

        self.video_ext_menu = self.initialize_ext_menu("video_res_dict")
        self.audio_ext_menu = self.initialize_ext_menu("audio_res_dict")

        self.video_res_slider = self.initialize_slider("video_res_dict")
        self.audio_res_slider = self.initialize_slider("audio_res_dict")

        self.first_video_ext = next(iter(self.info_dict["video_res_dict"]))
        self.first_audio_ext = next(iter(self.info_dict["audio_res_dict"]))

        self.video_ext_menu.set(self.first_video_ext)
        self.video_ext_menu.configure(command=self.configure_video_slider)

        self.audio_ext_menu.set(self.first_audio_ext)
        self.audio_ext_menu.configure(command=self.configure_audio_slider)

        self.download_btn = None
        self.video_res_list = None
        self.audio_res_list = None

        self.show_tab_elements()
        self.configure(command=self.show_tab_elements)

    def show_tab_elements(self):
        self.clear_frame(self.tab(self.get()))
        rowcount = 0

        self.tab(self.get()).grid_rowconfigure(0, weight=1)
        self.tab(self.get()).grid_rowconfigure(1, weight=1)
        self.tab(self.get()).grid_rowconfigure(2, weight=1)

        self.tab(self.get()).grid_columnconfigure(0, weight=2)
        self.tab(self.get()).grid_columnconfigure(1, weight=1)
        self.tab(self.get()).grid_columnconfigure(2, weight=1)

        self.download_btn = None

        if "video" in self.get().lower() and "audio" in self.get().lower():
            self.download_btn = self.initialize_download_btn()
            self.download_btn.grid(row=1, column=2, sticky="we")

        if "video" in self.get().lower():
            self.video_ext_menu = self.initialize_ext_menu("video_res_dict")
            self.video_res_slider = self.initialize_slider("video_res_dict")
            self.video_ext_menu.configure(command=self.configure_video_slider)
            self.video_ext_menu.set(self.first_video_ext)
            self.video_ext_menu.grid(row=rowcount, column=1)
            self.video_res_slider.grid(row=rowcount, column=0, sticky="we", pady=30)

            rowcount += 2

        if "audio" in self.get().lower():
            self.audio_ext_menu = self.initialize_ext_menu("audio_res_dict")
            self.audio_res_slider = self.initialize_slider("audio_res_dict")

            self.audio_ext_menu.configure(command=self.configure_audio_slider)
            self.audio_ext_menu.set(self.first_audio_ext)

            self.audio_ext_menu.grid(row=rowcount, column=1)
            self.audio_res_slider.grid(row=rowcount, column=0, sticky="we", pady=30)

        if self.download_btn is None:
            self.download_btn = self.initialize_download_btn()
            self.download_btn.grid(row=0, column=3)

    def configure_video_slider(self, val):
        self.video_ext_menu.set(val)
        self.configure_slider(self.video_res_slider, self.info_dict["video_res_dict"][f"{self.video_ext_menu.get()}"])

    def configure_audio_slider(self, val):
        self.audio_ext_menu.set(val)
        self.configure_slider(self.audio_res_slider, self.info_dict["audio_res_dict"][f"{self.audio_ext_menu.get()}"])

    def configure_slider(self, slider, value_list):
        slider.set_value_list(value_list)
        if len(value_list) > 1:
            slider.configure(from_=min(value_list), to=max(value_list))

        slider.set(max(value_list))

    def initialize_slider(self, key):

        if key == "audio_res_dict" and "mp4" in self.info_dict[key]:
            new_ext = "mp3"
            value = self.info_dict[key]["mp4"]
            self.info_dict[key][new_ext] = value

            del self.info_dict[key]["mp4"]

            ordered_keys = sorted(self.info_dict[key].keys())
            self.info_dict[key] = OrderedDict((chiave, self.info_dict[key][chiave]) for chiave in ordered_keys)
            first_ext = next(iter(self.info_dict[key]))

        first_ext = next(iter(self.info_dict[key]))
        first_res_list = self.info_dict[key][f"{first_ext}"] if first_ext in self.info_dict[key] else None
        slider = Slider.Slider(self.tab(self.get()), value_list=first_res_list)

        if len(first_res_list) > 1:
            slider.configure(from_=min(first_res_list), to=max(first_res_list))

        return slider

    def initialize_ext_menu(self, key):
        ext_menu = tk.CTkOptionMenu(self.tab((self.get())), values=list(self.info_dict[key].keys()))

        return ext_menu

    def initialize_download_btn(self):
        return tk.CTkButton(self.tab(self.get()), text="Download", fg_color="#C84B31",
                            command=self.main_frame.start_download)

    def set_res_list_in_dict(self):
        video_res_list = self.info_dict.pop("video_res_list")
        audio_res_list = self.info_dict.pop("audio_res_list")

        self.info_dict["video_res_dict"] = dict()
        self.info_dict["audio_res_dict"] = dict()

        for video_res_tuple in video_res_list:
            video_res = video_res_tuple[0]
            video_ext = video_res_tuple[1]

            video_ext = video_ext.replace("video/", "")
            video_res = int(video_res.replace("p", ""))

            if f"{video_ext}" not in self.info_dict["video_res_dict"]:
                self.info_dict["video_res_dict"][f"{video_ext}"] = []

            self.info_dict["video_res_dict"][f"{video_ext}"].append(video_res) if video_res not in \
                                                                                  self.info_dict["video_res_dict"][
                                                                                      f"{video_ext}"] else None
            self.info_dict["video_res_dict"][f"{video_ext}"].sort(reverse=True)

        for audio_res_tuple in audio_res_list:
            audio_res = audio_res_tuple[1]
            audio_ext = audio_res_tuple[0]

            audio_res = int(audio_res.replace("kbps", ""))

            if f"{audio_ext}" not in self.info_dict["audio_res_dict"]:
                self.info_dict["audio_res_dict"][f"{audio_ext}"] = []

            self.info_dict["audio_res_dict"][f"{audio_ext}"].append(audio_res) if audio_res not in \
                                                                                  self.info_dict["audio_res_dict"][
                                                                                      f"{audio_ext}"] else None
            self.info_dict["audio_res_dict"][f"{audio_ext}"].sort(reverse=True)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.grid_forget()

    def get_status(self):
        only_audio = True
        only_video = True

        if "video" in self.get().lower():
            only_audio = False
        if "audio" in self.get().lower():
            only_video = False

        return only_video, only_audio
