# proglog source code: https://github.com/Edinburgh-Genome-Foundry/Proglog/blob/master/proglog/proglog.py
from proglog import ProgressLogger
from tkinter import ttk

class ProgressBar(ProgressLogger):
    def __init__(self, root):
        super(ProgressBar, self).__init__(init_state=None)
        self.root = root

        self.pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )

        self.pb.grid(column=0, row=0, columnspan=2, padx=100, pady=20)



    def callback(self, **kw):
        super(ProgressBar, self).callback(**kw)

        # TODO: if merging video and audio, make the progress from the 3 splitted parts using kw parameter. Otherwise,
        #  proceed with normal count of percentage. Then return the value (for the progressBar from tkinter)

        if (kw["merge"] == True):
            print("merging video and audio file:", end=" ")

        print(f"{kw['total']}/100")

    def update_progress(self, value):

        while(self.pb["value"]< value):
            self.pb["value"] += 0.5
            self.pb.update()
            self.pb.after(10)

            value_label = ttk.Label(self.root, text = f"Current Progress: {self.pb['value']}%")
            value_label.grid(column=0, row=2, columnspan=2)
