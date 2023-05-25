import logging
from json import loads

import cv2
from google.cloud import vision
from google.cloud.vision import types

from garbage_detector import BASE_PATH
from garbage_detector import config
from garbage_detector.classifier import IntruderDetector

# @todo I propose to focus on this detector as it has lowest development effort data-science wise
class GoogleCloudVisionIntruderDetector(IntruderDetector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vision = vision.ImageAnnotatorClient()

    def _prepare_image_for_model(self, image):
        resize_to = (int(config.gcp.vision.image.size.width), int(config.gcp.vision.image.size.height))

        image = cv2.resize(image, resize_to)

        return image

    def _detect(self, image):
        frame_bytes = cv2.imencode('.jpg', image)[1].tostring()

        image = types.Image(content=frame_bytes)

        response = self.vision.label_detection(image=image)
        # key - category, value - confidence
        annotations = {l.description.lower(): round(l.score * 100, 2) for l in response.label_annotations}

        logging.info(f'Received annotations {annotations}')

        result = annotations.get(config.intruder.name)

        if result is not None:
            if result >= int(config.gcp.vision.classification.threshold):
                return True

        return False
