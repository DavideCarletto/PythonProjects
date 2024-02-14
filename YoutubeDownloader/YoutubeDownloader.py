import re
import pytube
import time  # to measure download time
from moviepy.editor import *
import os
import requests
import threading
import subprocess

yt_video_pattern = r"^https://www\.youtube\.com/shorts/([a-zA-Z0-9_-]+)$"
output_folder = "./media_downloads"
kw = {
    "total": 0,
    "merge": True,
    "elapsed-time": 0,
    "time-remaning": 0
}


def merge_audio_video(audio_file, video_file, output, progress_bar):
    ffmpeg_command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -strict experimental -progress pipe:1 "{output}"'
    progress_bar.progress_label.set_text(text="Merging audio and video file...")

    try:
        # Esegui il comando FFmpeg utilizzando subprocess e cattura l'output
        process = subprocess.Popen(ffmpeg_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True)

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
                progress_percentage = progress_bar.pb.get()*100 + ((current_duration / total_duration) * 100)
                print(f"Progresso: {progress_percentage:.2f}%")
                # progress_bar.update_progress(progress_percentage, progress_bar.pb.get()*100, factor=3)

        # Aspetta che il processo si completi
        process.wait()

        progress_bar.pb.stop()
        progress_bar.audio_converting_lable.grid_forget()
        progress_bar.show_text(progress_bar.download_status_lable)

    except subprocess.CalledProcessError as e:
        progress_bar.download_status_lable.configure(text ="Error while merging!")

    return

#TODO: rimodificare il file streams.py della libreria pytube in modo da visualizzare progress bar mannaggia la madonna
def download(main_frame,progress_bar, link, res, abr, only_audio, only_video, file_name):
    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)

    print(progress_bar, link, res, abr, only_audio, only_video)
    both = False
    factor = 1
    offset = 0

    try:

        if only_audio is False and only_video is False:
            both = True
            factor = 3
            offset = 23

        if only_audio is False:
            videofile = get_video_filter(yt, res)
            videofile.download(main_frame = main_frame, filename=f"{file_name}.mp4", progress_bar=progress_bar, type="video", factor = factor, offset = 0, output_path=output_folder)
            print(videofile)
            if only_video:
                progress_bar.percentage_label.grid_forget()
                progress_bar.show_text(progress_bar.download_status_lable)

        if only_video is False:
            output_file = os.path.join(output_folder, f"{file_name}.mp3")
            print(yt, abr)
            audiofile = get_audio_filter(yt, abr)
            print(type(audiofile))
            audiofile.download(main_frame=main_frame, filename="audio_temp.mp4", progress_bar=progress_bar, type ="audio", offset = offset, factor= factor, output_path=output_folder)
            input_file = os.path.join(output_folder, "audio_temp.mp4")

            progress_bar.show_text(progress_bar.audio_converting_lable)

            if only_audio is True:
                progress_bar.percentage_label.grid_forget()
                progress_bar.pb.start()
                convert_to_mp3(input_file, output_file, progress_bar)
                progress_bar.pb.stop()
                progress_bar.audio_converting_lable.grid_forget()

    except Exception as e:
        progress_bar.download_status_lable.configure(text="Download Failed!", text_color="#ff0000")
        print(e)

        if both:
            progress_bar.percentage_label.grid_forget()
            progress_bar.pb.start()
            video_file = os.path.join(output_folder, f"{file_name}.mp4")
            audio_file = os.path.join(output_folder, f"{file_name}.mp3")
            output_file = os.path.join(output_folder, "output_temp.mp4")
            threading.Thread(target=merge_audio_video(audio_file, video_file, output_file, progress_bar)).start()

            delete_file(f"./media_downloads/{file_name}.mp3")
            delete_file(f"./media_downloads/{file_name}.mp4")

            try:
                os.rename("./media_downloads/output_temp.mp4", f"./media_downloads/{file_name}.mp4")
                print(f"File rinominato da output_temp.mp4 a {file_name}")
            except OSError as e:
                print(f"Errore durante la rinomina: {e}")

        main_frame.show_search_frame()
        progress_bar.download_status_lable.configure(text =progress_bar.download_status_lable.cget("text") + "\n" + "Time taken: {:.0f} sec".format(time.time() - ti))
    return

def get_video_filter(yt, res):
    return yt.streams.filter(res=f"{res}p", progressive=True, only_video=False).first()


def get_audio_filter(yt, abr):
    #TODO: capire perchè non va abr e prendere l'audio migliore
    # return yt.streams.filter(abr=f"{abr}kbps", progressive=True, only_audio=False).first()
    print(yt.streams.filter(progressive=True, only_audio=False))
    return yt.streams.filter(progressive=True, only_audio=False).last()


def get_all_results(link, service):
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)

    info_dict = {"Title": yt.title, "Author": yt.author, "Published date": yt.publish_date, "Number of views": yt.views,
                 "Length of video": yt.length}
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

    thumbnail_url = get_thumbnail_url(link, service)
    image_data = get_image_data_from_url(thumbnail_url)

    return image_data, info_dict


def get_thumbnail_url(video_url, service):
    video_id = None

    if "shorts" in video_url:
        match = re.match(yt_video_pattern, video_url)
        if match:
            video_id = match.group(1)
    else:
        video_id = (video_url.split("v=")[1]).split("&")[0]

    thumbnail_url = ""
    response = service.videos().list(part='snippet', id=video_id).execute()
    if 'items' in response and len(response['items']) > 0:
        thumbnail_url = response['items'][0]['snippet']['thumbnails']['high']['url']

    return thumbnail_url


def get_image_data_from_url(url):
    response = requests.get(url)
    image_data = response.content

    return image_data


def convert_to_mp3(input_file, output_file, progress_bar):
    audio_clip = AudioFileClip(input_file)
    audio_clip.write_audiofile(output_file)

    audio_clip.close()
    os.remove(input_file)
    progress_bar.show_text(progress_bar.download_status_lable)

def delete_file(file_path):

    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File removed: {file_path}")
    except OSError as e:
        print(f"Error while deleting file '{file_path}': {e}")