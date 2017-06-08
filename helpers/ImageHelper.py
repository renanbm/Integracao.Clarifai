import base64
import requests


def CorrigirImagemBase64(base64Image):
    return base64Image[2:(len(base64Image) - 1)]


def get_url_as_corrected_base64(url):
    imagem = str(base64.b64encode(requests.get(url).content))
    return CorrigirImagemBase64(imagem)


def get_path_as_corrected_base64(path):
    with open(path, "rb") as image_file:
        imagem = str(base64.b64encode(image_file.read()))
    return CorrigirImagemBase64(imagem)


def get_url_as_pure_base64(url):
    return base64.b64encode(requests.get(url).content)


def get_path_as_pure_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read())
