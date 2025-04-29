import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm




def verificar_pdf_na_pasta(teste01):
    contador = 0  
    for pdf_file in os.listdir(teste01):
        if pdf_file.lower().endswith(".pdf"):
            contador += 1
    return contador > 0, contador  

teste01 = "C:/Users/User132/Documents/GitHub/projetospython/operação_pdf/teste01"
existe_pdf, total_pdfs = verificar_pdf_na_pasta(teste01)  

if existe_pdf:
    print(f"Existe {total_pdfs} arquivo(s) PDF na pasta.")
else:
    print(f"Não existe nenhum arquivo PDF na pasta.")

dir = os.listdir()
arquivos = [arquivo for arquivo in dir if '.pdf' in arquivo.lower()]

cartao_ponto = ('.PDF')

file = 'Colaboradores' 

if not os.path.exists(file):
    os.mkdir(file)

with open(cartao_ponto, 'rb') as reader:
    pdf = PdfReader(reader)

    def new_func(texto):
        cpf = (texto[3])
        return cpf

    for pagina in tqdm(pdf.pages):
        texto = pagina.extract_text().split('\n')
              
        if texto[4].isnumeric():
             cpf = new_func(texto) 
             print(cpf)
        elif texto[5].isnumeric():
             cpf = (texto[4])
             print(cpf)
        else:
             cpf = '000000' 

        nome = texto[2]
        
        cpf_num = cpf.split()[-1][-32:-18]
        cpf_num = [char for char in cpf_num if char.isnumeric()]
        cpf_num = ''.join(cpf_num)

        file_name = f'{file}/{nome} {cpf_num}.pdf'

        writer = PdfWriter()
        writer.add_page(pagina)
        with open(file_name, 'wb') as output:
             writer.write(output)

def contar_pdfs(diretorio):
    if not os.path.exists(diretorio):
        print(f"Erro: O diretório '{diretorio}' não existe.")
        return 0
    
    contagem = 0
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.lower().endswith('.pdf'):
            contagem += 1
    return contagem

quantidade = contar_pdfs(file)
print(f'Número de PDFs na pasta "{file}": {quantidade}')

print("\nLista de PDFs na pasta 'Colaboradores':")
for i, file_name in enumerate(os.listdir(file), 1):
    if file_name.lower().endswith('.pdf'):
        print(f"{i}. {file_name}")

