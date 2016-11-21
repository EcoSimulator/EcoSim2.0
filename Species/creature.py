class Creature:
    def __init__(self):
        self.ID = 0
        self.Name = "Creature"
        self.SciName = "-"
        self.ConStatus = "-"
        self.Description = "No description available."
        self.InfoSource = "-"
        self.Image = ""
        self.ImageSource = "-"

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getSciName(self):
        return "("+self.SciName+")"

    def getConStatus(self):
        return self.ConStatus

    def getDesc(self):
        return self.Description

    def getInfoSource(self):
        return self.InfoSource

    def getImage(self):
        return self.Image

    def getImageSource(self):
        return self.ImageSource


# individual species
class NoName(Creature):
    def __init__(self):
        self.ID = 0
        self.Name = "Creature"
        self.SciName = "-"
        self.ConStatus = "-"
        self.Description = "No description available."
        self.InfoSource = "-"
        self.Image = ""
        self.ImageSource = "-"

class Wolf(Creature):
    def __init__(self):
        self.ID = 1
        self.Name = "Gray Wolf"
        self.SciName = "Canis lupus"
        self.ConStatus = "Least concern"
        self.Description = "The gray wolf is a canid native to the wildenress and remote areas of Eurasia and North America. It is the largest extant member of its family, with males ageraging 43-45 kg (95-99 lb), and females 36-38.5 kg (79-85 lb). Like the red wolf, it is distinguished from other Canis species by its larger size and less pointed features, particularly on the ears and muzzle. Its winter fur is long and bushy, and predominantly a mottled gray in color, although nearly pure white, red, or brown to black also occur. As of 2005, 37 subspecies of C. lupus are recognized by MSW3."
        self.InfoSource = "https://en.wikipedia.org/wiki/Gray_wolf"
        self.Image = "wolf.jpg"
        self.ImageSource = "National Geographic"

class Deer(Creature):
    def __init__(self):
        self.ID = 2
        self.Name = "White-tailed Deer"
        self.SciName = "Odocoileus virginianus"
        self.ConStatus = "Least concern"
        self.Description = "The white-tailed deer is a medium-sized deer native to the United States, Canada, Mexico, Central America, and South America as far south as Peru and Bolivia. It has also been introduced to New Zealand, Cuba, Jamaica, Hispaniola, Puerto Rico, Bahamas, Lesser Antilles, and some countries in Europe, such as Finland, the Czech Republic, and Serbia. In the Americas, it is the most widely distributed wild ungulate."

class Bee(Creature):
    def __init__(self):
        self.ID = 3
        self.Name = "Western Honey Bee"
        self.SciName = "Apis mellifera"
        self.ConStatus = "-"
        self.Description = "The western honey bee is the most common of the ~40 species of honey bee worldwide. The genus name Ajpis is Latin for \"bee\", and mellifera means \"honey-bearing\", referring to the species' tendency to produce a large quantity of honey for storage over the winter. Like all honey bees, the western honey bee is eusocial, creating colonies wijth a single fertile female (the queen), many sterile females (workers), and a small proportion of fertile males (drones). Individual colonies can house tens of thousands of bees. Colony activities are organized by complex communication between individuals, through both odors and the dance language."

class Plant(Creature):
    def __init__(self):
        self.ID = 4
        self.Name = "Plant"
        self.SciName = "Plantus plant"
        self.ConStatus = "-"
        self.Description = "Plants grow out of the dirt. Deer like to eat them. Rabbits eat them, too. Some people don't eat meat and only eat plants because they are secretly rabbits in disguise."