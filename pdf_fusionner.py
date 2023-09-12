#by Valentin Luthringer 

import PyPDF2
import os

def main():
    script_directory = os.path.dirname(__file__)

    # Récupérer fichier PDF
    pdf_files = []
    while True:
        file_name = input("Entrez le chemin du fichier PDF (ou tapez 'q' pour quitter) : ")
        if file_name.lower() == 'q':
            break
        pdf_files.append(file_name)

    # Créer le chemin complet du fichier de sortie PDF
    output_filename = os.path.join(script_directory, "pdf_fusionnés.pdf")

    # Fusionner les fichiers PDF dans l'ordre d'insertion
    merge_pdfs(pdf_files, output_filename)

def merge_pdfs(pdf_files, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    pdf_merger.write(output_filename)
    pdf_merger.close()

    print(f"Les fichiers PDF ont été fusionnés avec succès en {output_filename}")

if __name__ == "__main__":
    main()
