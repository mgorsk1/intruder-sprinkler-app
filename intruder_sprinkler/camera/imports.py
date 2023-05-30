from intruder_sprinkler.camera.opencv import OpenCVCameraProvider


def get_camera_class(class_name):
    if class_name == 'OpenCVCameraProvider':
        return OpenCVCameraProvider
    else:
        raise NotImplementedError(f'Provided class name does not exist: {class_name}')
