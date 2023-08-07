import customtkinter as tk
from PIL import Image, ImageTk, ImageSequence
from AnimatedFrame import  AnimatedFrame
import AnimatedFrame
import TabView as tf
import main
from AutoScrollLabel import AutoScrollLabel
from ProgressBar import ProgressBar


initial_text_on_entry = "Inserire URL"
logo_path = "./Images/blue-download-icon-3.jpg"
yt_logo_path = "./Images/YtLogo.png"


class MainFrame(tk.CTkFrame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=2)

        self.grid_propagate(False)

        self.title_frame = tk.CTkFrame(self, height=100)  # ,style = "search_result_frame.TFrame")

        self.title_frame.grid_propagate(False)

        self.title_frame.grid_columnconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(1, weight=1)
        self.title_frame.grid(column=1, row=0, sticky="wesn")

        # TODO: da sistemare le immagini
        self.logo_download_frame = tk.CTkFrame(self.title_frame, width = 75, height = 75)
        self.logo_download_frame.grid(column=0, row=1, sticky = "e")
        self.logo_download_label = tk.CTkLabel(self.logo_download_frame, text="")

        self.logo_yt_frame = tk.CTkFrame(self.title_frame, height = 100)
        self.logo_yt_frame.grid_propagate(False)
        self.logo_yt_frame.grid(column=1, row=1, sticky="wns")
        self.logo_yt_label = tk.CTkLabel(self.logo_yt_frame, text="")

        self.progressbar_frame = tk.CTkFrame(self, height = 100)
        self.progressbar_frame.grid_propagate(False)
        self.progressbar_frame.grid(column=1, row=1, sticky="we")
        self.progressbar_frame.grid_columnconfigure(0, weight=1)
        self.progressbar_frame.grid_columnconfigure(1, weight=3)
        self.progressbar_frame.grid_columnconfigure(2, weight=1)
        self.progressbar_frame.grid_rowconfigure(0, weight = 1)

        self.progress_bar = ProgressBar(self.progressbar_frame)

        self.entry = tk.CTkEntry(self.progressbar_frame, placeholder_text=initial_text_on_entry)
        self.entry.grid(row=0, column=1, sticky="we")

        #TODO: container usefull for animation (not working)
        self.search_result_frame_container = tk.CTkFrame(self)
        self.search_result_frame_container.grid_propagate(False)
        self.search_result_frame_container.grid(row=2, column=0, columnspan=4, sticky="wens")

        self.search_result_frame_container.grid_columnconfigure(0, weight = 1)
        self.search_result_frame_container.grid_rowconfigure(0, weight = 1)

        self.search_result_frame = AnimatedFrame.AnimatedFrame(self.search_result_frame_container, width=10, height=10)

        self.search_result_frame.rowconfigure(0, weight=1)

        self.search_result_frame.columnconfigure(0, weight=1)
        self.search_result_frame.columnconfigure(1, weight=2)

        self.thumbnail_frame = tk.CTkFrame(self.search_result_frame)
        self.thumbnail_frame.grid_propagate(False)
        self.thumbnail_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=70)

        self.thumbnail_label = tk.CTkLabel(self.thumbnail_frame, text="")

        self.search_options_frame = tk.CTkFrame(self.search_result_frame)
        self.search_options_frame.columnconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(1, weight=2)

        self.search_options_frame.grid(column=1, row=0, sticky="nsew")

        self.search_button = tk.CTkButton(self.progressbar_frame, text="Search")
        self.show_search_btn()

        search_loading_gif = Image.open("Images/loading_spinner.gif")
        self.search_loading_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(search_loading_gif)]
        self.search_loading_label = tk.CTkLabel(self.progressbar_frame, text="")

        download_loading_gif = Image.open("Images/loading_fountain.gif")
        self.download_loading_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(download_loading_gif)]
        self.searching_lable = tk.CTkLabel(self.progressbar_frame, text="")

        self.title_lable = None
        self.author_label = None
        self.result_frame = None
        self.title = None
        self.loading_lable = None
        self.download_loading_label = None

    def visualize_scroll_result_frame(self, root, info_dict):

        self.title = info_dict["Title"]

        self.title_lable = AutoScrollLabel(root, text=f"{info_dict['Title']}", text_color="white", justify="left")
        self.author_label = tk.CTkLabel(root,
                                        text=f"Author: {info_dict['Author']}\t Lenght:{info_dict['Length of video']} sec",
                                        justify="left", font=("Roboto", 15))

        self.title_lable.lable.configure(font=("Roboto", 15))
        self.title_lable.set_fg_color("#343638")
        self.title_lable.frame.grid_configure(pady = 2, padx=20, sticky = "we")
        self.title_lable.show(row=0, column=0)
        self.title_lable.start_scrolling()
        self.author_label.grid(row=0, column=1, pady=5, padx=20)

        self.view_result_frame(root, info_dict)

    def view_result_frame(self, root, info_dict):
        self.result_frame = tf.TabView(root, self, info_dict=info_dict)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(row=1, column=0, sticky="wsen", padx=10, pady=10, columnspan=3)

    def start_download(self):
        self.show_loading_download_lable()
        link = self.entry.get()
        if link == "":
            link = "https://www.youtube.com/watch?v=dtwe19VLIR4"

        res = self.result_frame.video_res_slider.value
        abr = self.result_frame.audio_res_slider.value
        only_video, only_audio = self.result_frame.get_status()
        self.progress_bar.download_status_lable.configure(text ="Download completed!")
        self.progress_bar.download_status_lable.grid_forget()
        main.start_download(self, self.progress_bar, link, res, abr, only_audio, only_video, self.title)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.grid_forget()

    def update_gif(self, label, frames, frame_number=0):
        # Aggiorna l'immagine del frame corrente
        label.configure(image=frames[frame_number])
        frame_number = (frame_number + 1) % len(frames)
        self.after(35, self.update_gif, label, frames, frame_number)

    def show_searching_lable(self):
        self.search_loading_label.grid(row = 0, column = 2)
        self.searching_lable.configure(text = "Searching...", text_color="#565B5E")
        self.searching_lable.grid(row = 0, column  = 1, sticky = "s")
        self.update_gif(self.search_loading_label, self.search_loading_frames)

    def show_search_btn(self):
        self.search_button.grid(column=2, row=0)

    def update_on_search_found(self):
        self.search_loading_label.grid_forget()
        self.show_search_btn()
        self.searching_lable.configure(text="Video found!", text_color="#2aaa45")


    def show_loading_download_lable(self):
        self.clear_frame(self.result_frame.tab(self.result_frame.get()))
        self.loading_lable = tk.CTkLabel(self.result_frame.tab(self.result_frame.get()))
        self.download_loading_label = tk.CTkLabel(self.result_frame.tab(self.result_frame.get()), text="")
        self.download_loading_label.grid(column = 0, row = 1, columnspan = 3, sticky = "we")
        self.loading_lable.configure(text = "Loading...", text_color = "#565B5E")
        self.loading_lable.grid(row = 1, column  = 0, sticky = "sew", columnspan = 3)
        self.update_gif(self.download_loading_label, self.download_loading_frames)

    def delete_loading_download_label(self):
        self.clear_frame(self.result_frame.tab(self.result_frame.get()))
        self.result_frame.show_tab_elements()

    def show_search_frame(self):
        self.progress_bar.pb.grid_forget()
        self.search_button.grid(column=2, row=0)
        self.entry.grid(row=0, column=1, sticky="we")