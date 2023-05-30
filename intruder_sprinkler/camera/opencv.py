import cv2

from intruder_sprinkler.camera.base import CameraProvider

# this provider works with both remote webcams, usb webcams and rpi camera


class OpenCVCameraProvider(CameraProvider):
    def setup(self, url, *args):
        # 0 is for computer camera and needs to be explicitly int (str '0' won't work)
        url = url if url != '0' else 0
        self.camera = cv2.VideoCapture(url)

    def capture(self):
        return self.camera.read()
