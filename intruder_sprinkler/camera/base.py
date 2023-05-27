import abc


class CameraProvider(abc.ABC):
    @abc.abstractmethod
    def setup(self, *args, **kwarg):
        pass

    @abc.abstractmethod
    def capture(self):
        pass
