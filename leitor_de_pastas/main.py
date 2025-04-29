import os
import shutil

def copiar_arquivos(pasta_origem, pasta_destino):
    
    
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta '{pasta_destino}' criada com sucesso!")
    
    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(pasta_origem)
    
    # Contador de arquivos copiados, cada arquivo contado, ele add 1+ ao contador
    contador = 0
    
    
    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
        # Verifica se é um arquivo (não uma pasta) e move o arquivo para a pasta de origem,
        #se colocar 'shutil.copy' ele copia os arquivos e nao move
        if os.path.isfile(caminho_origem):
            shutil.move(caminho_origem, caminho_destino)
            contador += 1   
            print(f"Arquivo '{arquivo}' copiada com sucesso!")
    
    print(f"\nOperação concluída! {contador} arquivos foram copiados.")

if __name__ == "__main__":
    # deixar fixo a pasta onde os arquivos estao e as pastas onde deseja colocar os arquivos
    #obs* eles serao (movidos)
    origem = 'pastaparaler'
    destino = 'fortes'
    
    # Verifica se a pasta de origem existe.
    if os.path.exists(origem):
        copiar_arquivos(origem, destino)
   

        