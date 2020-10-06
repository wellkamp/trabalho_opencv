import cv2
from abc import ABCMeta
# Classe Mãe Imagem


# Classe abstrata python
class Imagem(metaclass=ABCMeta):
    def __init__(self, img):
        self._img = img

    # Retorna imagem Original
    @property
    def img(self):
        return cv2.imread(self._img)

    # Seta outra imagem
    @img.setter
    def img(self, img_nova):
        self._img = img_nova

    # Retorna imagem original em cinza
    def nivel_cinza(self):
        return cv2.imread(self._img, cv2.IMREAD_GRAYSCALE)

    # Salva imagem no diretorio
    def salvar_imagem(self, diretorio, img):
        cv2.imwrite(diretorio, img)

    # Retorina imagem salva
    def get_imagem_salva(self, diretorio):
        return cv2.imread(diretorio)

