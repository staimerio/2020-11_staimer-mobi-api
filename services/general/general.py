# Os
import os


def rmfile(path):
    """Delete files from a path
    :param path: Path of the folder with files to will delete
    """
    os.remove(path)