import cv2
from .imagem import Imagem


# Classe filha de Imagem
class Conversao_coloridas(Imagem):
    def __init__(self, img):
        super(Conversao_coloridas, self).__init__(img)

    # Faz a conversão para hsi
    def converte_hsi(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_RGB2HSV)
        H, S, I = cv2.split(img)
        cv2.imshow('H', H)  # Mostrando espectro
        cv2.imshow('S', S)  # Mostrando espectro
        cv2.imshow('I', I)  # Mostrando espectro
        hsi = cv2.merge((H, S, I))  # junção dos espectros
        voltar_para_RGB = cv2.cvtColor(hsi, cv2.COLOR_HSV2RGB)  # convertendo para RGB
        cv2.imshow('Transformada para RGB', voltar_para_RGB)  # Mostrando imagem convertida novamente
        cv2.imwrite('assets/imagens_salvas/colorida_hsi.tiff', voltar_para_RGB)

    # Faz a conversão para YCbCr
    def converte_YCbCr(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_RGB2YCrCb)
        Y, Cr, CB = cv2.split(img)
        cv2.imshow('Y', Y)  # Mostrando espectro
        cv2.imshow('Cr', Cr)  # Mostrando espectro
        cv2.imshow('CB', CB)  # Mostrando espectro
        ycrcb = cv2.merge((Y, Cr, CB))  # junção dos espectros
        voltar_para_RGB = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2RGB)  # convertendo para RGB
        cv2.imshow('Transformada para RGB', voltar_para_RGB)  # Mostrando imagem convertida novamente
        cv2.imwrite('assets/imagens_salvas/colorida_ycbcr.tiff', voltar_para_RGB)

    # Demonstra as imagens
    def demonstra_imagens(self):
        cv2.imshow('Original', self.img)
        cv2.waitKey(0)
        cv2.imshow('nivel cinza', self.nivel_cinza())
        cv2.waitKey(0)
        self.converte_hsi()
        cv2.waitKey(0)
        self.converte_YCbCr()
        cv2.waitKey(0)