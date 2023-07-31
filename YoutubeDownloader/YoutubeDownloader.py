import re
import pytube  # to download video from YouTube
import time  # to measure download time
from moviepy.editor import *
import os
import requests
import threading
import subprocess

yt_video_pattern = r"^https://www\.youtube\.com/shorts/([a-zA-Z0-9_-]+)$"
output_folder = "./media_downloads"
kw = {
    "total":0,
    "merge":True,
    "elapsed-time":0,
    "time-remaning":0
}

def merge_audio_video(audio_file, video_file, output, res, link,ti, pb):

    ffmpeg_command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -strict experimental -progress pipe:1 "{output}"'

    try:
        # Esegui il comando FFmpeg utilizzando subprocess e cattura l'output
        process = subprocess.Popen(ffmpeg_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True)

        total_duration = 0
        current_duration = 0

        # Analizza l'output del processo riga per riga e calcola il progresso in percentuale
        for line in process.stdout:
            duration_match = re.search(r'Duration: (\d\d:\d\d:\d\d.\d\d)', line)
            if duration_match:
                total_duration = sum(
                    float(x) * 60 ** i for i, x in enumerate(reversed(duration_match.group(1).split(":"))))

            time_match = re.search(r'time=(\d\d:\d\d:\d\d.\d\d)', line)
            if time_match:
                current_duration = sum(
                    float(x) * 60 ** i for i, x in enumerate(reversed(time_match.group(1).split(":"))))

            if total_duration > 0:
                progress_percentage = (current_duration / total_duration) * 100
                print(f"Progresso: {progress_percentage:.2f}%")

        # Aspetta che il processo si completi
        process.wait()

        print("Unione completata con successo!")
    except subprocess.CalledProcessError as e:
        print("Errore durante l'unione:", e)

    print(res, 'video successfully downloaded from', link)
    print('Time taken: {:.0f} sec'.format(time.time() - ti))
    return

def download(pb, link, res, abr, only_audio, only_video):

    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)

    print(pb, link, res, abr, only_audio, only_video)
    # try:
    if only_audio is False:
        videofile = get_video_filter(yt, res, only_video)
        videofile.download(filename="video.mp4", pb = pb, output_path= output_folder)
    if only_video is False:
        output_file = os.path.join(output_folder, "audio.mp3")
        audiofile = get_audio_filter(yt, abr, only_audio)
        audiofile.download(filename="audio_temp.mp4", pb = pb, output_path=output_folder)
        input_file = os.path.join(output_folder, "audio_temp.mp4")
        convert_to_mp3(input_file, output_file)
    # except Exception:

    if only_video is False and only_audio is False:
        video_file = os.path.join(output_folder, "video.mp4")
        audio_file = os.path.join(output_folder, "audio.mp3")
        output_file = os.path.join(output_folder, "output.mp4")
        threading.Thread(target= merge_audio_video(audio_file, video_file, output_file, res, link, ti, pb)).start()

    return

def get_video_filter(yt, res, only_video):
    return yt.streams.filter(res = f"{res}p", progressive=False, only_video= only_video).first()

def get_audio_filter(yt, abr, only_audio):
    return yt.streams.filter(abr = f"{abr}kbps", progressive=False, only_audio = only_audio).first()

def get_all_results(link, service):
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)

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
    image_data = get_image_data_from_url(thumbnail_url)

    return image_data, info_dict

def get_thumbnail_url(video_url, service):

    video_id = None

    if "shorts" in video_url:
        match = re.match(yt_video_pattern, video_url)
        if match:
            video_id = match.group(1)
    else:
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

def convert_to_mp3(input_file, output_file):
    audio_clip = AudioFileClip(input_file)
    audio_clip.write_audiofile(output_file)

    audio_clip.close()
    os.remove(input_file)