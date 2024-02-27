# Classe criada para transformar e relacionar os dados em um dicionário.

import csv # Importando biblioteca para leitura de csv.

class CSVtoDict:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_csv_to_dict(self):
        with open(self.filepath, 'r', encoding='utf-8') as file: 
            csv_reader = csv.reader(file) # Leitura do arquivo csv.
            headers = next(csv_reader) # Percorrendo o cabeçalho.
            data_dicts = [] # Criando um dicionário vazio para que seja adicionado os items posteriomente.
            for row in csv_reader:
                item_dict = {headers[i]: row[i] for i in range(len(headers))} # Relacionando as linhas ao cabeçalho.
                data_dicts.append(item_dict) # Adicionando os dados criados ao dicionário vazio. 
        return data_dicts # Retornar o dicionário preenchido."""