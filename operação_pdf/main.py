import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

dir = os.listdir()

arquivos = [arquivo for arquivo in dir if '.pdf' in arquivo.lower()]



file = 'Colaboradores' 
if not os.path.exists(file):
    os.mkdir(file)

with open(arquivos, 'rb' ) as reader:
    pdf = PdfReader(reader)

    for pagina in tqdm(pdf.pages):
        texto = pagina.extract_text().split('\n')
        nome = texto[2]

        if texto[4].isnumeric():
            cpf = (texto[3]) 
            print(cpf)
        elif texto[5].isnumeric():
            cpf = (texto[4])
            print(cpf)
        else:
            cpf = '000000' 
        
        
        cpf_num = cpf.split()[-1][-32:-18]
        cpf_num = [char for char in cpf_num if char.isnumeric()]
        cpf_num = '' .join(cpf_num)
        

        file_name = f'{file}/ {nome} {cpf_num}.pdf'

        writer = PdfWriter()
        writer.add_page(pagina)
        with open(file_name, 'wb') as output:
            writer.write(output)


