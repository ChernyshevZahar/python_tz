class board:
    
    def __init__(self):
        self.calls = [Cell(i) for i in range(0,9)]
        
    def display_board(self):
       print('--------------')
       for i in range(0,9,3):
           print(f'| {self.calls[i].symbol} | {self.calls[i+1].symbol} | {self.calls[i+2].symbol} |')


    def add_symbol(self,num,symbol):

        call = self.calls[num-1]
        
        if call.opathion:
            print('клетка занята')
            return False
        
        call.symbol = symbol
        call.opathion = True
        return True
             
    
    def check_game_over(self):
    
        win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
        ]

        for pos in win_positions:
            if self.calls[pos[0]].symbol != " " and self.calls[pos[0]].symbol == self.calls[pos[1]].symbol == self.calls[pos[2]].symbol:
                return True
        return False
        
    def reset_game(self):

        for call in self.calls:
            call.symbol = " "
            call.opathion = False
       
class Cell:
    
    def __init__(self,num):
      self.num = num
      self.symbol = " "
      self.opathion = False
    
class Player:
   
    def __init__(self,name,symbol):
       self.name = name
       self.wins = 0
       self.symbol = symbol
 
    
    def make_move(self):
        """Запрашивает ход игрока и проверяет корректность ввода."""
        while True:
            try:
                move = int(input((f"{self.name}, введите номер клетки для вашего хода (1-9): ")))
                if 1 > move < 9:
                    raise ValueError
                return move
            except ValueError:
                print('Неправильно! Введите номер клетки для вашего хода (1-9)')


class Game:
        def __init__(self, player1, player2):
            self.plaers = [player1,player2]
            self.border = board()
          
        def launch_move(self, player):
            """Выполняет ход текущего игрока."""
            while True:
                self.border.display_board()
                move = player.make_move()
                if self.border.add_symbol(move,player.symbol):
                    if self.border.check_game_over():
                        return True
                    return False
                print('Клетка занята')
                    

        def play_one_game(self):
            """Проводит одну игру до победы одного из игроков или ничьи."""
            while True:
                for payer in self.plaers:
                    if self.launch_move(payer):
                        self.border.display_board()
                        print (f"{payer.name} победил!")
                        payer.wins += 1
                        return 
                    if all(cell.opathion for cell in self.border.calls):
                        self.border.display_board()
                        print('Ничья!')
                        return 

            
        def start_games(self):
            """Запускает серию игр с возможностью перезапуска."""
            
            while True:
                self.border.reset_game()
                self.play_one_game()
                print(f'')
                agen = input("Хотите продолжить игру? (да/нет): ")
                if agen != 'да':
                    print('конец игры')
                    break
                    


# Создаем двух игроков
player1 = Player("Игрок 1", 'X')
player2 = Player("Игрок 2", 'O')
# Запускаем игру
game = Game(player1, player2)
game.start_games()