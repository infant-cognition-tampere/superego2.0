
class EyeTracker():

    def __init__(self, init_callback, data_callback):
        self.data_callback = data_callback

        init_callback()

    def start_recording(self, callbackfcn):
        callbackfcn()

    def stop_recording(self, callbackfcn):
        callbackfcn()

    def __del__(self):
        pass