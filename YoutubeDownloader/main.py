import threading

import customtkinter
import pytube.request
from googleapiclient.discovery import build
from moviepy.editor import *
from tkinter import ttk

import TabView
import YoutubeDownloader
import customtkinter as tk
from PIL import Image, ImageTk
import io
from ProgressBar import ProgressBar
import cv2
import json
import pytube.exceptions
import TabView as tf

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

API_KEY = os.environ.get("YT-API")
pytube.request.default_range_size = 1000000

not_calling = 2
call_counter = 0

thumbnail_path = "./Images/Thumbnail.png"
logo_path = "./Images/YtLogo.png"

thumbnail_frame_color = "#E5E8EB"
inital_text_on_entry = "Inserire URL"

def start_download(pb):
    threading.Thread(target=lambda: download_video(pb)).start()

def start_search(link ,service, thumbnail_label,root, frames):
    threading.Thread(target=lambda: search_videos(link, service,thumbnail_label,root, frames)).start()

def start_resize_image_on_resize_event(event, label, img_path):
    threading.Thread(target = lambda: resize_image_on_resize_event(event, label, img_path)).start()

def show_image_from_path(root, image_path, lable):

    img = Image.open(image_path)
    img = img.resize((root.winfo_width(), root.winfo_height()), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)

    root.pack_propagate(False)

    lable.configure(image=img)
    lable.image = img
    lable.pack_propagate(False)

    lable.pack()


def show_image_from_data(image_data, thumbnail_img, frame):
    img = Image.open(io.BytesIO(image_data))
    #TODO: black borders not removed
    # img = remove_black_borders(thumbnail_path)
    img.save(thumbnail_path)
    img = img.resize((frame.winfo_width(), frame.winfo_height()), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)


    frame.pack_propagate(False)

    thumbnail_img.configure(image=img)
    thumbnail_img.image = img
    thumbnail_img.pack_propagate(False)

    thumbnail_img.pack()


def remove_black_borders(image_path):
    def remove_black_borders(image_path):
        # Carica l'immagine a colori
        original_image = cv2.imread(image_path)

        # Converti l'immagine in scala di grigi
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Binarizza l'immagine, convertendo i pixel neri in bianchi e il contenuto dell'immagine in nero
        _, threshold_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

        # Trova i contorni nell'immagine binarizzata
        contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Trova il contorno più grande con un'area simile all'area dell'immagine completa
        max_contour_area = 0
        max_contour = None
        for contour in contours:
            contour_area = cv2.contourArea(contour)
            if contour_area > max_contour_area and contour_area > 0.95 * gray_image.size:
                max_contour_area = contour_area
                max_contour = contour

        # Calcola i limiti del contorno più grande
        x, y, w, h = cv2.boundingRect(max_contour)

        # Ritaglia l'immagine originale utilizzando i limiti del contorno più grande
        cropped_image = original_image[y:y + h, x:x + w]

        cv2.imwrite(image_path, cropped_image)

    return Image.open(image_path)

def resize_image_on_resize_event(event, label, img_path):
    global call_counter

    if call_counter % not_calling == 0:
        # Prendo le dimensioni attuali della finestra
        original_image = Image.open(img_path)
        frame_width = event.winfo_width()
        frame_height = event.winfo_height()

        # Ridimensiono l'immagine per adattarla alle dimensioni della finestra
        resized_image = original_image.resize((frame_width, frame_height), Image.BICUBIC)
        photo = ImageTk.PhotoImage(resized_image)

        # Aggiorno l'immagine nella label
        label.config(image=photo)
        label.image = photo
    call_counter+=1

def get_pl_ids():
    service = build("youtube", "v3", developerKey=API_KEY)
    nextPageToken = None

    while (True):

        list_request = service.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId="PLPV2KyIb3jR6TFcFuzI2bB7TMNIIBpKMQ",
            pageToken=nextPageToken
        )
        list_response = list_request.execute()

        # print(json.dumps(response, indent= 3))

        ls_id = []

        for item in list_response.get("items"):
            ls_id.append(item["contentDetails"]["videoId"])

        print(ls_id)


        vid_request = service.videos().list(
            part="id",
            id=",".join(ls_id)
        )

        vid_response = vid_request.execute()

        print(json.dumps(vid_response, indent = 3))


        nextPageToken = list_response.get("nextPageToken")

        if not nextPageToken:
            break


def download_video(pb):
    YoutubeDownloader.download(pb)
    return

def set_all_frame_color(style, frames):
    frames[0].configure(relief = "solid", borderwidth = 2)
    frames[2].configure(relief = "solid", borderwidth = 2)
    for frame in frames:
        frame.configure(style = style)


def search_videos(link, service, thumbnail_label, root, frames):
    try:
        image_data, info_dict = YoutubeDownloader.get_all_results(link, service)
        style = "search_result_frame.TFrame"
        set_all_frame_color(style, frames)
        show_image_from_data(image_data, thumbnail_label, root)
        visualize_scroll_result_frame(frames[2], info_dict)
    except pytube.exceptions.RegexMatchError:
        print("Errore, video non trovato")

def visualize_scroll_result_frame(root, info_dict):
    info_frame = ttk.Frame(root, style = "search_result_frame.TFrame")
    info_frame.grid(row = 0, column = 0, sticky = "wsen", padx = 0, pady = 0)

    info_frame.grid_rowconfigure(0, weight=1)
    info_frame.grid_rowconfigure(1, weight=1)
    info_frame.grid_rowconfigure(2, weight=1)

    info_frame.grid_columnconfigure(0, weight=1)

    title_lable = tk.CTkLabel(info_frame, text = f"{info_dict['Title']}", fg_color = thumbnail_frame_color, justify = "left", padx = 10, pady = 10, font = ("Roboto", 15) )
    title_lable.grid(row = 0, column = 0, sticky = "w")

    author_lable = tk.CTkLabel(info_frame, text = f"{info_dict['Author']}", fg_color = thumbnail_frame_color, justify = "left", padx = 10, pady = 2)
    author_lable.grid(row = 1, column = 0, sticky = "w")

    lenght_lable = tk.CTkLabel(info_frame, text = f"{info_dict['Length of video']}", fg_color = thumbnail_frame_color, justify = "left", padx = 10, pady = 2)
    lenght_lable.grid(row = 2, column = 0, sticky = "w")

    # scroll_result_frame = sf.ScrollableFrame(root, info_dict)
    # scroll_result_frame.configure(fg_color=thumbnail_frame_color)
    # scroll_result_frame.grid(row=1, column=0, sticky="wsen", padx = 0, pady = 0)

    view_result_frame(root)

def view_result_frame (root):

    result_frame = tf.TabView(root)
    result_frame.configure(fg_color=thumbnail_frame_color)
    result_frame.grid(row = 1, column = 0, sticky = "wsen", padx = 10)



def visualize_MainFrame():
    service = build("youtube", "v3", developerKey=API_KEY)

    # def on_entry_click(event):
    #     print(entry.get())
    #     if entry.get() == inital_text_on_entry:
    #         print("Ciao")
    #         entry.configure(textcolor='black', placeholder_text_color = "URL:")  # Imposta il colore del testo a nero quando inizia l'inserimento
    #
    # def on_focusout(event):
    #     if entry.get() == inital_text_on_entry:
    #         entry.configure(textcolor='black', placeholder_text_color = "URL:")  # Imposta il colore del testo a grigio quando il campo di testo perde il focus

    def get_entry_search(thumbnail_label, root, frames):
        link =  entry.get()
        link = "https://www.youtube.com/watch?v=HrRt3KX3MFQ"
        start_search(link, service,thumbnail_label,root, frames)

    root = tk.CTk()
    root.title("YoutubeDownloader")
    root.geometry("960x540+250+100")

    s = ttk.Style()
    s.configure("thumbnail_frame.TFrame", background = "black")
    s.configure("search_result_frame.TFrame", background = thumbnail_frame_color)

    root.grid_rowconfigure(0, weight = 1)
    root.grid_rowconfigure(1, weight = 2)
    root.grid_rowconfigure(2, weight = 3)

    root.grid_columnconfigure(0, weight = 2)
    root.grid_columnconfigure(1, weight = 3)
    root.grid_columnconfigure(3, weight = 2)

    logo_frame = ttk.Frame(root)#,style = "search_result_frame.TFrame")
    logo_frame.grid(column = 1, row = 0, sticky = "wesn", pady = 20)

    logo_lable = ttk.Label(logo_frame)
    show_image_from_path(logo_frame, logo_path, logo_lable)

    progressbar_frame = ttk.Frame(root)
    progressbar_frame.grid(column=1, row=1, sticky = "we")
    progressbar_frame.grid_columnconfigure(0, weight = 1)
    progressbar_frame.grid_columnconfigure(1, weight = 5)
    progressbar_frame.grid_columnconfigure(2, weight = 1)

    # pb = ProgressBar(progressbar_frame)

    # entry_var = tk.StringVar()
    # entry_var.set("URL: https://www.youtube.com/watch?v=mcdkexoJeDQ")

    # Creazione della text box
    entry = tk.CTkEntry(progressbar_frame, placeholder_text=inital_text_on_entry, text_color="gray")
    # entry.bind('<FocusIn>', on_entry_click)  # Associare l'evento di click per rimuovere il testo predefinito
    # entry.bind('<FocusOut>', on_focusout)  # Associare l'evento di perdita del focus per ripristinare il testo predefinito
    entry.grid(row = 1, column = 1,sticky = "we")

    search_result_frame = ttk.Frame(root)#, style="search_result_frame.TFrame")
    search_result_frame.grid_propagate(False)
    search_result_frame.grid(column=0, row=2, columnspan = 4, sticky = "nswe")

    search_result_frame.rowconfigure(0, weight = 1)

    search_result_frame.columnconfigure(0, weight=2)
    search_result_frame.columnconfigure(1, weight=3)

    thumbnail_frame = ttk.Frame(search_result_frame)#, style = "search_result_frame.TFrame")
    thumbnail_frame.grid(row = 0, column = 0, sticky = "nsew", padx = 50, pady = 40)

    thumbnail_label = ttk.Label(thumbnail_frame)


    thumbnail_label.bind("<Configure>", lambda event = thumbnail_frame, thumbnail_label = thumbnail_label: start_resize_image_on_resize_event(thumbnail_frame,thumbnail_label, thumbnail_path))
    logo_lable.bind("<Configure>", lambda event = logo_frame, logo_lable = logo_lable: start_resize_image_on_resize_event(logo_frame,logo_lable, logo_path))

    search_options_frame = ttk.Frame(search_result_frame)#,style="search_result_frame.TFrame")

    search_options_frame.columnconfigure(0, weight = 1)
    search_options_frame.rowconfigure(0,weight = 1)
    search_options_frame.rowconfigure(1, weight = 2)

    search_options_frame.grid(column = 1, row = 0, sticky = "nsew")

    frames = [search_result_frame, thumbnail_frame, search_options_frame]
    search_button = tk.CTkButton(progressbar_frame, text="Search", command = lambda: get_entry_search(thumbnail_label, thumbnail_frame, frames), fg_color="#749BC2")
    search_button.grid(column=2, row=1)

    # view_result_frame(search_options_frame)
    # download_button = tk.CTkButton(progressbar_frame, text="Download", command=lambda: start_download(pb))
    # download_button.grid(column=2, row=1, padx = 10)

    root.mainloop()


def main():
    # get_pl_ids()
    visualize_MainFrame()


if __name__ == "__main__":
    main()
