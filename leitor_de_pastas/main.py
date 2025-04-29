import os
import shutil

def copiar_arquivos(pasta_origem, pasta_destino):
    
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta '{pasta_destino}' criada com sucesso!")
    
    arquivos = os.listdir(pasta_origem)
    
    contador = 0
    
    
    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
      
        if os.path.isfile(caminho_origem):
            shutil.move(caminho_origem, caminho_destino)
            contador += 1   
            print(f"Arquivo '{arquivo}' copiada com sucesso!")
    
    print(f"\nOperação concluída! {contador} arquivos foram copiados.")

if __name__ == "__main__":
   
    origem = 'pastaparaler'
    destino = 'fortes'
    
    if os.path.exists(origem):
        copiar_arquivos(origem, destino)
   

        