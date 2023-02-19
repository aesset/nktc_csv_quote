# NTKC csv quote
Tooltje om de quotes goed te zetten van een ledenbestand, gedownload vanuit Google Sheets

# Installatie
- installeer python 3 (python 2 werkt niet)
- zet het bestandje ntkc_csv_quote.py in een directory, bv /testleden


# Gebruik
- zet de download van je leden testbestand vanuit Google Sheets in /testleden. Zie het bestand in dit project als voorbeeld.
- Open een terminal voor de commandline en type:


    python3 ntkc_csv_quote.py <<bestandsnaam>>

- het programma converteert de input naar een correct inputbestand voor het kampeerregister met dezelfde naam als de input file, met '_out' er achter.
- 