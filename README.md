
# Estrattore di Pagine da PDF

Questo script Python consente di estrarre un intervallo di pagine da un file PDF e di salvarle in un nuovo file PDF. Il programma è progettato per essere semplice e diretto, richiedendo l'inserimento del file PDF originale e l'intervallo di pagine desiderato.

## Funzionalità

- **Estrazione di pagine da PDF**: Inserisci il nome del file PDF e le pagine che desideri estrarre. Il programma genererà un nuovo file PDF con solo le pagine selezionate.
- **Creazione automatica del nome del file**: Se non specifichi un nome per il nuovo file PDF, lo script lo creerà automaticamente in base alle pagine estratte.
- **Controllo degli intervalli di pagine**: Se le pagine inserite non sono valide (ad esempio, troppo alte o basse rispetto al numero totale di pagine), il programma mostrerà un messaggio di errore.

## Esecuzione

1. Posiziona il tuo file PDF nella stessa cartella dello script.
2. Avvia il programma da terminale con il seguente comando:
   ```bash
   python div.py nome_file.pdf pagina_inizio pagina_fine [nome_nuovo_file]
   ```
   - `nome_file.pdf`: Il file PDF di origine da cui estrarre le pagine.
   - `pagina_inizio`: La prima pagina che desideri estrarre.
   - `pagina_fine`: L'ultima pagina che desideri estrarre.
   - `[nome_nuovo_file]`: Opzionale. Se non specificato, il file generato avrà un nome predefinito basato sull'intervallo di pagine.

   Esempio:
   ```bash
   python div.py documento.pdf 2 5 estratto
   ```
   Questo comando estrarrà le pagine 2-5 dal file `documento.pdf` e creerà un nuovo file chiamato `estratto.pdf`.

3. Se preferisci inserire l'intervallo di pagine manualmente, lo script richiederà gli input se non vengono forniti come argomenti da riga di comando.

## Requisiti

- Python 3.x
- Libreria `pypdf`, che puoi installare eseguendo:
   ```bash
   pip install pypdf
   ```

## Note aggiuntive

- Assicurati che il file PDF da cui stai estraendo le pagine sia nella directory corrente.
- Il programma genera un messaggio di errore se le pagine richieste non esistono nel file PDF.

## Esempio di utilizzo

```bash
python div.py report.pdf 10 20 nuovo_report
```

Questo comando estrarrà le pagine dalla 10 alla 20 dal file `report.pdf` e creerà un nuovo file chiamato `nuovo_report.pdf`.
