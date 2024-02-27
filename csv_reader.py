# Importando a biblioteca csv reader para leitura do arquivo. 
import csv

class CSVLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_csv(self): # Criando função de leitura de arquivo CSV.
        with open(self.filepath, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file) # Leitura do arquivo CSV. 
            headers = next(csv_reader) # Percorrendo o cabeçalho do arquivo.
            return headers, list(csv_reader)