from intruder_sprinkler.detector import IntruderDetector


class DummyIntruderDetector(IntruderDetector):
    def _prepare_image_for_model(self, image):
        pass

    def _detect(self, image):
        return False
