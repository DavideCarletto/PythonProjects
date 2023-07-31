from proglog import ProgressLogger
import customtkinter as tk
from tkinter import ttk
class ProgressBar(ProgressLogger):
    def __init__(self, root):
        super(ProgressBar, self).__init__(init_state=None)
        self.root = root

        self.pb = tk.CTkProgressBar(
            root,
            orientation='horizontal',
            mode='determinate',
            progress_color="green"
        )

        self.pb.set(0)


    def callback(self, **kw):
        super(ProgressBar, self).callback(**kw)

        # TODO: if merging video and audio, make the progress from the 3 splitted parts using kw parameter. Otherwise,
        #  proceed with normal count of percentage. Then return the value (for the progressBar from tkinter)

        if (kw["merge"] == True):
            print("merging video and audio file:", end=" ")

        print(f"{kw['total']}/100")

    def update_progress(self, value):

        while(self.pb.get()*100< value):
            self.pb.set(self.pb.get()+0.005)
            # print(self.pb.get())
            self.pb.update()

            # value_label = ttk.Label(self.root, text = f"Current Progress: {self.pb['value']}%")
            # value_label.grid(column=0, row=2, columnspan=2)

    def show(self, row, column):
        self.pb.grid(column=column, row=row)