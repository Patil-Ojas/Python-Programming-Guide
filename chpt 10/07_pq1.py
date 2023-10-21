
class programmer:
    company = "microsoft"
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def getdetails(self):
        print("name is", self.name, "pos is", self.pos, "in", self.company)


harry = programmer("harry", "swe")
veio = programmer("brug", "mle")
notme = programmer("bruh", "fsd")

print(veio.company)

harry.getdetails()
veio.getdetails()
notme.getdetails()
