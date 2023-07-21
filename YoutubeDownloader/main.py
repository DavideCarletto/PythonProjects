import threading
import pytube.request
from googleapiclient.discovery import build
from moviepy.editor import *
from ProgressBar import ProgressBar
from tkinter import ttk
import YoutubeDownloader
import tkinter as tk

API_KEY = os.environ.get("YT-API")
pytube.request.default_range_size = 1000000

def start_download(pb):
    print("Initialize download")
    threading.Thread(target=download_video(pb)).start()

def get_pl_ids():
    service = build("youtube", "v3", developerKey=API_KEY)
    nextPageToken = None

    while (True):

        list_request = service.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId="PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF",
            pageToken=nextPageToken
        )
        list_response = list_request.execute()

        # print(json.dumps(response, indent= 3))

        ls_id = []

        for item in list_response.get("items"):
            ls_id.append(item["contentDetails"]["videoId"])

        print(ls_id)

        '''
        vid_request = service.videos().list(
            part="id",
            id=",".join(ls_id)
        )

        vid_response = vid_request.execute()

        print(json.dumps(vid_response, indent = 3))
        '''

        nextPageToken = list_response.get("nextPageToken")

        if not nextPageToken:
            break



def visualize_MainFrame():

    root = tk.Tk()
    root.title("YoutubeDownloader")
    root.geometry("960x540+250+100")

    pb = ProgressBar(root)

    download_button = ttk.Button(root, text="Download", command=start_download(pb))
    download_button.grid(column=2, row=1, columnspan=2, padx=150, pady=20)

    root.mainloop()


def download_video(pb):
    YoutubeDownloader.download(pb)
    return

def main():
    # get_pl_ids()
    visualize_MainFrame()


if __name__ == "__main__":
    main()
