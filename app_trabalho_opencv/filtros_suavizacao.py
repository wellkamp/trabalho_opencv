import cv2
from .imagem import Imagem


# Classe filha de Imagem
class FiltroSuavizacao(Imagem):
    def __init__(self, img, valor1, valor2):
        super(FiltroSuavizacao, self).__init__(img)
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor_de_limiar = 0

    def filtro_media(self):
        img = cv2.blur(self.nivel_cinza(), (self.valor1, self.valor2))
        return img

    def maior_intensidade(self, img_agucada):
        maior = 0
        for y in range(0, img_agucada.shape[0]):
            for x in range(0, img_agucada.shape[1]):
                if (maior < img_agucada[y][x]).any():
                    maior = img_agucada[y][x]
                    # print(img[y][x])
                    # print(maior)

        self.valor_de_limiar = maior[0]

    def calcula_limiar(self):
        print('Valor de maior intensidade é: ', self.valor_de_limiar)
        valor_de_limiar = self.valor_de_limiar * 0.25
        print('Valor de limiar 25% do valor de maior intensidade: ', valor_de_limiar)
        return valor_de_limiar

    def limiarizacao(self):
        (T, bin) = cv2.threshold(self.filtro_media(), self.calcula_limiar(), 255, cv2.THRESH_BINARY)
        cv2.imwrite('assets/imagens_salvas/hubble_limiar.tiff', bin)
        return bin

    def filtro_mediana(self):
        img = cv2.medianBlur(self.nivel_cinza(), 5)
        return img

    def demonstra_imagens_1(self):
        cv2.imshow('Original nivel cinza', self.nivel_cinza())
        cv2.imshow('Filtro de media', self.filtro_media())
        cv2.imshow('Limiarizada', self.limiarizacao())
        cv2.waitKey(0)

    def demonstra_imagens_2(self):
        cv2.imshow('Original nivel cinza', self.nivel_cinza())
        cv2.imshow('Filtro de media', self.filtro_media())
        cv2.imshow('Filtro mediana', self.filtro_mediana())
        cv2.waitKey(0)
