# Criação da classe para contabilização dos dados em percentual. 

class GameStats:
    def __init__(self, game_data):
        self.game_data = game_data

    def calculate_free_paid_percentage(self):

        
        free_count = 0
        paid_count = 0
        
        # Iteração pelos dicionários para contar jogos gratuitos e pagos.
        for game in self.game_data:
            price = game['Price'] # Variável onde se encontra a informação sobre preços.
            if price == '0.0' or price == '[0.0]':  # Considerando variações na representação de preço gratuito.
                free_count += 1
            else:
                paid_count += 1
                
        total_games = free_count + paid_count
        if total_games > 0:  # Evitando divisão por zero.
            free_percentage = (free_count / total_games) * 100 # Transformação em porcentagem. 
            paid_percentage = (paid_count / total_games) * 100
            print(f"Porcentagem de jogos gratuitos: {free_percentage:.2f}%")
            print(f"Porcentagem de jogos pagos: {paid_percentage:.2f}%")
        else:
            print("Não há jogos para analisar.")