import os
import sys
from pypdf import PdfReader, PdfWriter

def estrai_pagine_da_pdf(nome_file_pdf, pagina_inizio, pagina_fine,nome_file=None):
    # Ottieni il percorso corrente del terminale (Git Bash)
    percorso_corrente = os.getcwd()
    
    # Verifica se il nome del file termina con '.pdf', altrimenti lo aggiunge
    if not nome_file_pdf.lower().endswith('.pdf'):
        nome_file_pdf += '.pdf'
    
    # Combina il percorso corrente con il nome del file inserito dall'utente
    input_pdf = os.path.join(percorso_corrente, nome_file_pdf)
    
    if nome_file:
        output_pdf = f"{nome_file}.pdf"
    else:
        nome_file = os.path.splitext(os.path.basename(input_pdf))[0]
        output_pdf = f"{nome_file} [{pagina_inizio}-{pagina_fine}].pdf"
    # Crea il nome del nuovo file con il range di pagine
    
    # Apri il file PDF di input
    with open(input_pdf, 'rb') as file_input:
        lettore_pdf = PdfReader(file_input)
        scrittore_pdf = PdfWriter()
        
        # Controlla che le pagine siano valide
        if pagina_inizio < 1 or pagina_fine > len(lettore_pdf.pages):
            raise ValueError("Le pagine specificate non sono valide.")
        
        # Aggiungi le pagine desiderate al nuovo PDF
        for num_pagina in range(pagina_inizio - 1, pagina_fine):
            pagina = lettore_pdf.pages[num_pagina]
            scrittore_pdf.add_page(pagina)
        
        # Scrivi il nuovo PDF
        with open(output_pdf, 'wb') as file_output:
            scrittore_pdf.write(file_output)
    
    print(f"File PDF salvato come: {output_pdf}")

# Verifica se l'utente ha fornito il nome del file come argomento
if len(sys.argv) < 2:
    print("Errore: devi fornire il nome del file PDF come primo argomento.")
    sys.exit(1)

# Ottieni il nome del file PDF dal primo argomento
nome_file_pdf = sys.argv[1]

# Richiedi le pagine di inizio e fine all'utente
if len(sys.argv)<3 :
    pagina_inizio = int(input("Inserisci la pagina di inizio: "))
else:
    pagina_inizio = int(sys.argv[2])

if len(sys.argv)<4:    
    pagina_fine = int(input("Inserisci la pagina di fine: "))
else:
    pagina_fine = int(sys.argv[3])

print(len(sys.argv))
if len(sys.argv)==5:    
    nome_file = sys.argv[4]
else:
    nome_file = None

# Esegui la funzione
estrai_pagine_da_pdf(nome_file_pdf, pagina_inizio, pagina_fine, nome_file)
