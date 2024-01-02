import os

from ..logging import LOGGER

EXTENSIONS = {".jpg", ".jpeg", ".png"}
DIRECTORIES = ["downloads", "cache"]


def dirr():
    for file in os.listdir():
        if any(file.endswith(ext) for ext in EXTENSIONS):
            try:
                os.remove(file)
            except OSError as e:
                LOGGER(__name__).error(f"Erro ao remover o arquivo {file}: {e}")

    for directory in DIRECTORIES:
        if directory not in os.listdir():
            try:
                os.mkdir(directory)
            except OSError as e:
                LOGGER(__name__).error(f"Erro ao criar o diretório {directory}: {e}")

    LOGGER(__name__).info("Directories Updated.")
