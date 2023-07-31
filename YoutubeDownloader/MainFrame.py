import customtkinter as tk
import TabView as tf
import main
from ProgressBar import ProgressBar

thumbnail_frame_color = "#E5E8EB"

inital_text_on_entry = "Inserire URL"
logo_path = "./Images/blue-download-icon-3.jpg"
yt_logo_path = ".\Images\YtLogo.png"


class MainFrame(tk.CTkFrame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=3)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=2)

        self.grid_propagate(False)

        self.title_frame = tk.CTkFrame(self, fg_color="white")  # ,style = "search_result_frame.TFrame")

        self.title_frame.grid_propagate(False)

        self.title_frame.grid_columnconfigure(0,weight = 1)
        self.title_frame.grid_columnconfigure(1,weight = 2)

        self.title_frame.grid_rowconfigure(0, weight = 1)
        self.title_frame.grid_rowconfigure(1, weight = 2)
        self.title_frame.grid_rowconfigure(2, weight = 1)

        self.title_frame.grid(column=1, row=0, sticky="we")

        #TODO: da sistemare le immagini
        self.logo_download_frame = tk.CTkFrame(self.title_frame)
        self.logo_download_frame.grid(column = 0, row = 1, sticky = "we")
        self.logo_download_lable = tk.CTkLabel(self.logo_download_frame, text = "")

        self.logo_yt_frame = tk.CTkFrame(self.title_frame)
        self.logo_yt_frame.grid_propagate(False)
        self.logo_yt_frame.grid(column = 1, row = 1, sticky = "wens")
        self.logo_yt_lable = tk.CTkLabel(self.logo_yt_frame, text = "")

        self.progressbar_frame = tk.CTkFrame(self)
        self.progressbar_frame.grid(column=1, row=1, sticky="we")
        self.progressbar_frame.grid_columnconfigure(0, weight=1)
        self.progressbar_frame.grid_columnconfigure(1, weight=5)
        self.progressbar_frame.grid_columnconfigure(2, weight=1)

        self.pb = ProgressBar(self.progressbar_frame)

        self.entry = tk.CTkEntry(self.progressbar_frame, placeholder_text=inital_text_on_entry)
        self.entry.grid(row=1, column=1, sticky="we")

        self.search_result_frame = tk.CTkFrame(self)
        self.search_result_frame.grid_propagate(False)
        self.search_result_frame.grid(column=0, row=2, columnspan=4, sticky="nswe")

        self.search_result_frame.rowconfigure(0, weight=1)

        self.search_result_frame.columnconfigure(0, weight=1)
        self.search_result_frame.columnconfigure(1, weight=2)

        self.thumbnail_frame = tk.CTkFrame(self.search_result_frame)
        self.thumbnail_frame.grid_propagate(False)
        self.thumbnail_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=70)

        self.thumbnail_label = tk.CTkLabel(self.thumbnail_frame, text = "")

        self.search_options_frame = tk.CTkFrame(self.search_result_frame)
        self.search_options_frame.columnconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(1, weight=2)

        self.search_options_frame.grid(column=1, row=0, sticky="nsew")

        self.search_button = tk.CTkButton(self.progressbar_frame, text="Search")
        self.search_button.grid(column=2, row=1)

        self.video_info_lable = None
        self.result_frame = None


    def visualize_scroll_result_frame(self, root, info_dict):
        self.title_lable = tk.CTkLabel(root, text=f"{info_dict['Title']}", justify="left", font=("Roboto", 15))
        self.author_lable = tk.CTkLabel(root, text=f"Author: {info_dict['Author']}\t Lenght:{info_dict['Length of video']} sec", justify="left", font=("Roboto", 15))

        self.title_lable.grid(row=0, column=0, sticky="w", pady = 5, padx = 20)
        self.author_lable.grid(row=0, column=1, pady = 5, padx = 20)

        self.view_result_frame(root, info_dict)

    def view_result_frame(self,root, info_dict):
        self.result_frame = tf.TabView(root, self, info_dict=info_dict)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(row=1, column=0, sticky="wsen", padx=10, pady = 10, columnspan = 3)

    def start_download(self):
        self.clear_frame(self.progressbar_frame)
        self.pb.show(row = 2, column = 1)
        link = "https://www.youtube.com/shorts/xLec1zTahlM"
        res = self.result_frame.video_res_slider.value
        abr = self.result_frame.audio_res_slider.value
        only_video, only_audio = self.result_frame.get_status()
        main.start_download(self.pb, link, res, abr, only_audio, only_video)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.grid_forget()
