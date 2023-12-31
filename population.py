from perceptron import *

class Population:
    def __init__(self):
        self.size = 20
        self.half_size = int(self.size/2)
        self.mutate = 0.2
        self.person = []
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
            self.person.append( Perceptron() )

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
                if (count <= 5):
                    player_krestir.score += 10 
                if (count >= 6):
                    player_krestir.score -= 6
                player_krestir.score += 8
                player_nolik.score -= 8
                break

            count += 1
                
            if (count == 10):
                player_krestir.score -= 3  
                player_nolik.score -= 3
                break    
            
            desk[player_nolik.step(desk, count)] = -1
            if (self.checkWin(desk)):
                victory = True
                if (count <= 5):
                    player_nolik.score += 10  
                if (count >= 6):
                    player_nolik.score -= 6     
                player_nolik.score += 8
                player_krestir.score -= 8
                break

            count += 1

            if (count == 10):
                player_krestir.score -= 3  
                player_nolik.score -= 3
                break   

    def Selection(self):
        temp_person = []

        for i in self.person:
            i.score = 0.0

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.Game(self.person[i], self.person[j])

        for i in self.person:
            temp_person.append(i)
     
        score_person = 0.0
        for i in self.person:
            score_person += i.score

        print("Общий счёт", score_person)

        self.person = sorted(temp_person, key=lambda Perceptron: Perceptron.score, reverse=True)[:-self.half_size]

        return score_person

        
    def Reproduction(self):
        for i in range(self.half_size):
            parent1 = int(random.uniform(0, self.half_size))
            parent2 = int(random.uniform(0, self.half_size))

            while parent1 == parent2:
                parent2 = int(random.uniform(0, self.half_size))    

            self.person.append( self.person[parent1].Crossover(self.person[parent2]) )  

    def Mutate(self):
        for i in self.person:
            i.Mutating(self.mutate)
        

        