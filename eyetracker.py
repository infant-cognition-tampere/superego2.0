import glib
from psychopy import event

class EyeTracker():

    def __init__(self, init_callback, data_callback):
        self.data_callback = data_callback

        # create a tracker object
    #    self.mouz = event.Mouse(win=win)

        glib.idle_add(self.refresh)
        #self.refresh()

        init_callback()

    def refresh(self):
  #      mp = mouz.getPos()
  #      print(mp)
        print("AAAAAAAAAAAAA")

    def start_recording(self, callbackfcn):
        callbackfcn()

    def stop_recording(self, callbackfcn):
        callbackfcn()

    def __del__(self):
        pass