import cv2
import mahotas
from matplotlib import pyplot as plt
from .imagem import Imagem


# Classe filha de Imagem
class Histograma(Imagem):
    def __init__(self, img):
        super().__init__(img)

    def plt_normal(self):
        plt.figure()
        plt.title('Histograma Equalizado')  # Titulo
        plt.xlabel('Intensidade')  # Titulo Eixo X
        plt.ylabel('Qt de pixel')  # Titulo Eixo Y
        plt.hist(self.nivel_cinza().ravel(), 256, [0, 256])  # Plotando o histograma normal
        plt.xlim([0, 256])
        plt.show()

    def plt_equalizado(self):
        plt.figure()
        plt.title('Histograma Equalizado')
        plt.xlabel('Intensidade')
        plt.ylabel('Qt de pixel')
        plt.hist(self.hist_equalizado().ravel(), 256, [0, 256])  # Plotando o histograma
        # self.salvar_imagem('assets/imagens_salvas/casal_equalizado.tiff', hist_eq)
        plt.xlim([0, 256])
        plt.show()

    def hist_equalizado(self):
        hist_eq = cv2.equalizeHist(self.nivel_cinza())  # Colocando em uma variavel a imagem equalizada
        return hist_eq

    def otsu(self):
        temp = self.hist_equalizado()
        T = mahotas.thresholding.otsu(temp)
        temp = temp.copy()
        temp[temp > T] = 255
        temp[temp < 255] = 0
        temp = cv2.bitwise_not(temp)
        return temp

    def demonstra_imagens(self):
        cv2.imshow('Original nivel cinza', self.nivel_cinza())
        cv2.imshow('Equalizada', self.hist_equalizado())
        cv2.imshow('Otsu', self.otsu())
        cv2.waitKey(0)



