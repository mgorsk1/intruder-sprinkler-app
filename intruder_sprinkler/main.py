import time
from typing import Any
from typing import Type  # noqa: TYP001

import cv2
from distutils.util import strtobool

from intruder_sprinkler import config
from intruder_sprinkler.camera.imports import get_camera_class
from intruder_sprinkler.detector import IntruderDetector
from intruder_sprinkler.detector.imports import get_detector_class
from intruder_sprinkler.sprinkler.manager import SprinklerManager

sprinkler_manager: Any
camera: Any
raw_capture: Any
detector: Type[IntruderDetector]


def setup():
    global sprinkler_manager
    global camera
    global detector
    global classifier

    # allow the camera to warmup
    time.sleep(0.1)

    camera = get_camera_class(config.camera.cls)()
    camera.setup(config.camera.url, config.camera.resolution.width, config.camera.resolution.height)

    detector = get_detector_class(config.detector.cls)()

    # used to turn sprinklers on/off
    sprinkler_manager = SprinklerManager(config.valve.gpio)


def detect(detector: Type[IntruderDetector], image):
    return detector.detect(image)  # type: ignore


if __name__ == '__main__':
    setup()

    start = None
    already_detected: bool = False

    while True:
        frame = camera.capture()
        image = cv2.flip(frame.array, 0)

        # @todo maybe introduce throttling so image is classified every N seconds (so not images are sent to GCP)
        detected = detect(detector, image)

        # new detection - attack
        if not already_detected and detected:
            sprinkler_manager.on()
            already_detected = True
        # enemy gone - shut down water
        elif already_detected and not detected:
            sprinkler_manager.off()
            already_detected = False
        # ongoing sprinkling
        else:
            pass
        if strtobool(config.camera.display):
            cv2.imshow('Frame', image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
