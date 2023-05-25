from intruder_sprinkler.detector.google_cloud_vision import GoogleCloudVisionIntruderDetector


def get_detector_class(class_name):
    if class_name == 'GoogleCloudVisionIntruderDetector':
        return GoogleCloudVisionIntruderDetector
    else:
        raise NotImplementedError(f'Provided class name does not exist: {class_name}')
