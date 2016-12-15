class Creature:
    def __init__(self):
        self.ID = 0
        self.name = "Creature"
        self.sci_name = "-"
        self.con_status = "-"
        self.description = "No description available."
        self.info_source = "-"
        self.image = ""
        self.image_source = "-"

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_sci_name(self):
        return "("+self.sci_name+")"

    def get_con_status(self):
        return self.con_status

    def get_desc(self):
        return self.description

    def get_info_source(self):
        return self.info_source

    def get_image(self):
        return self.image

    def get_image_source(self):
        return self.image_source


# individual species
class NoName(Creature):
    def __init__(self):
        self.ID = 0
        self.name = "Creature"
        self.sci_name = "-"
        self.con_status = "-"
        self.description = "No description available."
        self.info_source = "-"
        self.image = ""
        self.image_source = "-"

class Wolf(Creature):
    def __init__(self):
        self.ID = 1
        self.name = "Gray Wolf"
        self.sci_name = "Canis lupus"
        self.con_status = "Least concern"
        self.description = "The gray wolf is a canid native to the wildenress and remote areas of Eurasia and North America. It is the largest extant member of its family, with males ageraging 43-45 kg (95-99 lb), and females 36-38.5 kg (79-85 lb). Like the red wolf, it is distinguished from other Canis species by its larger size and less pointed features, particularly on the ears and muzzle. Its winter fur is long and bushy, and predominantly a mottled gray in color, although nearly pure white, red, or brown to black also occur. As of 2005, 37 subspecies of C. lupus are recognized by MSW3."
        self.info_source = "https://en.wikipedia.org/wiki/Gray_wolf"
        self.image = "wolf.jpg"
        self.image_source = "National Geographic"

class Deer(Creature):
    def __init__(self):
        self.ID = 2
        self.name = "White-tailed Deer"
        self.sci_name = "Odocoileus virginianus"
        self.con_status = "Least concern"
        self.description = "The white-tailed deer is a medium-sized deer native to the United States, Canada, Mexico, Central America, and South America as far south as Peru and Bolivia. It has also been introduced to New Zealand, Cuba, Jamaica, Hispaniola, Puerto Rico, Bahamas, Lesser Antilles, and some countries in Europe, such as Finland, the Czech Republic, and Serbia. In the Americas, it is the most widely distributed wild ungulate."
        self.info_source = "https://en.wikipedia.org/wiki/White-tailed_deer"
        self.image = "deer.jpg"
        self.image_source = "Wikipedia"

class Bee(Creature):
    def __init__(self):
        self.ID = 3
        self.name = "Western Honey Bee"
        self.sci_name = "Apis mellifera"
        self.con_status = "-"
        self.description = "The western honey bee is the most common of the ~40 species of honey bee worldwide. The genus name Ajpis is Latin for \"bee\", and mellifera means \"honey-bearing\", referring to the species' tendency to produce a large quantity of honey for storage over the winter. Like all honey bees, the western honey bee is eusocial, creating colonies wijth a single fertile female (the queen), many sterile females (workers), and a small proportion of fertile males (drones). Individual colonies can house tens of thousands of bees. Colony activities are organized by complex communication between individuals, through both odors and the dance language."
        self.info_source = "https://en.wikipedia.org/wiki/Western_honey_bee"
        self.image = "bee.jpg"
        self.image_source = "Wikipedia"

class Plant(Creature):
    def __init__(self):
        self.ID = 4
        self.name = "Plant"
        self.sci_name = "Plantus plant"
        self.con_status = "-"
        self.description = "Plants grow out of the dirt. Deer like to eat them. Rabbits eat them, too. Some people don't eat meat and only eat plants because they are secretly rabbits in disguise."
        self.info_source = "Me"
        self.image = "plant.jpg"
        self.image_source = "The Internet"

class Fish(Creature):
    def __init__(self):
        self.ID = 5
        self.name = "Pink Salmon"
        self.sci_name = "Oncorhynchus gorbuscha"
        self.con_status = "-"
        self.description = "Pink salmon or humpback salmon (Oncorhynchus gorbuscha) is a species of anadromous fish in the salmon family. It is the smallest and most abundant of the Pacific salmon. The scientific species name is based on the Russian common name for this species gorbusa, which literally means humpie."
        self.info_source = "Wikipedia"
        self.image = "salmon.jpg"
        self.image_source = "history.com"

class Bear(Creature):
    def __init__(self):
        self.ID = 6
        self.name = "Grizzly Bear"
        self.sci_name = "Ursus arctos"
        self.con_status = "Least concern"
        self.description = "The grizzly bear (Ursus arctos ssp.), less commonly known as the silvertip bear, is a large subspecies of brown bear inhabiting North America. Scientists generally do not use the name grizzly bear but call it the North American brown bear."
        self.info_source = "Wikipedia"
        self.image = "bear.jpg"
        self.image_source = "sciencenews.org"