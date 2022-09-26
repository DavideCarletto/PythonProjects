import threading
import pytube.request
from googleapiclient.discovery import build
from proglog import TqdmProgressBarLogger
from tkinter import  Tk
from tkinter import ttk
from moviepy.editor import *
import YoutubeDownloader


API_KEY = os.environ.get("YT-API")
pytube.request.default_range_size = 1000000




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



def yt_mp3_downlaod():

    class MyBarLogger(TqdmProgressBarLogger):
        def callback(self, **changes):
            # Every time the logger is updated, this function is called
            if len(self.bars):
                percentage = next(reversed(self.bars.items()))[1]['index'] / next(reversed(self.bars.items()))[1]['total']
                update_percentage(percentage)

    def progress_function(stream, chunk, bytes_remaining):
        progress = round((1 - bytes_remaining / stream.filesize) * 100, 3)
        print( f'{progress}% done...')

    def update_progress_label():
        return f"Current Progress: {int(round(pb['value'],0))}"

    def update_percentage(percentage):
        if(percentage<1):
            pb["value"] = percentage*100
            value_label["text"] = update_progress_label()
        pass

    def download_video():
        YoutubeDownloader.download()
        return
        # ti  = time.time()
        # yt = YouTube("https://www.youtube.com/watch?v=MUxHmvWYqFQ&ab_channel=60FpsGoodness",on_progress_callback=progress_function,use_oauth=True, allow_oauth_cache=True)
        # print(yt.streams.filter(adaptive=True))
        # v_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).first()
        #
        # a_stream = yt.streams.filter(only_audio=True).first()
        # print(yt.streams.get_highest_resolution())
        # v_file = v_stream.download("Video")
        # file = a_stream.download("Audio")
        #
        # print(v_file)
        # base, ext = os.path.splitext(file)
        # a_file = base + '.mp3'
        # os.rename(file, a_file)
        #
        # my_clip = VideoFileClip(v_file)
        # audio_background = AudioFileClip(a_file)
        # final_clip = my_clip.set_audio(audio_background)
        #
        # final_clip.write_videofile("finishedVideo.mp4", fps=30, logger=MyBarLogger(print_messages=False),threads=os.cpu_count())
        #
        # print('Time taken: {:.0f} sec'.format(time.time() - ti))


    root = Tk()
    root.title("Title")
    root.geometry("960x540+250+100")



    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=280
    )

    pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

    # label
    value_label = ttk.Label(root, text=update_progress_label())
    value_label.grid(column=0, row=1, columnspan=2)

    threading.Thread(target=download_video).start()

    root.mainloop()



def main():
    # get_pl_ids()
    yt_mp3_downlaod()


if __name__ == "__main__":
    main()
