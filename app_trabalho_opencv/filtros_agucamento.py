import cv2
import numpy as np
from .imagem import Imagem


# Classe filha de Imagem
class FiltroAgucamento(Imagem):
    def __init__(self, img):
        super(FiltroAgucamento, self).__init__(img)
        self.lap = ''

    def laplaciano(self):
        self.lap = cv2.Laplacian(self.nivel_cinza(), 8, 3)  # 8 U
        return self.lap

    def agucamento_imagem(self):
        img = cv2.subtract(self.nivel_cinza(), self.laplaciano())
        return img

    def demonstra_imagens(self):
        # resultado = np.vstack([np.hstack([self.img, self.laplaciano(), self.soma_imagem()])])
        cv2.imshow("Original Nivel de Cinza", self.nivel_cinza())
        cv2.imshow('Laplaciano', self.laplaciano())
        cv2.imshow('Agucada', self.agucamento_imagem())
        return cv2.waitKey(0)


'''
    Outra função para soma de imagens
    
    def soma_matriz_imagens(self):
        img = self.laplaciano()
        img2 = self.img
        result = []
        for row in range(0, img.shape[0]):
            result.append([])
            for column in range(0, img.shape[1]):
                result[row].append(img2[row][column] + img[row][column])

        # print(result)
        return result
'''
