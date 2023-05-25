import logging
from abc import ABC
from abc import abstractmethod
from time import sleep

import requests
from gpiozero import LED

from garbage_detector import config
from garbage_detector.utils.gcp import GCPHelper


class IntruderDetector(ABC):
    def __init__(self):
        self.classes = ['metal', 'paper', 'glass', 'plastic', 'cardboard']

        self.gcp = GCPHelper()

    @abstractmethod
    def _prepare_image_for_model(self, image):
        pass

    @abstractmethod
    def _detect(self, image) -> bool:
        # true if intruder detected, false if not
        pass

    def _upload_image_to_gcp(self, image, detection):
        photo_url = 


        return photo_url

    def detect(self, image) -> bool:
        """
        Detects intruder on an image and notifies the backend of this. Process:
            1. Call GCP to do detection on the image
            2. Upload the image to GCP Bucket
            3. Notifying the backend
        :param image: Image opened with OpenCV (cv2)
        :return:
        """
        logging.info('Starting detection process')

        image = self._prepare_image_for_model(image)

        detection = self._detect(image)

        if detection:
            self.gcp.upload_image(image, detection)

        return detection

    # @todo for later - call sonos api to say intruder detected
    def notify(self, detection):
        if detection:
            comms = 'intruder detected'
        else:
            comms = 'intruder gone'

        requests.get(f'http://localhost:5005/sayall/{comms}/en')

