import cv2
from threading import Thread

class CameraStream:
    def __init__(self, source=0, name="Camera"):
        self.stream = cv2.VideoCapture(source)
        self.name = name
        self.status, self.frame = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=(), daemon=True).start()
        return self

    def update(self):
        while not self.stopped:
            if not self.status:
                self.stop()
            else:
                (self.status, self.frame) = self.stream.read()

    def get_frame(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.stream.release()