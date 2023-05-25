from intruder_sprinkler.camera.base import CameraProvider


class RPICameraProvider(CameraProvider):
    def setup(self, url, width, height):
        from picamera2 import Picamera2

        res = (int(width), int(height))
        
        self.camera = Picamera2()
        video_config = self.camera.create_video_configuration(main={"size": res, "format": "RGB888"})
        self.camera.configure(video_config)
        self.camera.start()

    def capture(self):
        return _, self.camera.capture_array()
