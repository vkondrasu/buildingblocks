import random

class Board:
    def __init__(self, endPosition):
        self.endPosition = endPosition
        self.players ={}
        self.endOfGame = False
        self.winner = None
        self.dice = Dice()
        self.playerId = 0

        #make ladders and snakes configurable values

        self.ladders = {}
        self.ladders[2] = 23
        self.ladders[8] = 12
        self.ladders[17] = 93
        self.ladders[29] = 54
        self.ladders[32] = 51
        self.ladders[39] = 80
        self.ladders[62] = 78
        self.ladders[70] = 89
        self.ladders[75] = 96

        self.snakes = {}
        self.snakes[99] = 5
        self.snakes[92] = 76
        self.snakes[83] = 80
        self.snakes[67] = 50
        self.snakes[59] = 37
        self.snakes[41] = 20
        self.snakes[31] = 14

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

    def addPlayer(self, position):
        self.playerId += 1
        self.players[self.playerId] = Player(position)

class Player:
    def __init__(self, start):
        self.position = start

class Dice:
    def __init__(self) -> None:
        pass
    def rollDice(self):
        return random.randrange(1, 7)


b = Board(100)
b.addPlayer(1)
b.addPlayer(1)
b.addPlayer(1)

#this loop should go into b.playGame()
while not b.endOfGame:
    for player in b.players:
        b.rollDice(player)
        if b.endOfGame:
            print("winner is " + str(b.winner))
            break