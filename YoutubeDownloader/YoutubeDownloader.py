import pytube  # to download video from YouTube
import time  # to measure download time
from ffmpeg_progress_yield import FfmpegProgress
import os
import customtkinter as tk
from googleapiclient.discovery import build
from PIL import Image, ImageTk
import requests
import threading

kw = {
    "total":0,
    "merge":True,
    "elapsed-time":0,
    "time-remaning":0
}

def merge_audio_video(videofile, audiofile,res, link,ti, pb):
    cmd = [
        "ffmpeg", "-y", "-i", f"{videofile}", "-i", f"{audiofile}", "-c:v", "copy", "-c:a", "aac", "output.mp4"
    ]

    ff = FfmpegProgress(cmd)
    ff.run_command_with_progress(cmd)

    for progress in ff.run_command_with_progress():
        kw["total"] = progress
        pb(**kw)

    print(res, 'video successfully downloaded from', link)
    print('Time taken: {:.0f} sec'.format(time.time() - ti))
    return

def download(pb):
    if os.path.exists("audio.mp3"):
        os.remove("audio.mp3")
    elif os.path.exists("video.mp4"):
        os.remove("video.mp4")
    else:
        print("No file removed")

    # link = 'https://www.youtube.com/shorts/bBblxp5Z--8'
    # ti = time.time()
    # yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    # print('Title:', yt.title)
    # print('Author:', yt.author)
    # print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
    # print('Number of views:', yt.views)
    # print('Length of video:', yt.length, 'sec')
    #
    # for stream in yt.streams:
    #     # Puoi filtrare solo i formati video, ignorando gli audio
    #     if "video" in stream.mime_type:
    #         resolution = stream.resolution if stream.resolution else "Audio-only"
    #         print(f"Risoluzione: {resolution}, Formato: {stream.mime_type}")
    #     if "audio" in stream.mime_type:
    #         audio_format = stream.mime_type.replace("audio/", "")
    #         print(f"Formato audio: {audio_format}, Bitrate: {stream.abr} kbps")
    #
    # try:
    #     videofilter = yt.streams.filter(res="1080p", progressive=False).first()
    #     audiofilter = yt.streams.filter(abr='128kbps',progressive=False, only_audio=True).first()
    #     res = '1080p'
    # except:
    #     videofilter = yt.streams.filter(res='720p', progressive=False).first()
    #     audiofilter = yt.streams.filter(abr='128kbps', progressive=False, only_audio=True).first()
    #     res = '720p'
    #
    # videofile = videofilter.download(filename="video.mp4", pb = pb)
    # audiofile = audiofilter.download(filename="audio.mp4", pb = pb)
    #
    # threading.Thread(target= merge_audio_video(videofile,audiofile, res, link, ti, pb)).start()
    #
    # return

def get_all_results(link, service):
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    # print('Title:', yt.title)
    # print('Author:', yt.author)
    # print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
    # print('Number of views:', yt.views)
    # print('Length of video:', yt.length, 'sec')
    video_info_list = [yt.title, yt.author, yt.publish_date, yt.views, yt.length]

    info_dict = {"Title": yt.title, "Author":yt.author, "Published date": yt.publish_date, "Number of views": yt.views, "Length of video":yt.length}
    list_video_resolution = []
    list_audio_format = []

    for stream in yt.streams:
        # Puoi filtrare solo i formati video, ignorando gli audio
        if "video" in stream.mime_type:
            resolution = stream.resolution if stream.resolution else "Audio-only"
            list_video_resolution.append((resolution, stream.mime_type))
            # print(f"Risoluzione: {resolution}, Formato: {stream.mime_type}")
        if "audio" in stream.mime_type:
            audio_format = stream.mime_type.replace("audio/", "")
            list_audio_format.append((audio_format, stream.abr))
            # print(f"Formato audio: {audio_format}, Bitrate: {stream.abr} kbps")

    info_dict["video_res_list"] = list_video_resolution
    info_dict["audio_res_list"] = list_audio_format

    thumbnail_url =  get_thumbnail_url(link, service)
    # print(thumbnail_url)
    image_data = get_image_data_from_url(thumbnail_url)

    return image_data, info_dict

# Funzione per ottenere l'URL dell'immagine di copertina di un video
def get_thumbnail_url(video_url, service):
    video_id = video_url.split("v=")[1]
    thumbnail_url= ""
    response = service.videos().list(part='snippet', id=video_id).execute()
    if 'items' in response and len(response['items']) > 0:
        thumbnail_url = response['items'][0]['snippet']['thumbnails']['high']['url']

    return thumbnail_url

def get_image_data_from_url(url):
    response = requests.get(url)
    image_data = response.content

    return image_data