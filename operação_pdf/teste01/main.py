import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

class Cores:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

dir_files = os.listdir()
arquivos_pdf = [arquivo for arquivo in dir_files if arquivo.lower().endswith('.pdf')]

output_dir_geral = 'Colaboradores'
if not os.path.exists(output_dir_geral):
    os.mkdir(output_dir_geral)

for pdf_file in arquivos_pdf:
    print(f"\n{Cores.AZUL}→ Processando: {Cores.CIANO}{pdf_file}{Cores.RESET}")
    
    nome_pasta = os.path.splitext(pdf_file)[0]
    output_dir = os.path.join(output_dir_geral, nome_pasta)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"{Cores.VERDE}✔ Pasta criada: {output_dir}{Cores.RESET}")
    
    with open(pdf_file, 'rb') as reader:
        pdf = PdfReader(reader)

        def extrair_cpf(texto):
            if len(texto) > 4 and texto[4].isnumeric():
                return texto[3]
            elif len(texto) > 5 and texto[5].isnumeric():
                return texto[4]
            else:
                return '000000'

        for pagina in tqdm(pdf.pages, desc=f"{Cores.AMARELO}Extraindo páginas{Cores.RESET}", colour='yellow'):
            texto = pagina.extract_text().split('\n')
            
            if len(texto) < 3:
                continue
            
            nome = texto[2].strip()
            cpf = extrair_cpf(texto)
            cpf_num = ''.join(filter(str.isdigit, cpf))[-11:]
            file_name = f"{nome} {cpf_num}.pdf"
            file_path = os.path.join(output_dir, file_name)

            writer = PdfWriter()
            writer.add_page(pagina)
            
            with open(file_path, 'wb') as output:
                writer.write(output)
        
        print(f"{Cores.VERDE}✓ Concluído: {pdf_file}{Cores.RESET}\n")

print(f"\n{Cores.MAGENTA}════════ RESUMO ════════{Cores.RESET}")
for root, dirs, files in os.walk(output_dir_geral):
    if root == output_dir_geral:
        continue
    
    print(f"\n{Cores.AZUL}Pasta: {Cores.CIANO}{os.path.basename(root)}{Cores.RESET}")
    for i, file_name in enumerate(files, 1):
        if file_name.lower().endswith('.pdf'):
            print(f"  {Cores.VERDE}{i}.{Cores.RESET} {file_name}")