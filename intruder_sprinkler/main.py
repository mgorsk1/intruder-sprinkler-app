import time
from datetime import datetime
from typing import Any
from typing import Type  # noqa: TYP001

import cv2
import requests
from distutils.util import strtobool

from intruder_sprinkler import config
from intruder_sprinkler.camera.imports import get_camera_class
from intruder_sprinkler.detector import IntruderDetector
from intruder_sprinkler.detector.imports import get_detector_class

camera: Any
raw_capture: Any
detector: Type[IntruderDetector]


def setup():
    global camera
    global detector
    global classifier

    # allow the camera to warmup
    time.sleep(0.1)

    camera = get_camera_class(config.camera.cls)()
    camera.setup(config.camera.url, config.camera.resolution.width, config.camera.resolution.height)

    detector = get_detector_class(config.detector.cls)()


def detect(detector: Type[IntruderDetector], image):
    return detector.detect(image)  # type: ignore


if __name__ == '__main__':
    setup()

    start = None
    already_detected: bool = False
    i = 0

    last_detection = datetime.now()

    while True:
        i += 1
        success, image = camera.capture()

        if not success:
            continue

        # throttling to detect every n seconds no to overflow model
        now = datetime.now()
        delta = now - last_detection
        if delta.total_seconds() > float(config.detector.seconds):
            detected = detect(detector, image)
            i = 0

            # new detection - attack
            if not already_detected and detected:
                requests.post(f'{config.api.url}/on')
                already_detected = True
            # enemy gone - shut down water
            elif already_detected and not detected:
                requests.post(f'{config.api.url}/off')
                already_detected = False
            # ongoing sprinkling
            else:
                pass

            last_detection = now
        else:
            pass

        if strtobool(config.camera.display):
            cv2.imshow('Frame', image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
