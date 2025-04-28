import os
import shutil
from PyPDF2 import PdfReader, PdfWriter

diretorio = os.listdir()



def criar_pastas_para_pdfs(diretorio_atual=None):

   

    """
    Cria uma pasta para cada arquivo PDF no diretório e move o arquivo para dentro da pasta.
    O nome da pasta será o mesmo nome do arquivo PDF (sem a extensão).
    """
    if diretorio_atual is None:
        diretorio_atual = os.getcwd()  # Usa o diretório atual se nenhum for especificado
    
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio_atual)
    
    # Filtra apenas os arquivos PDF
    pdfs = [arq for arq in arquivos if arq.lower().endswith('.pdf')]
    
    if not pdfs:
        print("Nenhum arquivo PDF encontrado no diretório.")
        return
    
    print(f"Processando {len(pdfs)} arquivos PDF...")
    
    for pdf in pdfs:
        # Remove a extensão .pdf para obter o nome da pasta
        nome_pasta = os.path.splitext(pdf)[0]
        
        # Cria o caminho completo para a nova pasta
        caminho_pasta = os.path.join(diretorio_atual, nome_pasta)
        
        try:
            # Cria a pasta se não existir
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)
            
            # Caminhos de origem e destino
            caminho_origem = os.path.join(diretorio_atual, pdf)
            caminho_destino = os.path.join(caminho_pasta, pdf)
            
            # Move o arquivo PDF para a pasta
            shutil.move(caminho_origem, caminho_destino)
            
            print(f"Arquivo '{pdf}' movido para a pasta '{nome_pasta}/'")
            
        except Exception as e:
            print(f"Erro ao processar o arquivo {pdf}: {str(e)}")
    
    print("\nOperação concluída!")

# Exemplo de uso:
if __name__ == "__main__":
    print("Arquivos no diretório atual:")
    diretorio = os.listdir()
    for i, arquivo in enumerate(diretorio, 1):
        nome, extensao = os.path.splitext(arquivo)
        nome_sem_espaços = nome.replace("-", " ").replace('_',' ').split()
        arquivos = (nome_sem_espaços[1:-1])
        file = (' '.join(arquivos))
        print(file)
    
    print("\nDeseja criar pastas para os PDFs?")
    resposta = input("Digite 's' para confirmar ou qualquer tecla para cancelar: ").lower()
    
    if resposta == 's':
        criar_pastas_para_pdfs()
    else:
        print("Operação cancelada.")