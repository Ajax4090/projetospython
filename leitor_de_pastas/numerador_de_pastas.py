import os
from PyPDF2 import PdfReader, PdfWriter

diretorio = os.listdir()

for i, arquivo in enumerate(diretorio, 1):
    nome, extensao = os.path.splitext(arquivo)
    nome_sem_espacos = nome.replace("-", " ").replace('_', ' ').split()  # Remove todos os espaços
    
    # arquivos = (nome_sem_espacos[1:-1])
    # file = (' '.join(arquivos))

    # print(file)
    print(nome_sem_espacos)
    