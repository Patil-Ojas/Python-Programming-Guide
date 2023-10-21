
class Train:
    def __init__(self, tickets):
        self.tickets = tickets
        
    def book_ticet(self):
        self.tickets = self.tickets - 1 
        print("You booked a ticket in ", self.trainname, ".")
    
    def getStatus(self):
        print(self.tickets, " tickets are left.")
    
    def fareinfo(self):
        print("Fare price is ", self.price)

thomas = Train(10)
thomas.trainname = "Thomasthetank"
thomas.price = 10000

thomas.book_ticet()
thomas.getStatus()
thomas.fareinfo()

