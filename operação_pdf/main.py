import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

dir = os.listdir()

arquivos = [arquivo for arquivo in dir if '.pdf' in arquivo.lower()]

cartao_ponto = (arquivos[0])

file = 'Colaboradores' 
if not os.path.exists(file):
    os.mkdir(file)

with open(cartao_ponto, 'rb' ) as reader:
    pdf = PdfReader(reader)

    for pagina in tqdm(pdf.pages):
        texto = pagina.extract_text().split('\n')
        nome = texto[2]
        cpf = texto[3]
        
        
        cpf_num = cpf[48:-18]
        cpf_num = [char for char in cpf_num if char.isnumeric()]
        cpf_num = '' .join(cpf_num)
        

        file_name = f'{file}/ {nome} {cpf_num}.pdf'

        writer = PdfWriter()
        writer.add_page(pagina)
        with open(file_name, 'wb') as output:
            writer.write(output)


