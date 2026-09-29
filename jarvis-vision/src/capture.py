import mss
import numpy as np
import cv2

class ScreenCapture:
    def __init__(self, monitor_index=1):
        self.sct = mss.mss()
        if monitor_index >= len(self.sct.monitors):
            monitor_index = 1
        self.monitor = self.sct.monitors[monitor_index]

    def grab(self):
        shot = np.asarray(self.sct.grab(self.monitor))
        return cv2.cvtColor(shot, cv2.COLOR_BGRA2BGR)

    def close(self):
        self.sct.close()
