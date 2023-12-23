from perceptron import *

class Population:
    def __init__(self):
        self.size = 16
        self.mutate = 0.05
        self.krestik = []
        self.nolik = []

        self.victory_combined = [
		    [0, 4, 8],
		    [2, 4, 6],
		    [0, 1, 2],
		    [3, 4, 5],
		    [6, 7, 8],
		    [0, 3, 6],
		    [1, 4, 7],
		    [2, 5, 8],
        ]

        for i in range(self.size):
            self.krestik.append( Perceptron() )
            self.nolik.append( Perceptron() )

    def checkWin(self, desk):
        for i in self.victory_combined:
            if (desk[i[0]] == 1 and desk[i[1]] == 1 and desk[i[2]] == 1):
                return True
            elif (desk[i[0]] == -1 and desk[i[1]] == -1 and desk[i[2]] == -1):
                return True

        return False                   


    def Game(self, player_krestir : Perceptron, player_nolik : Perceptron):
        desk = [0] * 9
        victory = False
        count = 1

        while not victory:


            desk[player_krestir.step(desk, count)] = 1
            if (self.checkWin(desk)):
                victory = True
                player_krestir.score += 1
                player_nolik.score -= 2

                break

            count += 1
                
            if (count == 10):
                break    
            

            desk[player_nolik.step(desk, count)] = -1
            if (self.checkWin(desk)):
                victory = True
                player_nolik.score += 1
                player_krestir.score -= 2

                break

            count += 1

            if (count == 10):
                break  


    def Selection(self):
        for player_krestik in self.krestik:
            for player_nolik in self.nolik:
                self.Game(player_krestik, player_nolik)


                
    
                