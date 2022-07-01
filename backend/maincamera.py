import os
import cv2
import time
from CameraEvent import CameraEvent
import threading
from videoInput import *


class mainCamera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    event = CameraEvent()

    def __init__(self):
        """Start the background camera thread if it isn't running yet."""
        if mainCamera.thread is None:
            mainCamera.last_access = time.time()

            # start background frame thread
            mainCamera.thread = threading.Thread(target=self._thread)
            mainCamera.thread.start()

            # wait until first frame is available
            mainCamera.event.wait()

    def get_frame(self):
        """Return the current camera frame."""
        mainCamera.last_access = time.time()

        # wait for a signal from the camera thread
        mainCamera.event.wait()
        mainCamera.event.clear()

        return mainCamera.frame
    @staticmethod
    def frames():
        video_source = main
        camera = cv2.VideoCapture(video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start maincamera.')

        frame_count = 0
        while True:
            # read current frame
            if frame_count == int(camera.get(cv2.CAP_PROP_FRAME_COUNT)):
                frame_count =0
                camera.set(cv2.CAP_PROP_FRAME_COUNT,0)
            _, img = camera.read()
            frame_count+=1
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
    @classmethod
    def _thread(cls):
        """Camera background thread."""
        print('Starting camera thread.')
        frames_iterator = cls.frames()
        for frame in frames_iterator:
            mainCamera.frame = frame
            mainCamera.event.set()  # send signal to clients
            time.sleep(0)

            # if there hasn't been any clients asking for frames in
            # the last 10 seconds then stop the thread
            if time.time() - mainCamera.last_access > 3:
                frames_iterator.close()
                print('Stopping camera thread due to inactivity.')
                break
        mainCamera.thread = None