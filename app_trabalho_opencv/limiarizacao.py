import cv2
import numpy as np
from .imagem import Imagem


# Classe filha de Imagem
class Limiarizacao(Imagem):
    def __init__(self, img, limiar, tamanho):
        super().__init__(img)
        self._limiar = limiar
        self._tamanho = tamanho

    def limiar_function(self):
        (T, bin) = cv2.threshold(self.nivel_cinza(), self._limiar, self._tamanho, cv2.THRESH_BINARY)
        return bin

    def demonstra_imagens(self):
        resultado = np.vstack([np.hstack([self.nivel_cinza(), self.limiar_function()])])
        cv2.imshow("Limiarizacao", resultado)
        cv2.waitKey(0)

