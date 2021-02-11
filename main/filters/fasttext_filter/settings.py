from main.filters.utils import SettingsUtils
from enum import Enum
import os


class Settings:
    class DIRECTORY(Enum):
        RESOURCE_DIR = 'main/filters/fasttext_filter/resources/'
        OUTPUTS_DIR = 'main/filters/fasttext_filter/outputs/'
        GENERATED_SRC_DIR = 'main/filters/fasttext_filter/generated_src/'

    @staticmethod
    def do_the_prerequisites():
        Settings.__create_required_dirs()

    @staticmethod
    def __create_required_dirs():
        for directory in Settings.DIRECTORY:

            if not os.path.exists(directory.value):
                try:
                    os.makedirs(directory.value)
                except OSError as e:
                    print(e)
