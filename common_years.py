# Criação de classe que irá verificar ano com maior porcentagem de novos jogos e se há empate.
from collections import Counter
# A classe Counter do módulo collections serve para contar uma ocorrência em um conjunto de dados.

def find_most_common_years(data_dicts):
    
  
    # Extrai os anos de lançamento dos jogos e conta quantos jogos foram lançados em cada ano.
    release_years = Counter(int(game["Release date"].split()[-1]) for game in data_dicts)

    # Encontra o ano (ou anos) com o maior número de lançamentos.
    max_count = max(release_years.values())
    most_common_years = [year for year, count in release_years.items() if count == max_count]

    return most_common_years

