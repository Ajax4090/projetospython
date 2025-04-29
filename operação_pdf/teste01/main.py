import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

# Lista todos os PDFs no diretório atual
dir_files = os.listdir()
arquivos_pdf = [arquivo for arquivo in dir_files if arquivo.lower().endswith('.pdf')]

# Pasta geral de saída (opcional)
output_dir_geral = 'Colaboradores'
if not os.path.exists(output_dir_geral):
    os.mkdir(output_dir_geral)

# Processa cada PDF encontrado
for pdf_file in arquivos_pdf:
    print(f"\nProcessando: {pdf_file}...")
    
    # Cria uma pasta com o nome do arquivo PDF (sem extensão)
    nome_pasta = os.path.splitext(pdf_file)[0]  # Remove o .pdf
    output_dir = os.path.join(output_dir_geral, nome_pasta)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(pdf_file, 'rb') as reader:
        pdf = PdfReader(reader)

        def extrair_cpf(texto):
            if len(texto) > 4 and texto[4].isnumeric():
                return texto[3]
            elif len(texto) > 5 and texto[5].isnumeric():
                return texto[4]
            else:
                return '000000'

        for pagina in tqdm(pdf.pages, desc=f"Páginas ({pdf_file})"):
            texto = pagina.extract_text().split('\n')
            
            if len(texto) < 3:
                continue  # Pula páginas com formato inválido
            
            # Extrai nome e CPF
            nome = texto[2].strip()  # Remove espaços extras
            cpf = extrair_cpf(texto)
            
            # Formata CPF (remove caracteres não numéricos)
            cpf_num = ''.join(filter(str.isdigit, cpf))[-11:]  # Pega os últimos 11 dígitos

            # Nome do arquivo de saída
            file_name = f"{nome} {cpf_num}.pdf"
            file_path = os.path.join(output_dir, file_name)

            # Salva a página como um novo PDF
            writer = PdfWriter()
            writer.add_page(pagina)
            
            with open(file_path, 'wb') as output:
                writer.write(output)

# Conta e lista os PDFs gerados (por pasta)
print("\nResumo de arquivos gerados:")
for root, dirs, files in os.walk(output_dir_geral):
    if root == output_dir_geral:
        continue  # Ignora a pasta geral se só quiser as subpastas
    
    print(f"\nPasta: {os.path.basename(root)}")
    for i, file_name in enumerate(files, 1):
        if file_name.lower().endswith('.pdf'):
            print(f"  {i}. {file_name}")