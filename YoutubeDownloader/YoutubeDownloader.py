import pytube  # to download video from YouTube
import time  # to measure download time
from ffmpeg_progress_yield import FfmpegProgress
import threading
import os


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

    link = 'https://www.youtube.com/shorts/bBblxp5Z--8'
    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    print('Title:', yt.title)
    print('Author:', yt.author)
    print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
    print('Number of views:', yt.views)
    print('Length of video:', yt.length, 'sec')

    try:
        videofilter = yt.streams.filter(res="1080p", progressive=False).first()
        audiofilter = yt.streams.filter(abr='128kbps',progressive=False, only_audio=True).first()
        res = '1080p'
    except:
        videofilter = yt.streams.filter(res='720p', progressive=False).first()
        audiofilter = yt.streams.filter(abr='128kbps', progressive=False, only_audio=True).first()
        res = '720p'

    videofile = videofilter.download(filename="video.mp4", pb = pb)
    audiofile = audiofilter.download(filename="audio.mp4", pb = pb)

    threading.Thread(target= merge_audio_video(videofile,audiofile, res, link, ti, pb)).start()

    return
