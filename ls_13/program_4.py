
class ScoreLimitExceededError(Exception):
    def __init__(self):
        super().__init__('Нельзя добавлять больше 1000 очков')




class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self,skore):
        if self.score + skore > 1000:
            return ScoreLimitExceededError()
        self.score += skore
        
    def subtract_score(self,score):
        
        if (self.score - score) < 0:
            raise ValueError
        self.score -= score

    

if __name__ == "__main__":
    game_score = GameScore()
    try:
        # Добавляем 500 очков
        game_score.add_score(500)
        print(f"Текущий счет: {game_score.score}")
        # Пытаемся добавить еще 600 очков, что вызовет исключение
        game_score.add_score(600)
    except ScoreLimitExceededError as e:
        print(e)
    except ValueError as e:
        print(e)

    try:
        # Пытаемся вычесть больше очков, чем есть
        game_score.subtract_score(600)
    except ValueError as e:
        print(e)

    # Проверка работы метода subtract_score
    try:
        game_score.subtract_score(100)
        print(f"Текущий счет после вычитания: {game_score.score}")
    except ValueError as e:
        print(e)
        