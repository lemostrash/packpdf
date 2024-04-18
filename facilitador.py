from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(image_files, output_folder):
    # Verificar se existem arquivos para converter
    if not image_files:
        print("Nenhum arquivo JPG encontrado para converter.")
        return

    # Usar o nome do primeiro arquivo como base para o nome do PDF
    base_name = os.path.splitext(os.path.basename(image_files[0]))[0]
    output_filename = os.path.join(output_folder, f"{base_name}.pdf")

    # Iniciar o objeto de canvas do ReportLab
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Iterar sobre os arquivos de imagem
    for image_file in image_files:
        # Abrir a imagem
        img = Image.open(image_file)
        # Adicionar a imagem ao PDF
        c.drawInlineImage(img, 0, 0, width=letter[0], height=letter[1])
        # Adicionar uma nova página para a próxima imagem
        c.showPage()

    # Salvar o PDF
    c.save()
    print(f"PDF criado com sucesso: {output_filename}")

# Pasta onde os arquivos de imagem JPG estão localizados
input_folder = r"C:\Users\Lemonade\Downloads\FACILITADOR\docs"
# Pasta para salvar o arquivo PDF
output_folder = r"C:\Users\Lemonade\Downloads\FACILITADOR\pdf"

# Lista de arquivos na pasta de entrada
files = os.listdir(input_folder)
# Filtrar apenas arquivos JPG
image_files = [os.path.join(input_folder, f) for f in files if f.lower().endswith('.jpg')]

# Chamada da função para converter imagens em um único PDF
convert_images_to_pdf(image_files, output_folder)
