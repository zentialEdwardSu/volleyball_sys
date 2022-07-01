import os
import cv2
import time
from CameraEvent import CameraEvent
import threading
from videoInput import *


class sideICamera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    event = CameraEvent()

    def __init__(self):
        """Start the background camera thread if it isn't running yet."""
        if sideICamera.thread is None:
            sideICamera.last_access = time.time()

            # start background frame thread
            sideICamera.thread = threading.Thread(target=self._thread)
            sideICamera.thread.start()

            # wait until first frame is available
            sideICamera.event.wait()

    def get_frame(self):
        """Return the current camera frame."""
        sideICamera.last_access = time.time()

        # wait for a signal from the camera thread
        sideICamera.event.wait()
        sideICamera.event.clear()

        return sideICamera.frame
    @staticmethod
    def frames():
        video_source = side1
        camera = cv2.VideoCapture(video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start sideIcamera.')

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
            sideICamera.frame = frame
            sideICamera.event.set()  # send signal to clients
            time.sleep(0)

            # if there hasn't been any clients asking for frames in
            # the last 10 seconds then stop the thread
            if time.time() - sideICamera.last_access > 3:
                frames_iterator.close()
                print('Stopping camera thread due to inactivity.')
                break
        sideICamera.thread = None