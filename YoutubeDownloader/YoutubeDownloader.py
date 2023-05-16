import ffmpeg  # to merge audio/video streaams
import pytube  # to download video from YouTube
import time  # to measure download time
from ffmpeg_progress_yield import FfmpegProgress
import threading
from ProgressBar import ProgressBar

kw = {
    "total":0,
    "merge":True,
    "elapsed-time":0,
    "time-remaning":0
}

def merge_audio_video(videofile, audiofile,res, link,ti):
    cmd = [
        "ffmpeg", "-y", "-i", f"{videofile}", "-i", f"{audiofile}", "-c:v", "copy", "-c:a", "aac", "output.mp4"
    ]

    ff = FfmpegProgress(cmd)
    ff.run_command_with_progress(cmd)

    pbar = ProgressBar()
    for progress in ff.run_command_with_progress():
        kw["total"] = progress
        pbar(**kw)

    print(res, 'video successfully downloaded from', link)
    print('Time taken: {:.0f} sec'.format(time.time() - ti))
    return

def download():

    link = 'https://www.youtube.com/shorts/bBblxp5Z--8'
    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    print('Title:', yt.title)
    print('Author:', yt.author)
    print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
    print('Number of views:', yt.views)
    print('Length of video:', yt.length, 'sec')
    videofile = ""
    audiofile = ""

    try:
        videofile = yt.streams.filter(res="1080p", progressive=False).first().download(filename='video.mp4')
        audiofile = yt.streams.filter(progressive=False, only_audio=True).first().download(filename='audio.mp3')
        res = '1080p'
    except:
        videofile = yt.streams.filter(res='720p', progressive=False).first().download(filename='video.mp4')
        audiofile = yt.streams.filter(abr='128kbps', progressive=False).first().download(filename='audio.mp3')
        res = '720p'

    # audio = ffmpeg.input('./audio.mp3')
    # print(audio)
    # video = ffmpeg.input('./video.mp4')
    # print(video)
    # ffmpeg.concat(video, audio, v = 1, a = 1).output("./mix_delayed_audio.mp4").run(overwrite_output=True)

    threading.Thread(target= merge_audio_video(videofile,audiofile, res, link, ti)).start()

    return

