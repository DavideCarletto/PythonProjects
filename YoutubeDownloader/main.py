import threading
import pytube.request
from googleapiclient.discovery import build
from moviepy.editor import *
import MainFrame
import YoutubeDownloader
import customtkinter as tk
from PIL import Image, ImageTk
import io
import numpy as np
import json
import pytube.exceptions
import cv2

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

API_KEY = os.environ.get("YT-API")
pytube.request.default_range_size = 1000000

not_calling = 2
call_counter = 0

thumbnail_path = "./Images/Thumbnail.png"
# logo_path = "./Images/blue-download-icon-3.jpg"


def remove_black_borders_from_image(image_bytes, tolerance=10):
    # Carica l'immagine da bytes utilizzando OpenCV
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

    # Converti l'immagine in scala di grigi
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applica una soglia per binarizzare l'immagine
    _, binary_image = cv2.threshold(grayscale_image, tolerance, 255, cv2.THRESH_BINARY)

    # Trova i contorni dell'immagine binarizzata
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Trova i limiti dei bordi neri
    top_border, bottom_border = image.shape[0], 0
    for contour in contours:
        for point in contour[:, 0]:
            y = point[1]
            top_border = min(top_border, y)
            bottom_border = max(bottom_border, y)

    # Ritaglia l'immagine per rimuovere i bordi neri
    cropped_image = image[top_border:bottom_border, :]

    # Converti l'immagine ritagliata in formato JPEG
    success, output_image_bytes = cv2.imencode('.png', cropped_image)
    if not success:
        raise Exception("Errore durante la codifica dell'immagine JPEG.")

    return output_image_bytes.tobytes()

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



def start_resize_image_on_resize_event(event,frame,  label, img_path, resize_factor = 1):
    threading.Thread(target=lambda: resize_image_on_resize_event(event,frame,  label, img_path, resize_factor)).start()

def resize_image_on_resize_event(event, frame, label, img_path, resize_factor):
    global call_counter
    if call_counter % not_calling == 0:
        original_image = Image.open(img_path)

        resized_image = original_image.resize((int(frame.winfo_width()/resize_factor), int(frame.winfo_height()/resize_factor)), Image.BICUBIC)
        photo = ImageTk.PhotoImage(resized_image)

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
    frames[0].configure(border_width=1, border_color="#565B5E")
    frames[2].configure(border_width=1, border_color="#565B5E")
    for frame in frames:
        frame.configure(fg_color=color)

def show_image_from_data(image_data, thumbnail_img, frame):
    # TODO: black borders not removed
    img_bytes = remove_black_borders_from_image(image_data, tolerance=10)
    with open(f"{thumbnail_path}", 'wb') as f:
        f.write(img_bytes)

    img = Image.open(io.BytesIO(img_bytes))
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

def start_download(pb, link, res, abr, only_audio, only_video):
    threading.Thread(target=lambda: download_video(pb, link, res, abr, only_audio, only_video)).start()

def download_video(pb, link, res, abr, only_audio, only_video):
    YoutubeDownloader.download(pb, link, res, abr, only_audio, only_video)
    return

def visualize_MainFrame():
    service = build("youtube", "v3", developerKey=API_KEY)

    def get_entry_search(thumbnail_label, root, frames):
        link = main_frame.entry.get()
        link = "https://www.youtube.com/shorts/xLec1zTahlM"
        start_search(link, service, thumbnail_label, root, frames, main_frame)

    root = tk.CTk()
    root.title("YoutubeDownloader")
    root.geometry("960x600+250+100")

    root.grid_propagate(False)
    root.grid_columnconfigure(0, weight =1)
    root.grid_rowconfigure(0, weight =1)

    main_frame = MainFrame.MainFrame(master=root)
    main_frame.grid(row = 0, column = 0, sticky = "nsew")

    show_image_from_path(main_frame.logo_download_frame, MainFrame.logo_path, main_frame.logo_download_lable)
    show_image_from_path(main_frame.logo_yt_frame, MainFrame.yt_logo_path, main_frame.logo_yt_lable)

    main_frame.thumbnail_label.bind("<Configure>", lambda event=main_frame, frame = main_frame.thumbnail_frame, lable=main_frame.thumbnail_label: start_resize_image_on_resize_event(event, frame, lable, thumbnail_path))
    main_frame.logo_download_lable.bind("<Configure>", lambda event=main_frame, frame = main_frame.logo_download_frame, lable=main_frame.logo_download_lable: start_resize_image_on_resize_event(event,  frame, lable, MainFrame.logo_path))
    main_frame.logo_yt_lable.bind("<Configure>", lambda event=main_frame, frame = main_frame.logo_yt_frame, lable=main_frame.logo_yt_lable: start_resize_image_on_resize_event(event, frame,  lable, MainFrame.yt_logo_path))

    frames = [main_frame.search_result_frame, main_frame.thumbnail_frame, main_frame.search_options_frame]
    main_frame.search_button.configure(command=lambda: get_entry_search(main_frame.thumbnail_label, main_frame.thumbnail_frame, frames))

    root.mainloop()

def clear_folder(folder_path):
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File removed: {file_path}")
        except OSError as e:
            print(f"Error while deleting file '{file_path}': {e}")

def main():
    # get_pl_ids()
    clear_folder(YoutubeDownloader.output_folder)
    visualize_MainFrame()


if __name__ == "__main__":
    main()
