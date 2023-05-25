import cv2

from intruder_sprinkler.camera.base import CameraProvider


class OpenCVCameraProvider(CameraProvider):
    def setup(self, url, *args):
        self.camera = cv2.VideoCapture(url)

    def capture(self):
        return self.camera.read()
