from app_trabalho_opencv import Limiarizacao
from app_trabalho_opencv import Histograma
from app_trabalho_opencv import Filtro_suavizacao
from app_trabalho_opencv import Filtro_agucamento
from app_trabalho_opencv import Conversao_coloridas


def main():
    # Limiarização
    limiarizacao = Limiarizacao('assets/casal_original.tiff', 128, 255)
    limiarizacao.limiar_function()
    limiarizacao.salvar_imagem('assets/imagens_salvas/casal_limiarizado.tiff', limiarizacao.limiar_function())
    limiarizacao.demonstra_imagens()

    # Histogramas
    histograma = Histograma('assets/casal_original.tiff')
    histograma.plt_normal()
    histograma.plt_equalizado()
    histograma.salvar_imagem('assets/imagens_salvas/casal_equalizado.tiff', histograma.hist_equalizado())
    histograma.demonstra_imagens()

    # Filtro Suavização 1
    suav = Filtro_suavizacao('assets/hubble_original.tif', 15, 15)
    suav.salvar_imagem('assets/imagens_salvas/hubble_media.tiff', suav.filtro_media())
    suav.maior_intensidade(suav.get_imagem_salva('assets/imagens_salvas/hubble_media.tiff'))
    suav.demonstra_imagens_1()

    # Filtro Suavização 2
    suav2 = Filtro_suavizacao('assets/circuito_original.tif', 3, 3)
    suav2.salvar_imagem('assets/imagens_salvas/circuito_original_media.tiff', suav2.filtro_media())
    suav2.salvar_imagem('assets/imagens_salvas/circuito_original_mediana.tiff', suav2.filtro_mediana())
    suav2.maior_intensidade(suav2.get_imagem_salva('assets/imagens_salvas/circuito_original_mediana.tiff'))
    suav2.demonstra_imagens_2()

    # Filtro Aguçamento
    aguc = Filtro_agucamento('assets/moon_original.tif')
    aguc.salvar_imagem('assets/imagens_salvas/moon_agucada.tiff', aguc.agucamento_imagem())
    aguc.demonstra_imagens()

    # Coloridas
    c = Conversao_coloridas('assets/colorida_original.tiff')
    c.demonstra_imagens()
    

if __name__ == '__main__':
    main()
