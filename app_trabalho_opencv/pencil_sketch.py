import cv2
from .imagem import Imagem


class PencilScketch(Imagem):
    def __init__(self, img):
        super(PencilScketch, self).__init__(img)

    def pencil_scketch(self):
        img = cv2.bitwise_not(self.nivel_cinza())
        img = cv2.GaussianBlur(img, (15, 15), 0)
        img = cv2.divide(self.nivel_cinza(), 255 - img, scale=256)
        return img

    def demonstra_imagem(self):
        cv2.imshow('Desenhado', self.pencil_scketch())
        cv2.waitKey(0)
