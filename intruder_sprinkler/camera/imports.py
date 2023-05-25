from intruder_sprinkler.camera.opencv import OpenCVCameraProvider
from intruder_sprinkler.camera.rpi import RPICameraProvider


def get_camera_class(class_name):
    if class_name == 'OpenCVCameraProvider':
        return OpenCVCameraProvider
    elif class_name == 'RPICameraProvider':
        return RPICameraProvider
    else:
        raise NotImplementedError(f'Provided class name does not exist: {class_name}')
