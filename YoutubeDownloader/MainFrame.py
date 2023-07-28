import customtkinter as tk
import TabView as tf

thumbnail_frame_color = "#E5E8EB"

inital_text_on_entry = "Inserire URL"
logo_path = "./Images/blue-download-icon-3.jpg"
yt_logo_path = ".\Images\YtLogo.png"

class MainFrame(tk.CTkFrame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # s = ttk.Style()
        # s.configure("thumbnail_frame.TFrame", background="black")
        # s.configure("search_result_frame.TFrame", background=thumbnail_frame_color)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=3)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=2)

        self.grid_propagate(False)

        self.title_frame = tk.CTkFrame(self)  # ,style = "search_result_frame.TFrame")
        self.title_frame.grid_propagate(False)

        self.title_frame.grid_columnconfigure(0, weight = 1)
        self.title_frame.grid_columnconfigure(1, weight = 2)

        self.title_frame.grid_rowconfigure(0, weight = 2)

        self.title_frame.pack_propagate(False)
        self.title_frame.grid(column=1, row=0, sticky="we")

        #TODO: da sistemare le immagini
        self.logo_frame = tk.CTkFrame(self.title_frame)
        self.logo_frame.pack_propagate(False)
        self.logo_frame.grid(column = 0, row = 0, sticky = "w", padx = (50,0), pady = (70, 10), columnspan = 1)

        self.logo_lable = tk.CTkLabel(self.logo_frame, text = "")

        self.title_lable = tk.CTkLabel(self.title_frame, text = "")
        self.title_lable.pack_propagate(False)
        self.title_lable.grid(column = 1, row = 0, sticky = "e", padx = (0,50), pady = (70, 10),columnspan = 1)

        self.progressbar_frame = tk.CTkFrame(self)
        self.progressbar_frame.grid(column=1, row=1, sticky="we")
        self.progressbar_frame.grid_columnconfigure(0, weight=1)
        self.progressbar_frame.grid_columnconfigure(1, weight=5)
        self.progressbar_frame.grid_columnconfigure(2, weight=1)

        # pb = ProgressBar(progressbar_frame)

        self.entry = tk.CTkEntry(self.progressbar_frame, placeholder_text=inital_text_on_entry)
        self.entry.grid(row=1, column=1, sticky="we")

        self.search_result_frame = tk.CTkFrame(self)  # , style="search_result_frame.TFrame")
        self.search_result_frame.grid_propagate(False)
        self.search_result_frame.grid(column=0, row=2, columnspan=4, sticky="nswe")

        self.search_result_frame.rowconfigure(0, weight=1)

        self.search_result_frame.columnconfigure(0, weight=2)
        self.search_result_frame.columnconfigure(1, weight=3)

        self.thumbnail_frame = tk.CTkFrame(self.search_result_frame)  # , style = "search_result_frame.TFrame")
        self.thumbnail_frame.grid_propagate(False)
        self.thumbnail_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=40)

        self.thumbnail_label = tk.CTkLabel(self.thumbnail_frame, text = "")

        self.search_options_frame = tk.CTkFrame(self.search_result_frame)  # ,style="search_result_frame.TFrame")
        self.search_options_frame.columnconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(0, weight=1)
        self.search_options_frame.rowconfigure(1, weight=2)

        self.search_options_frame.grid(column=1, row=0, sticky="nsew")

        self.search_button = tk.CTkButton(self.progressbar_frame, text="Search")
        self.search_button.grid(column=2, row=1)

        self.video_info_lable = None
        self.result_frame = None
        # view_result_frame(search_options_frame)
        # download_button = tk.CTkButton(progressbar_frame, text="Download", command=lambda: start_download(pb))
        # download_button.grid(column=2, row=1, padx = 10)


    def visualize_scroll_result_frame(self, root, info_dict):
        self.video_info_lable = tk.CTkLabel(root, text=f"{info_dict['Title']}, \t{info_dict['Author']}, \t{info_dict['Length of video']} sec", justify="left", font=("Roboto", 15))
        self.video_info_lable.grid(row=0, column=0, sticky="wesn", padx=10, pady=5)

        self.view_result_frame(root, info_dict)

    def view_result_frame(self,root, info_dict):
        self.result_frame = tf.TabView(root, info_dict=info_dict)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(row=1, column=0, sticky="wsen", padx=10, pady = 10)