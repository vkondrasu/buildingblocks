import random

class Board:
    def __init__(self, endPosition, laddersMap, snakesMap):
        self.endPosition = endPosition
        self.players ={}
        self.endOfGame = False
        self.winner = None
        self.dice = Dice()
        self.playerId = 0
        self.ladders = laddersMap
        self.snakes = snakesMap

    def rollDice(self, player_id):
        move = self.dice.rollDice()
        
        newPosition = self.players[player_id].position + move
        if newPosition == self.endPosition:
            self.winner = player_id
            self.endOfGame = True

        if newPosition > self.endPosition:
            return

        if newPosition in self.snakes:
            newPosition = self.snakes[newPosition]

        if newPosition in self.ladders:
            newPosition = self.ladders[newPosition]

        print("Player " + str(player_id) + " moved from " + str(self.players[player_id].position) + " to " + str(newPosition))
        self.players[player_id].position = newPosition

    def addPlayer(self, position=1):
        self.playerId += 1
        self.players[self.playerId] = Player(position)

    def playGame(self):
        while not self.endOfGame:
            for player in self.players:
                self.rollDice(player)
                if self.endOfGame:
                    print("winner is " + str(b.winner))
                    break
        

class Player:
    #take start default parameter as 1
    def __init__(self, start=1):
        self.position = start

class Dice:
    def __init__(self) -> None:
        pass
    def rollDice(self):
        return random.randrange(1, 7)

ladders_map = {2:23, 8:12, 17:93, 29:54, 32:51, 39:80, 62:78, 70:89, 75:96}
'''
        self.ladders[2] = 23
        self.ladders[8] = 12
        self.ladders[17] = 93
        self.ladders[29] = 54
        self.ladders[32] = 51
        self.ladders[39] = 80
        self.ladders[62] = 78
        self.ladders[70] = 89
        self.ladders[75] = 96
        '''

snakes_map = {99:5, 92:76, 83:80, 67:50, 59:37, 41:20, 31:14}
'''
        self.snakes[99] = 5
        self.snakes[92] = 76
        self.snakes[83] = 80
        self.snakes[67] = 50
        self.snakes[59] = 37
        self.snakes[41] = 20
        self.snakes[31] = 14
        '''
b = Board(100, ladders_map, snakes_map)
b.addPlayer()
b.addPlayer()
b.addPlayer()
b.addPlayer()

b.playGame()