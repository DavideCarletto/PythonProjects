# proglog source code: https://github.com/Edinburgh-Genome-Foundry/Proglog/blob/master/proglog/proglog.py
from proglog import ProgressLogger

class ProgressBar(ProgressLogger):

     def __init__(self):
         super(ProgressBar, self).__init__(init_state=None)

     def callback(self, **kw):
          super(ProgressBar, self).callback(**kw)

          # TODO: if merging video and audio, make the progress from the 3 splitted parts using kw parameter. Otherwise,
          #  proceed with normal count of percentage. Then return the value (for the progressBar from tkinter)

          if(kw["merge"] == True):
            print("merging video and audio file:", end=" ")

          print(f"{kw['total']}/100")
