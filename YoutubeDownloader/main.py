import threading
import pytube
from googleapiclient.discovery import build
from moviepy.editor import *
import MainFrame
import YoutubeDownloader
import customtkinter as tk
from PIL import Image, ImageTk
import io
import numpy as np
import json
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
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(grayscale_image, tolerance, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    top_border, bottom_border = image.shape[0], 0
    for contour in contours:
        for point in contour[:, 0]:
            y = point[1]
            top_border = min(top_border, y)
            bottom_border = max(bottom_border, y)

    cropped_image = image[top_border:bottom_border, :]

    success, output_image_bytes = cv2.imencode('.png', cropped_image)
    if not success:
        raise Exception("Errore durante la codifica dell'immagine JPEG.")

    return output_image_bytes.tobytes()


def get_pl_ids():
    service = build("youtube", "v3", developerKey=API_KEY)
    next_page_token = None

    while True:

        list_request = service.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId="PLPV2KyIb3jR6TFcFuzI2bB7TMNIIBpKMQ",
            pageToken=next_page_token
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

        print(json.dumps(vid_response, indent=3))

        next_page_token = list_response.get("nextPageToken")

        if not next_page_token:
            break


def start_resize_image_on_resize_event(event, frame, label, img_path, resize_factor=1):
    threading.Thread(target=lambda: resize_image_on_resize_event(event, frame, label, img_path, resize_factor)).start()


def resize_image_on_resize_event(event, frame, label, img_path, resize_factor):
    global call_counter
    if call_counter % not_calling == 0:
        original_image = Image.open(img_path)

        resized_image = original_image.resize(
            (int(frame.winfo_width() / resize_factor), int(frame.winfo_height() / resize_factor)), Image.BICUBIC)
        photo = ImageTk.PhotoImage(resized_image)

        label.configure(image=photo)
        label.image = photo
    call_counter += 1


def start_search(link, service, thumbnail_label, root, frames, main_frame):
    threading.Thread(target=lambda: search_videos(link, service, thumbnail_label, root, frames, main_frame)).start()


def search_videos(link, service, thumbnail_label, root, frames, main_frame):
    main_frame.search_button.grid_forget()
    # main_frame.clear_frame(main_frame.progressbar_frame)
    main_frame.progress_bar.clear()
    main_frame.show_searching_lable()
    try:
        image_data, info_dict = YoutubeDownloader.get_all_results(link, service)
        show_image_from_data(image_data, thumbnail_label, root)
        main_frame.update_on_search_found()
        set_all_frame_color("#343638", frames)
        # main_frame.search_result_frame.start_animation(duration=0.5)
        main_frame.visualize_scroll_result_frame(frames[2], info_dict)

    except Exception:
        main_frame.search_loading_label.grid_forget()
        main_frame.searching_lable.configure(text="Error: video not found!", text_color="#ff0000")
        main_frame.show_search_frame()


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


def start_download(main_frame,progress_bar, link, res, abr, only_audio, only_video, file_name):
    threading.Thread(target=lambda: download_video(main_frame,progress_bar, link, res, abr, only_audio, only_video, file_name)).start()


def download_video(main_frame,progress_bar, link, res, abr, only_audio, only_video, file_name):
    YoutubeDownloader.download(main_frame,progress_bar, link, res, abr, only_audio, only_video, file_name)
    return


def visualize_mainFrame():
    service = build("youtube", "v3", developerKey=API_KEY)

    def get_entry_search(thumbnail_label, root, frames):
        link = main_frame.entry.get()

        if link == "":
            link = "https://www.youtube.com/watch?v=dtwe19VLIR4"

        start_search(link, service, thumbnail_label, root, frames, main_frame)

    root = tk.CTk()
    root.title("YoutubeDownloader")
    root.geometry("960x600+250+100")

    root.grid_propagate(False)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    main_frame = MainFrame.MainFrame(master=root)
    main_frame.grid(row=0, column=0, sticky="nsew")

    show_image_from_path(main_frame.logo_download_frame, MainFrame.logo_path, main_frame.logo_download_label)
    show_image_from_path(main_frame.logo_yt_frame, MainFrame.yt_logo_path, main_frame.logo_yt_label)

    main_frame.thumbnail_label.bind("<Configure>", lambda event=main_frame, frame=main_frame.thumbnail_frame,
                                                          lable=main_frame.thumbnail_label: start_resize_image_on_resize_event(
        event, frame, lable, thumbnail_path))
    main_frame.logo_download_label.bind("<Configure>", lambda event=main_frame, frame=main_frame.logo_download_frame,
                                                              lable=main_frame.logo_download_label: start_resize_image_on_resize_event(
        event, frame, lable, MainFrame.logo_path))
    main_frame.logo_yt_label.bind("<Configure>", lambda event=main_frame, frame=main_frame.logo_yt_frame,
                                                        lable=main_frame.logo_yt_label: start_resize_image_on_resize_event(
        event, frame, lable, MainFrame.yt_logo_path))

    frames = [main_frame.search_result_frame, main_frame.thumbnail_frame, main_frame.search_options_frame]
    main_frame.search_button.configure(
            command=lambda: get_entry_search(main_frame.thumbnail_label, main_frame.thumbnail_frame, frames))

    root.mainloop()


def main():
    # get_pl_ids()
    visualize_mainFrame()


if __name__ == "__main__":
    main()
