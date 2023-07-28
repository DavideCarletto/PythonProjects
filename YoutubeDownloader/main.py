import threading

import pytube.request
from googleapiclient.discovery import build
from moviepy.editor import *

import MainFrame
import TabView
import YoutubeDownloader
import customtkinter as tk
from PIL import Image, ImageTk
import io
from ProgressBar import ProgressBar
import cv2
import json
import pytube.exceptions

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

API_KEY = os.environ.get("YT-API")
pytube.request.default_range_size = 1000000

not_calling = 2
call_counter = 0

thumbnail_path = "./Images/Thumbnail.png"
# logo_path = "./Images/blue-download-icon-3.jpg"

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



def start_resize_image_on_resize_event(event, label, img_path, resize_factor = 1):
    threading.Thread(target=lambda: resize_image_on_resize_event(event, label, img_path, resize_factor)).start()

def resize_image_on_resize_event(event, label, img_path, resize_factor):
    global call_counter
    if call_counter % not_calling == 0:
        # Prendo le dimensioni attuali della finestra
        original_image = Image.open(img_path)
        frame_width = event.winfo_width()
        frame_height = event.winfo_height()

        # Ridimensiono l'immagine per adattarla alle dimensioni della finestra
        resized_image = original_image.resize((int(frame_width/resize_factor), int(frame_height/resize_factor)), Image.BICUBIC)
        photo = ImageTk.PhotoImage(resized_image)

        # Aggiorno l'immagine nella label
        label.configure(image=photo)
        label.image = photo
    call_counter += 1

def start_search(link, service, thumbnail_label, root, frames, main_frame):
    threading.Thread(target=lambda: search_videos(link, service, thumbnail_label, root, frames, main_frame)).start()

def search_videos(link, service, thumbnail_label, root, frames, main_frame):
    print("Inizio ricerca")
    try:
        image_data, info_dict = YoutubeDownloader.get_all_results(link, service)
        show_image_from_data(image_data, thumbnail_label, root)
        main_frame.visualize_scroll_result_frame(frames[2], info_dict)
        set_all_frame_color("#343638", frames)
    except pytube.exceptions.RegexMatchError:
        print("Errore, video non trovato")

def set_all_frame_color(color, frames):
    frames[0].configure(border_width=1, border_color="white")
    frames[2].configure(border_width=1, border_color="white")
    for frame in frames:
        frame.configure(fg_color=color)

def show_image_from_data(image_data, thumbnail_img, frame):
    img = Image.open(io.BytesIO(image_data))
    # TODO: black borders not removed
    # img = remove_black_borders(thumbnail_path)
    img.save(thumbnail_path)
    img = img.resize((frame.winfo_width(), frame.winfo_height()), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)

    frame.pack_propagate(False)

    thumbnail_img.configure(image=img)
    thumbnail_img.image = img
    thumbnail_img.pack_propagate(False)

    thumbnail_img.pack()

def show_image_from_path(root, image_path, lable):

    img = Image.open(image_path)
    img = img.resize((root.winfo_width(), root.winfo_height()), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)

    root.pack_propagate(False)

    lable.configure(image=img)
    lable.image = img
    lable.pack_propagate(False)

    lable.pack()

def start_download(pb):
    threading.Thread(target=lambda: download_video(pb)).start()


def download_video( pb):
    YoutubeDownloader.download(pb)
    return

def visualize_MainFrame():
    service = build("youtube", "v3", developerKey=API_KEY)

    def get_entry_search(thumbnail_label, root, frames):
        link = main_frame.entry.get()
        link = "https://www.youtube.com/watch?v=HrRt3KX3MFQ"
        start_search(link, service, thumbnail_label, root, frames, main_frame)

    root = tk.CTk()
    root.title("YoutubeDownloader")
    root.geometry("960x540+250+100")

    root.grid_propagate(False)
    root.grid_columnconfigure(0, weight =1)
    root.grid_rowconfigure(0, weight =1)

    main_frame = MainFrame.MainFrame(master=root)
    main_frame.grid(row = 0, column = 0, sticky = "nsew")

    show_image_from_path(main_frame.logo_frame, MainFrame.logo_path, main_frame.logo_lable)

    main_frame.thumbnail_label.bind("<Configure>", lambda event=main_frame.thumbnail_frame,thumbnail_label=main_frame.thumbnail_label: start_resize_image_on_resize_event(main_frame.thumbnail_frame, thumbnail_label, thumbnail_path))
    main_frame.logo_lable.bind("<Configure>", lambda event=main_frame.title_frame, logo_lable=main_frame.logo_lable: start_resize_image_on_resize_event(main_frame.logo_frame, logo_lable, MainFrame.logo_path))
    main_frame.title_lable.bind("<Configure>", lambda event=main_frame.title_frame, title_lable=main_frame.title_lable: start_resize_image_on_resize_event(main_frame.logo_frame, title_lable, MainFrame.yt_logo_path))

    frames = [main_frame.search_result_frame, main_frame.thumbnail_frame, main_frame.search_options_frame]
    main_frame.search_button.configure(command=lambda: get_entry_search(main_frame.thumbnail_label, main_frame.thumbnail_frame, frames))

    root.mainloop()
def main():
    # get_pl_ids()
    visualize_MainFrame()


if __name__ == "__main__":
    main()
