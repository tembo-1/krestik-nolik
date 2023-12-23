from perceptron import *

class Population:
    def __init__(self):
        self.size = 16
        self.mutate = 0.05
        self.krestik = []
        self.nolik = []
        self.num_sloy = 4
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
                player_nolik.score -= 1

                break

            count += 1
                
            if (count == 10):
                break    
            

            desk[player_nolik.step(desk, count)] = -1
            if (self.checkWin(desk)):
                victory = True
                player_nolik.score += 1
                player_krestir.score -= 1

                break

            count += 1

            if (count == 10):
                break  


    def Selection(self):
        temp_krestik = []
        temp_nolik = []

        for player_krestik in self.krestik:
            for player_nolik in self.nolik:
                self.Game(player_krestik, player_nolik)

        for player_krestik in self.krestik:
            temp_krestik.append(player_krestik)

        for player_nolik in self.nolik:
            temp_nolik.append(player_nolik)       

        self.krestik = sorted(temp_krestik, key=lambda Perceptron: Perceptron.score, reverse=True)[:-8]
        self.nolik = sorted(temp_nolik, key=lambda Perceptron: Perceptron.score, reverse=True)[:-8]

        score_krestik = 0.0
        for i in self.krestik:
            score_krestik += i.score/16

        score_nolik = 0.0
        for i in self.nolik:
            score_nolik += i.score/16

        print("Счёт крестиков", score_krestik)
        print("Счёт ноликов", score_nolik) 
        


    def Reproduction(self):
        for i in range(8):
            parent_krestik1 = int(random.uniform(0, 8))
            parent_krestik2 = int(random.uniform(0, 8))

            parent_nolik1 = int(random.uniform(0, 8))
            parent_nolik2 = int(random.uniform(0, 8))

            while parent_krestik1 == parent_krestik2:
                parent_krestik2 = int(random.uniform(0, 8))    

            self.krestik.append( self.krestik[parent_krestik1].Crossover(self.krestik[parent_krestik2]) )

            while parent_nolik1 == parent_nolik2:
                parent_nolik2 = int(random.uniform(0, 8))

            self.nolik.append( self.nolik[parent_nolik1].Crossover(self.nolik[parent_nolik2]) )    

    def Mutate(self):
        for i in self.krestik:
            i.Mutating(self.mutate)
        for i in self.nolik:
            i.Mutating(self.mutate)
        

        