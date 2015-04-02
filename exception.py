__author__ = "gjoshi"


class PathNotFoundError(Exception):
    def __init__(self, source, destination):
        msg = "No path exists from {0} to {1}".format(source, destination)
        super(PathNotFoundError, self).__init__(msg)