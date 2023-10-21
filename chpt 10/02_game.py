
# gta vice city mhm


class Remote():
    def leftBottonPressed(self):
        pass
    def rightBottonPressed(self):
        pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass
    
    def moveBottom(self):
        pass

    def moveTop(self):
        pass


remote1 = Remote()
player1 = Player()

# layer of abstraction
# like while playing gta do we wish to know HOW vercetti is taking left

if (remote1.leftBottonPressed()):
    player1.moveLeft()

if (remote1.rightBottonPressed()):
    player1.moveRight()

