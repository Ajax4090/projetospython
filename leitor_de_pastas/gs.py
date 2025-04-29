import os
import shutil


def funcao_principal():
    

    pasta_destino = "pasta_lida"
    if not os.path.exists(pasta_destino):
        os.mkdir(pasta_destino)

    processar_boletos(pasta_destino)

    return





def processar_boletos(pasta_destino):
    dir = "CONDOMINIAIS/BOLETOS"
    nome_arquivos = (os.listdir(dir))
    nomes_tradados = []
    for nome_arquivo in nome_arquivos:
        nome_tratados = nome_arquivo.replace('_', ' ')
        nome_tratados =  nome_tratados.split("-")
        nome_tratados = nome_tratados[1:-1]
        nome_tratado = ' '.join(nome_tratados)
       

        pasta_processada  = f'{pasta_destino}/{nome_tratado}'

        if not os.path.exists(pasta_processada):
             os.mkdir(pasta_processada)
        
        origem = f'{dir}/{nome_arquivo}'
        destino = f'{pasta_processada}/{nome_arquivo}'
        
        shutil.copy(origem, destino)  

        


funcao_principal()