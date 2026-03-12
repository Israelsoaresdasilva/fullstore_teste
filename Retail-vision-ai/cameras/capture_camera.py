import cv2
from config.settings import CAMERA_RTSP

class CameraCapture:

    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_RTSP)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame

    def show(self, frame):
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == 27:
            exit()