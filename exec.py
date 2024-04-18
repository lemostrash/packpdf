import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_images_to_pdf(input_folder, output_folder):
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    if not image_files:
        print("Nenhum arquivo JPG encontrado para converter.")
        return

    base_name = os.path.splitext(os.path.basename(image_files[0]))[0]
    output_filename = os.path.join(output_folder, f"{base_name}.pdf")

    c = canvas.Canvas(output_filename, pagesize=letter)
    for image_file in image_files:
        img = Image.open(image_file)
        c.drawInlineImage(img, 0, 0, width=letter[0], height=letter[1])
        c.showPage()
    c.save()
    print(f"PDF criado com sucesso: {output_filename}")

def choose_folders():
    input_folder = filedialog.askdirectory(title="Selecione a pasta de entrada")
    output_folder = filedialog.askdirectory(title="Selecione a pasta de saída")
    if input_folder and output_folder:
        convert_images_to_pdf(input_folder, output_folder)

def main():
    root = tk.Tk()
    root.title("Conversor de Imagens JPG para PDF")

    btn_convert = tk.Button(root, text="Converter Imagens", command=choose_folders)
    btn_convert.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
