from . import __version__ as version


def print_description():
    print("Name of the Module: {}".format(version.__title__))
    print("Description: {}".format(version.__description__))